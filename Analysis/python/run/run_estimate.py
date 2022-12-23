#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--sensitivityStudyName",  dest="sensitivityStudyName",  default = "baseline",        type="str",    action="store",      help="Name of sensitivity study")
parser.add_option("--noMultiThreading",      dest="noMultiThreading",      default = False,             action="store_true",  help="noMultiThreading?")
parser.add_option("--noSystematics",         dest="noSystematics",         default = False,             action="store_true",  help="no systematics?")
parser.add_option("--makeYieldsTable",       dest="makeYieldsTable",       default = False,             action="store_true",  help="Make yields table")
parser.add_option("--selectEstimator",       dest="selectEstimator",       default=None,                action="store",       help="select estimator?")
parser.add_option("--selectRegion",          dest="selectRegion",          default=None, type="int",    action="store",       help="select region?")
parser.add_option("--year",                  dest="year",                  default="2016postVFP", type="str", action="store", help="Which year?")
parser.add_option("--nThreads",              dest="nThreads",              default=1, type="int",       action="store",       help="How many threads?")
parser.add_option('--logLevel',              dest="logLevel",              default='INFO',              action='store',       help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
#parser.add_option("--control",               dest="control",               default=None,                action='store',      choices=[None, "DY", "VV", "DYVV", "TTZ1", "TTZ2", "TTZ3", "TTZ4", "TTZ5", "CR1aX","CR1aY", "CR1bX", "CR1bY"], help="For CR region?")
parser.add_option("--all",                   dest="all",                   default=False,               action='store_true',  help="Run over all SR and CR?")
parser.add_option("--control",               dest="control",               default=False,               action='store_true',  help="For CR region?")
parser.add_option("--useGenMet",             dest="useGenMet",             default=False,               action='store_true',  help="use genMET instead of recoMET, used for signal studies")
parser.add_option("--overwrite",             dest="overwrite",             default=False,               action='store_true',  help="overwrite existing results?")
parser.add_option("--lowMETregion",        action='store_true',            default=False,                                     help="Add low MET region")
parser.add_option("--l1pT_CR_split",       action='store_true',            default=False,                                     help="lepton pT CR split")
parser.add_option("--splitCTZ",            action='store_true',            default=False,                                     help="Split CT into MET and HT in Z region")
parser.add_option("--lowHTbin",            action='store_true',            default=False,                                     help="Add low HT bin")
parser.add_option("--mT_cut_value",        action='store',                 default=95,                  choices=[95,100,105], help="second mT threshold")
parser.add_option("--mTregions",           action='store',                 default='3',                 choices=['3','4', '5','high5','low5','6'],    help="number of mT regions")
parser.add_option("--CT_cut_value",        action='store',                 default=400,                 choices=[400, 450],   help="CT cut threshold")
parser.add_option("--isPrompt",            action='store_true',            default=False,                                     help="prompt leptons contributing to regions")
#parser.add_option("--isdPhiMetJets",       action='store_true',            default=False,   help="cut on min(dPhi(met,Jets>60)), not on dPhiJets")
#parser.add_option("--isdPhiComb",          action='store_true',            default=False,   help="cut on min(dPhi(met,Jets>60)), and on dPhiJets")

(options, args) = parser.parse_args()

from StopsCompressed.Analysis.estimators import *
if options.l1pT_CR_split:
    _NBINS = 68
    if options.mT_cut_value == 95:
        if options.mTregions == 4:
            _NBINS = 88
            if options.CT_cut_value == 450:
                print "Using regions_splitCR_4mTregions_CT450.py for definition of regions."
                from StopsCompressed.Analysis.regions_splitCR_4mTregions_CT450 import controlRegions, signalRegions, regionMapping
            else:     
                print "Using regions_splitCR_4mTregions.py for definition of regions."
                from StopsCompressed.Analysis.regions_splitCR_4mTregions       import controlRegions, signalRegions, regionMapping
        else:
            print "Using regions_splitCR.py for definition of regions."
            from StopsCompressed.Analysis.regions_splitCR	                   import controlRegions, signalRegions, regionMapping
    elif options.mT_cut_value == 100: 
        print "Using regions_splitCR_mT100.py for definition of regions."
        from StopsCompressed.Analysis.regions_splitCR_mT100	                   import controlRegions, signalRegions, regionMapping
    elif options.mT_cut_value == 105:
        print "Using regions_mt105_splitCR.py for definition of regions."
        from StopsCompressed.Analysis.regions_mt105_splitCR	                   import controlRegions, signalRegions, regionMapping
    else:
        raise NotImplementedError
elif options.lowMETregion: 
    if options.mTregions == '3':
        _NBINS = 80
        print "Using regions_lowMET.py for definition of regions."
        from StopsCompressed.Analysis.regions_lowMET  	                           import controlRegions, signalRegions, regionMapping, regionNames
    elif options.mTregions == '4':
        if options.splitCTZ:
            if options.lowHTbin:
                _NBINS = 136
                print "Using regions_lowMET_4mTregions_splitCTZ_lowHTbin.py for definition of regions."
                from StopsCompressed.Analysis.regions_lowMET_4mTregions_splitCTZ_lowHTbin import controlRegions, signalRegions, regionMapping, regionNames
            else:
                _NBINS = 104
                print "Using regions_lowMET_4mTregions_splitCTZ.py for definition of regions."
                from StopsCompressed.Analysis.regions_lowMET_4mTregions_splitCTZ          import controlRegions, signalRegions, regionMapping, regionNames
        else:
            _NBINS = 104
            print "Using regions_lowMET_4mTregions.py for definition of regions."
            from StopsCompressed.Analysis.regions_lowMET_4mTregions                import controlRegions, signalRegions, regionMapping, regionNames
    elif options.mTregions == 'low5':
        _NBINS = 132
        print "Using regions_lowMET_low5mTregions.py for definition of regions."
        from StopsCompressed.Analysis.regions_lowMET_low5mTregions                    import controlRegions, signalRegions, regionMapping, regionNames
    elif options.mTregions == 'high5':
        _NBINS = 128
        print "Using regions_lowMET_high5mTregions.py for definition of regions."
        from StopsCompressed.Analysis.regions_lowMET_high5mTregions               import controlRegions, signalRegions, regionMapping, regionNames
    elif options.mTregions == '5' and options.splitCTZ and options.lowHTbin: # FIXME: 5 = high5
        _NBINS = 168
        print "Using regions_lowMET_5mTregions_splitCTZ_lowHTbin.py for definition of regions."
        from StopsCompressed.Analysis.regions_lowMET_5mTregions_splitCTZ_lowHTbin import controlRegions, signalRegions, regionMapping, regionNames
    elif options.mTregions == '6':
        if options.splitCTZ:
            if options.lowHTbin:
                _NBINS = 204
                print "Using regions_lowMET_6mTregions_splitCTZ_lowHTbin.py for definition of regions."
                from StopsCompressed.Analysis.regions_lowMET_6mTregions_splitCTZ_lowHTbin import controlRegions, signalRegions, regionMapping, regionNames
        else:
            _NBINS = 156
            print "Using regions_lowMET_6mTregions.py for definition of regions."
            from StopsCompressed.Analysis.regions_lowMET_6mTregions                    import controlRegions, signalRegions, regionMapping, regionNames
    else:
        raise NotImplementedError
else:
    _NBINS = 56
    if (options.mT_cut_value == 95):
        print "Using regions.py for definition of regions."
        from StopsCompressed.Analysis.regions	               import controlRegions, signalRegions, regionMapping, regionNames
    elif (options.mT_cut_value == 100):
        print "Using regions_mT100.py for definition of regions."
        from StopsCompressed.Analysis.regions_mT100	           import controlRegions, signalRegions, regionMapping
    elif (options.mT_cut_value == 105):
        print "Using regions_mt105.py for definition of regions."
        from StopsCompressed.Analysis.regions_mt105	           import controlRegions, signalRegions, regionMapping
    else:
        raise NotImplementedError


sensitivityStudyName = "{}_nbins{}_mt{}_{}mTregions_CT{}_isPrompt{}_lowMETregion{}".format(options.sensitivityStudyName, _NBINS,options.mT_cut_value,options.mTregions,options.CT_cut_value,options.isPrompt,options.lowMETregion)

# signal
if options.year == "2016":
    from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import signals_T2tt
    signals = signals_T2tt
elif options.year == "2018":
    from StopsCompressed.samples.nanoTuples_Autumn18_signal_postProcessed import signals_T2tt, signals_T2bW, signals_TChiWZ
    signals = signals_T2tt + signals_T2bW + signals_TChiWZ
else:
    raise NotImplementedError

# Logging
import StopsCompressed.Tools.logger as logger
logger = logger.get_logger(options.logLevel, logFile = None )
import Analysis.Tools.logger as logger_an
logger_an = logger_an.get_logger(options.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger('INFO', logFile = None )


from StopsCompressed.Analysis.Setup import Setup
from StopsCompressed.Analysis.SetupHelpers import *
channels = allChannels # ['all']
#channels = lepChannels # ['e', 'mu']
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

if options.isPrompt:
	setup.parameters["l1_prompt"] = True
#if options.isdPhiMetJets:
#	setup.parameters["dphiMetJets"] = True
#	setup.parameters["dphiJets"] 	= False
#if options.isdPhiComb:
#	setup.parameters["dphiMetJets"] = True
#	setup.parameters["dphiJets"] 	= True
estimators = estimatorList(setup)

estList = ['WJets','Top','Others', 'ZInv', 'QCD'] # ordered as opposed to below..
#estList = setup.processes.keys() # = smarter way? equivalent as estList defined from processes in setup?
#estList.remove('Data')

allEstimators = estimators.constructEstimatorList(estList)
if options.makeYieldsTable: 
    allEstimators += [ MCBasedEstimate(name=s.name, sample=s) for s in signals if s.name in ["T2tt_550_510", "TChiWZ_200_170"]] # NOTE: choosing several signal points for yields table
else:
    allEstimators += [ MCBasedEstimate(name=s.name, sample=s) for s in signals]

if options.selectEstimator:
    # Select estimate
    if not options.selectEstimator == 'Data':
        estimate = next((e for e in allEstimators if e.name == options.selectEstimator), None)
        estimate.isData = False
    else:
        estimate = DataObservation(name='Data', sample=setup.processes['Data'], cacheDir=setup.defaultCacheDir(specificNameForSensitivityStudy=sensitivityStudyName))
        estimate.isSignal = False
        estimate.isData   = True
    
    if not estimate:
      logger.warn(options.selectEstimator + " not known")
      exit(0)
    
    for sig in ['T2tt', 'T2bW', 'TChiWZ', 'TTbarDM', 'T8bbllnunu']:
        if estimate.name.count(sig): estimate.isSignal = True
    
    for sig in ['T2tt', 'T2bW', 'TChiWZ']: # not sure about TT, T8 etc.
        isFastSim = estimate.name.count(sig)
    else:
        isFastSim = False
    
    if isFastSim:
      setup = setup.sysClone(sys={'reweight':['reweightLeptonFastSimSF'], 'remove':['reweightPU36fb']})

    #setup = setup.sysClone()
    setup.verbose=True
    def wrapper(args):
            r,channel,setup = args
            logger.info("Running estimate for region %s, channel %s for estimator %s"%(r,channel, options.selectEstimator if options.selectEstimator else "None"))
            res = estimate.cachedEstimate(r,channel, setup, save=True, overwrite=options.overwrite)
            #print "Estimate:", res
            return (estimate.uniqueKey(r,channel, setup), res )
    
    estimate.initCache(setup.defaultCacheDir(specificNameForSensitivityStudy=sensitivityStudyName))
    
    jobs=[]
    for channel in channels:
        for (i, r) in enumerate(allRegions):
            if options.selectRegion is not None and options.selectRegion != i: continue
            jobs.append((r, channel, setup))
            if not estimate.isData and not options.noSystematics:
                if estimate.isSignal: jobs.extend(estimate.getSigSysJobs(r,channel,  setup, isFastSim))
                else:                 jobs.extend(estimate.getBkgSysJobs(r,channel,  setup))
    
    results = map(wrapper, jobs)
    #print "Results:", results
    for channel in (['all']):
        for (i, r) in enumerate(allRegions):
            #print r
            if options.selectRegion is not None and options.selectRegion != i: continue
            if options.useGenMet: estimate.cachedEstimate(r, setup.sysClone({'selectionModifier':'genMet'}), save=True, overwrite=options.overwrite)
            else: estimate.cachedEstimate(r,channel, setup, save=True, overwrite=options.overwrite)
            if not estimate.isData and not options.noSystematics:
                if estimate.isSignal: 
                    map(lambda args:estimate.cachedEstimate(*args, save=True, overwrite=options.overwrite), estimate.getSigSysJobs(r, channel,  setup, isFastSim))
                else: 
                    map(lambda args:estimate.cachedEstimate(*args, save=True, overwrite=options.overwrite), estimate.getBkgSysJobs(r,  channel, setup))
    		# print estimate.getBkgSysJobs(r,  channel, setup) 
    
            logger.info('Done with region: %s', r)
        logger.info('Done with channel: %s', channel)
    logger.info('Done.')


# Yields Table

if options.makeYieldsTable and not options.selectRegion and options.noSystematics and not options.selectEstimator:
    allResults = {}
    
    newRegionsOnly = False
    suffix = ""
    if newRegionsOnly: suffix += "_newRegionsOnly"
    
    scaleYieldsTable = 0.6
    
    if scaleYieldsTable != 1:
        suffix += "_scaled{}".format(scaleYieldsTable).replace(".","p")

    from StopsCompressed.Tools.user import plot_directory#, analysis_results

    texdir = os.path.join(plot_directory, 'yields', options.year, 'yieldsTables', sensitivityStudyName) 

    if not os.path.exists(texdir): os.makedirs(texdir)
    
    for channel in channels:
        for res in allEstimators:
            res.initCache(setup.defaultCacheDir(specificNameForSensitivityStudy=sensitivityStudyName))
            allResults[res.name] = {} 
            for (i, r) in enumerate(allRegions):
                allResults[res.name][r] = res.cachedEstimate(r, channel, setup, overwrite = False) * scaleYieldsTable

        estListFull = estList + [x for x in allResults.keys() if x not in estList] # workaround to get ordered table 
        ofile = "yieldsTable_%s_%s%s.tex"%(sensitivityStudyName, channel, suffix)
        ofilename = "%s/%s"%(texdir,ofile)
        print "Writing to ", ofilename 
        with open(ofilename, "w") as f:
            f.write("\\documentclass[a4paper,10pt,oneside]{article} \n \\usepackage{caption} \n \\usepackage{rotating} \n")
            f.write("\\usepackage[a4paper,bindingoffset=0.2in,left=1cm,right=1cm,top=1cm,bottom=1cm,footskip=.25in]{geometry} \n")
            f.write("\\begin{document}\n")
            f.write("\\begin{table}\n")
            f.write("\\centering\n")
            f.write("\\begin{tabular}{|c" + "|c"*len(allResults) + "|} \n")
            f.write("\\hline Region & " + " & ".join(res for res in estListFull).replace("_", "\_") + "\\\\ \\hline \\hline \n")
            for (i, r) in enumerate(allRegions):
                if newRegionsOnly and not 'Z' in regionNames[i]: continue # selecting new regions only
                f.write("%s & "%regionNames[i] + " & ".join("${:0.1f} \pm {:1.1f}$".format(allResults[res][r].val, allResults[res][r].sigma) for res in estListFull) + "\\\\ \\hline \n")
            f.write("\\end{tabular}\n")
            f.write("\\end{table}\n")
            f.write("\\end{document}")
        os.system("cd "+texdir+";pdflatex "+ofile)
