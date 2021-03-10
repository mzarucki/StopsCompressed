#!/usr/bin/env python
#regionsLegacytest1
import ROOT
import os
import math
import pickle
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',       action='store', default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],             help="Log level for logging")
argParser.add_argument("--signal",         action='store', default='T2tt',          nargs='?', choices=["T2tt","TTbarDM","T8bbllnunu_XCha0p5_XSlep0p05", "T8bbllnunu_XCha0p5_XSlep0p5", "T8bbllnunu_XCha0p5_XSlep0p95", "T2bt","T2bW", "T8bbllnunu_XCha0p5_XSlep0p09", "ttHinv"], help="which signal?")
argParser.add_argument("--only",           action='store', default=None,            nargs='?',                                                                                           help="pick only one masspoint?")
argParser.add_argument("--scale",          action='store', default=1.0, type=float, nargs='?',                                                                                           help="scaling all yields")
argParser.add_argument("--overwrite",      default = False, action = "store_true", help="Overwrite existing output files")
argParser.add_argument("--keepCard",       default = False, action = "store_true", help="Overwrite existing output files")
argParser.add_argument("--control2016",    default = False, action = "store_true", help="Fits for DY/VV/TTZ CR")
argParser.add_argument("--signal2016",     default = False, action = "store_true", help="Fits for DY/VV/TTZ CR")
argParser.add_argument("--controlDYVV",    default = False, action = "store_true", help="Fits for DY/VV CR")
argParser.add_argument("--controlTTZ",     default = False, action = "store_true", help="Fits for TTZ CR")
argParser.add_argument("--controlTT",      default = False, action = "store_true", help="Fits for TT CR (MT2ll<100)")
argParser.add_argument("--controlAll",     default = False, action = "store_true", help="Fits for all CRs")
argParser.add_argument("--fitAll",         default = False, action = "store_true", help="Fits SR and CR together")
argParser.add_argument("--fitAllNoTT",     default = False, action = "store_true", help="Fits SR and CR together")
argParser.add_argument("--aggregate",      default = False, action = "store_true", help="Use aggregated signal regions")
argParser.add_argument("--expected",       default = False, action = "store_true", help="Use sum of backgrounds instead of data.")
argParser.add_argument("--unblind",        default = False, action = "store_true", help="Use real data in the signal regions.")
argParser.add_argument("--DMsync",         default = False, action = "store_true", help="Use two regions for MET+X syncing")
argParser.add_argument("--noSignal",       default = False, action = "store_true", help="Don't use any signal (force signal yield to 0)?")
argParser.add_argument("--useTxt",         default = False, action = "store_true", help="Use txt based cardFiles instead of root/shape based ones?")
argParser.add_argument("--fullSim",        default = False, action = "store_true", help="Use FullSim signals")
argParser.add_argument("--signalInjection",default = False, action = "store_true", help="Inject signal?")
argParser.add_argument("--significanceScan",         default = False, action = "store_true", help="Calculate significance instead?")
argParser.add_argument("--removeSR",       default = [], nargs='*', action = "store", help="Remove signal region(s)?")
argParser.add_argument("--skipFitDiagnostics", default = False, action = "store_true", help="Don't do the fitDiagnostics (this is necessary for pre/postfit plots, but not 2D scans)?")
argParser.add_argument("--extension",      default = '', action = "store", help="Extension to dir name?")
argParser.add_argument("--year",           default=2016,     action="store",      help="Which year?")
argParser.add_argument("--dpm",            default= False,   action="store_true",help="Use dpm?",)
argParser.add_argument("--scaleWjets",     default=0.0, choices=[0.0,-0.1,0.1], type=float,  action="store",help="scaling Wjets for testing",)
argParser.add_argument("--scaleTTbar",     default=0.0, choices=[0.0,-0.1,0.1], type=float,   action="store",help="scaling TTbar for testing",)

args = argParser.parse_args()

removeSR = [ int(r) for r in args.removeSR ] if len(args.removeSR)>0 else False

year = int(args.year)

# Logging
import Analysis.Tools.logger as logger 
logger  = logger.get_logger(args.logLevel, logFile = None)

import StopsCompressed.Tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import Analysis.Tools.logger as logger_an
logger_an = logger_an.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger('INFO', logFile = None )

