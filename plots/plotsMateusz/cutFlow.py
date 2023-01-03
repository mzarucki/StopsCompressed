# Script for making cut-flow tables 

import ROOT
import os, sys
import argparse

from Workspace.HEPHYPythonTools.helpers import getChain, getPlotFromChain, getYieldFromChain
from Analysis.Tools.u_float import u_float

from array import array
from math import pi, sqrt #cos, sin, sinh, log

#Input options
parser = argparse.ArgumentParser(description = "Input options")
parser.add_argument("--channel",  dest = "channel", help = "Lepton channel", type = str, choices = ['all', 'mu', 'e'], default = "all")
parser.add_argument("--getData",  dest = "getData",  help = "Get data samples", type = int, default = 1)
parser.add_argument("--region",   dest = "region",  help = "Analysis region", type = str, default = "presel")
parser.add_argument("--year",     dest = "year",  help = "Year", type = str, default = "2018")
parser.add_argument("--doYields", dest = "doYields",  help = "Calulate yields", type = int, default = 0)
parser.add_argument("--highWeightVeto",  dest = "highWeightVeto",  help = "High weight event veto", action = "store_true")
#parser.add_argument("--skim", dest = "skim",  help = "Skim", type = str, default = "preIncLep")
parser.add_argument("--logy",     dest = "logy",  help = "Toggle logy", type = int, default = 1)
parser.add_argument("--save",     dest = "save",  help = "Toggle save", type = int, default = 1)
parser.add_argument("--verbose",  dest = "verbose",  help = "Verbosity switch", type = int, default = 0)
args = parser.parse_args()

#Arguments
channel = args.channel
getData = args.getData
year = args.year
doYields = args.doYields
highWeightVeto = args.highWeightVeto
#skim = args.skim
logy = args.logy
save = args.save
verbose = args.verbose

#Samples
if year == "2018":
    # MC
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import WJets_18, TTJets_18, ZInv_18, QCD_18, Others_18
    # Signals
    from StopsCompressed.samples.nanoTuples_Autumn18_signal_postProcessed import signals_T2tt, signals_T2bW, signals_TChiWZ
    signals      = signals_T2tt + signals_T2bW + signals_TChiWZ
    sigList = []#"T2tt_500_420", "T2tt_500_490"] # just choosing benchmark signals
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

for s in selSignals:
    samples[s.name] = s

#samples = [WJets, Top, ZInv, QCD, Others]

samplesList = sorted(samples.keys())
dataList = ['Data']

import StopsCompressed.Analysis.regions as regions # NOTE: 2016 analysis regions

from StopsCompressed.Analysis.Setup import Setup
setup = Setup(year=year)

lumi_pb = Data.lumi
lumi_fb = Data.lumi/1000.0

#weight_str = "weight * {lumi_weight}".format(lumi_weight = lumi_fb)

#weight_       = lambda event, sample: event.weight*event.reweightHEM
#sample.weight = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightwPt * event.reweightLeptonSF * genEff * lumi_year[event.year]/1000

if args.region != "presel":
    region = getattr(regions, args.region)

cut_name = args.region
presel = {}
weight_str = {}
cut_str = {'Data':{}, 'MC':{}}#, 'DataMC':{}}

parameters = {
    "MET"         : (200, -999),
    "HT"          : (300,-999),
    "nISRJet"     : (1,-999),
    "dphiJets"    : True,
    "hardJets"    : True,
    "tauVeto"     : True,
    "lepVeto"     : True,
    "jetVeto"     : True,
    "l1_prompt"   : False,
    "dphiMetJets" : False,
}

for dataMC in ["Data", "MC"]:#, "DataMC"]:
    presel[dataMC] = setup.selection(dataMC, channel = channel, isFastSim = False, **parameters)
    #presel[dataMC] = setup.preselection(dataMC, channel = channel)
    if args.region != "presel":
        cut_str[dataMC]['full'] = "&&".join([region.cutString(setup.sys['selectionModifier']), presel[dataMC]['cut']])
    else:    
        cut_str[dataMC]['full'] = presel[dataMC]['cut']
        
    cutList = [x for x in cut_str[dataMC]['full'].split('&&') if 'Flag' not in x] # NOTE: stripping filters

    for i in range(len(cutList)): # NOTE: stripping filters
        cut_str[dataMC]['nMinus%i'%i] = "&&".join(cutList[0:len(cutList)-i])

    if dataMC == "MC":
        weight_str[dataMC] = presel[dataMC]["weightStr"] + "* {lumi_weight}".format(lumi_weight = lumi_fb)
    else: # if data
        weight_str[dataMC] = "weight" # NOTE: hard-coded for data, which does not contain all branches
        #weight_str[dataMC] = presel[x]["weightStr"]

yields = {}
    
scaleYields = 0.6

for samp in samplesList:
    yields[samp] = {}
    for cut in cut_str['MC']:
        yields[samp][cut] = u_float(getYieldFromChain(samples[samp].chain, cutString = cut_str['MC'][cut], weight = weight_str['MC'], returnError = True)) * scaleYields
        print "Yield for sample %s in region %s for cut %s: %s"%(samp, args.region, cut, yields[samp][cut])
        
# Yields Table

makeYieldsTable = True
sensitivityStudyName = "baseline"

if makeYieldsTable:
    allResults = {}
    
    newRegionsOnly = False
    suffix = ""
    if newRegionsOnly: suffix += "_newRegionsOnly"
    
    if scaleYields != 1:
        suffix += "_scaled{}".format(scaleYields).replace(".","p")

    from StopsCompressed.Tools.user import plot_directory#, analysis_results

    texdir = os.path.join(plot_directory, 'yields', args.year, 'cutFlowTables', sensitivityStudyName)

    if not os.path.exists(texdir): os.makedirs(texdir)

    ofile = "cutFlowTable_%s_%s_%s%s.tex"%(sensitivityStudyName, args.region, channel, suffix)
    ofilename = "%s/%s"%(texdir,ofile)
    print "Writing to ", ofilename
    with open(ofilename, "w") as f:
        f.write("\\documentclass[a4paper,10pt,oneside]{article} \n \\usepackage{caption} \n \\usepackage{rotating} \n")
        f.write("\\usepackage[a4paper,bindingoffset=0.2in,left=1cm,right=1cm,top=1cm,bottom=1cm,footskip=.25in]{geometry} \n")
        f.write("\\begin{document}\n")
        f.write("\\begin{table}\n")
        f.write("\\centering\n")
        f.write("\\begin{tabular}{|c" + "|c"*len(yields) + "|} \n")
        f.write("\\hline Cut & " + " & ".join(s for s in yields).replace("_", "\_") + "\\\\ \\hline \\hline \n")
        for cut in sorted(cut_str['MC']):
            f.write("%s &"%cut + " & ".join("${:0.1f} \pm {:1.1f}$".format(yields[s][cut].val, yields[s][cut].sigma) for s in yields) + "\\\\ \\hline \n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
        f.write("\\end{document}")
    os.system("cd "+texdir+";pdflatex "+ofile)
    
