# Standard imports 
import os
import ROOT

# RootTools
from RootTools.core.standard import *

# Logging
import logging
logger = logging.getLogger(__name__)

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance


def getSubDir(dataset, path):
    import re
    m=re.match("\/(.*)\/(.*)\/(.*)",dataset)
    if not m :
        print "NO GOOD DATASET"
        return
    if os.environ['USER'] in ['tomc']: 
      d=re.match("(.*)/cmgTuples/(.*)",path)
      return m.group(1)+"/"+m.group(2)+'_'+d.group(2)
    else :                             
      return m.group(1)+"_"+m.group(2)

def fromHeppySample(sample, data_path, module = None, maxN = None):
    ''' Load CMG tuple from local directory
    '''

    import importlib
    if module is not None:
        module_ = module
    elif "Run2016" in sample:
        module_ = 'CMGTools.RootTools.samples.samples_13TeV_DATA2016'
        #module_ = 'CMGTools.StopsDilepton.samples_13TeV_Moriond2017'
    elif ("T2tt" in sample) or ("T2bt" in sample) or ("T2bW" in sample):
        module_ = 'CMGTools.RootTools.samples.samples_13TeV_signals'
    elif "T8bbllnunu" in sample:
        module_ = 'CMGTools.RootTools.samples.samples_13TeV_signals'
    elif "TTbarDM" in sample:
        module_ = 'CMGTools.StopsDilepton.TTbarDMJets_signals_RunIISummer16MiniAODv2'
    elif "HToInv" in sample:
        module_ = 'CMGTools.StopsDilepton.Higgs_signals_RunIISummer16MiniAODv2'
    else: 
        module_ = 'CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2'

    try:
        heppy_sample = getattr(importlib.import_module( module_ ), sample)
    except:
        raise ValueError( "Could not load sample '%s' from %s "%( sample, module_ ) )

    subDir = getSubDir(heppy_sample.dataset, data_path)
    if not subDir:
        raise ValueError( "Not a good dataset name: '%s'"%heppy_sample.dataset )

    path = os.path.join( data_path, subDir )
    from StopsDilepton.tools.user import runOnGentT2
    if runOnGentT2: 
        sample = Sample.fromCMGCrabDirectory(
            heppy_sample.name, 
            path, 
            treeFilename = 'tree.root', 
            treeName = 'tree', isData = heppy_sample.isData, maxN = maxN)
    else:  # Vienna -> Load from DPM 
        if True: #'/dpm' in data_path:

            from RootTools.core.helpers import renew_proxy
            user = os.environ['USER']
            # Make proxy in afs to allow batch jobs to run
            proxy_path = os.path.expandvars('$HOME/private/.proxy')
            proxy = renew_proxy( proxy_path )
            logger.info( "Using proxy %s"%proxy )

            if module is not None:
                module_ = module
            if "Run2016" in sample:
                from StopsDilepton.samples.heppy_dpm_samples import data_03Feb2017_heppy_mapper as data_heppy_mapper
                return data_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif ("T2tt" in sample) or ("T8bb" in sample) or ("T2b" in sample):
                from StopsDilepton.samples.heppy_dpm_samples import SUSY_heppy_mapper
                return SUSY_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "TTbarDM" in sample:
                from StopsDilepton.samples.heppy_dpm_samples import ttbarDM_heppy_mapper
                return ttbarDM_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "HToInv" in sample:
                from StopsDilepton.samples.heppy_dpm_samples import Higgs_heppy_mapper
                return Higgs_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            else: 
                from StopsDilepton.samples.heppy_dpm_samples import mc_heppy_mapper
                return mc_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            raise ValueError
        else:                           
            sample = Sample.fromCMGOutput(
                heppy_sample.name, 
                path, 
                treeFilename = 'tree.root', 
                treeName = 'tree', isData = heppy_sample.isData, maxN = maxN)

    sample.heppy = heppy_sample
    return sample

from StopsCompressed.Tools.helpers import getObjFromFile, writeObjToFile

