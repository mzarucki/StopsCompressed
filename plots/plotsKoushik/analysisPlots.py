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
argParser.add_argument('--targetDir',          action='store',      default='v01')
argParser.add_argument('--selection',          action='store',      default='nISRJets1-ntau0-deltaPhiJets-jet3Veto-lepSel-met200-ht300')
#argParser.add_argument('--selection',          action='store',      default='nISRJets1-ntau0-deltaPhiJets-nHardJetsTo2-lepSel-met200-ht300')
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
    postProcessing_directory = "StopsCompressed/nanoTuples/"
    from StopsCompressed.samples.nanoTuples_Summer16_postProcessed import *
    samples = [TTLep_pow_16 , TTSingleLep_pow_16]

if args.small:
    for sample in samples:
        #sample.reduceFiles( factor=40 )
        sample.reduceFiles( to=1 ) 
# Text on the plots
#
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextSize(0.04)
tex.SetTextAlign(11) # align right
lumi_scale = 35.9

def drawObjects( plotData ):
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.55, 0.95, ' L=%3.1f fb{}^{-1} (13 TeV) '% ( lumi_scale ) )
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.targetDir, args.era , args.selection, ("log" if log else ""))
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot

      _drawObjects = []

      plotting.draw(plot,
        plot_directory = plot_directory_,
        ratio = None,
        logX = False, logY = log, sorting = False,
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        scaling = {},
        legend = ( (0.18,0.88-0.03*sum(map(len, plot.histos)),0.9,0.88), 2),
        drawObjects = drawObjects( True ) + _drawObjects,
        copyIndexPHP = True, extensions = ["png"],
      )

# Read variables and sequences
read_variables = [
            "weight/F", "l1_pt/F", "l1_eta/F" , "l1_phi/F", "l1_muIndex/I", 
            "JetGood[pt/F,eta/F,phi/F,genPt/F]", 
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", "genWeight/F",'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I"]
read_variables += [
            "nMuon/I",
            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O,genPartIdx/I,genPartFlav/b]"
            ]
read_variables += ['reweightPU/F', 'Pileup_nTrueInt/F','reweightBTag_SF/F', 'GenMET_pt/F', 'GenMET_phi/F']


sequence = []

weight_ = lambda event, sample: event.weight

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
for sample in samples: sample.scale = lumi_scale

stack = Stack( TTSingleLep_pow_16, TTLep_pow_16)
# Use some defaults
Plot.setDefaults(stack = stack, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper', histo_class=ROOT.TH1D)
plots = []

plots.append(Plot(
    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "l1_pt/F" ),
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
    binning=[40,200,1000],
  ))
plots.append(Plot(
    texX = 'H_{T} (GeV)', texY = 'Number of Events ',
    attribute = TreeVariable.fromString( "HT/F" ),
    binning=[40,200,1000],
  ))
plots.append(Plot(
    texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
    name = 'jet1_pt', attribute = lambda event, sample: event.JetGood_pt[0],
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
    binning=[14,0,14],
  ))
plots.append(Plot(
    texX = 'number of ISR jets', texY = 'Number of Events',
    attribute = TreeVariable.fromString('nISRJets/I'),
    binning=[14,0,14],
  ))
plotting.fill(plots, read_variables = read_variables, sequence = sequence)
drawPlots(plots)
logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )
