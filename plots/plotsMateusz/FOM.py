# Script for making FOM plots

import ROOT
import os, sys
import argparse
import Workspace.DegenerateStopAnalysis.toolsMateusz.ROOToptions
from Workspace.DegenerateStopAnalysis.toolsMateusz.drawFunctions import *
from Workspace.DegenerateStopAnalysis.toolsMateusz.pythonFunctions import *
from Workspace.DegenerateStopAnalysis.tools.degTools import CutClass, getStackFromHists, setEventListToChains, setup_style, makeDir, anyIn, makeLegend, getFOMPlotFromStacks, makeLumiTag, drawCMSHeader
from Workspace.HEPHYPythonTools.helpers import getChain, getPlotFromChain, getYieldFromChain

from StopsCompressed.Tools.genFilter import genFilter

from array import array
from math import pi, sqrt #cos, sin, sinh, log

#Sets TDR style
setup_style()

#Input options
parser = argparse.ArgumentParser(description = "Input options")
parser.add_argument("--sensitivityStudyName", default = "baseline",  type=str,    action="store",      help="Name of sensitivity study")
parser.add_argument("--plots",    dest = "plots",   help = "Plots", type = str, default = None, nargs ="+")
parser.add_argument("--region",   dest = "region",  help = "Analysis region", type = str, default = "SR1")
parser.add_argument("--getData",  dest = "getData", help = "Get data samples", type = int, default = 0)
parser.add_argument("--year",     dest = "year",    help = "Year", type = str, default = "2018")
parser.add_argument("--channel",  dest = "channel", help = "Lepton channel", type = str, choices = ['all', 'mu', 'e'], default = "all")
parser.add_argument("--nMinus1",  dest = "nMinus1", help = "nMinus1", type = int, default = 1)
parser.add_argument("--highWeightVeto",  dest = "highWeightVeto",  help = "High weight event veto", action = "store_true")
#parser.add_argument("--skim", dest = "skim",  help = "Skim", type = str, default = "preIncLep")
parser.add_argument("--logy",     dest = "logy",  help = "Toggle logy", type = int, default = 1)
parser.add_argument("--save",     dest = "save",  help = "Toggle save", type = int, default = 1)
parser.add_argument("--verbose",  dest = "verbose",  help = "Verbosity switch", type = int, default = 0)
args = parser.parse_args()
if not len(sys.argv) > 1:
   print makeLine()
   print "No arguments given. Using default settings."
   print makeLine()
   #exit()

#Arguments
sensitivityStudyName = args.sensitivityStudyName
getData = args.getData
year = args.year
channel = args.channel
nMinus1 = args.nMinus1
highWeightVeto = args.highWeightVeto
#skim = args.skim
logy = args.logy
save = args.save
verbose = args.verbose

print makeDoubleLine()
print "Creating FOM plots %s in %s"%(args.plots, args.region)
print makeDoubleLine()

#Samples
if year == "2018":
    # MC
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import WJets_18, TTJets_18, ZInv_18, QCD_18, Others_18
    # Signals
    from StopsCompressed.samples.nanoTuples_Autumn18_signal_postProcessed import signals_T2tt, signals_T2bW, signals_TChiWZ
    signals = signals_T2tt + signals_T2bW + signals_TChiWZ
    sigList = ["T2tt_500_420", "T2tt_500_460", "T2tt_500_490", "TChiWZ_200_150", "TChiWZ_200_170", "TChiWZ_200_190"] # benchmark signals: mStop = 500; mCha = 200 GeV
    #sigList = ["T2tt_550_470", "T2tt_550_510", "T2tt_550_540", "TChiWZ_200_150", "TChiWZ_200_170", "TChiWZ_200_190"] # benchmark signals: mStop = 550; mCha = 200 GeV
    selSignals = [s for s in signals if s.name in sigList]
    assert len(sigList) == len(selSignals)

    # Data
    if getData:
        from StopsCompressed.samples.nanoTuples_Run2018_postProcessed import Run2018
        Data = Run2018

    WJets        = WJets_18
    Top          = TTJets_18
    ZInv         = ZInv_18
    QCD          = QCD_18
    Others       = Others_18
else:
    print "Year %s not in choices. Exiting."%year
    sys.exit(0)

samples = {
         'WJets'     : WJets,
         'Top'       : Top,
         'ZInv'      : ZInv,
         'QCD'       : QCD,
         'Others'    : Others
     }

sampleList = ['QCD', 'ZInv', 'Others', 'Top', 'WJets'] # NOTE: hard-coded due to plotting order
assert len(sampleList) == len(samples.keys())

if getData: 
    dataList = ['Data']
else:
    dataList = []

plotsDict = {
   "lep_mt"        :{'var':"mt",                   "bins":[40,0,200],      "decor":{"title":"lepMt",                         "x":"m_{{T}}({lepLatex})",                     "y":"Events", 'log':[0,logy,0]}},
   "lep_pt"        :{'var':"l1_pt",                "bins":[40,0,200],      "decor":{"title":"lepPt",                         "x":"p_{{T}}({lepLatex})",                     "y":"Events", 'log':[0,logy,0]}},
   "lep_eta"       :{'var':"l1_eta",               "bins":[20,-3,3],       "decor":{"title":"lepEta",                        "x":"#eta({lepLatex})",                        "y":"Events", 'log':[0,logy,0]}},
   "lep_phi"       :{'var':"l1_phi",               "bins":[20,-3.15,3.15], "decor":{"title":"lepPhi",                        "x":"#phi({lepLatex})",                        "y":"Events", 'log':[0,logy,0]}},
   "lep_dxy"       :{'var':"l1_dxy",               "bins":[40,-0.02,0.02], "decor":{"title":"lepDxy",                        "x":"d_{{xy}}({lepLatex})",                    "y":"Events", 'log':[0,logy,0]}},
   "lep_dxySig"    :{'var':"(l1_dxy/l1_dxyErr)",   "bins":[40,-2,2],       "decor":{"title":"lepDxySig",                     "x":"d_{{xy}}/#sigma_{{dxy}}({lepLatex})",     "y":"Events", 'log':[0,logy,0]}},
   "lep_dz"        :{'var':"l1_dz",                "bins":[40,-0.1,0.1],   "decor":{"title":"lepDz",                         "x":"d_{{z}}({lepLatex})",                     "y":"Events", 'log':[0,logy,0]}},
   "lep_dzSig"     :{'var':"(l1_dz/l1_dzErr)",     "bins":[40,-2,2],       "decor":{"title":"lepDzSig",                      "x":"d_{{z}}/#sigma_{{dz}}({lepLatex})",       "y":"Events", 'log':[0,logy,0]}},
   "lep_relIso"    :{'var':"l1_relIso03",          "bins":[30,0,3],        "decor":{"title":"lepRelIso",                     "x":"Relative Isolation ({lepLatex})",         "y":"Events", 'log':[0,logy,0]}},
   "lep_miniRelIso":{'var':"l1_miniRelIso",        "bins":[30,0,3],        "decor":{"title":"lepMiniRelIso",                 "x":"Mini Relative Isolation ({lepLatex})",    "y":"Events", 'log':[0,logy,0]}},
   "lep_HI"        :{'var':"l1_HI",                "bins":[50,0,5],        "decor":{"title":"lepHI",                         "x":"Hybrid Isolation ({lepLatex})",           "y":"Events", 'log':[0,logy,0]}},
   "lep_charge"    :{'var':"l1_charge",            "bins":[3,-1,1],        "decor":{"title":"lepCharge",                     "x":"Charge ({lepLatex})",                     "y":"Events", 'log':[0,logy,0]}},
   "lep_Wpt"       :{'var':"lep_wPt",              "bins":[40,200,600],    "decor":{"title":"lepWpt",                        "x":"W-p_{{T}} ({lepLatex})",                  "y":"Events", 'log':[0,logy,0]}},
   "MET"           :{'var':"MET_pt",               "bins":[40,200,1000],   "decor":{"title":"MET",                           "x":"p^{miss}_{T}",                            "y":"Events", 'log':[0,logy,0]}},
   "HT"            :{'var':"HT",                   "bins":[40,200,1000],   "decor":{"title":"HT",                            "x":"H_{T}",                                   "y":"Events", 'log':[0,logy,0]}},
   "CT1"           :{'var':"CT1",                  "bins":[40,100,1000],   "decor":{"title":"CT1",                           "x":"C_{T1}",                                  "y":"Events", 'log':[0,logy,0]}},
   "CT2"           :{'var':"CT2",                  "bins":[40,100,1000],   "decor":{"title":"CT2",                           "x":"C_{T2}",                                  "y":"Events", 'log':[0,logy,0]}},
   "ISR_pt"        :{'var':"ISRJets_pt",           "bins":[45,100,1000],   "decor":{"title":"ISR Jet p_{T}",                 "x":"ISR Jet p_{T}",                           "y":"Events", 'log':[0,logy,0]}},
   "nJets"         :{'var':"nJetGood",             "bins":[10,0,10],       "decor":{"title":"# of Jets with p_{T} > 30 GeV", "x":"N(Jets p_{T} > 30 GeV)",                  "y":"Events", 'log':[0,logy,0]}},
   "dPhiJetMet"    :{'var':"dPhiJetMet",           "bins":[30,0,3.15],     "decor":{"title":"dPhiJetMet",                    "x":"#Delta#phi(Leading Jet,p^{miss}_{T})",    "y":"Events", 'log':[0,logy,0]}},
   "dPhiLepMet"    :{'var':"dPhiLepMet",           "bins":[30,0,3.15],     "decor":{"title":"dPhiLepMet",                    "x":"#Delta#phi({lepLatex},p^{{miss}}_{{T}})", "y":"Events", 'log':[0,logy,0]}},
   "dPhiLepJet"    :{'var':"dPhiLepJet",           "bins":[30,0,3.15],     "decor":{"title":"dPhiLepJet",                    "x":"#Delta#phi({lepLatex},Leading Jet)",      "y":"Events", 'log':[0,logy,0]}},
   "ratio_MET-HT"  :{'var':"(MET_pt/HT)",          "bins":[40,0,2],        "decor":{"title":"ratioMETHT",                    "x":"p^{miss}_{T}/H_{T}",                      "y":"Events", 'log':[0,logy,0]}},
   "ratio_MET-lep" :{'var':"(MET_pt/l1_pt)",       "bins":[40,0,20],       "decor":{"title":"ratioMETlepPt",                 "x":"p^{{miss}}_{{T}}/p_{{T}}({lepLatex})",      "y":"Events", 'log':[0,logy,0]}},
   "ratio_MET-Wpt" :{'var':"(MET_pt/lep_wPt)",     "bins":[40,0.5,1.5],    "decor":{"title":"ratioMETlepWpt",                "x":"p^{{miss}}_{{T}}/W-p_{{T}}({lepLatex})",    "y":"Events", 'log':[0,logy,0]}},
   "recoil_ISR-MET":{'var':"(ISRJets_pt/MET_pt)",  "bins":[40,0,1.5],      "decor":{"title":"recoilISRMET",                  "x":"ISR Jet p_{T}/p^{miss}_{T}",              "y":"Events", 'log':[0,logy,0]}},
   "recoil_ISR-HT" :{'var':"(ISRJets_pt/HT)",      "bins":[40,0,2],        "decor":{"title":"recoilISRHT",                   "x":"ISR Jet p_{T}/H_{T}",                     "y":"Events", 'log':[0,logy,0]}},
   "recoil_ISR-lep":{'var':"(ISRJets_pt/l1_pt)",   "bins":[40,0,20],       "decor":{"title":"recoilISRlepPt",                "x":"ISR Jet p_{{T}}/p_{{T}}({lepLatex})",     "y":"Events", 'log':[0,logy,0]}},
   "recoil_ISR-Wpt":{'var':"(ISRJets_pt/lep_wPt)", "bins":[40,0,2],        "decor":{"title":"recoilISRlepWpt",               "x":"ISR Jet p_{{T}}/W-p_{{T}}({lepLatex})",   "y":"Events", 'log':[0,logy,0]}},
   }

