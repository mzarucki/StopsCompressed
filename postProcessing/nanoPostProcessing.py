#!/usr/bin/env python

# standard imports
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import sys
import os
import copy
import random
import subprocess
import datetime
import shutil
import uuid

from array import array
from operator import mul
from math import sqrt, atan2, sin, cos

# RootTools
from RootTools.core.standard import *

# User specific
import StopsCompressed.Tools.user as user

# Tools for object selection
from StopsCompressed.Tools.helpers           import nonEmptyFile, fill_vector_collection
from StopsCompressed.Tools.helpers           import deltaR, deltaPhi
from StopsCompressed.Tools.objectSelection   import muonSelector, eleSelector,  getGoodMuons, getGoodElectrons, getGoodTaus #tauSelector,
from StopsCompressed.Tools.objectSelection   import getGoodJets, isBJet, jetId, getGenPartsAll, getJets, getPhotons, getAllJets
#from StopsDilepton.Tools.triggerEfficiency   import triggerEfficiency
#from StopsDilepton.Tools.leptonSF            import leptonSF as leptonSF_
#from StopsDilepton.Tools.leptonFastSimSF     import leptonFastSimSF as leptonFastSimSF_

from Analysis.Tools.puProfileCache           import *
from Analysis.Tools.L1PrefireWeight          import L1PrefireWeight
from Analysis.Tools.LeptonTrackingEfficiency import LeptonTrackingEfficiency
from Analysis.Tools.isrWeight                import ISRweight
from Analysis.Tools.helpers                  import checkRootFile, deepCheckRootFile, deepCheckWeight

# central configuration
targetLumi = 1000 #pb-1 Which lumi to normalize to