from RootTools.core.standard import *
from StopsCompressed.Tools.user            import cache_directory 
from StopsCompressed.Analysis.test_Setup import Setup
from StopsCompressed.Analysis.SetupHelpers import *
from StopsCompressed.Analysis.estimators   import *
from StopsCompressed.Analysis.backup_regions      import regionMapping,signalRegions, controlRegions, region
#from StopsCompressed.Analysis.regions_splitCR      import signalRegions, controlRegions
#from StopsCompressed.Analysis.regions_splitCR_v2      import signalRegions, controlRegions
from StopsCompressed.Analysis.MCBasedEstimate import MCBasedEstimate
from StopsCompressed.Analysis.DataObservation import DataObservation
from StopsCompressed.Analysis.Cache           import Cache
from copy import deepcopy
from Analysis.Tools.u_float    import u_float
from math                           import sqrt
#read gen filter efficicency
from StopsCompressed.Tools.genFilter import genFilter
genFilter = genFilter(year=year)
##https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSYSignalSystematicsRun2
from Analysis.Tools.cardFileWriter import testCardFileWriter

setup = Setup(year=year)
def getRegion(region, CR=False):
	if CR == True:
		for key,val in region.items():
			if 'CR' in key:
				CR.append(region)
		return CR
		#CR = [val for key,val in region.items() if 'CR' in key]
		#return CR
	else:
		for key,val in region.items():
			if 'SR' in key:
				SR.append(region)
		return SR
		#SR = [val for key,val in region.items() if 'SR' in key]
		#return SR

# Define channels for CR
#setup.channels = lepChannels
setup.channels = allChannels

# Define regions for CR
if args.control2016:
	setup.regions   = controlRegions
elif args.signal2016:
	setup.regions   = signalRegions
elif args.fitAll:
	setup.regions   = controlRegions+signalRegions

# Define estimators for CR
estimators           = estimatorList(setup)
setup.estimators     = estimators.constructEstimatorList(['WJets','DY','Top','ZInv','singleTop', 'VV', 'TTX', 'QCD'])

setups = [setup]

if args.control2016:       subDir = 'CRregion_test3'
elif args.signal2016:       subDir = 'SRregion_test3'
elif args.fitAll:	subDir = 'fitAllregion_test3'
#else:                       subDir += 'signalOnly'

baseDir = os.path.join(setup.analysis_results, str(year), subDir)

sSubDir = 'expected' if args.expected else 'observed'
#if args.signalInjection: sSubDir += '_signalInjected'
#
limitDir    = os.path.join(baseDir, 'cardFiles', args.signal + args.extension, sSubDir)
overWrite   = (args.only is not None) or args.overwrite
if args.keepCard:
    overWrite = False
useCache    = True
verbose     = True

if not os.path.exists(limitDir): os.makedirs(limitDir)
cacheFileName = os.path.join(limitDir, 'calculatedLimits')
limitCache    = Cache(cacheFileName, verbosity=2)

cacheFileNameS  = os.path.join(limitDir, 'calculatedSignifs')
signifCache     = Cache(cacheFileNameS, verbosity=2)

fastSim = False # default value
if   args.signal == "T2tt" and not args.fullSim:    fastSim = True

if fastSim:
    logger.info("Assuming the signal sample is FastSim!")
else:
    logger.info("Assuming the signal sample is FullSim!")

## load the signal scale cache
from StopsCompressed.Tools.resultsDB       import resultsDB

#cacheDir    = "/afs/hephy.at/data/cms05/StopsDileptonLegacy/results/PDF_v2_NNPDF30/%s/"%year
#scale_cache = resultsDB(cacheDir+'PDFandScale_unc.sq', "scale", ["name", "region", "CR", "channel", "PDFset"])
#PDF_cache   = resultsDB(cacheDir+'PDFandScale_unc.sq', "PDF", ["name", "region", "CR", "channel", "PDFset"])

def getScaleUnc(name, r, niceName, channel):
  scaleUnc = scale_cache.get({"name": name, "region":r, "CR":niceName, "channel":channel, "PDFset":'scale'})
  scaleUnc = scaleUnc.val if scaleUnc else 0
  return min(max(0.01, scaleUnc),0.10)

def getPDFUnc(name, r, niceName, channel):
  PDFUnc = PDF_cache.get({"name": name, "region":r, "CR":niceName, "channel":channel, "PDFset":'NNPDF30'})
  PDFUnc = PDFUnc.val if PDFUnc else 0
  return min(max(0.01, PDFUnc),0.10)