plotsDict_mu = {
   "mu_looseId" :{'var':"Muon_looseId[l1_muIndex[0]]",  "bins":[3,0,3], "decor":{"title":"muLooseId",  "x":"Loose ID ({lepLatex})",  "y":"Events", 'log':[0,logy,0]}},
   "mu_mediumId":{'var':"Muon_mediumId[l1_muIndex[0]]", "bins":[3,0,3], "decor":{"title":"muMediumId", "x":"Medium ID ({lepLatex})", "y":"Events", 'log':[0,logy,0]}},
   "mu_tightId" :{'var':"Muon_tightId[l1_muIndex[0]]",  "bins":[3,0,3], "decor":{"title":"muTightId",  "x":"Tight ID ({lepLatex})",  "y":"Events", 'log':[0,logy,0]}},
   }

if channel == "mu": plotsDict.update(plotsDict_mu)

from StopsCompressed.Analysis.Setup import Setup
setup = Setup(year=year)

lumi_pb = 59.83*1000 #Data.lumi
lumi_fb = 59.83      #Data.lumi/1000.0

#weight_str = "weight * {lumi_weight}".format(lumi_weight = lumi_fb)

#weight_       = lambda event, sample: event.weight*event.reweightHEM
#sample.weight = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightwPt * event.reweightLeptonSF * genEff * lumi_year[event.year]/1000

if sensitivityStudyName in ["baseline", "baseline_redSys"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins56_mt95_3mTregions_CT400_isPromptFalse_lowMETregionFalse"
    import StopsCompressed.Analysis.regions as regions # NOTE: 2016 analysis regions
elif sensitivityStudyName in ["baselinePlusLowMET", "baselinePlusLowMET3", "baselinePlusLowMET3_redSys"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins80_mt95_3mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_4mTregions", "baselinePlusLowMET3_redSys_4mTregions"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins104_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_4mTregions as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_4mTregions_splitCTZ", "baselinePlusLowMET3_redSys_4mTregions_splitCTZ"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins104_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_4mTregions_splitCTZ as regions
elif sensitivityStudyName in ["baselinePlusLowMET_4mTregions_splitCTZ_lowHTbin", "baselinePlusLowMET3_redSys_4mTregions_splitCTZ_lowHTbin"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins136_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_4mTregions_splitCTZ_lowHTbin as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_low5mTregions", "baselinePlusLowMET3_redSys_low5mTregions"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins132_mt95_low5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_low5mTregions as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_high5mTregions", "baselinePlusLowMET3_redSys_high5mTregions"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins128_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_high5mTregions as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_high5mTregions_splitCTZ_lowHTbin", "baselinePlusLowMET3_redSys_high5mTregions_splitCTZ_lowHTbin"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins168_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_high5mTregions_splitCTZ_lowHTbin as regions
elif sensitivityStudyName in ["baselinePlusLowMET_high5mTregions_splitCTZ3_lowHTbin", "baselinePlusLowMET3_redSys_high5mTregions_splitCTZ3_lowHTbin"]:
    fullSensitivityStudyName = args.sensitivityStudyName + "_nbins208_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_high5mTregions_splitCTZ3_lowHTbin as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_high5mTregions_splitCTZ3_lowHTbin_tightIPZ", "baselinePlusLowMET3_redSys_high5mTregions_splitCTZ3_lowHTbin_tightIPZ"]:
    fullSensitivityStudyName = args.sensitivityStudyName + "_nbins208_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_high5mTregions_splitCTZ3_lowHTbin_tightIPZ as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_6mTregions", "baselinePlusLowMET3_redSys_6mTregions"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins156_mt95_6mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_6mTregions as regions 
elif sensitivityStudyName in ["baselinePlusLowMET_6mTregions_splitCTZ_lowHTbin", "baselinePlusLowMET3_redSys_6mTregions_splitCTZ_lowHTbin"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins204_mt95_6mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_6mTregions_splitCTZ_lowHTbin as regions
elif sensitivityStudyName in ["extra"]:
    fullSensitivityStudyName = sensitivityStudyName
    import StopsCompressed.Analysis.regions_extra as regions 
else:
    raise NotImplementedError

cut_name = args.region
if args.region != "presel":
    region = getattr(regions, args.region)
presel = {}
weight_str = {}
cut_str = {'Data':{'nMinus1':{}}, 'MC':{'nMinus1':{}}}

if args.plots:
    plotList = args.plots
else:
    plotList = ["MET", "HT", "CT1", "CT2", "lep_pt", "lep_mt", "ISR_pt", "nJets"]

for dataMC in ["Data", "MC"]: # DataMC
    presel[dataMC] = setup.preselection(dataMC, channel = channel)
    if args.region == "presel":
        cut_str[dataMC]['full'] = presel[dataMC]['cut']
    else:
        cut_str[dataMC]['full'] = "&&".join([region.cutString(setup.sys['selectionModifier']), presel[dataMC]['cut']])

    if highWeightVeto:
        cut_str[dataMC]['full'] += "&& weight < 5"
   
    if nMinus1:
        for p in plotList:
            # CT1 fully correlated with MET and HT
            if p == "CT1": 
                cut_str[dataMC]['nMinus1'][p] = "&&".join([x for x in cut_str[dataMC]['full'].split('&&') if plotsDict[p]['var'] not in x and 'MET' not in x and 'HT' not in x])
            elif p == "HT": 
                cut_str[dataMC]['nMinus1'][p] = "&&".join([x for x in cut_str[dataMC]['full'].split('&&') if plotsDict[p]['var'] not in x and 'CT1' not in x and 'CT2' not in x and 'ISRJets_pt' not in x])
            # CT2 fully correlated with MET and ISR jet pT
            elif p == "CT2":
                cut_str[dataMC]['nMinus1'][p] = "&&".join([x for x in cut_str[dataMC]['full'].split('&&') if plotsDict[p]['var'] not in x and 'MET' not in x and 'ISRJets_pt' not in x and 'HT' not in x])
            elif p == "ISR_pt": 
                cut_str[dataMC]['nMinus1'][p] = "&&".join([x for x in cut_str[dataMC]['full'].split('&&') if plotsDict[p]['var'] not in x and 'CT2' not in x])
            elif p == "MET":
                cut_str[dataMC]['nMinus1'][p] = "&&".join([x for x in cut_str[dataMC]['full'].split('&&') if plotsDict[p]['var'] not in x and 'CT1' not in x and 'CT2' not in x])
            else:
                cut_str[dataMC]['nMinus1'][p] = "&&".join([x for x in cut_str[dataMC]['full'].split('&&') if plotsDict[p]['var'] not in x])
 
    if dataMC == "MC":
        weight_str[dataMC] = presel[dataMC]["weightStr"] + "* {lumi_weight}".format(lumi_weight = lumi_fb)
    else: # if data
        weight_str[dataMC] = "weight" # NOTE: hard-coded for data, which does not contain all branches
        #weight_str[dataMC] = presel[x]["weightStr"]

isDataPlot = getData
bkgList = sampleList
plotLimits = []
fomIntegral = True
fomTitles = False
ratioNorm = False
leg = True
unity = True
dOpt = "hist"

addOverFlowBin = 'upper'
plotLimits = [1, 100]
denoms=["bkg"]
noms = sigList
fom = "SOB" # "SOBSYS", "AMS", "AMSSYS", "AMS1", "AMSc"
fomLimits = [0,0.8]
normalize = False
plotMin = 0.1
    
binningIsExplicit = False
variableBinning = (False, 1)
 
canvs = {}
hists = {}

for samp in sampleList + sigList:
    hists[samp] = {}

stacks = {'bkg':{}, 'sig':{}} 

#for p in plotsDict.iterkeys():
for p in plotList:
    if nMinus1:
        cut_string = cut_str['MC']['nMinus1'][p]
    else:
        cut_string = cut_str['MC']['full']

    bkgHists = []
    # MC
    for samp in sampleList:
        hists[samp][p] = getPlotFromChain(samples[samp].chain, plotsDict[p]['var'], plotsDict[p]['bins'], cut_string, weight = weight_str["MC"], addOverFlowBin = addOverFlowBin, binningIsExplicit = binningIsExplicit, variableBinning = variableBinning, uniqueName = False)
  
        hists[samp][p].SetFillColor(samples[samp].color)
        hists[samp][p].SetName("hist_%s_%s"%(samp,p))
        bkgHists.append(hists[samp][p])
 
    stacks['bkg'][p] = getStackFromHists(bkgHists)
   
    # Signal 
    #stacks = getBkgSigStacks(samples, plotsDict, cut, sampleList = sampleList, plotList = plotList, normalize = normalize, transparency = normalize, scale = mc_scale, sName = cut_name)
    sigHists = [] 
    for i, sig in enumerate(sigList):
        if "T2tt" in sig:
            mStop = int(sig.split('_')[1])
            mNeu  = int(sig.split('_')[2])

            gFilter = genFilter(year = args.year, signal = "T2tt")
            genEff  = gFilter.getEff(mStop,mNeu) # NOTE: uses ROOT file insead
            #genEff  = gFilter.getEffFromPkl(mStop,mNeu)
        elif "T2bW" in sig:
            mStop = int(sig.split('_')[1])
            mNeu  = int(sig.split('_')[2])

            gFilter = genFilter(year = args.year, signal = "T2bW")
            genEff  = gFilter.getEffFromPkl(mStop,mNeu)
        elif "TChiWZ" in sig:
            mCha  = int(sig.split('_')[1])
            mNeu  = int(sig.split('_')[2])

            gFilter = genFilter(year = args.year, signal = "TChiWZ")
            genEff  = gFilter.getEffFromPkl(mCha,mNeu)
        else:
            raise NotImplementedError
    
        hists[sig][p] = getPlotFromChain(selSignals[i].chain, plotsDict[p]['var'], plotsDict[p]['bins'], cut_string, weight = "(%s * %s)"%(weight_str["MC"], genEff), addOverFlowBin = addOverFlowBin, binningIsExplicit = binningIsExplicit, variableBinning = variableBinning, uniqueName = False)
        hists[sig][p].SetName("hist_%s_%s"%(sig,p))
        hists[sig][p].SetMarkerSize(1.2)
        if "T2" in sig:
            hists[sig][p].SetMarkerStyle(5)
            hists[sig][p].SetMarkerColor(ROOT.kRed-(3*(i%3)))
            hists[sig][p].SetLineColor(ROOT.kRed-(3*(i%3)))
        else:
            hists[sig][p].SetMarkerStyle(4)
            hists[sig][p].SetMarkerSize(0.5)
            hists[sig][p].SetMarkerColor(ROOT.kCyan+(3*(i%3)))
            hists[sig][p].SetLineColor(ROOT.kCyan+(3*(i%3)))
        sigHists.append(hists[sig][p])

    stacks['sig'][p] = getStackFromHists(sigHists)
    
    ret = {}

    canvs[p] = {}
    
    if fom:
        denoms = denoms if type(denoms)==type([]) else [denoms]
        if not denoms or len(denoms)==1:
            padRatios=[2,1]
        else:
            padRatios=[2]+[1]*(len(denoms))

        canvs[p] = makeCanvasMultiPads(c1Name = "canv_%s_%s"%(cut_name,p), c1ww = 800, c1wh = 800, joinPads = True, padRatios = padRatios, pads = [])
        cSave, cMain, cFom = 0, 1, 2 # index of the main canvas and the canvas to be saved
    else:
        canvs[p] = ROOT.TCanvas("canv_%s_%s"%(cut_name,p), "canv_%s_%s"%(cut_name, p), 800, 800), None, None
        cSave, cMain = 0, 0

    canvs[p][cMain].cd()

    ret.update({
            'canvs':canvs       ,
            'stacks':stacks     ,
            'hists':hists       ,
            'fomHists':{}       ,
            'sigBkgDataList': [sigList,bkgList,dataList],
            'legs':[]           ,
            'hist_info' : {}    ,
            'junk' : []    ,
            })
    
    dOpt = "hist"
    
    if normalize:
        #stacks['bkg'][p].SetFillStyle(3001)
        #stacks['bkg'][p].SetFillColorAlpha(kBlue, 0.35)
        dOpt+="nostack"
    
    if len(bkgList):
        bkgStack = stacks['bkg'][p]
        bkgStack.Draw(dOpt)

        errBarHist = bkgStack.GetStack().Last().Clone(p+"errBarHist")
        errBarHist.SetFillColor(ROOT.kBlue-5)
        errBarHist.SetFillStyle(3001)
        errBarHist.SetMarkerSize(0)
        errBarHist.Draw("E2 same")
        ret['junk'].append(errBarHist)
        
        refStack = bkgStack
        dOpt+=" same"
    
    if isDataPlot:
        dataHist = hists['Data'][p]
        #dataHist = hists[dataList[0]][p]
        dataHist.SetMarkerSize(0.9)
        dataHist.SetMarkerStyle(20)
        dataHist.Draw("E0P %s"%dOpt.replace("hist",""))
    
    if len(sigList):
        #stacks['sig'][p].Draw("E0P")
        stacks['sig'][p].Draw("E0P %s nostack"%dOpt.replace("hist",""))
        #refStack = stacks['sig'][p]
    
    if len(dataList):
        refStack = dataHist

    if plotsDict[p].has_key("decor"):
        if plotsDict[p]['decor'].has_key("y"): decorAxis(refStack, 'y', plotsDict[p]['decor']['y'], tOffset=1.2, tSize = 0.05)
        if plotsDict[p]['decor'].has_key("x"):
            if any(x in p.lower() for x in ['lep', 'mu', 'ele']): decorAxis(refStack, 'x', plotsDict[p]['decor']['x'].format(lepLatex = channel).replace('all','l'), tOffset=1.4, tSize = 0.04)
            else:          decorAxis(refStack, 'x', plotsDict[p]['decor']['x'], tOffset=1.4, tSize = 0.04)
        if plotsDict[p]['decor'].has_key("title"): refStack.SetTitle(plotsDict[p]['decor']['title'])
        if plotsDict[p]['decor'].has_key("log"):
            logx, logy, logz = plotsDict[p]['decor']['log']
            if logx: canvs[p][cMain].SetLogx(1)
            if logy: canvs[p][cMain].SetLogy(1)
    
    if plotMin: refStack.SetMinimum(plotMin)

    if plotLimits:
        refStack.SetMinimum(plotLimits[0])
    if logy:
        refStack.SetMaximum(25*refStack.GetMaximum())
    else:
        refStack.SetMaximum(1.2*refStack.GetMaximum())

    if leg:
        leg = ROOT.TLegend()

        if getData:
            leg.AddEntry("hist_Data_%s"%p, "Data", "P")
        for sig in sigList:
            leg.AddEntry("hist_%s_%s"%(sig,p), sig, "P")
        for samp in sampleList:
            leg.AddEntry("hist_%s_%s"%(samp,p), samp, "F")
        leg.SetBorderSize(0)
        leg.Draw()

        alignLegend(leg, x1 = 0.75, x2 = 0.9, y1 = 0.5, y2 = 0.8)
        ret['legs'].append(leg)

    if fom:
        if plotsDict[p]['decor'].has_key('fom_reverse'):
            fom_reverse = plotsDict[p]['decor']['fom_reverse']
        else: fom_reverse = True

        getFOMPlotFromStacks(ret, p, sampleList, fom=fom, fomIntegral=fomIntegral, fom_reverse=fom_reverse, normalize=normalize,
                                      denoms=denoms, noms=noms, ratioNorm=ratioNorm, fomLimits=fomLimits,
                                      leg=leg, unity=unity, verbose=verbose)
        
        if bkgList:
            canvs[p][cMain].cd()
            ret['hists']['bkg'][p].SetFillColor(1)
            ret['hists']['bkg'][p].SetFillStyle(3001)
            ret['hists']['bkg'][p].SetMarkerSize(0)
            ret['hists']['bkg'][p].Draw("E2same")
        for c in canvs[p]:
           if c: c.RedrawAxis()

    if not fom:
        canvs[p][cMain].SetRightMargin(10)
    else:
        canvs[p][cMain].SetRightMargin(0.03)
        canvs[p][cSave].SetRightMargin(0.03)
        canvs[p][cFom].SetRightMargin(0.03)

    for c in canvs[p]:
       if c: c.RedrawAxis()

    canvs[p][cMain].cd()
    canvs[p][cMain].RedrawAxis()
    canvs[p][cMain].Update()
    #canvs[p][cMain].SetLeftMargin(15) 

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    #latex.SetTextAlign(11)

    lumiTag = makeLumiTag(lumi_pb)
    print "Reweighting %s MC histograms to lumi %s"%(p, lumiTag)

    if isDataPlot:
        drawCMSHeader(lumi = lumi_fb)
    else:
        drawCMSHeader(lumi = lumi_fb, preliminary = "Simulation")

    ret['latex'] = latex
  
    canvs[p][cSave].Update()

    #Save
    if save: #web address: https://mzarucki.web.cern.ch/
        from StopsCompressed.samples.default_locations import default_locations
        samples_tag = default_locations.mc_2018_postProcessing_directory.split("/")[0]
        tag = "2022/StopsCompressed/" + samples_tag

        suffix = "_%s_%s_%s"%(cut_name, channel, fom)
        savedir = "/eos/user/m/mzarucki/www/%s/FOM/%s/%s/%s"%(tag, sensitivityStudyName, args.region, channel)
 
        if nMinus1:
            savedir += "/nMinus1"
            suffix += "_nMinus1"
        else:
            savedir += "/Not_nMinus1"
        
        if highWeightVeto:
            savedir += "/highWeightVeto"
            suffix += "_highWeightVeto"
        
        makeDir("%s/root"%(savedir))
        makeDir("%s/pdf"%(savedir))

        canvs[p][cSave].SaveAs("%s/%s%s.png"%(savedir, p, suffix))
        canvs[p][cSave].SaveAs("%s/root/%s%s.root"%(savedir, p, suffix))
        canvs[p][cSave].SaveAs("%s/pdf/%s%s.pdf"%(savedir, p, suffix))
