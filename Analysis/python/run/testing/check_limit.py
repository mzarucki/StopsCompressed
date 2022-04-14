#!/usr/bin/env python
#regionsLegacytest1
import ROOT
import os
import math
import pickle
import argparse
import glob
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
argParser.add_argument("--usePromptSignalOnly",default = False, action = "store_true", help="use only prompt singal events")
argParser.add_argument("--significanceScan",         default = False, action = "store_true", help="Calculate significance instead?")
argParser.add_argument("--removeSR",       default = [], nargs='*', action = "store", help="Remove signal region(s)?")
argParser.add_argument("--skipFitDiagnostics", default = False, action = "store_true", help="Don't do the fitDiagnostics (this is necessary for pre/postfit plots, but not 2D scans)?")
argParser.add_argument("--extension",      default = '', action = "store", help="Extension to dir name?")
argParser.add_argument("--year",           default=2016,     action="store",      help="Which year?")
argParser.add_argument("--dpm",            default= False,   action="store_true",help="Use dpm?",)
argParser.add_argument("--scaleWjets",     default=0.0, choices=[0.0,-0.1,0.1], type=float,  action="store",help="scaling Wjets for testing",)
argParser.add_argument("--scaleTTbar",     default=0.0, choices=[0.0,-0.1,0.1], type=float,   action="store",help="scaling TTbar for testing",)
argParser.add_argument("--l1pT_CR_split",      action='store_true',           default=False,   help="plot region plot background substracted")
argParser.add_argument("--mT_cut_value",       action='store',                default=95, choices=[95,100,105], type=int,   help="plot region plot background substracted")
argParser.add_argument("--extra_mT_cut",       action='store_true',           default=False,   help="plot region plot background substracted")
argParser.add_argument("--CT_cut_value",       action='store',                default=400, type=int,choices=[400,450],   help="plot region plot background substracted")
argParser.add_argument("--isPrompt",           action='store_true',           default=False,   help="promplt leptons contributing to regions")
argParser.add_argument("--R1only",        action='store_true',           default=False,   help="")
argParser.add_argument("--R2only",        action='store_true',           default=False,   help="")


args = argParser.parse_args()

# for macro in glob.glob(os.path.join(os.environ['CMSSW_BASE'], 'src/StopsCompressed/Analysis/python/run/testing/*.C')) :
#   if ROOT.gROOT.LoadMacro(macro): #compile it
#       raise OSError("Unable to load: {}".format(macro))


removeSR = [ int(r) for r in args.removeSR ] if len(args.removeSR)>0 else False

year = str(args.year)

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
from StopsCompressed.Analysis.Setup import Setup
# from StopsCompressed.Analysis.test_Setup import Setup
from StopsCompressed.Analysis.SetupHelpers import *
from StopsCompressed.Analysis.estimators   import *
if (args.l1pT_CR_split) :
    _NBINS = 68
    if (args.mT_cut_value == 95) :
        if (args.extra_mT_cut) :
          _NBINS = 88
          if (args.CT_cut_value == 450 ) :
            from StopsCompressed.Analysis.regions_splitCR_4mTregions_CT450 import controlRegions, signalRegions, regionMapping
          else :  
            if (args.R1only) :
              from StopsCompressed.Analysis.regions_splitCR_4mTregions_R1only import controlRegions, signalRegions, regionMapping
            elif (args.R2only) :
              from StopsCompressed.Analysis.regions_splitCR_4mTregions_R2only import controlRegions, signalRegions, regionMapping
            else :
              from StopsCompressed.Analysis.regions_splitCR_4mTregions import controlRegions, signalRegions, regionMapping
        else :    
          from StopsCompressed.Analysis.regions_splitCR	         import controlRegions, signalRegions, regionMapping
    elif (args.mT_cut_value == 100) :
        from StopsCompressed.Analysis.regions_splitCR_mT100	   import controlRegions, signalRegions, regionMapping
    elif (args.mT_cut_value == 105) :
        from StopsCompressed.Analysis.regions_mt105_splitCR	   import controlRegions, signalRegions, regionMapping
else :
    _NBINS = 56
    if (args.mT_cut_value == 95) :
        from StopsCompressed.Analysis.regions	                 import controlRegions, signalRegions, regionMapping
    elif (args.mT_cut_value == 100) :
        from StopsCompressed.Analysis.regions_mT100	           import controlRegions, signalRegions, regionMapping
    elif (args.mT_cut_value == 105) :
        from StopsCompressed.Analysis.regions_mt105	           import controlRegions, signalRegions, regionMapping

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
from Analysis.Tools.cardFileWriter import cardFileWriter

setup = Setup(year=year)

def getRegion(region, CR=False):
	if CR == True:
		for key,val in region.items():
			if 'CR' in key:
				CR.append(region)
		return CR
	else:
		for key,val in region.items():
			if 'SR' in key:
				SR.append(region)
		return SR
	
# Define channels for CR
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
#setup.estimators     = estimators.constructEstimatorList(['WJets','Top','ZInv','singleTop', 'VV', 'TTX', 'QCD'])
setup.estimators     = estimators.constructEstimatorList(['WJets','Top','ZInv','Others', 'QCD'])
if args.isPrompt:
	        setup.parameters["l1_prompt"] = True
#setup.estimators     = estimators.constructEstimatorList(['WJets','DY','Top','ZInv','singleTop', 'VV', 'TTX', 'QCD'])
# setup.estimators     = estimators.constructEstimatorList(['WJets','Top','ZInv','singleTop', 'VV', 'TTX', 'QCD']) # removing DY

setups = [setup]

if args.control2016:      subDir = 'CRregion_test3'
elif args.signal2016:     subDir = 'SRregion_test3'
#TODO new name here for all mass points needed!
#elif args.fitAll:	        subDir = "fitAllregion_nbins{}_mt{}_extramT{}_CT{}_R1only{}_R2only{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.R1only,args.R2only)
##For UL tests with dPhiMetJets and combination of dphi jets cuts
#elif args.fitAll:	        subDir = "fitAllregion_dphiMetJets_nbins{}_mt{}_extramT{}_CT{}_isPrompt{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.isPrompt)
#elif args.fitAll:	        subDir = "fitAllregion_dphiComb_nbins{}_mt{}_extramT{}_CT{}_isPrompt{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.isPrompt)
elif args.fitAll:	        subDir = "fitAllregion_dphiJets_nbins{}_mt{}_extramT{}_CT{}_isPrompt{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.isPrompt)
baseDir = os.path.join(setup.analysis_results, str(year), subDir)

