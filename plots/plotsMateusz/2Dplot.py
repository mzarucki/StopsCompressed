# Script for making 2D plots 

import ROOT
import os, sys
import argparse
#import Workspace.DegenerateStopAnalysis.toolsMateusz.ROOToptions
from Workspace.DegenerateStopAnalysis.toolsMateusz.drawFunctions import *
from Workspace.DegenerateStopAnalysis.toolsMateusz.pythonFunctions import *
from Workspace.DegenerateStopAnalysis.tools.degTools import getStackFromHists, setEventListToChains, setup_style, makeDir, anyIn, makeLegend, getFOMPlotFromStacks, makeLumiTag, drawCMSHeader
from Workspace.HEPHYPythonTools.helpers import getChain, getPlotFromChain, getYieldFromChain

from StopsCompressed.Tools.genFilter import genFilter

#Sets TDR style
#setup_style()

ROOT.gStyle.SetOptStat(0)

#Input options
parser = argparse.ArgumentParser(description="Input options")
parser.add_argument("--sensitivityStudyName", default = "baseline",  type=str,    action="store",      help="Name of sensitivity study")
parser.add_argument("--var1", dest="var1",  help="Variable 1", type=str, default="leadJetPt") #"muPt"
parser.add_argument("--var2", dest="var2",  help="Variable 2", type=str, default="MET")
parser.add_argument("--region",   dest = "region",  help = "Analysis region", type = str, default = None)
#parser.add_argument("--slice", dest="slice",  help="Pt Slice Bounds (low,up)", type=int, nargs=2, metavar = ('slice_low', 'slice_up'))
parser.add_argument("--year",     dest = "year",    help = "Year", type = str, default = "2018")
parser.add_argument("--channel",  dest = "channel", help = "Lepton channel", type = str, choices = ['all', 'mu', 'e'], default = "all")
parser.add_argument("--samples", dest="samples",  help="Samples", type=str, default=["T2tt_550_510"], nargs = "+")
parser.add_argument("--maxZ", dest="maxZ",  help="Z-axis maximum", type=int, default=None)
parser.add_argument("--log", dest="logy",  help="Log scale", type=int, default=1)
parser.add_argument("--drawLegend", dest="drawLegend",  help="Draw legend", type=int, default=1)
parser.add_argument("--save", dest="save",  help="Toggle Save", type=int, default=1)
parser.add_argument("--verbose", dest = "verbose",  help = "Verbosity switch", type = int, default = 0)
args = parser.parse_args()
if not len(sys.argv) > 1:
   print makeLine()
   print "No arguments given. Using default settings."
   print makeLine()
   #exit()

#Arguments
sensitivityStudyName = args.sensitivityStudyName
year = args.year
channel = args.channel
var1 = args.var1
var2 = args.var2
#slice = args.slice
samples = args.samples 
maxZ = args.maxZ
log = args.logy
drawLegend = args.drawLegend
save = args.save
verbose = args.verbose

print "Plotting 2D distribution of %s vs. %s in samples: %s"%(var1, var2, samples)

#Samples
if year == "2018":
    # MC
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import WJets_18, TTJets_18, ZInv_18, QCD_18, Others_18
    # Signals
    from StopsCompressed.samples.nanoTuples_Autumn18_signal_postProcessed import signals_T2tt, signals_T2bW, signals_TChiWZ, signals_MSSM
    signals      = signals_T2tt + signals_T2bW + signals_TChiWZ + signals_MSSM
    #sigList = ["T2tt_500_420", "T2tt_500_460", "T2tt_500_490", "TChiWZ_200_150", "TChiWZ_200_170", "TChiWZ_200_190"] # just choosing benchmark signals
    selSignals = [s for s in signals if s.name in samples]
    assert len(selSignals) <= 1 # one signal at a time
    #assert len(sigList) == len(selSignals)

    ## Data
    #if getData:
    #    from StopsCompressed.samples.nanoTuples_Run2018_postProcessed import Run2018
    #    Data = Run2018

    WJets        = WJets_18
    Top          = TTJets_18
    ZInv         = ZInv_18
    QCD          = QCD_18
    Others       = Others_18
else:
    print "Year %s not in choices. Exiting."%year
    sys.exit(0)

samplesDict = {
         'WJets'     : WJets,
         'Top'       : Top,
         'ZInv'      : ZInv,
         'QCD'       : QCD,
         'Others'    : Others
     }
         
if selSignals:
    samplesDict[selSignals[0].name] = selSignals[0]

plotsDict = {
   "lep_mt"    :{'var':"mt",                 "bins":[40,0,200],      "decor":{"title":"lepMt",                         "x":"m_{{T}}({lepLatex})",                 "y":"Events", 'log':[0,log,0]}},
   "lep_pt"    :{'var':"l1_pt",              "bins":[50,0,100],      "decor":{"title":"lepPt",                         "x":"p_{{T}}({lepLatex})",                 "y":"Events", 'log':[0,log,0]}},
   "lep_eta"   :{'var':"l1_eta",             "bins":[20,-3,3],       "decor":{"title":"lepEta",                        "x":"#eta({lepLatex})",                    "y":"Events", 'log':[0,log,0]}},
   "lep_phi"   :{'var':"l1_phi",             "bins":[60,-3.15,3.15], "decor":{"title":"lepPhi",                        "x":"#phi({lepLatex})",                    "y":"Events", 'log':[0,log,0]}},
   "lep_dxy"   :{'var':"l1_dxy",             "bins":[40,-0.02,0.02], "decor":{"title":"lepDxy",                        "x":"d_{{xy}}({lepLatex})",                "y":"Events", 'log':[0,log,0]}},
   "lep_dxyErr":{'var':"l1_dxyErr",          "bins":[40,0,0.02],     "decor":{"title":"lepDxyErr",                     "x":"#sigma_{{dxy}}({lepLatex})",          "y":"Events", 'log':[0,log,0]}},
   "lep_dxySig":{'var':"(l1_dxy/l1_dxyErr)", "bins":[40,-10,10],     "decor":{"title":"lepDxySig",                     "x":"d_{{xy}}/#sigma_{{dxy}}({lepLatex})", "y":"Events", 'log':[0,log,0]}},
   "lep_dz"    :{'var':"l1_dz",              "bins":[40,-0.1,0.1],   "decor":{"title":"lepDz",                         "x":"d_{{z}}({lepLatex})",                 "y":"Events", 'log':[0,log,0]}},
   "lep_dzErr" :{'var':"l1_dzErr",           "bins":[40,0,0.1],      "decor":{"title":"lepDzErr",                      "x":"#sigma_{{dz}}({lepLatex})",           "y":"Events", 'log':[0,log,0]}},
   "lep_dzSig" :{'var':"(l1_dz/l1_dzErr)",   "bins":[40,-10,10],     "decor":{"title":"lepDzSig",                      "x":"d_{{z}}/#sigma_{{dz}}({lepLatex})",   "y":"Events", 'log':[0,log,0]}},
   "MET"       :{'var':"MET_pt",             "bins":[40,200,1000],   "decor":{"title":"MET",                           "x":"p^{miss}_{T}",                        "y":"Events", 'log':[0,log,0]}},
   "MET_phi"   :{'var':"MET_phi",            "bins":[60,-3.15,3.15], "decor":{"title":"METPhi",                        "x":"#phi(p^{miss}_{T})",                  "y":"Events", 'log':[0,log,0]}},
   "genMET"    :{'var':"GenMET_pt",          "bins":[40,200,1000],   "decor":{"title":"Generated MET",                 "x":"Gen. p^{miss}_{T}",                   "y":"Events", 'log':[0,log,0]}},
   "HT"        :{'var':"HT",                 "bins":[40,200,1000],   "decor":{"title":"HT",                            "x":"H_{T}",                               "y":"Events", 'log':[0,log,0]}},
   "CT1"       :{'var':"CT1",                "bins":[40,100,1000],   "decor":{"title":"CT1",                           "x":"C_{T1}",                              "y":"Events", 'log':[0,log,0]}},
   "CT2"       :{'var':"CT2",                "bins":[40,100,1000],   "decor":{"title":"CT2",                           "x":"C_{T2}",                              "y":"Events", 'log':[0,log,0]}},
   "ISR_pt"    :{'var':"ISRJets_pt",         "bins":[45,100,1000],   "decor":{"title":"ISR Jet p_{T}",                 "x":"ISR Jet p_{T}",                       "y":"Events", 'log':[0,log,0]}},
   "ISR_phi"   :{'var':"JetGood_phi[0]",     "bins":[60,-3.15,3.15], "decor":{"title":"ISRPhi",                        "x":"#phi(ISR Jet)",                       "y":"Events", 'log':[0,log,0]}},
   "nJets"     :{'var':"nJetGood",           "bins":[10,0,10],       "decor":{"title":"# of Jets with p_{T} > 30 GeV", "x":"N(Jets p_{T} > 30 GeV)",              "y":"Events", 'log':[0,log,0]}},
   }

for p in plotsDict:
    if plotsDict[p]['decor'].has_key("x") and any(x in p.lower() for x in ['lep', 'mu', 'ele']): 
        plotsDict[p]['decor']['x'] = plotsDict[p]['decor']['x'].format(lepLatex = channel).replace('all','l')

from StopsCompressed.Analysis.Setup import Setup
setup = Setup(year = year)

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
elif sensitivityStudyName in ["baselinePlusLowMET_4mTregions_ratioCTZ", "baselinePlusLowMET3_redSys_4mTregions_ratioCTZ"]:
    fullSensitivityStudyName = sensitivityStudyName + "_nbins328_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
    import StopsCompressed.Analysis.regions_lowMET_4mTregions_ratioCTZ as regions
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
if args.region not in [None, "presel"]:
    region = getattr(regions, args.region)

c1 = ROOT.TCanvas("c1", "Canvas 1", 1800, 1500)
if len(samples) > 1: # simultaneous
    c1.SetRightMargin(0.1)
else:
    c1.SetRightMargin(0.18)

presel = setup.preselection("MC", channel = channel)
    
if args.region == "presel":
    cut_str = presel['cut']
elif args.region:
    cut_str = "&&".join([region.cutString(setup.sys['selectionModifier']), presel['cut']])
else:
    cut_str = "1"

weight_str = presel["weightStr"] + "* {lumi_weight}".format(lumi_weight = lumi_fb)

#print "Using cut string: ", cut_str
#print "Using weight string: ", weight_str

hists = {}
    
if drawLegend:
    leg = ROOT.TLegend(0.55, 0.2, 0.85, 0.4)