def extractEra(sampleName):
    return sampleName[sampleName.find("Run"):sampleName.find("Run")+len('Run2000A')]

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--logLevel',    action='store',         nargs='?',  choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],   default='INFO', help="Log level for logging" )
    argParser.add_argument('--samples',     action='store',         nargs='*',  type=str, default=['TTZToLLNuNu_ext'],                  help="List of samples to be post-processed, given as CMG component name" )
    argParser.add_argument('--nJobs',       action='store',         nargs='?',  type=int, default=1,                                    help="Maximum number of simultaneous jobs." )
    argParser.add_argument('--job',         action='store',                     type=int, default=0,                                    help="Run only jobs i" )
    argParser.add_argument('--targetDir',   action='store',         nargs='?',  type=str, default=user.postProcessing_output_directory, help="Name of the directory the post-processed files will be saved" )
    argParser.add_argument('--processingEra', action='store',       nargs='?',  type=str, default='postProcessed_80X_v22',              help="Name of the processing era" )
    argParser.add_argument('--runOnLxPlus',   action='store_true',                                                                      help="Change the global redirector of samples to run on lxplus")
    argParser.add_argument('--skim',        action='store',         nargs='?',  type=str, default='singleLep',                          help="Skim conditions to be applied for post-processing" )
    argParser.add_argument('--LHEHTCut',    action='store',         nargs='?',  type=int, default=-1,                                   help="LHE cut." )
    argParser.add_argument('--year',        action='store',                     type=int,                                               help="Which year?" )
    argParser.add_argument('--overwrite',   action='store_true',                                                                        help="Overwrite existing output files, bool flag set to True  if used" )
    argParser.add_argument('--keepAllJets', action='store_true',                                                                        help="Keep also forward jets?" )
    argParser.add_argument('--small',       action='store_true',                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used" )
    argParser.add_argument('--susySignal',  action='store_true',                                                                        help="Is SUSY signal?" )
    argParser.add_argument('--fastSim',     action='store_true',                                                                        help="FastSim?" )
    argParser.add_argument('--TTDM',        action='store_true',                                                                        help="Is TTDM signal?" )
    # argParser.add_argument('--triggerSelection',            action='store_true',                                                        help="Trigger selection?" ) 
    argParser.add_argument('--keepLHEWeights',              action='store_true',                                                        help="Keep LHEWeights?" )
    argParser.add_argument('--skipNanoTools',               action='store_true',                                                        help="Skipt the nanoAOD tools step for computing JEC/JER/MET etc uncertainties")
    argParser.add_argument('--keepNanoAOD',                 action='store_true',                                                        help="Keep nanoAOD output?")
    argParser.add_argument('--reuseNanoAOD',                action='store_true',                                                        help="Keep nanoAOD output?")
    argParser.add_argument('--reduceSizeBy',                action='store',     type=int,                                               help="Reduce the size of the sample by a factor of...")

    return argParser

options = get_parser().parse_args()

# Logging
import StopsCompressed.Tools.logger as _logger
logFile = '/tmp/%s_%s_%s_njob%s.txt'%(options.skim, '_'.join(options.samples), os.environ['USER'], str(0 if options.nJobs==1 else options.job))
logger  = _logger.get_logger(options.logLevel, logFile = logFile)

import Analysis.Tools.logger as _logger_an
logger_an = _logger_an.get_logger(options.logLevel, logFile = logFile )

import RootTools.core.logger as _logger_rt
logger_rt = _logger_rt.get_logger(options.logLevel, logFile = logFile )

# Flags 
isSingleLep     = options.skim.lower().startswith('singlelep')

# Skim condition
skimConds = []

if isSingleLep:
    skimConds.append( "Sum$(Electron_pt>5&&abs(Electron_eta)<2.5) + Sum$(Muon_pt>3.5&&abs(Muon_eta)<2.4)>=1" )

#Samples: Load samples
maxN = 1 if options.small else None
if options.small:
    options.job = 0
    options.nJobs = 1000 # set high to just run over 1 input file

if options.runOnLxPlus:
    # Set the redirector in the samples repository to the global redirector
    from Samples.Tools.config import redirector_global as redirector

if options.year == 2016:
    from Samples.nanoAOD.Summer16_private_legacy_v1 import allSamples as mcSamples
    from Samples.nanoAOD.Run2016_14Dec2018  import allSamples as dataSamples
    allSamples = mcSamples + dataSamples
elif options.year == 2017:
    from Samples.nanoAOD.Fall17_private_legacy_v1   import allSamples as mcSamples
    from Samples.nanoAOD.Run2017_31Mar2018_private  import allSamples as dataSamples
    allSamples = mcSamples + dataSamples
elif options.year == 2018:
    from Samples.nanoAOD.Autumn18_private_legacy_v1 import allSamples as mcSamples
    from Samples.nanoAOD.Run2018_17Sep2018_private  import allSamples as dataSamples
    allSamples = mcSamples + dataSamples
else:
    raise NotImplementedError

samples = []
for selectedSamples in options.samples:
    for sample in allSamples:
        if selectedSamples == sample.name:
            samples.append(sample)

if len(samples)==0:
    logger.info( "No samples found. Was looking for %s. Exiting" % options.samples )
    sys.exit(-1)

isData = False not in [s.isData for s in samples]
isMC   =  True not in [s.isData for s in samples]


if options.susySignal:
    xSection = None
    ## special filet for bad jets in FastSim: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSRecommendationsICHEP16#Cleaning_up_of_fastsim_jets_from
    #skimConds.append( "Sum$(JetFailId_pt>30&&abs(JetFailId_eta)<2.5&&JetFailId_mcPt==0&&JetFailId_chHEF<0.1)+Sum$(Jet_pt>30&&abs(Jet_eta)<2.5&&Jet_mcPt==0&&Jet_chHEF<0.1)==0" )
else:
    # Check that all samples which are concatenated have the same x-section.
    assert isData or len(set([s.xSection for s in samples]))==1, "Not all samples have the same xSection: %s !"%(",".join([s.name for s in samples]))
    assert isMC or len(samples)==1, "Don't concatenate data samples"

    xSection = samples[0].xSection if isMC else None

# set default era
era = None
if isData:
    era = extractEra(samples[0].name)[-1]
## Trigger selection
#if isData and options.triggerSelection:
#    from StopsDilepton.tools.triggerSelector import triggerSelector
#    era = extractEra(samples[0].name)[-1]
#    logger.info( "######### Era %s ########", era )
#    ts = triggerSelector(options.year, era=era)
#    triggerCond  = ts.getSelection(options.samples[0] if isData else "MC")
#    treeFormulas = {"triggerDecision": {'string':triggerCond} }
#
#    logger.info("Sample will have the following trigger skim: %s"%triggerCond)
#    skimConds.append( triggerCond )
#elif isData and not options.triggerSelection:
#    raise Exception( "Data should have a trigger selection" )
#
#triggerEff          = triggerEfficiency(options.year)

#Samples: combine if more than one
if len(samples)>1:
    sample_name =  samples[0].name+"_comb"
    logger.info( "Combining samples %s to %s.", ",".join(s.name for s in samples), sample_name )
    sample      = Sample.combine(sample_name, samples, maxN = maxN)
    sampleForPU = Sample.combine(sample_name, samples, maxN = -1)
elif len(samples)==1:
    sample      = samples[0]
    sampleForPU = samples[0]
else:
    raise ValueError( "Need at least one sample. Got %r",samples )

# Add scale etc. friends
has_susy_weight_friend = False
if options.susySignal and options.fastSim:
    # Make friend sample
    friend_dir = "/afs/hephy.at/data/cms05/StopsCompressed/nanoTuples/signalWeights/%s/%s"% (options.year, sample.name )
    if os.path.exists( friend_dir ):
        weight_friend = Sample.fromDirectory( "weight_friend", directory = [friend_dir] ) 
        if weight_friend.chain.BuildIndex("luminosityBlock", "event")>0:
            has_susy_weight_friend = True
    else:
        raise RuntimeError( "We need the LHE weight friend tries. Not found in: %s" % friend_dir )

if options.reduceSizeBy > 1:
    logger.info("Sample size will be reduced by a factor of %s", options.reduceSizeBy)
    logger.info("Recalculating the normalization of the sample. Before: %s", sample.normalization)
    if isData:
        NotImplementedError ( "Data samples shouldn't be reduced in size!!" )
    sample.reduceFiles( factor = options.reduceSizeBy )
    # recompute the normalization
    sample.clear()
    sample.name += "_redBy%s"%options.reduceSizeBy
    sample.normalization = sample.getYieldFromDraw(weightString="genWeight")['val']
    logger.info("New normalization: %s", sample.normalization)

if isMC:
    from Analysis.Tools.puReweighting import getReweightingFunction
    if options.year == 2016:
        nTrueInt_puRW       = getReweightingFunction(data="PU_2016_35920_XSecCentral", mc="Summer16")
        nTrueInt_puRWDown   = getReweightingFunction(data="PU_2016_35920_XSecDown",    mc="Summer16")
        nTrueInt_puRWVDown  = getReweightingFunction(data="PU_2016_35920_XSecVDown",   mc="Summer16")
        nTrueInt_puRWUp     = getReweightingFunction(data="PU_2016_35920_XSecUp",      mc="Summer16")
        nTrueInt_puRWVUp    = getReweightingFunction(data="PU_2016_35920_XSecVUp",     mc="Summer16")
        nTrueInt_puRWVVUp   = getReweightingFunction(data="PU_2016_35920_XSecVVUp",    mc="Summer16")
    elif options.year == 2017:
        # keep the weight name for now. Should we update to a more general one?
        puProfiles = puProfile( source_sample = sampleForPU )
        mcHist = puProfiles.cachedTemplate( selection="( 1 )", weight='genWeight', overwrite=False ) # use genWeight for amc@NLO samples. No problems encountered so far
        nTrueInt_puRW       = getReweightingFunction(data="PU_2017_41860_XSecCentral",  mc=mcHist)
        nTrueInt_puRWDown   = getReweightingFunction(data="PU_2017_41860_XSecDown",     mc=mcHist)
        nTrueInt_puRWVDown  = getReweightingFunction(data="PU_2017_41860_XSecVDown",    mc=mcHist)
        nTrueInt_puRWUp     = getReweightingFunction(data="PU_2017_41860_XSecUp",       mc=mcHist)
        nTrueInt_puRWVUp    = getReweightingFunction(data="PU_2017_41860_XSecVUp",      mc=mcHist)
        nTrueInt_puRWVVUp   = getReweightingFunction(data="PU_2017_41860_XSecVVUp",     mc=mcHist)
    elif options.year == 2018:
        # keep the weight name for now. Should we update to a more general one?
        nTrueInt_puRW       = getReweightingFunction(data="PU_2018_58830_XSecCentral",  mc="Autumn18")
        nTrueInt_puRWDown   = getReweightingFunction(data="PU_2018_58830_XSecDown",     mc="Autumn18")
        nTrueInt_puRWVDown  = getReweightingFunction(data="PU_2018_58830_XSecVDown",    mc="Autumn18")
        nTrueInt_puRWUp     = getReweightingFunction(data="PU_2018_58830_XSecUp",       mc="Autumn18")
        nTrueInt_puRWVUp    = getReweightingFunction(data="PU_2018_58830_XSecVUp",      mc="Autumn18")
        nTrueInt_puRWVVUp   = getReweightingFunction(data="PU_2018_58830_XSecVVUp",     mc="Autumn18")

## lepton SFs
#leptonTrackingSF    = LeptonTrackingEfficiency(options.year)
#leptonSF            = leptonSF_(options.year)
#
#if options.fastSim:
#   leptonFastSimSF  = leptonFastSimSF_(options.year)

options.skim = options.skim + '_small' if options.small else options.skim

# LHE cut (DY samples)
if options.LHEHTCut>0:
    sample.name+="_lheHT"+str(options.LHEHTCut)
    logger.info( "Adding upper LHE cut at %f", options.LHEHTCut )
    skimConds.append( "LHE_HTIncoming<%f"%options.LHEHTCut )

sampleName = sample.name

# output directory (store temporarily when running on dpm)
from StopsCompressed.Tools.user import postProcessing_output_directory as user_directory
directory = os.path.join( options.targetDir, options.processingEra ) 
output_directory = os.path.join( directory, options.skim, sampleName )

len_orig = len(sample.files)
## sort the list of files?
sample = sample.split( n=options.nJobs, nSub=options.job)
logger.info(  "fileBasedSplitting: Run over %i/%i files for job %i/%i."%(len(sample.files), len_orig, options.job, options.nJobs))
logger.debug( "fileBasedSplitting: Files to be run over:\n%s", "\n".join(sample.files) )

## top pt reweighting
#from StopsDilepton.tools.topPtReweighting import getUnscaledTopPairPtReweightungFunction, getTopPtDrawString, getTopPtsForReweighting
## Decision based on sample name -> whether TTJets or TTLep is in the sample name
#isTT = sample.name.startswith("TTJets") or sample.name.startswith("TTLep") or sample.name.startswith("TT_pow")
#doTopPtReweighting = isTT and not options.noTopPtReweighting
#
#if sample.name.startswith("TTLep"):
#    sample.topScaleF = 1.002 ## found to be universal for years 2016-2018, and in principle negligible
#
#if doTopPtReweighting:
#    logger.info( "Sample will have top pt reweighting." )
#    topPtReweightingFunc = getUnscaledTopPairPtReweightungFunction(selection = "dilep")
#    # Compute x-sec scale factor on unweighted events
#    selectionString = "&&".join(skimConds)
#    if hasattr(sample, "topScaleF"):
#        # If you don't want to get the SF for each subjob run the script and add the topScaleF to the sample
#        topScaleF = sample.topScaleF
#    else:
#        reweighted  = sample.getYieldFromDraw( selectionString = selectionString, weightString = getTopPtDrawString(selection = "dilep") + '*genWeight')
#        central     = sample.getYieldFromDraw( selectionString = selectionString, weightString = 'genWeight')
#
#        topScaleF = central['val']/reweighted['val']
#
#    logger.info( "Found topScaleF %f", topScaleF )
#else:
#    topScaleF = 1
#    logger.info( "Sample will NOT have top pt reweighting. topScaleF=%f",topScaleF )

# systematic variations
addSystematicVariations = (not isData)

# B tagging SF
from Analysis.Tools.BTagEfficiency import BTagEfficiency
#btagEff = BTagEfficiency( fastSim = options.fastSim, year=options.year, tagger='DeepCSV' )
btagEff = BTagEfficiency( fastSim = options.fastSim, year=options.year, tagger='CSVv2' )

# L1 prefire weight
L1PW = L1PrefireWeight(options.year)

if os.path.exists(output_directory) and options.overwrite:
    if options.nJobs > 1:
        logger.warning( "NOT removing directory %s because nJobs = %i", output_directory, options.nJobs )
    else:
        logger.info( "Output directory %s exists. Deleting.", output_directory )
        shutil.rmtree(output_directory)

try:    #Avoid trouble with race conditions in multithreading
    os.makedirs(output_directory)
    logger.info( "Created output directory %s.", output_directory )
except:
    pass

filename, ext = os.path.splitext( os.path.join(output_directory, sample.name + '.root') )
fileNumber    = options.job if options.job is not None else 0
outfilename   = filename+ext

# checking overwrite or file exists
if not options.overwrite:
    if os.path.isfile(outfilename):
        logger.info( "Output file %s found.", outfilename)
        if checkRootFile( outfilename, checkForObjects=["Events"] ) and deepCheckRootFile( outfilename ) and deepCheckWeight( outfilename ):
            logger.info( "File already processed. Source: File check ok! Skipping." ) # Everything is fine, no overwriting
            sys.exit(0)
        else:
            logger.info( "File corrupt. Removing file from target." )
            os.remove( outfilename )
            logger.info( "Reprocessing." )
    else:
        logger.info( "Sample not processed yet." )
        logger.info( "Processing." )

else:
    logger.info( "Overwriting.")

#branches to be kept for data and MC
branchKeepStrings_DATAMC = [\
    "run", "luminosityBlock", "event", "fixedGridRhoFastjetAll", "PV_npvs", "PV_npvsGood",
    "MET_*", "RawMET_phi", "RawMET_pt", "RawMET_sumEt",
    "Flag_*",
    "nJet", "Jet_*",
    "nElectron", "Electron_*",
    "nMuon", "Muon_*",
    "nTau", "Tau_*",
]
if not options.fastSim:
    branchKeepStrings_DATAMC += ["HLT_*"]

if options.year == 2017:
    branchKeepStrings_DATAMC += [\
        "METFixEE2017_*",
    ]

#branches to be kept for MC samples only
branchKeepStrings_MC = [ "Generator_*", "GenPart_*", "nGenPart", "genWeight", "Pileup_nTrueInt","GenMET_pt","GenMET_phi"] #, "nISR"] keep, if you run the nanoAODTools ISR counter
if not options.fastSim:
    branchKeepStrings_MC.append("LHEScaleWeight")

#branches to be kept for data only
branchKeepStrings_DATA = [ ]

# Jet variables to be read from chain
jetCorrInfo = []
jetMCInfo   = ['genJetIdx/I','hadronFlavour/I']

if isData:
    lumiScaleFactor=None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_DATA
    from FWCore.PythonUtilities.LumiList import LumiList
    # Apply golden JSON
    lumiList = LumiList(os.path.expandvars(sample.json))
    logger.info( "Loaded json %s", sample.json )
else:
    lumiScaleFactor = xSection*targetLumi/float(sample.normalization) if xSection is not None else None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_MC

jetVars         = ['pt/F', 'chEmEF/F', 'chHEF/F', 'neEmEF/F', 'neHEF/F', 'rawFactor/F', 'eta/F', 'phi/F', 'jetId/I', 'btagDeepB/F', 'btagCSVV2/F', 'area/F', 'pt_nom/F', 'corr_JER/F'] + jetCorrInfo
if isMC:
    jetVars     += jetMCInfo
    jetVars     += ['pt_jesTotalUp/F', 'pt_jesTotalDown/F', 'pt_jerUp/F', 'pt_jerDown/F', 'corr_JER/F', 'corr_JEC/F']
jetVarNames     = [x.split('/')[0] for x in jetVars]
# those are for writing leptons
lepVars         = ['pt/F','eta/F','phi/F','pdgId/I','cutBased/I','miniPFRelIso_all/F','pfRelIso03_all/F','sip3d/F','lostHits/I','convVeto/I','dxy/F','dz/F','charge/I','deltaEtaSC/F','mediumId/I','eleIndex/I','muIndex/I']
lepVarNames     = [x.split('/')[0] for x in lepVars]

read_variables = map(TreeVariable.fromString, [ 'MET_pt/F', 'MET_phi/F', 'run/I', 'luminosityBlock/I', 'event/l', 'PV_npvs/I', 'PV_npvsGood/I'] )
if options.year == 2017:
    read_variables += map(TreeVariable.fromString, [ 'METFixEE2017_pt/F', 'METFixEE2017_phi/F', 'METFixEE2017_pt_nom/F', 'METFixEE2017_phi_nom/F'])
    if isMC:
        read_variables += map(TreeVariable.fromString, [ 'METFixEE2017_pt_jesTotalUp/F', 'METFixEE2017_pt_jesTotalDown/F', 'METFixEE2017_pt_jerUp/F', 'METFixEE2017_pt_jerDown/F', 'METFixEE2017_pt_unclustEnDown/F', 'METFixEE2017_pt_unclustEnUp/F', 'METFixEE2017_phi_jesTotalUp/F', 'METFixEE2017_phi_jesTotalDown/F', 'METFixEE2017_phi_jerUp/F', 'METFixEE2017_phi_jerDown/F', 'METFixEE2017_phi_unclustEnDown/F', 'METFixEE2017_phi_unclustEnUp/F', 'METFixEE2017_pt_jer/F', 'METFixEE2017_phi_jer/F'])
else:
    read_variables += map(TreeVariable.fromString, [ 'MET_pt_nom/F', 'MET_phi_nom/F' ])
    if isMC:
        read_variables += map(TreeVariable.fromString, [ 'MET_pt_jesTotalUp/F', 'MET_pt_jesTotalDown/F', 'MET_pt_jerUp/F', 'MET_pt_jerDown/F', 'MET_pt_unclustEnDown/F', 'MET_pt_unclustEnUp/F', 'MET_phi_jesTotalUp/F', 'MET_phi_jesTotalDown/F', 'MET_phi_jerUp/F', 'MET_phi_jerDown/F', 'MET_phi_unclustEnDown/F', 'MET_phi_unclustEnUp/F', 'MET_pt_jer/F', 'MET_phi_jer/F'])
if isMC:
    read_variables += map(TreeVariable.fromString, [ 'GenMET_pt/F', 'GenMET_phi/F' ])

read_variables += [ TreeVariable.fromString('nPhoton/I'),
                    VectorTreeVariable.fromString('Photon[pt/F,eta/F,phi/F,mass/F,cutBased/I,pdgId/I]') if (options.year == 2016) else VectorTreeVariable.fromString('Photon[pt/F,eta/F,phi/F,mass/F,cutBasedBitmap/I,pdgId/I]') ]

new_variables = [ 'weight/F']
if isMC:
    read_variables += [ TreeVariable.fromString('Pileup_nTrueInt/F') ]
    # reading gen particles for top pt reweighting
    read_variables.append( TreeVariable.fromString('nGenPart/I') )
    #read_variables.append( TreeVariable.fromString('nISR/I') ) # keep if you run the ISR counter 
    #new_variables.extend([ 'reweightTopPt/F', 'reweight_nISR/F', 'reweight_nISRUp/F', 'reweight_nISRDown/F'] )
    read_variables.append( VectorTreeVariable.fromString('GenPart[pt/F,mass/F,phi/F,eta/F,pdgId/I,genPartIdxMother/I,status/I,statusFlags/I]', nMax=200 )) # default nMax is 100, which would lead to corrupt values in this case
    read_variables.append( TreeVariable.fromString('genWeight/F') )
    read_variables.append( TreeVariable.fromString('nGenJet/I') )
    read_variables.append( VectorTreeVariable.fromString('GenJet[pt/F,eta/F,phi/F]' ) )
    new_variables.extend([ 'reweightPU/F','reweightPUUp/F','reweightPUDown/F', 'reweightPUVUp/F','reweightPUVVUp/F', 'reweightPUVDown/F', 'reweightL1Prefire/F', 'reweightL1PrefireUp/F', 'reweightL1PrefireDown/F'])

read_variables += [\
    TreeVariable.fromString('nElectron/I'),
    VectorTreeVariable.fromString('Electron[pt/F,eta/F,phi/F,pdgId/I,cutBased/I,miniPFRelIso_all/F,pfRelIso03_all/F,sip3d/F,lostHits/b,convVeto/O,dxy/F,dz/F,charge/I,deltaEtaSC/F,vidNestedWPBitmap/I]'),
    TreeVariable.fromString('nMuon/I'),
    VectorTreeVariable.fromString('Muon[pt/F,eta/F,phi/F,pdgId/I,mediumId/O,miniPFRelIso_all/F,pfRelIso03_all/F,sip3d/F,dxy/F,dz/F,charge/I]'),
    TreeVariable.fromString('nJet/I'),
    VectorTreeVariable.fromString('Tau[pt/F,eta/F,phi/F,idMVAnewDM2017v2/b,neutralIso/F,idAntiMu/O,genPartFlav/O,genPartIdx/I,dxy/F,dz/F,charge/I]'),
    TreeVariable.fromString('nTau/I'),
    VectorTreeVariable.fromString('Jet[%s]'% ( ','.join(jetVars) ) ),
]

new_variables += [\
    'nlep/I',
    'JetGood[%s]'% ( ','.join(jetVars+['index/I']) + ',genPt/F' ),
    #'BTag[%s]'% ( ','.join(jetVars+['index/I'])  ),
    'JetGoodBTS[%s]'% ( ','.join(jetVars +['index/I'])  ),
    'met_pt/F', 'met_phi/F', 'met_pt_min/F', 'ISRJets_pt/F', 'CT1/F', 'CT2/F'
]

# Add weight branches for susy signal samples from friend tree
if has_susy_weight_friend:
    new_variables.extend([ "LHE[weight/F]", "LHE_weight_original/F"] )
cache_dir = "/afs/hephy.at/data/cms08/StopsCompressed/signals/caches/2016"
if options.susySignal:
    from StopsCompressed.samples.helpers import getT2ttSignalWeight #, getT2ttISRNorm
    logger.info( "SUSY signal samples to be processed: %s", ",".join(s.name for s in samples) )
    assert len(samples)==1, "Can only process one SUSY sample at a time."
    logger.info( "Signal weights will be drawn from %s files. If that's not the whole sample, stuff will be wrong.", len(samples[0].files))
    logger.info( "Fetching signal weights..." )
    logger.info( "Weights will be stored in %s for future use.", output_directory)
    signalWeight = getT2ttSignalWeight( samples[0], lumi = targetLumi, cacheDir = cache_dir ) #Can use same x-sec/weight for T8bbllnunu as for T2tt
    logger.info("Done fetching signal weights.")

    masspoints = signalWeight.keys()

if sample.isData: new_variables.extend( ['jsonPassed/I','isData/I'] )
new_variables.extend( ['nBTag/I','nISRJets/I', 'nHardBJets/I', 'nSoftBJets/I', 'HT/F', 'dphij0j1/F'] )

new_variables.append( 'lep[%s]'% ( ','.join(lepVars) ) )

if isSingleLep:
    new_variables.extend( ['nGoodMuons/I','nGoodTaus/I', 'nGoodElectrons/I', 'nGoodLeptons/I' ] )
    new_variables.extend( ['l1_pt/F', 'l1_eta/F', 'l1_phi/F', 'l1_pdgId/I', 'l1_index/I', 'l1_jetPtRelv2/F', 'l1_jetPtRatiov2/F', 'l1_miniRelIso/F', 'l1_relIso03/F', 'l1_dxy/F', 'l1_dz/F', 'l1_mIsoWP/I', 'l1_eleIndex/I', 'l1_muIndex/I' , 'mt/F'] )
#    if isMC: 
#        new_variables.extend(['reweightLeptonSF/F', 'reweightLeptonSFUp/F', 'reweightLeptonSFDown/F'])

if addSystematicVariations:
    for var in ['jesTotalUp', 'jesTotalDown', 'jerUp', 'jer', 'jerDown', 'unclustEnUp', 'unclustEnDown']:
        if not var.startswith('unclust'):
            new_variables.extend( ['nJetGood_'+var+'/I', 'HT_'+var+'/F', 'nBTag_'+var+'/I'] )
        new_variables.extend( ['met_pt_'+var+'/F', 'met_phi_'+var+'/F'] )

# Btag weights Method 1a
for var in btagEff.btagWeightNames:
    if var!='MC':
        new_variables.append('reweightBTag_'+var+'/F')

#if options.susySignal or options.TTDM:
#    read_variables += map(TreeVariable.fromString, ['met_genPt/F', 'met_genPhi/F'] )
if options.susySignal:
    new_variables  += ['reweightXSecUp/F', 'reweightXSecDown/F', 'mStop/I', 'mNeu/I']
    if  'T8bbllnunu' in options.samples[0]:
        new_variables  += ['mCha/I', 'mSlep/I', 'sleptonPdg/I']
    if 'T2tt' in options.samples[0]:
        new_variables  += ['weight_pol_L/F', 'weight_pol_R/F']

if not options.skipNanoTools:
    ### nanoAOD postprocessor
    from importlib import import_module
    from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor   import PostProcessor
    from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel       import Collection
    from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop       import Module
   
    ## ISRCounter is in the StopsDilepton branch in the HephyAnalysisSW fork of NanoAODTools
    #from PhysicsTools.NanoAODTools.postprocessing.modules.common.ISRcounter        import ISRcounter
    
    logger.info("Preparing nanoAOD postprocessing")
    logger.info("Will put files into directory %s", output_directory)
    cut = '&&'.join(skimConds)

    from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
    METBranchName = 'MET' if not options.year == 2017 else 'METFixEE2017'

    # check if files are available (e.g. if dpm is broken this should result in an error)
    for f in sample.files:
        if not checkRootFile(f):
            raise IOError ("File %s not available"%f)

    # remove empty files. this is necessary in 2018 because empty miniAOD files exist.
    sample.files = [ f for f in sample.files if nonEmptyFile(f) ]
    newFileList = []
    logger.info("Starting nanoAOD postprocessing")
    for f in sample.files:
        JMECorrector = createJMECorrector(isMC=(not sample.isData), dataYear=options.year, runPeriod=era, jesUncert="Total", jetType = "AK4PFchs", metBranchName=METBranchName, isFastSim=options.fastSim, applySmearing=False)
        modules = [
            JMECorrector()
        ]
        
        #if not sample.isData:
        #    modules.append( ISRcounter() )

        # need a hash to avoid data loss
        file_hash = str(hash(f))
        p = PostProcessor(output_directory, [f], cut=cut, modules=modules, postfix="_for_%s_%s"%(sample.name, file_hash))
        if not options.reuseNanoAOD:
            p.run()
        newFileList += [output_directory + '/' + f.split('/')[-1].replace('.root', '_for_%s_%s.root'%(sample.name, file_hash))]
    logger.info("Done. Replacing input files for further processing.")
    
    sample.files = newFileList

# Define a reader

reader = sample.treeReader( \
    variables = read_variables ,
    selectionString = "&&".join(skimConds)
    )

# using hybridIsolation as defined in 2016 AN 
eleSelector_ = eleSelector( "hybridIso", year = options.year )
muSelector_  = muonSelector("hybridIso", year = options.year )
#tauSelector_ = tauSelector("loose")
def filler( event ):
    # shortcut
    r = reader.event
    #workaround  = (r.run, r.luminosityBlock, r.event) # some fastsim files seem to have issues, apparently solved by this.
    event.isData = s.isData
    
    if isMC:

        ## overlap removal by lukas ##
        # GEN Particles
        gPart = getGenPartsAll(r)
        # GEN Jets
        gJets = getJets( r, jetVars=['pt','eta','phi','mass','partonFlavour','hadronFlavour','index'], jetColl="GenJet" )

    # weight
    if options.susySignal:
        if has_susy_weight_friend:
            if weight_friend.chain.GetEntryWithIndex(r.luminosityBlock, r.event)>0:
                event.LHE_weight_original =  weight_friend.chain.GetLeaf("LHE_weight_original").GetValue()
                event.nLHE = int(weight_friend.chain.GetLeaf("nLHE").GetValue())
                for nEvt in range(event.nLHE):
                    event.LHE_weight[nEvt] = weight_friend.chain.GetLeaf("LHE_weight").GetValue(nEvt)


        r.GenSusyMStop = max([p['mass']*(abs(p['pdgId']==1000006)) for p in gPart])
        r.GenSusyMNeutralino = max([p['mass']*(abs(p['pdgId']==1000022)) for p in gPart])
        if 'T8bbllnunu' in options.samples[0]:
            r.GenSusyMChargino = max([p['mass']*(abs(p['pdgId']==1000024)) for p in gPart])
            r.GenSusyMSlepton = max([p['mass']*(abs(p['pdgId']==1000011)) for p in gPart]) #FIXME check PDG ID of slepton in sample
            logger.debug("Slepton is selectron with mass %i", r.GenSusyMSlepton)
            event.sleptonPdg = 1000011
            if not r.GenSusyMSlepton > 0:
                r.GenSusyMSlepton = max([p['mass']*(abs(p['pdgId']==1000013)) for p in gPart])
                logger.debug("Slepton is smuon with mass %i", r.GenSusyMSlepton)
                event.sleptonPdg = 1000013
            if not r.GenSusyMSlepton > 0:
                r.GenSusyMSlepton = max([p['mass']*(abs(p['pdgId']==1000015)) for p in gPart])
                logger.debug("Slepton is stau with mass %i", r.GenSusyMSlepton)
                event.sleptonPdg = 1000015
            event.mCha  = int(round(r.GenSusyMChargino,0))
            event.mSlep = int(round(r.GenSusyMSlepton,0))

        try:
            event.weight=signalWeight[(int(r.GenSusyMStop), int(r.GenSusyMNeutralino))]['weight'] #* r.genWeight
        except KeyError:
            logger.info("Couldn't find weight for %s, %s. Setting weight to 0.", r.GenSusyMStop, r.GenSusyMNeutralino)
            event.weight = 0.
        event.mStop = int(r.GenSusyMStop)
        event.mNeu  = int(r.GenSusyMNeutralino)
        try:
            event.reweightXSecUp    = signalWeight[(r.GenSusyMStop, r.GenSusyMNeutralino)]['xSecFacUp']
            event.reweightXSecDown  = signalWeight[(r.GenSusyMStop, r.GenSusyMNeutralino)]['xSecFacDown']
        except KeyError:
            logger.info("Couldn't find weight for %s, %s. Setting weight to 0.", r.GenSusyMStop, r.GenSusyMNeutralino)
            event.reweightXSecUp    = 0.
            event.reweightXSecDown  = 0.
    elif isMC:
        if hasattr(r, "genWeight"):
            event.weight = lumiScaleFactor*r.genWeight if lumiScaleFactor is not None else 1
        else:
            event.weight = lumiScaleFactor if lumiScaleFactor is not None else 1
    elif sample.isData:
        event.weight = 1
    else:
        raise NotImplementedError( "isMC %r isData %r susySignal? %r TTDM? %r" % (isMC, isData, options.susySignal, options.TTDM) )

    # lumi lists and vetos
    if sample.isData:
        #event.vetoPassed  = vetoList.passesVeto(r.run, r.lumi, r.evt)
        event.jsonPassed  = lumiList.contains(r.run, r.luminosityBlock)
        # store decision to use after filler has been executed
        event.jsonPassed_ = event.jsonPassed

    if isMC and hasattr(r, "Pileup_nTrueInt"):
        event.reweightPU     = nTrueInt_puRW       ( r.Pileup_nTrueInt ) 
        event.reweightPUDown = nTrueInt_puRWDown   ( r.Pileup_nTrueInt )
        event.reweightPUVDown= nTrueInt_puRWVDown  ( r.Pileup_nTrueInt )
        event.reweightPUUp   = nTrueInt_puRWUp     ( r.Pileup_nTrueInt )
        event.reweightPUVUp  = nTrueInt_puRWVUp    ( r.Pileup_nTrueInt )
        event.reweightPUVVUp = nTrueInt_puRWVVUp   ( r.Pileup_nTrueInt )

    # top pt reweighting
    #if isMC:
        #event.reweightTopPt     = topPtReweightingFunc(getTopPtsForReweighting(r)) * topScaleF if doTopPtReweighting else 1.
        #ISRnorm = getT2ttISRNorm(samples[0], r.GenSusyMStop, r.GenSusyMNeutralino, masspoints, options.year, signal=sample.name, cacheDir='/afs/hephy.at/data/cms01/stopsDilepton/signals/caches/%s/'%(options.year)) if renormISR else 1
        #event.reweight_nISR     = isr.getWeight(r, norm=ISRnorm )             if options.susySignal else 1
        #event.reweight_nISRUp   = isr.getWeight(r, norm=ISRnorm, sigma=1)     if options.susySignal else 1
        #event.reweight_nISRDown = isr.getWeight(r, norm=ISRnorm, sigma=-1)    if options.susySignal else 1

    if options.keepAllJets:
        jetAbsEtaCut = 99.
    else:
        jetAbsEtaCut = 2.4
    
    allSlimmedJets      = getJets(r)
    allSlimmedPhotons   = getPhotons(r, year=options.year)
    if options.year == 2018:
        event.reweightL1Prefire, event.reweightL1PrefireUp, event.reweightL1PrefireDown = 1., 1., 1.
    else:
        event.reweightL1Prefire, event.reweightL1PrefireUp, event.reweightL1PrefireDown = L1PW.getWeight(allSlimmedPhotons, allSlimmedJets)

    # get leptons before jets in order to clean jets
    electrons  = getGoodElectrons(r, ele_selector = eleSelector_)
    muons      = getGoodMuons(r,     mu_selector = muSelector_ )
    #taus       = getGoodTaus(r, tau_selector = tauSelector_ )
    taus       = getGoodTaus(r)
    for e in electrons:
        e['pdgId']      = int( -11*e['charge'] )
        e['eleIndex']   = e['index']
        e['muIndex']    = -1
    for m in muons:
        m['pdgId']      = int( -13*m['charge'] )
        m['muIndex']    = m['index']
        m['eleIndex']   = -1

    leptons = electrons + muons
    leptons.sort(key = lambda p:-p['pt'])

    for iLep, lep in enumerate(leptons):
        lep['index'] = iLep

    fill_vector_collection( event, "lep", lepVarNames, leptons)
    event.nlep = len(leptons)

    # now get jets, cleaned against good leptons

    #jetPtVar = 'pt_nom' # see comment below

    # with the latest change, getAllJets calculates the correct jet pt (removing JER) and stores it as Jet_pt again. No need for Jet_pt_nom anymore
    allJetsNotClean = getAllJets(r, [], ptCut=0, absEtaCut=99, jetVars=jetVarNames, jetCollections=["Jet"], idVar=None)
    reallyAllJets= getAllJets(r, leptons, ptCut=0, absEtaCut=99, jetVars=jetVarNames, jetCollections=["Jet"], idVar='jetId') # keeping robert's comment: ... yeah, I know.
    allJets      = filter(lambda j:abs(j['eta'])<jetAbsEtaCut, reallyAllJets)
    jets         = filter(lambda j:jetId(j, ptCut=30,   absEtaCut=jetAbsEtaCut, ptVar='pt'), allJets)
    ISRJets      = filter(lambda j:jetId(j, ptCut=100,  absEtaCut=jetAbsEtaCut), jets) 

    bJets        = filter(lambda j:      isBJet(j, tagger="CSVv2", year=options.year) and abs(j['eta'])<=2.4    , jets)
    softBJets    = filter(lambda j:      isBJet(j, tagger="CSVv2", year=options.year) and abs(j['eta'])<=2.4  and j['pt']<60   , jets)
    hardBJets    = filter(lambda j:      isBJet(j, tagger="CSVv2", year=options.year) and abs(j['eta'])<=2.4  and j['pt']>60   , jets)
    nonBJets     = filter(lambda j:not ( isBJet(j, tagger="CSVv2", year=options.year) and abs(j['eta'])<=2.4 )  , jets)

    # store the correct MET (EE Fix for 2017, MET_min as backup in 2017)
    
    if options.year == 2017:# and not options.fastSim:
        # v2 recipe. Could also use our own recipe
        event.met_pt    = r.METFixEE2017_pt_nom
        event.met_phi   = r.METFixEE2017_phi_nom
        #event.met_pt_min = r.MET_pt_min not done anymore
    else:
        event.met_pt    = r.MET_pt_nom 
        event.met_phi   = r.MET_phi_nom

    # Filling jets
    maxNJet = 100
    store_jets = jets 
    store_jets = store_jets[:maxNJet]
    store_jets.sort( key = lambda j:-j['pt'])
    event.nJetGood   = len(store_jets)
    for iJet, jet in enumerate(store_jets):
        event.JetGood_index[iJet] = jet['index']
        for b in jetVarNames:
            getattr(event, "JetGood_"+b)[iJet] = jet[b]
        if isMC:
            if store_jets[iJet]['genJetIdx'] >= 0:
                if r.nGenJet<maxNJet:
                    try:
                        event.JetGood_genPt[iJet] = r.GenJet_pt[store_jets[iJet]['genJetIdx']]
                    except IndexError:
                        event.JetGood_genPt[iJet] = -1
                else:
                    event.JetGood_genPt[iJet] = -1
        getattr(event, "JetGood_pt")[iJet] = jet['pt']

    #veto events with 3rd jet pt>60
    #if len(jets)<=2 or (len(jets)>2 and jets[2]['pt']<60):

    # dphi between leading(ISR) and subleading jet with pt >60
    if len (jets) > 1 and jets[1]['pt']>60:
      event.dphij0j1= deltaPhi(jets[0]['phi'],jets[1]['phi'])  
           
        
#    # Filling bjets sorted by pt
#    maxNBJet = 10
#    store_bjets = bJets if not options.keepAllJets else soft_jets + hard_jets 
#    store_bjets = store_bjets[:maxNBJet]
#    store_bjets.sort( key = lambda j:-j['pt'])
#    event.nBJetStored   = len(store_bjets)
#    for iJet, jet in enumerate(store_bjets):
#        event.BTag_index[iJet] = jet['index']
#        for b in jetVarNames:
#            getattr(event, 'BTag_'+b)[iJet] = jet[b]
#        getattr(event, 'BTag_pt')[iJet] = jet['pt']

    # Filling bjets sorted by bTag
    maxNBJet = 10
    store_bjets_d = bJets if not options.keepAllJets else soft_jets + hard_jets 
    store_bjets_d = store_bjets_d[:maxNBJet]
    store_bjets_d.sort( key = lambda j:-j['btagCSVV2'])
    event.nJetGoodBTS = len(store_bjets_d)
    for iJet, jet in enumerate(store_bjets_d):
        event.JetGoodBTS_index[iJet] = jet['index']
        for b in jetVarNames:
            getattr(event, 'JetGoodBTS_'+b)[iJet] = jet[b]
        getattr(event, 'JetGoodBTS_pt')[iJet] = jet['pt']

    event.HT          = sum([j['pt'] for j in jets])
    event.nBTag       = len(bJets)
    event.nSoftBJets  = len(softBJets)
    event.nHardBJets  = len(hardBJets)
    event.nISRJets    = len(ISRJets)
    if event.nISRJets >= 1:
        event.ISRJets_pt  = ISRJets[0]['pt'] 
        
    event.CT1         = min(event.met_pt, event.HT-100) 
    event.CT2         = min(event.met_pt, event.ISRJets_pt)
    alljets_sys   = {}
    jets_sys      = {}
    bjets_sys     = {}
    nonBjets_sys  = {}

    if addSystematicVariations:
        for var in ['jesTotalUp', 'jesTotalDown', 'jerUp', 'jerDown', 'unclustEnUp', 'unclustEnDown']: # don't use 'jer' as of now
            setattr(event, 'met_pt_'+var,  getattr(r, 'METFixEE2017_pt_'+var)  if options.year == 2017 else getattr(r, 'MET_pt_'+var) )
            setattr(event, 'met_phi_'+var, getattr(r, 'METFixEE2017_phi_'+var) if options.year == 2017 else getattr(r, 'MET_phi_'+var) )
            if not var.startswith('unclust'):
                corrFactor = 'corr_JER' if var == 'jer' else None
                alljets_sys[var]    = allJetsNotClean
                jets_sys[var]       = filter(lambda j: jetId(j, ptCut=30, absEtaCut=jetAbsEtaCut, ptVar='pt_'+var if not var=='jer' else 'pt_nom', corrFactor=corrFactor), allJets)
                bjets_sys[var]      = filter(lambda j: isBJet(j) and abs(j['eta'])<2.4, jets_sys[var])
                nonBjets_sys[var]   = filter(lambda j: not ( isBJet(j) and abs(j['eta'])<2.4), jets_sys[var])
                
                # calculate ht
                HT = sum([j['pt_nom']*j['corr_JER'] for j in jets_sys[var]]) if var == 'jer' else sum([j['pt_'+var] for j in jets_sys[var]])

                setattr(event, 'nJetGood_'+var, len(jets_sys[var]))
                setattr(event, 'HT_'+var,       HT)
                setattr(event, 'nBTag_'+var,    len(bjets_sys[var]))

    if isSingleLep:
        event.nGoodMuons      = len(filter( lambda l:abs(l['pdgId'])==13, leptons))
        event.nGoodElectrons  = len(filter( lambda l:abs(l['pdgId'])==11, leptons))
        event.nGoodLeptons    = len(leptons)
        event.nGoodTaus       = len(taus)
        if len(leptons)>=1 :
            event.l1_pt         = leptons[0]['pt']
            event.l1_eta        = leptons[0]['eta']
            event.l1_phi        = leptons[0]['phi']
            event.l1_pdgId      = leptons[0]['pdgId']
            event.l1_index      = leptons[0]['index']
            event.l1_miniRelIso = leptons[0]['miniPFRelIso_all']
            event.l1_relIso03   = leptons[0]['pfRelIso03_all']
            event.l1_dxy        = leptons[0]['dxy']
            event.l1_dz         = leptons[0]['dz']
            event.l1_eleIndex   = leptons[0]['eleIndex']
            event.l1_muIndex    = leptons[0]['muIndex']
            event.mt            = sqrt (2 * event.l1_pt * event.met_pt * (1 - cos(event.l1_phi - event.met_phi) ) )
        
            
#        if isMC:
#            leptonsForSF   = ( leptons[:1]) if isSingleLep else [] )
#            leptonSFValues = [ leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=((l['eta'] + l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta'])) for l in leptonsForSF ]
#            event.reweightLeptonSF     = reduce(mul, [sf[0] for sf in leptonSFValues], 1)
#            event.reweightLeptonSFDown = reduce(mul, [sf[1] for sf in leptonSFValues], 1)
#            event.reweightLeptonSFUp   = reduce(mul, [sf[2] for sf in leptonSFValues], 1)  
#            if event.reweightLeptonSF ==0:
#                logger.error( "reweightLeptonSF is zero!")
#
#            if options.fastSim:
#                leptonFastSimSFValues = [ leptonFastSimSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=((l['eta'] + l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta'])) for l in leptonsForSF ]
#                event.reweightLeptonFastSimSF     = reduce(mul, [sf[0] for sf in leptonFastSimSFValues], 1)
#                event.reweightLeptonFastSimSFDown = reduce(mul, [sf[1] for sf in leptonFastSimSFValues], 1)
#                event.reweightLeptonFastSimSFUp   = reduce(mul, [sf[2] for sf in leptonFastSimSFValues], 1)  
#                if event.reweightLeptonFastSimSF ==0:
#                    logger.error( "reweightLeptonFastSimSF is zero!")
#
#            event.reweightLeptonTrackingSF   = reduce(mul, [leptonTrackingSF.getSF(pdgId = l['pdgId'], pt = l['pt'], eta = ((l['eta'] + l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta']))  for l in leptonsForSF], 1)

    # trigger efficiencies
    if isMC:
        #trig_eff, trig_eff_err =  triggerEff.getSF(event.l1_pt, event.l1_eta, event.l1_pdgId, event.l2_pt, event.l2_eta, event.l2_pdgId)

    # add systematic variations for derived observables 
        if addSystematicVariations:
            for var in ['jesTotalUp', 'jesTotalDown', 'jerUp', 'jerDown', 'unclustEnUp', 'unclustEnDown']: # don't use 'jer' as of now
                pass

    # B tagging weights method 1a
    if isMC:
        for j in jets:
            btagEff.addBTagEffToJet(j)
        for var in btagEff.btagWeightNames:
            if var!='MC':
                setattr(event, 'reweightBTag_'+var, btagEff.getBTagSF_1a( var, bJets, filter( lambda j: abs(j['eta'])<2.4, nonBJets ) ) )

# Create a maker. Maker class will be compiled. This instance will be used as a parent in the loop
treeMaker_parent = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in new_variables ],
    treeName = "Events"
    )

# Split input in ranges
eventRanges = reader.getEventRanges( )

logger.info( "Splitting into %i ranges of %i events on average. FileBasedSplitting: %s. Job number %s",  
        len(eventRanges), 
        (eventRanges[-1][1] - eventRanges[0][0])/len(eventRanges), 
        'Yes',
        options.job)

#Define all jobs
jobs = [(i, eventRanges[i]) for i in range(len(eventRanges))]

filename, ext = os.path.splitext( os.path.join(output_directory, sample.name + '.root') )

if len(eventRanges)>1:
    raise RuntimeError("Using fileBasedSplitting but have more than one event range!")

clonedEvents = 0
convertedEvents = 0
outputLumiList = {}
for ievtRange, eventRange in enumerate( eventRanges ):

    logger.info( "Processing range %i/%i from %i to %i which are %i events.",  ievtRange, len(eventRanges), eventRange[0], eventRange[1], eventRange[1]-eventRange[0] )

    _logger.   add_fileHandler( outfilename.replace('.root', '.log'), options.logLevel )
    _logger_rt.add_fileHandler( outfilename.replace('.root', '_rt.log'), options.logLevel )
    
    tmp_directory = ROOT.gDirectory
    outputfile = ROOT.TFile.Open(outfilename, 'recreate')
    tmp_directory.cd()

    if options.small: 
        logger.info("Running 'small'. Not more than 10000 events") 
        nMaxEvents = eventRange[1]-eventRange[0]
        eventRange = ( eventRange[0], eventRange[0] +  min( [nMaxEvents, 10000] ) )

    # Set the reader to the event range
    reader.setEventRange( eventRange )

    clonedTree = reader.cloneTree( branchKeepStrings, newTreename = "Events", rootfile = outputfile )

    clonedEvents += clonedTree.GetEntries()
    # Clone the empty maker in order to avoid recompilation at every loop iteration
    maker = treeMaker_parent.cloneWithoutCompile( externalTree = clonedTree )

    maker.start()
    # Do the thing
    reader.start()

    while reader.run():
        maker.run()
        if sample.isData:
            if maker.event.jsonPassed_:
                if reader.event.run not in outputLumiList.keys():
                    outputLumiList[reader.event.run] = set([reader.event.luminosityBlock])
                else:
                    if reader.event.luminosityBlock not in outputLumiList[reader.event.run]:
                        outputLumiList[reader.event.run].add(reader.event.luminosityBlock)

    convertedEvents += maker.tree.GetEntries()
    maker.tree.Write()
    outputfile.Close()
    logger.info( "Written %s", outfilename)

  # Destroy the TTree
    maker.clear()
    sample.clear()

logger.info( "Converted %i events of %i, cloned %i",  convertedEvents, reader.nEvents , clonedEvents )

# Storing JSON file of processed events
if sample.isData and convertedEvents>0: # avoid json to be overwritten in cases where a root file was found already
    jsonFile = filename+'_%s.json'%(0 if options.nJobs==1 else options.job)
    LumiList( runsAndLumis = outputLumiList ).writeJSON(jsonFile)
    logger.info( "Written JSON file %s", jsonFile )

if not options.keepNanoAOD and not options.skipNanoTools:
    for f in sample.files:
        try:
            os.remove(f)
            logger.info("Removed nanoAOD file: %s", f)
        except OSError:
            logger.info("nanoAOD file %s seems to be not there", f)

logger.info("Copying log file to %s", output_directory )
copyLog = subprocess.call(['cp', logFile, output_directory] )
if copyLog:
    logger.info( "Copying log from %s to %s failed", logFile, output_directory)
else:
    logger.info( "Successfully copied log file" )
    os.remove(logFile)
    logger.info( "Removed temporary log file" )

if checkRootFile( outfilename, checkForObjects=["Events"] ) and deepCheckRootFile( outfilename ) and deepCheckWeight( outfilename ):
    logger.info( "Target: File check ok!" )
else:
    logger.info( "Corrupt rootfile! Removing file: %s"%outfilename )
    os.remove( outfilename )
    raise Exception("Corrupt rootfile! File not copied: %s"%source )

