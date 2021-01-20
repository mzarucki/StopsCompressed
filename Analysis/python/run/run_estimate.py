#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",      dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--noSystematics",         dest="noSystematics",         default = False,             action="store_true", help="no systematics?")
parser.add_option("--selectEstimator",       dest="selectEstimator",       default=None,                action="store",      help="select estimator?")
parser.add_option("--selectRegion",          dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--year",                  dest="year",                  default=2016, type="int",    action="store",      help="Which year?")
parser.add_option("--nThreads",              dest="nThreads",              default=8, type="int",       action="store",      help="How many threads?")
parser.add_option('--logLevel',              dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
#parser.add_option("--control",               dest="control",               default=None,                action='store',      choices=[None, "DY", "VV", "DYVV", "TTZ1", "TTZ2", "TTZ3", "TTZ4", "TTZ5", "CR1aX","CR1aY", "CR1bX", "CR1bY"], help="For CR region?")
parser.add_option("--control",               dest="control",               default=False,                action='store_true', help="For CR region?")
parser.add_option("--useGenMet",             dest="useGenMet",             default=False,               action='store_true', help="use genMET instead of recoMET, used for signal studies")
parser.add_option("--overwrite",             dest="overwrite",             default=False,               action='store_true', help="overwrite existing results?")
parser.add_option("--all",                   dest="all",                   default=False,               action='store_true', help="Run over all SR and CR?")

(options, args) = parser.parse_args()
from StopsCompressed.Analysis.estimators   import *
from StopsCompressed.Analysis.regions      import signalRegions, controlRegions
#from StopsCompressed.Analysis.regions_splitCR      import signalRegions, controlRegions
#from StopsCompressed.Analysis.regions_splitCR_v2      import signalRegions, controlRegions
from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed   import signals_T2tt


# Logging
import Analysis.Tools.logger as logger
logger  = logger.get_logger(options.logLevel, logFile = None)

import StopsCompressed.Tools.logger as logger
logger = logger.get_logger(options.logLevel, logFile = None )
import Analysis.Tools.logger as logger_an
logger_an = logger_an.get_logger(options.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger('INFO', logFile = None )


from StopsCompressed.Analysis.Setup import Setup
from StopsCompressed.Analysis.SetupHelpers import *
channels = allChannels
#channels = lepChannels
#for c in channels: print c
setup = Setup(year=options.year)

if options.control:
	allRegions= controlRegions
elif options.all:
	allRegions = controlRegions + signalRegions
	#print len(allRegions)
#allRegions = controlRegions + signalRegions  #if (options.control ) else signalRegions
#for s in allRegions: print s
from StopsCompressed.Analysis.MCBasedEstimate import MCBasedEstimate
from StopsCompressed.Analysis.DataObservation import DataObservation

# signals, so far only T2tt
signals_T2tt = []
#postProcessing_directory = "stops_2016_nano_v0p3/dilep/"
#from StopsDilepton.samples.cmgTuples_FastSimT8bbllnunu_mAODv2_25ns_postProcessed    import signals_T8bbllnunu_XCha0p5_XSlep0p05, signals_T8bbllnunu_XCha0p5_XSlep0p5, signals_T8bbllnunu_XCha0p5_XSlep0p95
#from StopsDilepton.samples.cmgTuples_FullSimTTbarDM_mAODv2_25ns_postProcessed import signals_TTbarDM
#allEstimators += [ MCBasedEstimate(name=s.name, sample={channel:s for channel in channels + trilepChannels}) for s in signals_TTbarDM + signals_T2tt + signals_T8bbllnunu_XCha0p5_XSlep0p5 + signals_T8bbllnunu_XCha0p5_XSlep0p05 + signals_T8bbllnunu_XCha0p5_XSlep0p95]

estimators = estimatorList(setup)
allEstimators = estimators.constructEstimatorList(['WJets','DY','Top','ZInv','singleTop', 'VV', 'TTX', 'QCD'])
allEstimators += [ MCBasedEstimate(name=s.name, sample={channel:s for channel in channels}) for s in signals_T2tt ]
# Select estimate
if not options.selectEstimator == 'Data':
    estimate = next((e for e in allEstimators if e.name == options.selectEstimator), None)
    estimate.isData = False
else:
    estimate = DataObservation(name='Data', sample=setup.processes['Data'], cacheDir=setup.defaultCacheDir())
    estimate.isSignal = False
    estimate.isData   = True

if not estimate:
  logger.warn(options.selectEstimator + " not known")
  exit(0)


if estimate.name.count('T2tt') or estimate.name.count('TTbarDM') or estimate.name.count('T8bbllnunu'): estimate.isSignal = True

isFastSim = estimate.name.count('T2tt')
isFastSim = estimate.name.count('T8bbllnunu')
if isFastSim:
  setup = setup.sysClone(sys={'reweight':['reweightLeptonFastSimSF'], 'remove':['reweightPU36fb']})


#setup = setup.sysClone()
setup.verbose=True
def wrapper(args):
        r,channel,setup = args
        logger.info("Running estimate for region %s, channel %s for estimator %s"%(r,channel, options.selectEstimator if options.selectEstimator else "None"))
        res = estimate.cachedEstimate(r,channel, setup, save=True, overwrite=options.overwrite)
        return (estimate.uniqueKey(r,channel, setup), res )

estimate.initCache(setup.defaultCacheDir())

jobs=[]
for channel in channels:
    for (i, r) in enumerate(allRegions):
        if options.selectRegion is not None and options.selectRegion != i: continue
        jobs.append((r, channel, setup))
        if not estimate.isData and not options.noSystematics:
            if estimate.isSignal: jobs.extend(estimate.getSigSysJobs(r,channel,  setup, isFastSim))
            else:                 jobs.extend(estimate.getBkgSysJobs(r,channel,  setup))

results = map(wrapper, jobs)
#print results
for channel in (['all']):
    for (i, r) in enumerate(allRegions):
	#print r
        if options.selectRegion is not None and options.selectRegion != i: continue
        if options.useGenMet: estimate.cachedEstimate(r, setup.sysClone({'selectionModifier':'genMet'}), save=True)
        else: estimate.cachedEstimate(r,channel, setup, save=True, overwrite=options.overwrite)
        if not estimate.isData and not options.noSystematics:
            if estimate.isSignal: map(lambda args:estimate.cachedEstimate(*args, save=True, overwrite=options.overwrite), estimate.getSigSysJobs(r, channel,  setup, isFastSim))
            else: 
	    	map(lambda args:estimate.cachedEstimate(*args, save=True, overwrite=options.overwrite), estimate.getBkgSysJobs(r,  channel, setup))
		#print estimate.getBkgSysJobs(r,  channel, setup) 

        logger.info('Done with region: %s', r)
    logger.info('Done with channel: %s', channel)
logger.info('Done.')