def wrapper(s):
    xSecScale = 1
    #print "mStop: ", s.mStop, "mNeu: ", s.mNeu
    genEff = genFilter.getEff(s.mStop,s.mNeu)
    if genEff ==0 :
	    print "no gen eff found in map for %s,%s", s.mStop, s.mNeu
	    genEff = 0.48
    c = testCardFileWriter.cardFileWriter()
    c.releaseLocation = os.path.abspath('.') # now run directly in the run directory

    logger.info("Running over signal: %s", s.name)

    cardFileName = os.path.join(limitDir, s.name+'.txt')
    if not os.path.exists(cardFileName) or overWrite:
        counter=0
        c.reset()
        c.setPrecision(3)
        shapeString = 'lnN' if args.useTxt else 'shape'
        # experimental
        #JEC     = 'JEC_%s'%year
        #JER     = 'JER_%s'%year
        #PU      = 'PU_%s'%year
        Lumi    = 'Lumi_%s'%year
        #leptonSF    = 'leptonSF_%s'%year
        #c.addUncertainty(PU,           shapeString)
	#c.addUncertainty(JEC,          shapeString)
	#c.addUncertainty(JER,          shapeString)
        c.addUncertainty(Lumi,          "lnN")
        # c.addUncertainty(Lumi,          shapeString)
        #c.addUncertainty(leptonSF,   shapeString)
        #c.addRateParameter("WJets", 1,'[0.5,1.5]')
        #c.addRateParameter("Top", 1,'[0.5,1.5]')
	c.addCR(controlRegions)
	c.addSR(signalRegions)
        for setup in setups:
          eSignal     = MCBasedEstimate(name=s.name, sample=s, cacheDir=setup.defaultCacheDir())
          observation = DataObservation(name='Data', sample=setup.processes['Data'], cacheDir=setup.defaultCacheDir())
          for e in setup.estimators: e.initCache(setup.defaultCacheDir())
	  #CR1aXbin=[]
	  #CR1aYbin=[]
	  for r in setup.regions:
            print r 
            for channel in setup.channels:
                niceName = ' '.join([channel, r.__str__()])
                logger.info("Bin name: %s", niceName)
                binname = 'Bin'+str(counter)
                counter += 1
                total_exp_bkg = 0
                c.addBin(binname, [e.name.split('-')[0] for e in setup.estimators ], niceName)
		#if 'CT1>=300'in niceName:
		#	print "should be only CT1>=300 in nicename: ", niceName
		#	#c.addFreeParameter("CR1aXW", 'WJets',1,'[0.,10.]')
		#	CR1aXbin.append(binname)
		#elif 'CT1>=400'in niceName:
		#	print "should be only CT1>=400 in nicename: ", niceName
		#	#c.addFreeParameter("CR1aXW", 'WJets',1,'[0.,10.]')
		#	CR1aYbin.append(binname)
                for e in setup.estimators:
                  name = e.name.split('-')[0]
		  #print name
                  expected = e.cachedEstimate(r, channel, setup)

                  Wcorr = 0
                  if e.name.count('WJets'):
                    Wcorr = expected.val*args.scaleWjets
                
                  TTbarcorr = 0
                  if e.name.count('Top'):
                    TTbarcorr = expected.val*args.scaleTTbar
                    
                  total_exp_bkg += expected.val
                  total_exp_bkg += Wcorr
                  total_exp_bkg += TTbarcorr
                  
                  logger.info("Expectation for process %s: %s", e.name, expected.val)                                                                                                                       
                  
                  expected = expected * args.scale
                  logger.info("Expectation for process %s: %s", e.name, expected.val)
                  if e.name.count('WJets'):
                    c.specifyExpectation(binname, 'WJets',  expected.val)
#                    W_SF = 1
#                    if W_SF != 1: logger.warning("Scaling WJets background by %s", W_SF)
#                    c.specifyExpectation(binname, 'WJets',  expected.val * W_SF)
                  elif e.name.count("DY"):
                    DY_SF = 1
                    c.specifyExpectation(binname, name, expected.val*DY_SF)
                    if DY_SF != 1: logger.warning("Scaling DY background by %s", DY_SF)
                  elif e.name.count("Top"):
                    Top_SF = 1
                    c.specifyExpectation(binname, name, expected.val*Top_SF)
                    if Top_SF != 1: logger.warning("Scaling Top background by %s", Top_SF)
                  elif e.name.count("singleTop"):
                    singleTop_SF = 1
                    c.specifyExpectation(binname, name, expected.val*singleTop_SF)
                    if singleTop_SF != 1: logger.warning("Scaling singleTop background by %s", singleTop_SF)
                  elif e.name.count("VV"):
                    c.specifyExpectation(binname, name, expected.val)
                  elif e.name.count("ZInv"):
                    c.specifyExpectation(binname, name, expected.val)
                  elif e.name.count("TTX"):
                    TTX_SF = 1
#                    TTX_expected = TTX.cachedEstimate(r, channel, setup)
#                    logger.info("TTX expected %s", expected.val)
#                    expected = expected+TZX_expected
#                    logger.info("TTX expected %s", expected.val)
                    c.specifyExpectation(binname, name, expected.val*TTX_SF)
                    if TTX_SF != 1: logger.warning("Scaling TTX background by %s", TTX_SF)
                  elif e.name.count("QCD"):
                    c.specifyExpectation(binname, name, expected.val)
#                    #c.specifyUncertainty("TTX", binname, name, 1.10)
#                  elif e.name.count("TZX"):
#                    logger.info("TZX has been added to TTZ")
#                  elif e.name.count("TTXNoZ") or e.name.count("rare"):
#                    c.specifyExpectation(binname, name, expected.val)

                  if expected.val>0 or True:
                      names = [name]
                      for name in names:
                        sysChannel = 'all' # could be channel as well
                        uncScale = 1
                        #c.specifyUncertainty(PU,         binname, name, 1 + e.PUSystematic(         r, sysChannel, setup).val * uncScale )
			#if JEC > 0.0005:
			#	c.specifyUncertainty(JEC,        binname, name, 1 + e.JECSystematic(        r, sysChannel, setup).val )
			#if JER > 0.0005:
                        #	c.specifyUncertainty(JER,        binname, name, 1 + e.JERSystematic(        r, sysChannel, setup).val)
                        #c.specifyUncertainty(leptonSF, binname, name, 1 + e.leptonSFSystematic(   r, channel, setup).val * uncScale ) 

                        #MC bkg stat (some condition to neglect the smaller ones?)
                        uname = 'Stat_'+binname+'_'+name
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, name, 1 + (expected.sigma/expected.val) * uncScale if expected.val>0 else 1)
		c.addMap(regionMapping)	
                #signal
                eSignal.isSignal = True
                e = eSignal
		#genEff = 0.3
                
                if fastSim:
#                    if args.signal == 'T2tt': # change this for next round. small impact
#                        signalSetup = setup.sysClone(sys={'reweight':['reweight_nISR', 'reweightLeptonFastSimSF']})
#                    else:
#                        signalSetup = setup.sysClone(sys={'reweight':[ 'reweightLeptonFastSimSF'], 'remove':[]})
		    signalSetup = setup.sysClone()
                    if year == 2016:
                        #signal = 0.5 * (e.cachedEstimate(r, channel, signalSetup) + e.cachedEstimate(r, channel, signalSetup.sysClone({'selectionModifier':'GenMET'})))
                        signal = 0.5 * (e.cachedEstimate(r, channel, signalSetup) + e.cachedEstimate(r, channel, signalSetup))
                    else:
                        signal = e.cachedEstimate(r, channel, signalSetup)
                else:
                    signalSetup = setup.sysClone(sys={'reweight':['reweight_nISR'], 'remove':[]}) 
                    signal = e.cachedEstimate(r, channel, signalSetup)

                signal = signal * args.scale

                if signal.val<0.01 and niceName.count("control")==0:
                    signal.val = 0.001
                    signal.sigma = 0.001
                #c.specifyExpectation(binname, 'signal', signal.val*xSecScale )
                c.specifyExpectation(binname, 'signal', signal.val*xSecScale*genEff )


                #logger.info("Signal expectation: %s", signal.val*xSecScale)
                logger.info("Signal expectation: %s", signal.val*xSecScale*genEff)


                if signal.val>0.001:
                  if not fastSim:
                    c.specifyUncertainty('PDF',      binname, 'signal', 1 + getPDFUnc(eSignal.name, r, niceName, channel))
                    logger.info("PDF uncertainty for signal is: %s", getPDFUnc(eSignal.name, r, niceName, channel))
                  #c.specifyUncertainty(PU,              binname, 'signal', 1 + e.PUSystematic(         r, channel, signalSetup).val )
                  #if not args.useTxt:
                    #c.specifyUncertainty(JEC,             binname, 'signal', 1 + e.JECSystematic(        r, channel, signalSetup).val )
#                    c.specifyUncertainty(unclEn,          binname, 'signal', e.unclusteredSystematicAsym(r, channel, signalSetup) )
                    #c.specifyUncertainty(JER,             binname, 'signal', 1 + e.JERSystematic(        r, channel, signalSetup).val )
                  #else:
                    #c.specifyUncertainty(JEC,             binname, 'signal', 1 + e.JECSystematic(        r, channel, signalSetup).val[1] )
#                    c.specifyUncertainty(unclEn,          binname, 'signal', e.unclusteredSystematicAsym(r, channel, signalSetup)[1] )
                    #c.specifyUncertainty(JER,             binname, 'signal', 1 + e.JERSystematic(        r, channel, signalSetup).val[1] )
                  #c.specifyUncertainty(SFb,             binname, 'signal', 1 + e.btaggingSFbSystematic(r, channel, signalSetup).val )
                  #c.specifyUncertainty(SFl,             binname, 'signal', 1 + e.btaggingSFlSystematic(r, channel, signalSetup).val )
                  #c.specifyUncertainty(leptonSF,      binname, 'signal', 1 + e.leptonSFSystematic(   r, channel, signalSetup).val )
#
                  #if fastSim: 
                  #  c.specifyUncertainty('btagFS',   binname, 'signal', 1 + e.btaggingSFFSSystematic(r, channel, signalSetup).val )
                  uname = 'Stat_'+binname+'_signal'
                  c.addUncertainty(uname, 'lnN')
                  c.specifyUncertainty(uname, binname, 'signal', 1 + signal.sigma/signal.val if signal.val>0 else 1 )
            
                else:
                  uname = 'Stat_'+binname+'_signal'
                  c.addUncertainty(uname, 'lnN')
                  c.specifyUncertainty(uname, binname, 'signal', 1 )
                
                logger.info("Done with MC. Now working on observation.")
                ## Observation ##
                # expected
                #if (args.expected or (not args.unblind and not niceName.count('control'))) and not args.signalInjection:
                if args.expected :
                    c.specifyObservation(binname, int(round(total_exp_bkg,0)))
                    logger.info("Expected observation: %s", int(round(total_exp_bkg,0)))
                # expected with signal injected
                elif args.signalInjection:
                    pseudoObservation = int(round(total_exp_bkg+signal.val,0))
                    c.specifyObservation(binname, pseudoObservation)
                    logger.info("Expected observation (signal is injected!): %s", pseudoObservation)
                # real observation (can be scaled for studies)
                else:
		    #print "be here", total_exp_bkg
                    c.specifyObservation(binname, int(args.scale*observation.cachedObservation(r, channel, setup).val))
                    logger.info("Observation: %s", int(args.scale*observation.cachedObservation(r, channel, setup).val))
                
	c.addRateParameter('WJets',1,'[0.,10.]')
	# c.addRateParameter('Top',1,'[0.,10.]')
	#c.addRateParameter("CR1aYW", 'WJets',1,'[0.,10.]')
	#c.addFreeParamBin("CR1aXW",CR1aXbin)
	#c.addFreeParamBin("CR1aYW",CR1aYbin)
        if year == 2016:
            lumiUncertainty = 1.025
        elif year == 2017:
            lumiUncertainty = 1.023
        elif year == 2018:
            lumiUncertainty = 1.025
        
        c.specifyFlatUncertainty(Lumi, lumiUncertainty)
        cardFileNameTxt     = c.writeToFile(cardFileName,noMCStat=True)
        cardFileNameShape   = c.writeToShapeFile(cardFileName.replace('.txt', '_shape.root'), noMCStat=True)
        cardFileName = cardFileNameTxt if args.useTxt else cardFileNameShape
    else:
        print "File %s found. Reusing."%cardFileName
    
    if   args.signal == "TTbarDM":                      sConfig = s.mChi, s.mPhi, s.type
    elif args.signal == "T2tt":                         sConfig = s.mStop, s.mNeu
    elif args.signal == "T2bt":                         sConfig = s.mStop, s.mNeu
    elif args.signal == "T2bW":                         sConfig = s.mStop, s.mNeu
    elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p05": sConfig = s.mStop, s.mNeu
    elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p09": sConfig = s.mStop, s.mNeu
    elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p5":  sConfig = s.mStop, s.mNeu
    elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p95": sConfig = s.mStop, s.mNeu
    elif args.signal == "ttHinv":                       sConfig = ("ttHinv", "2l")

    if not args.significanceScan:
        if useCache and not overWrite and limitCache.contains(sConfig):
          res = limitCache.get(sConfig)
        else:
          res = c.calcLimit(cardFileName)#, options="--run blind")
          if not args.skipFitDiagnostics:
              c.calcNuisances(cardFileName)
          limitCache.add(sConfig, res)
    else:
        if useCache and not overWrite and signifCache.contains(sConfig):
            res = signifCache.get(sConfig)
        else:
            res = c.calcSignif(cardFileName)
            signifCache.add(sConfig,res)
    

    ###################
    # extract the SFs #
    ###################
    if not args.useTxt and args.only and not args.skipFitDiagnostics:
        # Would be a bit more complicated with the classical txt files, so only automatically extract the SF when using shape based datacards
        from StopsCompressed.Tools.getPostFit import getPrePostFitFromMLF
        
        # get the most signal region like bins


        print cardFileName
        combineWorkspace = cardFileName.replace('shapeCard.txt','shapeCard_FD.root')
        print "Extracting fit results from %s"%combineWorkspace
        
        try:
            fitResults      = getPrePostFitFromMLF(combineWorkspace)
        except:
            fitResults = False

        if fitResults:
            
	    for r in range(12) :
		    preFitResults   = fitResults['results']['shapes_prefit']['Bin{}'.format(r)]
		    preFitShapes    = fitResults['hists']['shapes_prefit']['Bin{}'.format(r)]
		    postFitResults  = fitResults['results']['shapes_fit_b']['Bin{}'.format(r)]
		    postFitShapes   = fitResults['hists']['shapes_fit_b']['Bin{}'.format(r)]
		    print "WJet-sprefit" ,  preFitResults['WJets']
		    print "WJet-spostfit" ,postFitResults['WJets']
		    print 
		    print "Top-prefit" ,  preFitResults['Top']
		    print "Top-postfit" ,postFitResults['Top']
		    print 
		    print "DY-prefit" ,  preFitResults['DY']
		    print "DY-postfit" ,postFitResults['DY']
		    print 
		    print "singleTop-prefit" ,  preFitResults['singleTop']
		    print "singleTop-postfit" ,postFitResults['singleTop']
		    print 
		    print "VV-prefit" ,  preFitResults['VV']
		    print "VV-postfit" ,postFitResults['VV']
		    print 
		    print "ZInv-prefit" ,  preFitResults['ZInv']
		    print "ZInv-postfit" ,postFitResults['ZInv']
		    print 
		    print "TTX-prefit" ,  preFitResults['TTX']
		    print "TTX-postfit" ,postFitResults['TTX']
		    # print 
		    # print "QCD-prefit" ,  preFitResults['QCD']
		    # print "QCD-postfit" ,postFitResults['QCD']
		    top_prefit  = preFitResults['Top']
		    top_postfit = postFitResults['Top']
		    top_prefit_SR_err   = ROOT.Double()
		    top_postfit_SR_err  = ROOT.Double()

		    WJ_prefit  = preFitResults['WJets']
		    WJ_postfit = postFitResults['WJets']
		    WJ_prefit_SR_err   = ROOT.Double()
		    WJ_postfit_SR_err  = ROOT.Double()
		    #
		    TTX_prefit  = preFitResults['TTX']
		    TTX_postfit = postFitResults['TTX']

		    #ttZ_prefit_SR_err   = ROOT.Double()
		    #ttZ_postfit_SR_err  = ROOT.Double()
		    #ttZ_prefit_SR  = preFitShapes['TTZ'].IntegralAndError(iBinTTZLow, iBinTTZHigh, ttZ_prefit_SR_err)
		    #ttZ_postfit_SR = postFitShapes['TTZ'].IntegralAndError(iBinTTZLow, iBinTTZHigh, ttZ_postfit_SR_err)
		    #
		    DY_prefit  = preFitResults['DY']
		    DY_postfit = postFitResults['DY']

		    DY_prefit_SR_err   = ROOT.Double()
		    DY_postfit_SR_err  = ROOT.Double()
		    #
		    MB_prefit  = preFitResults['VV']
		    MB_postfit = postFitResults['VV']
		    #
		    QCD_prefit_SR_err   = ROOT.Double()
		    QCD_postfit_SR_err  = ROOT.Double()

		    #MB_prefit_SR_err   = ROOT.Double()
		    #MB_postfit_SR_err  = ROOT.Double()
		    #MB_prefit_SR  = preFitShapes['multiBoson'].IntegralAndError(iBinDYLow, iBinDYHigh, MB_prefit_SR_err)
		    #MB_postfit_SR = postFitShapes['multiBoson'].IntegralAndError(iBinDYLow, iBinDYHigh, MB_postfit_SR_err)

		    #other_prefit  = preFitResults['TTXNoZ']
		    #other_postfit = postFitResults['TTXNoZ']

		    #other_prefit_SR_err   = ROOT.Double()
		    #other_postfit_SR_err  = ROOT.Double()
		    #other_prefit_SR  = preFitShapes['TTXNoZ'].IntegralAndError(iBinOtherLow, iBinOtherHigh, other_prefit_SR_err)
		    #other_postfit_SR = postFitShapes['TTXNoZ'].IntegralAndError(iBinOtherLow, iBinOtherHigh, other_postfit_SR_err)

		    print
		    print "## Scale Factors for backgrounds, integrated over {} regions: ##".format(r)
		    print "{:20}{:4.2f}{:3}{:4.2f}".format('top:',          (top_postfit/top_prefit).val, '+/-',  top_postfit.sigma/top_postfit.val)
		    print "{:20}{:4.2f}{:3}{:4.2f}".format('WJ:',          (WJ_postfit/WJ_prefit).val, '+/-',  WJ_postfit.sigma/WJ_postfit.val)
		    print "{:20}{:4.2f}{:3}{:4.2f}".format('TTX:',          (TTX_postfit/TTX_prefit).val, '+/-',  TTX_postfit.sigma/TTX_postfit.val)
		    print "{:20}{:4.2f}{:3}{:4.2f}".format('Drell-Yan:',    (DY_postfit/DY_prefit).val,   '+/-',  DY_postfit.sigma/DY_postfit.val)
		    print "{:20}{:4.2f}{:3}{:4.2f}".format('multiBoson:',   (MB_postfit/MB_prefit).val,   '+/-',  MB_postfit.sigma/MB_postfit.val)
		    #print "{:20}{:4.2f}{:3}{:4.2f}".format('other:',        (other_postfit/other_prefit).val, '+/-',  other_postfit.sigma/other_postfit.val)
	#	     AN and split CR have different binning, of course

    if xSecScale != 1:
        for k in res:
            res[k] *= xSecScale
    
    if res: 
      if   args.signal == "TTbarDM":                        sString = "mChi %i mPhi %i type %s" % sConfig
      elif args.signal == "T2tt":                           sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "T2bt":                           sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "T2bW":                           sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p05":   sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p09":   sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p5":    sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "T8bbllnunu_XCha0p5_XSlep0p95":   sString = "mStop %i mNeu %i" % sConfig
      elif args.signal == "ttHinv":                         sString = "ttH->inv"
      if args.significanceScan:
        try:   
            print "Result: %r significance %5.3f"%(sString, res['-1.000'])
            return sConfig, res
        except:
            print "Problem with limit: %r" + str(res)
            return None
      else:
        try:
            print "Result: %r obs %5.3f exp %5.3f -1sigma %5.3f +1sigma %5.3f"%(sString, res['-1.000'], res['0.500'], res['0.160'], res['0.840'])
            return sConfig, res
        except:
            print "Problem with limit: %r"%str(res)
            return None


######################################
# Load the signals and run the code! #
######################################

if args.signal == "T2tt":
    if year == 2016:
        if args.fullSim:
             from StopsCompressed.samples.nanoTuples_Summer16_FullSimSignal_postProcessed import signals_T2tt as jobs
        else:
            #data_directory              = '/scratch/priya.hussain/StopsCompressed/nanoTuples/'
            data_directory              = '/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/'
            postProcessing_directory    = 'compstops_2016_nano_v21/MetSingleLep/'
            #postProcessing_directory    = 'compstops_2016_nano_v11/MetSingleLep/'
            from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import signals_T2tt as jobs
    elif year == 2017:
        if args.fullSim:
             from StopsDilepton.samples.nanoTuples_Fall17_FullSimSignal_postProcessed import signals_T2tt as jobs
        else:
            data_directory              = '/afs/hephy.at/data/cms07/nanoTuples/'
            postProcessing_directory    = 'stops_2017_nano_v0p22/dilep/'
            from StopsDilepton.samples.nanoTuples_FastSim_Fall17_postProcessed import signals_T2tt as jobs
    elif year == 2018:
        if args.fullSim:
            data_directory              = '/afs/hephy.at/data/cms07/nanoTuples/'
            postProcessing_directory    = 'stops_2018_nano_v0p19/inclusive/'
            from StopsDilepton.samples.nanoTuples_Autumn18_FullSimSignal_postProcessed import signals_T2tt as jobs
        else:
            data_directory              = '/afs/hephy.at/data/cms07/nanoTuples/'
            postProcessing_directory    = 'stops_2018_nano_v0p21/dilep/'
            from StopsDilepton.samples.nanoTuples_FastSim_Autumn18_postProcessed import signals_T2tt as jobs