for i, samp in enumerate(samples):
    if "T2tt" in samp:
        mStop = int(samp.split('_')[1])
        mNeu  = int(samp.split('_')[2])

        gFilter = genFilter(year = args.year, signal = "T2tt")
        #genEff  = gFilter.getEff(mStop,mNeu) # NOTE: uses ROOT file insead # FIXME: for some reason messes up plotting
        genEff  = gFilter.getEffFromPkl(mStop,mNeu)
    elif "T2bW" in samp:
        mStop = int(samp.split('_')[1])
        mNeu  = int(samp.split('_')[2])

        gFilter = genFilter(year = args.year, signal = "T2bW")
        genEff  = gFilter.getEffFromPkl(mStop,mNeu)
    elif "TChiWZ" in samp:
        mCha  = int(samp.split('_')[1])
        mNeu  = int(samp.split('_')[2])

        gFilter = genFilter(year = args.year, signal = "TChiWZ")
        genEff  = gFilter.getEffFromPkl(mCha,mNeu)
    elif "MSSM" in samp:
        mu = int(samp.split('_')[1])
        M1 = int(samp.split('_')[2])

        gFilter = genFilter(year = args.year, signal = "MSSM")
        genEff  = gFilter.getEffFromPkl(mu,M1)
    else:
        genEff = 1
   
    hists[samp] = make2DHist(samplesDict[samp].chain, plotsDict[var1]['var'], plotsDict[var2]['var'], "(%s)*(%s)"%(cut_str,weight_str), plotsDict[var1]['bins'][0], plotsDict[var1]['bins'][1], plotsDict[var1]['bins'][2], plotsDict[var2]['bins'][0], plotsDict[var2]['bins'][1], plotsDict[var2]['bins'][2])
    if genEff != 1: hists[samp].Scale(genEff)
    hists[samp].SetName("2D_" + var1 + "_" + var2)
    hists[samp].SetTitle(plotsDict[var1]['decor']['title'] + " vs " + plotsDict[var2]['decor']['title'] + " Distribution (%s)"%args.region)
    hists[samp].GetXaxis().SetTitle("%s / GeV"%plotsDict[var1]['decor']['x'])
    hists[samp].GetYaxis().SetTitle("%s / GeV"%plotsDict[var2]['decor']['x'])
    hists[samp].GetXaxis().SetTitleOffset(0.9) 
    hists[samp].GetYaxis().SetTitleOffset(1.2) 
    hists[samp].GetZaxis().SetTitleOffset(0.9)
    hists[samp].SetName("hist_%s"%samp)

    if len(samples) > 1: # more than one sample
        dOpt = "scat" #"box"
        dOpt += " same"
        #if i > 1: dOpt += " same"
        if 'T2' in samp or 'TChi' in samp or 'MSSM' in samp:
            hists[samp].SetMarkerStyle(3)
            hists[samp].SetMarkerSize(2)
        else:
            hists[samp].SetMarkerSize(1.5)
        hists[samp].SetMarkerColor(samplesDict[samp].color)
        hists[samp].Draw(dOpt)
    else:
        hists[samp].Draw("COLZ") #CONT1-5 #plots the graph with axes and points

    if maxZ:
        hists[samp].GetZaxis().SetRangeUser(0, maxZ)
    else:
        hists[samp].GetZaxis().SetRangeUser(0, hists[samp].GetMaximum()*1.5)

    if log: ROOT.gPad.SetLogz() 
    #alignStats(hist)

    if drawLegend:
        leg.AddEntry("hist_%s"%samp, samplesDict[samp].texName, "P")

if drawLegend:
    leg.SetBorderSize(0)
    leg.Draw()
   
c1.Modified()
c1.Update()

#Save
if save: #web address: https://mzarucki.web.cern.ch/
    from StopsCompressed.samples.default_locations import default_locations
    samples_tag = default_locations.mc_2018_postProcessing_directory.split("/")[0]
    tag = "2022/StopsCompressed/" + samples_tag

    suffix = "_%s_%s"%(cut_name, channel)
    if maxZ: suffix += "_maxZ%i"%maxZ

    savedir = "/eos/user/m/mzarucki/www/%s/2Dplots/%s/%s/%s/%svs%s"%(tag, sensitivityStudyName, args.region, channel, var1, var2)

    if len(samples) > 1:
        savedir += "/simultaneous"

    makeDir("%s/root"%(savedir))
    makeDir("%s/pdf"%(savedir))

    c1.SaveAs("%s/2D_%svs%s_%s%s.png"%(savedir, var1, var2, "-".join(samples), suffix))
    c1.SaveAs("%s/root/2D_%svs%s_%s%s.root"%(savedir, var1, var2, "-".join(samples), suffix))
    c1.SaveAs("%s/pdf/2D_%svs%s_%s%s.pdf"%(savedir, var1, var2, "-".join(samples), suffix))
