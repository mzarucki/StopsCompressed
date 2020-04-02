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
from Analysis.Tools.puProfileCache import *

#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           		action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--era',                		action='store',      default="2018",  	type=str )
argParser.add_argument('--eos',                		action='store_true', 			help='change sample directory to location eos directory' )
argParser.add_argument('--small',              		action='store_true', 			help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          		action='store',      default='v0p1')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-njet2p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-lpt0to50')
argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-mt170')
argParser.add_argument('--reweightPU',         		action='store',      default=None, 		  choices=['VDown', 'Down', 'Central', 'Up', 'VUp', 'VVUp'])
argParser.add_argument('--badMuonFilters',     		action='store',      default="Summer2016",  	  help="Which bad muon filters" )
argParser.add_argument('--noBadPFMuonFilter',           action='store_true', default=False)
argParser.add_argument('--noBadChargedCandidateFilter', action='store_true', default=False)

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.targetDir += "_small"
if args.reweightPU:                   args.targetDir += "_%s"%args.reweightPU

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
    samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, QCD_HT_17, VV_17, TTX_17]
    #from StopsCompressed.samples.nanoTuples_Run2017_14Dec2018_postProcessed import *
    from StopsCompressed.samples.nanoTuples_Run2017_nanoAODv6_postProcessed import *
    signals = []
elif "2018" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import *
    samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, VV_18, TTX_18]
    from StopsCompressed.samples.nanoTuples_Run2018_nanoAODv6_postProcessed import *
    signals = []
try:
    data_sample = eval(args.era)
except Exception as e:
    logger.error( "Didn't find %s", args.era )
    raise e


# Text on the plots
#
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextSize(0.04)
tex.SetTextAlign(11) # align right
#lumi_scale = 35.9

def drawObjects( plotData, dataMCScale):
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, ' L=%3.1f fb{}^{-1}(13 TeV) Scale %3.2f'% ( lumi_scale , dataMCScale) )
      #(0.15, 0.95, ' L=%3.1f fb{}^{-1}(13 TeV) Scale %3.2f Integral %3.2f'% ( lumi_scale , dataMCScale, mcIntegral) )
      #(0.15, 0.95, 'Scale %3.2f MCIntegral %3.2f DataIntegral %3.2f'% ( dataMCScale, mcIntegral, mcIntegral) )
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots,mode, dataMCScale):
  for log in [False, True]:
    
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots','leptonID', args.targetDir, args.era ,mode +("log" if log else ""), args.selection)
    for plot in plots:
      #if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      #for l in plot.histos:
	#if len(l)>1: print "yayy", [ l[x].GetName() for x in range(len(l))]
	#if len(l)>1: mc_integral=  sum([ l[x].Integral() for x in range(len(l))]) 
      _drawObjects = []
      plotting.draw(plot,
        plot_directory = plot_directory_,
        ratio = {'yRange':(0.1,1.9)},
        #ratio = None,
        logX = False, logY = log, sorting = False,
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        scaling = {},
        legend = ( (0.18,0.88-0.03*sum(map(len, plot.histos)),0.9,0.88), 2),
        drawObjects = drawObjects( True, dataMCScale) + _drawObjects,
        copyIndexPHP = True, extensions = ["png","pdf", "root"],
      )

# Read variables and sequences
read_variables = [
            "weight/F", "l1_pt/F", "l1_eta/F" , "l1_phi/F", "l1_pdgId/I", "l1_muIndex/I", "l1_eleIndex/I", "reweightHEM/F","l1_miniRelIso/F", "l1_relIso03/F", 
            "JetGood[pt/F, eta/F, phi/F, genPt/F]", 
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", 'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I","event/I","run/I"]
read_variables += [
            "nMuon/I",
            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O]",
	     "Electron[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,pdgId/I,tightCharge/I,lostHits/b,vidNestedWPBitmap/I, eInvMinusPInv/F, hoe/F, sieie/F ,deltaEtaSC/F]"
            ]
#for s in samples:
#    s.read_variables += ["genWeight/F",'reweightPU/F', 'Pileup_nTrueInt/F','reweightBTag_SF/F', 'GenMET_pt/F', 'GenMET_phi/F', 'Muon[genPartIdx/I,genPartFlav/b]']


sequence = []

#def make_weight (event, sample):
#	print event.weight, event.reweightL1Prefire, event.reweightHEM, event.reweightPU
#sequence.append (make_weight)