if args.only is not None:
    if args.only.isdigit():
        wrapper(jobs[int(args.only)])
    else:
        
        jobNames = [ x.name for x in jobs ]
        wrapper(jobs[jobNames.index(args.only)])
    exit(0)
results = map(wrapper, jobs)
results = [r for r in results if r]


#########################################################################################
# Process the results. Make 2D hists for SUSY scans, or table for the DM interpretation #
#########################################################################################

limitPrefix = args.signal
if args.significanceScan:
  limitResultsFilename = os.path.join(baseDir, 'limits', args.signal, limitPrefix,'signifResults.root')
else:
  if not os.path.isdir(os.path.join(baseDir, 'limits', args.signal, limitPrefix)):
    os.makedirs(os.path.join(baseDir, 'limits', args.signal, limitPrefix))
  limitResultsFilename = os.path.join(baseDir, 'limits', args.signal, limitPrefix,'limitResults.root')
  pklFile = os.path.join(baseDir, 'limits', args.signal, limitPrefix,'limitResults.pkl')

## new try, other thing is buggy
def toGraph2D(name,title,length,x,y,z):
    result = ROOT.TGraph2D(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i,x[i],y[i],z[i])
    h = result.GetHistogram()
    h.SetMinimum(min(z))
    h.SetMaximum(max(z))
    c = ROOT.TCanvas()
    result.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result