def getSignalWeight(sample, lumi, cacheDir, channel = 'stop13TeV'):
    '''Get a dictionary for signal weights
    '''
    from StopsCompressed.Tools.xSecSusy import xSecSusy
    #from StopsCompressed.Tools.genFilter import genFilter
    #genFilter = genFilter(year=2016)
    xSecSusy_ = xSecSusy()
    signalWeight={}
    mMax = 2000
    bStr = str(mMax)+',0,'+str(mMax)

    if channel == "stop13TeV":
        mass1_name = "mStop"
        mass2_name = "mNeu"
        mass1_pdgId = 1000006 
        mass2_pdgId = 1000022
    elif channel == "TChiWZ_13TeV":
        mass1_name = "mCha"
        mass2_name = "mNeu"
        mass1_pdgId = 1000024
        mass2_pdgId = 1000022
    else:
        raise NotImplementedError

    if not os.path.isdir(cacheDir):
        os.makedirs(cacheDir)
    cacheFile = os.path.join(cacheDir, "%s_signalCounts.root"%sample.name)
    if os.path.isfile(cacheFile):
        logger.info("Loading signal weights from %s", cacheFile)
        hNEvents = getObjFromFile(cacheFile, "hNEvents")
    else:
        sample.chain.Draw("Max$(GenPart_mass*(abs(GenPart_pdgId)=={mass2_pdgId})):Max$(GenPart_mass*(abs(GenPart_pdgId)=={mass1_pdgId}))>>hNEvents(".format(mass1_pdgId = mass1_pdgId, mass2_pdgId = mass2_pdgId) + ','.join([bStr, bStr])+")", "", "goff")

        hNEvents = ROOT.gDirectory.Get("hNEvents")
        logger.info("Writing signal weights to %s", cacheFile)
        writeObjToFile(cacheFile, hNEvents)

    for i in range (mMax):
        for j in range (mMax):
            n = hNEvents.GetBinContent(hNEvents.FindBin(i,j))
            if n>0:
                signalWeight[(i,j)] = {'weight':lumi*xSecSusy_.getXSec(channel=channel,mass=i,sigma=0)/n, 'xSecFacUp':xSecSusy_.getXSec(channel=channel,mass=i,sigma=1)/xSecSusy_.getXSec(channel=channel,mass=i,sigma=0), 'xSecFacDown':xSecSusy_.getXSec(channel=channel,mass=i,sigma=-1)/xSecSusy_.getXSec(channel=channel,mass=i,sigma=0)}

    	        logger.info("Found {mass1_name} %5i {mass2_name} %5i Number of events: %6i, xSec: %10.6f, weight: %6.6f (+1 sigma rel: %6.6f, -1 sigma rel: %6.6f)".format(mass1_name = mass1_name, mass2_name = mass2_name), i,j,n, xSecSusy_.getXSec(channel=channel,mass=i,sigma=0),  signalWeight[(i,j)]['weight'], signalWeight[(i,j)]['xSecFacUp'], signalWeight[(i,j)]['xSecFacDown'])

                #genEff = genFilter.getEff(i,j) # TODO: add gen filter weights? only after mass point splitting?
                #         signalWeight[(i,j)] = {'weight':lumi*genEff*xSecSusy_.getXSec(channel=channel,mass=i,sigma=0)/n, 'xSecFacUp':xSecSusy_.getXSec(channel=channel,mass=i,sigma=1)/xSecSusy_.getXSec(channel=channel,mass=i,sigma=0), 'xSecFacDown':xSecSusy_.getXSec(channel=channel,mass=i,sigma=-1)/xSecSusy_.getXSec(channel=channel,mass=i,sigma=0)}
                #logger.info( "Found mStop %5i mNeu %5i Number of events: %6i, xSec: %10.6f, weight: %6.6f (+1 sigma rel: %6.6f, -1 sigma rel: %6.6f), genEff: %6.6f", i,j,n, xSecSusy_.getXSec(channel=channel,mass=i,sigma=0),  signalWeight[(i,j)]['weight'], signalWeight[(i,j)]['xSecFacUp'], signalWeight[(i,j)]['xSecFacDown'], genEff)
    del hNEvents
    return signalWeight


def GetFilterEff(deltaM) :
    if deltaM == 30 :
        return 0.327
    else :
        return 1.

def getISRNorm(sample, mass1, mass2, massPoints, year, signal="T2tt", fillCache=False, cacheDir='/tmp/ISR/', overwrite=False):
    '''
    Get the normalization for the ISR reweighting. Needs post-processed samples for nISR.
    '''
    from StopsCompressed.Tools.user import analysis_results
    from StopsCompressed.Analysis.Cache import Cache
    #from StopsCompressed.Tools.genFilter import genFilter
    #genFilter = genFilter(year=year)
    signalWeight={}
    mMax = 2000
    bStr = str(mMax)+','+str(mMax)
    #print bStr
    
    cache = Cache(cacheDir, verbosity=2)

    if signal == "T2tt":
        mass1_pdgId = 1000006 
        mass2_pdgId = 1000022
    elif signal == "TChiWZ": # NOTE: ISR/W-pt reweighting is probably more relevant than the nISR reweighting for EWKinos (see https://indico.cern.ch/event/616816/contributions/2489809/attachments/1418579/2174166/17-02-22_ana_isr_ewk.pdf)
        mass1_pdgId = 1000024
        mass2_pdgId = 1000022

    key = (mass1, mass2, signal, year)

    # get the norm for all
    if (fillCache and not cache.contains(key)) or overwrite:
        from StopsCompressed.Tools.isrWeight import ISRweight
        isr = ISRweight()
        isrWeightString = isr.getWeightString()
        sample.chain.Draw("Max$(GenPart_mass*(abs(GenPart_pdgId)=={mass2_pdgId})):Max$(GenPart_mass*(abs(GenPart_pdgId)=={mass1_pdgId}))>>hReweighted(".format(mass1_pdgId = mass1_pdgId, mass2_pdgId = mass2_pdgId) + ','.join([bStr, bStr])+")", isrWeightString+'*(1)',"goff")
        hReweighted = ROOT.gDirectory.Get("hReweighted")

        sample.chain.Draw("Max$(GenPart_mass*(abs(GenPart_pdgId)=={mass2_pdgId})):Max$(GenPart_mass*(abs(GenPart_pdgId)=={mass1_pdgId}))>>hCentral(".format(mass1_pdgId = mass1_pdgId, mass2_pdgId = mass2_pdgId) + ','.join([bStr, bStr])+")", '(1)',"goff")
        hCentral = ROOT.gDirectory.Get("hCentral")

        for mass1, mass2 in massPoints:
            key = (mass1, mass2, signal, year)
            norm = hCentral.GetBinContent(hCentral.GetXaxis().FindBin(mass1), hCentral.GetYaxis().FindBin(mass2)) / hReweighted.GetBinContent(hReweighted.GetXaxis().FindBin(mass1), hReweighted.GetYaxis().FindBin(mass2))
            cache.add(key, norm)

    if not cache.contains(key):
        return False
    else:
        return cache.get(key)