def lepton_ID (event, sample):
	event.l1_ip3d  		 = float('nan')  
        event.l1_nStations 	 = float('nan')  
        event.l1_segmentComp 	 = float('nan') 
        event.l1_highPtId 	 = float('nan')  
        event.l1_sip3d  	 = float('nan') 
        #event.l1_nTrackerLayers  = float('nan')  
        event.l1_sieie 		 = float('nan') 
        event.l1_lostHits	 = float('nan')  
        event.l1_hoe 		 = float('nan') 
        event.l1_eInvMinusPInv   = float('nan') 
        event.l1_deltaEtaSC  	 = float('nan') 
	if abs(event.l1_pdgId) == 13:
		event.l1_ip3d  	      = event.Muon_ip3d[event.l1_muIndex]
		event.l1_sip3d        = event.Muon_sip3d[event.l1_muIndex]
		event.l1_nStations    = event.Muon_nStations[event.l1_muIndex]
		event.l1_segmentComp  = event.Muon_segmentComp[event.l1_muIndex]
		event.l1_highPtId     = event.Muon_highPtId[event.l1_muIndex]
		#event.l1_nTrackLayers = event.nTrackLayers

	elif abs(event.l1_pdgId) == 11:
		event.l1_ip3d  	        = event.Electron_ip3d[event.l1_eleIndex]
		event.l1_sip3d          = event.Electron_sip3d[event.l1_eleIndex]
		event.l1_sieie          = event.Electron_sieie[event.l1_eleIndex]
		event.l1_hoe  	      	= event.Electron_hoe[event.l1_eleIndex]
		event.l1_eInvMinusPInv  = event.Electron_eInvMinusPInv[event.l1_eleIndex]
		#event.l1_deltaEtaSC     = event.Electron_deltaEtaSC[event.l1_eleIndex]
		
sequence.append(lepton_ID)

def getLeptonSelection( mode ):
	if   mode == 'mu': return "nGoodMuons>=1&&nGoodElectrons==0"
	elif mode == 'e' : return "nGoodMuons==0&&nGoodElectrons>=1"

yields   = {}
allPlots = {}
allModes = ['mu','e']
for index, mode in enumerate(allModes):
	yields[mode] = {}
	data_sample.setSelectionString([getFilterCut(isData=True, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter), getLeptonSelection(mode)])
	lumi_scale                 = data_sample.lumi/1000
	data_sample.scale          = 1.
	data_sample.style          = styles.errorStyle(ROOT.kBlack)
	data_sample.name 	   = "data"
	if signals:
	    T2tt_500_470.color = ROOT.kPink+6
	    T2tt_375_365.color = ROOT.kAzure+1
	    for s in signals: s.style = styles.errorStyle( color=s.color, markerSize = 0.6)
	
	weight_ = lambda event, sample: event.weight

	for sample in samples :
		sample.scale = lumi_scale
		sample.style = styles.fillStyle(sample.color)
		sample.read_variables  = ['reweightPU/F', 'Pileup_nTrueInt/F',]
		sample.read_variables += ['reweightPU%s/F'%args.reweightPU if args.reweightPU != "Central" else "reweightPU/F"]
		if args.reweightPU == 'Central':
			sample.weight         = lambda event, sample: event.reweightPU
		else:
			sample.weight         = lambda event, sample: getattr(event, "reweightPU"+args.reweightPU if args.reweightPU != "Central" else "reweightPU")
		sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter), getLeptonSelection(mode)])
	stack_ = Stack( samples, data_sample )
	#stack_ = Stack( samples, data_sample, T2tt_375_365, T2tt_500_470 )

	if args.small:
		for sample in samples + [data_sample]:
			sample.normalization = 1.
			sample.reduceFiles( factor = 40 )
			sample.scale /= sample.normalization

	# Use some defaults
	Plot.setDefaults(stack = stack_, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper', histo_class=ROOT.TH1D)
	plots = []

	plots.append(Plot(
	    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_pt/F" ),
	    binning=[40,0,200],
	  ))
	plots.append(Plot(
	    texX = '#eta (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_eta/F" ),
	    binning=[15,-3,3],
	  ))
	plots.append(Plot(
	    texX = '#phi (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_phi/F" ),
	    binning=[20,-pi,pi],
	  ))
	plots.append(Plot(
	    texX = 'dxy (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_dxy/F" ),
	    binning=[20,-.02,.02],
	  ))
	plots.append(Plot(
	    texX = 'dz (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_dz/F" ),
	    binning=[20,-.1,.1],
	  ))
	plots.append(Plot(
	    texX = 'relIso03_all(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_relIso03/F" ),
	    binning=[30,0,.5],
	  ))
	plots.append(Plot(
	    texX = 'miniRelIso_all(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_miniRelIso/F" ),
	    binning=[30,0,.5],
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
	    name = 'jet1_pt', attribute = lambda event, sample: event.JetGood_pt[0],
	    binning=[45,100,1000],
	  ))
	plots.append(Plot(
	    texX = '#eta(leading jet) (GeV)', texY = 'Number of Events',
	    name = 'jet1_eta', attribute = lambda event, sample: abs(event.JetGood_eta[0]),
	    binning=[10,0,3],
	  ))
	plots.append(Plot(
	    texX = '#phi(leading jet) (GeV)', texY = 'Number of Events',
	    name = 'jet1_phi', attribute = lambda event, sample: event.JetGood_phi[0],
	    binning=[10,-pi,pi],
	  ))
	if args.selection.count('njet2'):
		plots.append(Plot(
		    texX = 'p_{T}(sub-leading jet) (GeV)', texY = 'Number of Events ',
		    name = 'jet2_pt', attribute = lambda event, sample: event.JetGood_pt[1],
		    binning=[45,0,1000],
		  ))
		plots.append(Plot(
		    texX = '#eta(sub-leading jet) (GeV)', texY = 'Number of Events',
		    name = 'jet2_eta', attribute = lambda event, sample: abs(event.JetGood_eta[1]),
		    binning=[10,0,3],
		  ))
		plots.append(Plot(
		    texX = '#phi(sub-leading jet) (GeV)', texY = 'Number of Events',
		    name = 'jet2_phi', attribute = lambda event, sample: event.JetGood_phi[1],
		    binning=[10,-pi,pi],
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
	    texX = 'number of btagged jets', texY = 'Number of Events',
	    attribute = TreeVariable.fromString('nBTag/I'),
	    binning=[10,0,10],
	  ))
	plots.append(Plot(
	    texX = 'number of ISR jets', texY = 'Number of Events',
	    attribute = TreeVariable.fromString('nISRJets/I'),
	    binning=[3,0,3],
	  ))
	plots.append(Plot(
	   name = 'PV_npvsGood', texX = 'N_{PV} (good)', texY = 'Number of Events',
	   attribute = TreeVariable.fromString( "PV_npvsGood/I" ),
	   binning=[100,0,100],
	  ))
	plots.append(Plot(
	    name = 'yield', texX = 'yield', texY = 'Number of Events',
	    attribute = lambda event, sample: 0.5 + index ,
	    binning=[3, 0, 3],
	  ))
	plots.append(Plot(
		texX = 'ip3d(l_{1}) ', texY = 'Number of Events',
		name = 'l1_ip3d', attribute = lambda event, sample: event.l1_ip3d,
		binning=[50,0,.05], addOverFlowBin = 'both',
	  ))
	plots.append(Plot(
		texX = 'sip3d(l_{1}) ', texY = 'Number of Events',
		name = 'l1_sip3d', attribute = lambda event, sample: event.l1_sip3d,
		binning=[10,0,10],
	  ))
	plots.append(Plot(
		texX = '#sigma_{i#etai#eta}(l_{1})', texY = 'Number of Events',
		name = 'l1_sieie', attribute = lambda event, sample: event.l1_sieie,
		binning=[20,0,0.02],
	  ))
	plots.append(Plot(
		texX = 'nStations(l_{1}) ', texY = 'Number of Events',
		name = 'l1_nStations', attribute = lambda event, sample: event.l1_nStations,
		binning=[20,0,20], addOverFlowBin = 'both',
	  ))
	plots.append(Plot(
		texX = 'highPtId(l_{1}) (GeV)', texY = 'Number of Events',
		name = 'l1_highPtId', attribute = lambda event, sample: event.l1_highPtId,
		binning=[3,0,3],
	  ))
	plots.append(Plot(
		texX = 'segmentComp(l_{1}) (GeV)', texY = 'Number of Events',
		name = 'l1_segmentComp', attribute = lambda event, sample: event.l1_segmentComp,
		binning=[10,0,1],
	  ))
	plots.append(Plot(
		texX = 'H/E(l_{1})', texY = 'Number of Events',
		name = 'l1_hoe', attribute = lambda event, sample: event.l1_hoe,
		binning=[20,0,0.1],
	  ))
	plots.append(Plot(
		texX = '1/E - 1/p (l_{1})', texY = 'Number of Events',
		name = 'l1_eInvMinusPInv', attribute = lambda event, sample: event.l1_eInvMinusPInv,
		binning=[50,-0.05,0.05],
	  ))

	plotting.fill(plots, read_variables = read_variables, sequence = sequence)

	#Get normalization yields from yield histogram
	for plot in plots:
	    if plot.name == "yield":
	      for i, l in enumerate(plot.histos):
		for j, h in enumerate(l):
		  yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
		  h.GetXaxis().SetBinLabel(1, "#mu")
		  h.GetXaxis().SetBinLabel(2, "e")
	yields[mode]["MC"] = sum(yields[mode][s.name] for s in samples)
	dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

	drawPlots(plots, mode, dataMCScale)
	allPlots[mode] = plots

# Add the different channels into all	
yields['all'] = {}
for y in yields[allModes[0]]:
	try:	yields['all'][y] = sum(yields[c][y] for c in (['mu','e']))
	except: yields['all'][y] = 0
dataMCScale = yields['all']["data"]/yields['all']["MC"] if yields['all']["MC"] != 0 else float('nan')

for plot in allPlots['mu']:
	for plot2 in (p for p in allPlots['e'] if p.name == plot.name): 
		for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
			for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
				if i==k:
					j.Add(l)
drawPlots(allPlots['mu'], 'all', dataMCScale)