if not args.signal == 'ttHinv':
    mStop_list = []
    mLSP_list  = []
    dm_list  = []
    exp_list   = []
    obs_list   = []
    exp_up_list   = []
    exp_down_list   = []
    
    for r in results:
        s, res = r
        mStop, mNeu = s
	dm = mStop - mNeu
        #if mStop%50>0: continue
        #if mNeu%50>0 and not mNeu>(mStop-125): continue
        mStop_list.append(mStop)
        mLSP_list.append(mNeu)
        dm_list.append(dm)
        exp_list.append(res['0.500'])
        exp_up_list.append(res['0.160'])
        exp_down_list.append(res['0.840'])
        obs_list.append(res['-1.000'])
    
    scatter         = ROOT.TGraph(len(mStop_list))
    scatter.SetName('scatter')
    for i in range(len(mStop_list)):
        scatter.SetPoint(i,mStop_list[i],mLSP_list[i])
    
    exp_graph       = toGraph2D('exp','exp',len(mStop_list),mStop_list,mLSP_list,exp_list)
    exp_up_graph    = toGraph2D('exp_up','exp_up',len(mStop_list),mStop_list,mLSP_list,exp_up_list)
    exp_down_graph  = toGraph2D('exp_down','exp_down',len(mStop_list),mStop_list,mLSP_list,exp_down_list)
    obs_graph       = toGraph2D('obs','obs',len(mStop_list),mStop_list,mLSP_list,obs_list)

    exp_dm_graph       = toGraph2D('exp_dm','exp_dm',len(mStop_list),mStop_list,dm_list,exp_list)
    exp_dm_up_graph    = toGraph2D('exp_dm_up','exp_dm_up',len(mStop_list),mStop_list,dm_list,exp_up_list)
    exp_dm_down_graph  = toGraph2D('exp_dm_down','exp_dm_down',len(mStop_list),mStop_list,dm_list,exp_down_list)
    obs_dm_graph       = toGraph2D('obs_dm','obs_dm',len(mStop_list),mStop_list,dm_list,obs_list)
    
    outfile = ROOT.TFile(limitResultsFilename, "recreate")
    scatter        .Write()
    exp_graph      .Write()
    exp_down_graph .Write()
    exp_up_graph   .Write()
    obs_graph      .Write()

    exp_dm_graph      .Write()
    exp_dm_up_graph   .Write()
    exp_dm_down_graph .Write()
    obs_dm_graph      .Write()
    outfile.Close()
    
    val = {}
    val['stop']  = mStop_list
    val['lsp']   = mLSP_list
    val['dm']    = dm_list
    val['0.500'] = exp_list
    val['0.160'] = exp_up_list
    val['0.840'] = exp_down_list
    val['-1.000'] = obs_list
    #print val
    pickle.dump( val, file(pklFile,'w'))
    print pklFile
    print limitResultsFilename

# Make table for DM
if args.signal == "TTbarDM":
  limitPrefix = args.signal
  # Create table
  texdir = os.path.join(baseDir, 'limits', args.signal, limitPrefix)
  if not os.path.exists(texdir): os.makedirs(texdir)

  for type in sorted(set([type_ for ((mChi, mPhi, type_), res) in results])):
    for lim, key in [['exp','0.500'], ['obs', '-1.000']]:
        chiList = sorted(set([mChi  for ((mChi, mPhi, type_), res) in results if type_ == type]))
        phiList = sorted(set([mPhi  for ((mChi, mPhi, type_), res) in results if type_ == type]))
        ofilename = texdir + "/%s_%s.tex"%(type, lim)
        print "Writing to ", ofilename 
        with open(ofilename, "w") as f:
          f.write("\\begin{tabular}{cc|" + "c"*len(phiList) + "} \n")
          f.write(" & & \multicolumn{" + str(len(phiList)) + "}{c}{$m_\\phi$ (GeV)} \\\\ \n")
          f.write("& &" + " & ".join(str(x) for x in phiList) + "\\\\ \n \\hline \\hline \n")
          for chi in chiList:
            resultList = []
            for phi in phiList:
              result = ''
              try:
                for ((c, p, t), r) in results:
                  if c == chi and p == phi and t == type:
                      result = "%.2f" % r[key]
              except:
                pass
              resultList.append(result)
            if chi == chiList[0]: f.write("\\multirow{" + str(len(chiList)) + "}{*}{$m_\\chi$ (GeV)}")
            f.write(" & " + str(chi) + " & " + " & ".join(resultList) + "\\\\ \n")
          f.write(" \\end{tabular}")
