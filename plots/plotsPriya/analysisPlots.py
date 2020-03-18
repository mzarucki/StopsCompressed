#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode

import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools
import copy
import array
import operator

from math   import pi, sqrt, sin, cos, atan2
from RootTools.core.standard import *
from StopsCompressed.Tools.user             import plot_directory
from Analysis.Tools.metFilters              import getFilterCut
from Analysis.Tools.metFilters              import getFilterCut
from StopsCompressed.Tools.cutInterpreter   import cutInterpreter

#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--era',                action='store',      type=str,      default="2018")
argParser.add_argument('--eos',                action='store_true', help='change sample directory to location eos directory' )
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v19')
argParser.add_argument('--selection',          action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
#argParser.add_argument('--selection',          action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
argParser.add_argument('--badMuonFilters',     action='store',      default="Summer2016",  help="Which bad muon filters" )
argParser.add_argument('--noBadPFMuonFilter',           action='store_true', default=False)
argParser.add_argument('--noBadChargedCandidateFilter', action='store_true', default=False)
args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.targetDir += "_small"

#
# Make samples, will be searched for in the postProcessing directory
#
from Analysis.Tools.puReweighting import getReweightingFunction

if "2016" in args.era:
    year = 2016
elif "2017" in args.era:
    year = 2017
elif "2018" in args.era:
    year = 2018
logger.info( "Working in year %i", year )
if args.eos and "2016" in args.era:
    data_directory = "/eos/cms/store/group/phys_susy/hephy/"
    postProcessing_directory = "stopsCompressed/nanoTuples/"
    from StopsCompressed.samples.nanoTuples_Summer16_postProcessed import *
    samples = [TTLep_pow_16 , TTSingleLep_pow_16]
    
    
elif "2016" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Summer16_postProcessed import *
    samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16, QCD_HT_16, VV_16, TTX_16]
    from StopsCompressed.samples.nanoTuples_Run2016_17July2018_postProcessed import *
    #from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import *
    #signals = [T2tt_375_365,T2tt_500_470 ]
    signals = []
elif "2017" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Fall17_postProcessed import *
    samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16, QCD_HT_16, VV_16, TTX_16]
    from StopsCompressed.samples.nanoTuples_Run2017_nanoAODv6_postProcessed import *
    signals = []
elif "2018" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import *
    samples =[Top_pow_1l_18, WJets_18, Top_pow_18]

try:
    data_sample = eval(args.era)
except Exception as e:
    logger.error( "Didn't find %s", args.era )
    raise e
lumi_scale                 = data_sample.lumi/1000
data_sample.scale          = 1.
for sample in samples : 
    sample.scale = lumi_scale
    sample.setSelectionString(getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter))
#for sample in samples + signals : sample.scale = lumi_scale

if args.small:
    for sample in samples + [data_sample]:
	sample.normalization = 1.
        sample.reduceFiles( factor=40 )
	sample.scale /= sample.normalization
        #sample.reduceFiles( to=1 ) 
# Text on the plots
#
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextSize(0.04)
tex.SetTextAlign(11) # align right
#lumi_scale = 35.9

def drawObjects( plotData, dataMCScale, mcIntegral ):
    lines = [
      #(0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.15, 0.95, ' L=%3.1f fb{}^{-1}(13 TeV) Scale %3.2f Integral %3.2f'% ( lumi_scale , dataMCScale, mcIntegral) )
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots,dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.targetDir, args.era , args.selection, ("log" if log else ""))
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      for l in plot.histos: mc_integral=  sum([ l[x].Integral() for x in range(len(l))]) #mc_integral= l[0].Integral() 
      #for l in plot.histos: print [ l[x].GetName() for x in range(len(l))] #mc_integral= l[0].Integral() 
      #for l in plot.histos: mc_integral= l[0].Integral() 

      _drawObjects = []
      plotting.draw(plot,
        plot_directory = plot_directory_,
        ratio = {'yRange':(0.1,1.9)},
        #ratio = None,
        logX = False, logY = log, sorting = False,
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        scaling = {},
        legend = ( (0.18,0.88-0.03*sum(map(len, plot.histos)),0.9,0.88), 2),
        drawObjects = drawObjects( True, dataMCScale, mc_integral ) + _drawObjects,
        copyIndexPHP = True, extensions = ["png","pdf", "root"],
      )

# Read variables and sequences
read_variables = [
            "weight/F", "l1_pt/F", "l1_eta/F" , "l1_phi/F", "l1_pdgId/I", "l1_muIndex/I", 
            "JetGood[pt/F,eta/F,phi/F,genPt/F]", 
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", 'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I","event/I","run/I"]
#read_variables += [
#            "nMuon/I",
#            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O]"
#            ]
#for s in samples:
#    s.read_variables += ["genWeight/F",'reweightPU/F', 'Pileup_nTrueInt/F','reweightBTag_SF/F', 'GenMET_pt/F', 'GenMET_phi/F', 'Muon[genPartIdx/I,genPartFlav/b]']


sequence = []
def lepton_flavour (event, sample):
	event.mu_pt = -999
	event.el_pt = -999
	if abs(event.l1_pdgId) == 13:
		event.mu_pt = event.l1_pt
	elif abs(event.l1_pdgId) == 11:
		event.el_pt = event.l1_pt
sequence.append(lepton_flavour)

weight_ = lambda event, sample: event.weight
data_sample.setSelectionString(getFilterCut(isData=True, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter))
#for sample in samples:
#    if args.reweightPU and args.reweightPU not in ["noPUReweighting", "nvtx"]:
#        sample.read_variables.append('reweightPU/F' if args.reweightPU=='Central' else 'reweightPU%s/F'%args.reweightPU )
#    if args.reweightPU == "noPUReweighting":
#        sample.weight         = lambda event, sample: event.reweightDilepTrigger*event.reweightLeptonSF*event.reweightBTag_SF*event.reweightLeptonTrackingSF*event.reweightL1Prefire
#    elif args.reweightPU == "nvtx":
#        sample.weight         = lambda event, sample: nvtx_puRW(event.PV_npvsGood) * event.reweightDilepTrigger*event.reweightLeptonSF*event.reweightBTag_SF*event.reweightLeptonTrackingSF*event.reweightL1Prefire
#    elif args.reweightPU:
#        pu_getter = operator.attrgetter('reweightPU' if args.reweightPU=='Central' else "reweightPU%s"%args.reweightPU)
#        sample.weight         = lambda event, sample: pu_getter(event) * event.reweightDilepTrigger*event.reweightLeptonSF*event.reweightBTag_SF*event.reweightLeptonTrackingSF*event.reweightL1Prefire
#    else: #default
#
#        sample.weight         = lambda event, sample: event.reweightPU*event.reweightBTag_SF
#    sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter)])

for sample in samples: sample.style = styles.fillStyle(sample.color)
data_sample.style          	    = styles.errorStyle(ROOT.kBlack)
data_sample.name = "data"
if signals:
    T2tt_500_470.color = ROOT.kPink+6
    T2tt_375_365.color = ROOT.kAzure+1
    for s in signals: s.style = styles.errorStyle( color=s.color, markerSize = 0.6)

stack_ = Stack( samples, data_sample )
#stack_ = Stack( samples, data_sample, T2tt_375_365, T2tt_500_470 )

for sample in samples: print sample.scale 

# Use some defaults
Plot.setDefaults(stack = stack_, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper', histo_class=ROOT.TH1D)
#Plot2D.setDefaults(stack = stack_, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection))
plots = []
#plots2D = []
yields = {}

plots.append(Plot(
    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "l1_pt/F" ),
    binning=[40,0,200],
  ))

plots.append(Plot(name= "mu_pt_distribution ",
    texX = 'p_{T}(mu) (GeV)', texY = 'Number of Events ',
    attribute = lambda event, sample: event.mu_pt,
    binning=[40,0,200],
  ))

plots.append(Plot(name = "electron_pt_distribution",
    texX = 'p_{T}(el) (GeV)', texY = 'Number of Events ',
    attribute = lambda event, sample: event.el_pt,
    binning=[40,0,200],
  ))
plots.append(Plot(
    texX = 'ISR Jet p_{T} (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "ISRJets_pt/F" ),
    binning=[45,100,1000],
  ))
plots.append(Plot(
    texX = 'MET (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "met_pt/F" ),
    binning=[50,0,1000],
  ))
plots.append(Plot(
    texX = 'H_{T} (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "HT/F" ),
    binning=[40,200,1000],
  ))
plots.append(Plot(
    texX = 'M_{T} (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "mt/F" ),
    binning=[40,0,200],
  ))

plots.append(Plot(
    texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
    attribute = TreeVariable.fromString( "JetGood_pt/F"),
    binning=[45,100,1000],
  ))
plots.append(Plot(
    texX = 'C_{T1} (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "CT1/F" ),
    binning=[45,100,1000],
  ))
plots.append(Plot(
    texX = 'number of jets', texY = 'Number of Events',
    attribute = TreeVariable.fromString('nJetGood/I'),
    binning=[10,0,10],
  ))
plots.append(Plot(
    texX = 'number of ISR jets', texY = 'Number of Events',
    attribute = TreeVariable.fromString('nISRJets/I'),
    binning=[3,0,3],
  ))
plots.append(Plot(
    name = 'yield', texX = 'yield', texY = 'Number of Events',
    attribute = lambda event, sample: 0.5 ,
    binning=[3, 0, 3],
  ))

plotting.fill(plots, read_variables = read_variables, sequence = sequence)

#Get normalization yields from yield histogram
for plot in plots:
    if plot.name == "yield":
      for i, l in enumerate(plot.histos):
        for j, h in enumerate(l):
          yields[plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5))
yields["MC"] = sum(yields[s.name] for s in samples)
dataMCScale        = yields["data"]/yields["MC"] if yields["MC"] != 0 else float('nan')

drawPlots(plots,dataMCScale)