sSubDir = 'expected' if args.expected else 'observed'
if args.signalInjection : sSubDir += '_signalInjected'

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
  genEff = genFilter.getEff(s.mStop,s.mNeu)
  if genEff ==0 :
    print "no gen eff found in map for %s,%s", s.mStop, s.mNeu
    genEff = 0.48
  c = cardFileWriter.cardFileWriter()
  c.releaseLocation = os.path.abspath('.') # now run directly in the run directory

  logger.info("Running over signal: %s", s.name)

  cardFileName = os.path.join(limitDir, s.name+'.txt')
  if not os.path.exists(cardFileName) or overWrite:
    counter=0
    c.reset()
    c.setPrecision(3)
    shapeString = 'lnN' if args.useTxt else 'shape'
    
    SFb     = 'SFb_%s'%year
    SFl     = 'SFl_%s'%year
    nISR    = 'nISR_%s'%year
    wPt     = 'wPt_%s'%year
    JEC     = 'JEC_%s'%year
    JER     = 'JER_%s'%year
    #leptonSF= 'leptonSF_new_%s'%year
    leptonSF= 'leptonSF_%s'%year
    leptonSFsignal= 'leptonSFsignal_%s'%year
    
    PU      = 'PU_%s'%year

    Lumi    = 'Lumi_%s'%year

    leptonSFsyst = 'leptonSFsyst_%s'%year
    
    c.addUncertainty(Lumi,          "lnN")
    c.addUncertainty(leptonSFsyst,          "lnN")

    c.addUncertainty(SFb,          shapeString)
    c.addUncertainty(SFl,          shapeString)
    c.addUncertainty(nISR,           shapeString)
    c.addUncertainty(wPt,           shapeString)
    c.addUncertainty(JEC,          shapeString)
    c.addUncertainty(JER,          shapeString)
    c.addUncertainty(leptonSF,   shapeString)
    c.addUncertainty(leptonSFsignal,          "lnN")
    c.addUncertainty(PU,           shapeString)

    if '2016' in year:
      lumiUncertainty = 1.025
      print "lumi unc for 2016 era, both pre/post"
    elif year == 2017:
      lumiUncertainty = 1.023
    elif year == 2018:
      lumiUncertainty = 1.025



    c.addCR(controlRegions)
    c.addSR(signalRegions)
    for setup in setups:
      eSignal     = MCBasedEstimate(name=s.name, sample=s, cacheDir=setup.defaultCacheDir(specificNameForSensitivityStudy="others_nbins{}_mt{}_extramT{}_CT{}_isPrompt{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.isPrompt)))
      observation = DataObservation(name='Data', sample=setup.processes['Data'], cacheDir=setup.defaultCacheDir(specificNameForSensitivityStudy="others_nbins{}_mt{}_extramT{}_CT{}_isPrompt{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.isPrompt)))
      for e in setup.estimators : 
        e.initCache(setup.defaultCacheDir(specificNameForSensitivityStudy="others_nbins{}_mt{}_extramT{}_CT{}_isPrompt{}".format(_NBINS,args.mT_cut_value,args.extra_mT_cut,args.CT_cut_value,args.isPrompt)))
      
      for r in setup.regions:
        print r 
        for channel in setup.channels:
          niceName = ' '.join([channel, r.__str__()])
          logger.info("Bin name: %s", niceName)
          binname = 'Bin'+str(counter)
          counter += 1
          total_exp_bkg = 0
          c.addBin(binname, [e.name.split('-')[0] for e in setup.estimators ], niceName)

          for e in setup.estimators :
            name = e.name.split('-')[0]

            if "signal" in name :
              print name 
              exit(0)
            
  
            expected = e.cachedEstimate(r, channel, setup)
            logger.info("Expectation for process %s: %s", e.name, expected.val)                                                                                                                       
              
            expected = expected * args.scale
            logger.info("Expectation for process %s after scaling: %s", e.name, expected.val)
            

            Wcorr = 0
            if e.name.count('WJets'):
              Wcorr = expected.val*args.scaleWjets
            
            TTbarcorr = 0
            if e.name.count('Top'):
              TTbarcorr = expected.val*args.scaleTTbar
                
            total_exp_bkg += expected.val
            total_exp_bkg += Wcorr
            total_exp_bkg += TTbarcorr
              
            


            # if e.name.count("WJets"):
            #   pass
            # elif e.name.count("Top") :
            #   pass
            # else :
            #   c.specifyFlatUncertainty(Lumi, lumiUncertainty)

            
            if e.name.count('WJets'):
              c.specifyExpectation(binname, 'WJets',  expected.val)
            elif e.name.count("Top"):
              Top_SF = 1
              c.specifyExpectation(binname, name, expected.val*Top_SF)
              if Top_SF != 1: logger.warning("Scaling Top background by %s", Top_SF)
            elif e.name.count("Others"):
              c.specifyExpectation(binname, name, expected.val)
            elif e.name.count("ZInv"):
              c.specifyExpectation(binname, name, expected.val)
            elif e.name.count("QCD"):
              c.specifyExpectation(binname, name, expected.val)               
            if expected.val>0 or True:
              names = [name]
              
              
              for name in names : 
                sysChannel = 'all' # could be channel as well
                uncScale = 1
                
                #MC bkg stat (some condition to neglect the smaller ones?)
                uname = 'Stat_'+binname+'_'+name
                c.addUncertainty(uname, 'lnN')
                c.specifyUncertainty(uname, binname, name, 1 + (expected.sigma/expected.val) * uncScale if expected.val>0 else 1)

                
                c.specifyUncertainty(SFb,        binname, name, 1 + e.btaggingSFbSystematic(r, channel, setup).val * uncScale )
                c.specifyUncertainty(SFl,        binname, name, 1 + e.btaggingSFlSystematic(r, channel, setup).val * uncScale )
                c.specifyUncertainty(JEC,        binname, name, 1 + e.JECSystematic(r, sysChannel, setup).val )
                c.specifyUncertainty(JER,        binname, name, 1 + e.JERSystematic(r, sysChannel, setup).val)
                c.specifyUncertainty(leptonSF,   binname, name, 1 + e.leptonSFSystematic(   r, channel, setup).val * uncScale ) 
                c.specifyUncertainty(PU,         binname, name, 1 + e.PUSystematic(         r, sysChannel, setup).val * uncScale )
                c.specifyUncertainty(leptonSFsyst, binname, name, 1.01)

                if name == "WJets":
                  c.specifyUncertainty(wPt,        binname, name, 1 + e.wPtSystematic(         r, sysChannel, setup).val * uncScale )
                  print "wpt sys: {}".format(e.wPtSystematic(         r, sysChannel, setup).val)
                  #pass #c.specifyUncertainty(Lumi, binname, name, 1)
                elif name == "Top" :
                  c.specifyUncertainty(nISR,       binname, name, 1 + e.nISRSystematic(         r, sysChannel, setup).val * uncScale )
                  #pass #c.specifyUncertainty(Lumi, binname, name, 1)
                else :
                  c.specifyUncertainty(Lumi, binname, name, lumiUncertainty)



          c.addMap(regionMapping)	
          #signal
          eSignal.isSignal = True
          e = eSignal
            
          if fastSim :
            signalSetup = setup.sysClone()
            if  '2016' in year:
              extra_pars = {} # use default parameters
              if (args.usePromptSignalOnly) :
                extra_pars = {'l1_prompt':True}
              
              signalSetup = setup.sysClone(sys={'reweight':['reweight_nISR'], 'remove':[]},parameters=extra_pars) 

              signal = e.cachedEstimate(r, channel, signalSetup)
            else:
              signal = e.cachedEstimate(r, channel, signalSetup)
          else:
            signalSetup = setup.sysClone()
	    if  '2016' in year:
	      extra_pars = {} # use default parameters
	      if (args.usePromptSignalOnly):
	        extra_pars = {'l1_prompt':True}
                signalSetup = setup.sysClone(sys={'reweight':[], 'remove':['reweight_nISR']},parameters=extra_pars)
	        
                signal = e.cachedEstimate(r, channel, signalSetup)
	      else:
	        signal = e.cachedEstimate(r, channel, signalSetup)

          
          signal = signal * args.scale

          if signal.val<0.01 :#and niceName.count("control")==0:
              signal.val = 0.001
              signal.sigma = 0.001
          
          c.specifyExpectation(binname, 'signal', signal.val*xSecScale*genEff )
          logger.info("Signal expectation: %s", signal.val*xSecScale*genEff)

          c.specifyUncertainty(Lumi, binname, 'signal', lumiUncertainty)
          c.specifyUncertainty(leptonSFsignal, binname, 'signal', 1.01)
          c.specifyUncertainty(leptonSFsyst, binname, 'signal', 1.01)
          logger.info("adding lumi uncertainty for signal")
          if signal.val>0.001:

            c.specifyUncertainty(SFb,             binname, 'signal', 1 + e.btaggingSFbSystematic(r, channel, signalSetup).val )
            c.specifyUncertainty(SFl,             binname, 'signal', 1 + e.btaggingSFlSystematic(r, channel, signalSetup).val )
            c.specifyUncertainty(JEC,             binname, 'signal', 1 + e.JECSystematic(        r, channel, signalSetup).val )
            c.specifyUncertainty(JER,             binname, 'signal', 1 + e.JERSystematic(        r, channel, signalSetup).val )
            # c.specifyUncertainty(leptonSF,      binname, 'signal', 1 + e.leptonSFSystematic(   r, channel, signalSetup).val )
            
            c.specifyUncertainty(PU,              binname, 'signal', 1 + e.PUSystematic(         r, channel, signalSetup).val )

            #if not fastSim:
            #  c.specifyUncertainty('PDF',      binname, 'signal', 1 + getPDFUnc(eSignal.name, r, niceName, channel))
            #  logger.info("PDF uncertainty for signal is: %s", getPDFUnc(eSignal.name, r, niceName, channel))
              
              
            uname = 'Stat_'+binname+'_signal'
            c.addUncertainty(uname, 'lnN')
            c.specifyUncertainty(uname, binname, 'signal', 1 + signal.sigma/signal.val if signal.val>0 else 1 )
          else:
            uname = 'Stat_'+binname+'_signal'
            c.addUncertainty(uname, 'lnN')
            c.specifyUncertainty(uname, binname, 'signal', 1 )
          
          logger.info("Done with MC. Now working on observation.")
            
            
            
          ## Observation ##
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
            c.specifyObservation(binname, int(args.scale*observation.cachedObservation(r, channel, setup).val))
            logger.info("Observation: %s", int(args.scale*observation.cachedObservation(r, channel, setup).val))


      # c.addRateParameter('WJets',1,'[0.,3.]')
      # c.addRateParameter('Top',1,'[0.,3.]')
      
      c.addRateParameter('WJetsAndTop',1,'[0.,3.]')
      # c.addRateParameter('Top',1,'[0.,3.]')

      # if year == 2016:
      #     lumiUncertainty = 1.025
      # elif year == 2017:
      #     lumiUncertainty = 1.023
      # elif year == 2018:
      #     lumiUncertainty = 1.025
      
      # c.specifyFlatUncertainty(Lumi, lumiUncertainty)
      cardFileNameTxt     = c.writeToFile(cardFileName,noMCStat=False)
      cardFileNameShape   = c.writeToShapeFile(cardFileName.replace('.txt', '_shape.root'), noMCStat=False)
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
        print "ZInv-prefit" ,  preFitResults['ZInv']
        print "ZInv-postfit" ,postFitResults['ZInv']
        print 
        print "Others-prefit" ,  preFitResults['Others']
        print "Others-postfit" ,postFitResults['Others']
        
        top_prefit  = preFitResults['Top']
        top_postfit = postFitResults['Top']
        top_prefit_SR_err   = ROOT.Double()
        top_postfit_SR_err  = ROOT.Double()

        WJ_prefit  = preFitResults['WJets']
        WJ_postfit = postFitResults['WJets']
        WJ_prefit_SR_err   = ROOT.Double()
        WJ_postfit_SR_err  = ROOT.Double()
        
        Others_prefit  = preFitResults['Others']
        Others_postfit = postFitResults['Others']


        DY_prefit_SR_err   = ROOT.Double()
        DY_postfit_SR_err  = ROOT.Double()


        QCD_prefit_SR_err   = ROOT.Double()
        QCD_postfit_SR_err  = ROOT.Double()

        print
        print "## Scale Factors for backgrounds, integrated over {} regions: ##".format(r)
        print "{:20}{:4.2f}{:3}{:4.2f}".format('top:',          (top_postfit/top_prefit).val, '+/-',  top_postfit.sigma/top_postfit.val)
        print "{:20}{:4.2f}{:3}{:4.2f}".format('WJ:',          (WJ_postfit/WJ_prefit).val, '+/-',  WJ_postfit.sigma/WJ_postfit.val)
        print "{:20}{:4.2f}{:3}{:4.2f}".format('Others:',          (Others_postfit/Others_prefit).val, '+/-',  Others_postfit.sigma/Others_postfit.val)


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
  if year == "2016postVFP":
    if args.fullSim:
      from StopsCompressed.samples.nanoTuples_UL16_FullSimSignal_postProcessed import signals_T2tt as jobs
    else:
      #data_directory              = '/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/'
      data_directory              = '/scratch/priya.hussain/StopsCompressed/nanoTuples/'
      postProcessing_directory    = 'compstops_2016_nano_v27/Met/'
      #postProcessing_directory    = 'compstops_2016_nano_v28/Met/'
      from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import signals_T2tt as jobs
  if year == "2016preVFP":
    if args.fullSim:
      from StopsCompressed.samples.nanoTuples_UL16APV_FullSimSignal_postProcessed import signals_T2tt as jobs
    else:
      #data_directory              = '/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/'
      data_directory              = '/scratch/priya.hussain/StopsCompressed/nanoTuples/'
      postProcessing_directory    = 'compstops_2016_nano_v27/Met/'
      #postProcessing_directory    = 'compstops_2016_nano_v28/Met/'
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

for i, j in enumerate(jobs):
    if "T2tt_1024_1006" in j.name :
        print "~removing ", j.name
        del jobs[i]


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
    print "Stop: ", mStop, "mLSP: ", mNeu 
    dm = mStop - mNeu
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
  pickle.dump( val, file(pklFile,'w'))
  print "pklFile: {}".format(pklFile)
  print "limitResultsFilename: {}".format(limitResultsFilename)

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
