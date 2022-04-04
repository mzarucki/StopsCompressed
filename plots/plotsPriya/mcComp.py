'''
Analysis script for standard plots
'''
#
# Standard imports and batch mode

import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools
import copy
import array
import operator

from math   import pi, sqrt, sin, cos, atan2, log
from RootTools.core.standard import *
from StopsCompressed.Tools.user             import plot_directory
from Analysis.Tools.metFilters              import getFilterCut
from StopsCompressed.Tools.cutInterpreter   import cutInterpreter
#from Analysis.Tools.puProfileCache import *
from StopsCompressed.Tools.helpers           import deltaR, deltaPhi,ptRatio
from StopsCompressed.Tools.objectSelection   import muonSelector, eleSelector,  getGoodMuons, getGoodElectrons, getGoodTaus, getAllJets
#read gen filter efficicency
from StopsCompressed.Tools.genFilter import genFilter
#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           		action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--era',                		action='store',      default="Run2018",  	type=str )
argParser.add_argument('--eos',                		action='store_true', 			help='change sample directory to location eos directory' )
argParser.add_argument('--small',              		action='store_true', 			help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          		action='store',      default='v_UL01')
argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-lpt0to50-mt100')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-njet1-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-lpt0to50-mt100')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-lpt0to50')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-HEMElVetoWidePt')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-mt170')
argParser.add_argument('--reweightPU',         		action='store',      default=None, 		  choices=['VDown', 'Down', 'Central', 'Up', 'VUp', 'VVUp'])
argParser.add_argument('--badMuonFilters',     		action='store',      default="Summer2016",  	  help="Which bad muon filters" )
argParser.add_argument('--noBadPFMuonFilter',           action='store_true', default=False)
argParser.add_argument('--noBadChargedCandidateFilter', action='store_true', default=False)
argParser.add_argument('--preHEM',             action='store_true', default=False)
argParser.add_argument('--postHEM',            action='store_true', default=False)

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.targetDir += "_small"
if args.reweightPU:                   args.targetDir += "_%s"%args.reweightPU
if args.preHEM:                       args.targetDir += "_preHEM"
if args.postHEM:                       args.targetDir += "_postHEM"

#
# Make samples, will be searched for in the postProcessing directory
#
from Analysis.Tools.puReweighting import getReweightingFunction

from StopsCompressed.samples.nanoTuples_UL16APV_postProcessed import *
from StopsCompressed.samples.nanoTuples_UL16_postProcessed import *
samples = [WJetsToLNu_HT_16APV, WJetsToLNu_HT_16]
samples = [ WJetsToLNu_HT_16, WJetsToLNu_HT_16APV]


if args.small:
	for sample in samples:
		sample.normalization = 1.
		sample.reduceFiles( factor = 60 )
		#sample.scale /= sample.normalization

# Text on the plots
#
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextSize(0.04)
tex.SetTextAlign(11) # align right
#lumi_scale = 35.9

def drawObjects( plotData, dataMCScale):
    lines = [
      (0.15, 0.95, 'CMS Simulation'), 
      (0.45, 0.95, ' L= 1 fb{}^{-1}(13 TeV)' )
      #(0.45, 0.95, ' L= 19.5,16.5 fb{}^{-1}(13 TeV)' )
      #(0.45, 0.95, ' L= 19.5,16.5 fb{}^{-1} (13 TeV) Scale %3.2f'% ( dataMCScale) )
      #(0.15, 0.95, ' L=%3.1f fb{}^{-1}(13 TeV) Scale %3.2f Integral %3.2f'% ( lumi_scale , dataMCScale, mcIntegral) )
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots,mode, dataMCScale):
  for log in [False, True]:
    
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.targetDir, args.era ,mode +("log" if log else ""), args.selection)
    for plot in plots:
      
      _drawObjects = []
      plotting.draw(plot,
        plot_directory = plot_directory_,
	ratio = {'yRange':(0.1,1.9), 'texY': 'preVFP / postVFP'},
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
            "weight/F", "l1_pt/F", "l1_eta/F" , "l1_phi/F", "l1_pdgId/I", "l1_muIndex/I", "reweightHEM/F","l1_miniRelIso/F", "l1_relIso03/F", "nlep/I",
	    "lep[pt/F, eta/F, phi/F]",
            "JetGood[pt/F, eta/F, phi/F, genPt/F]", 
            "Jet[pt/F, eta/F, phi/F, jetId/I]", 
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", 'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I","event/I","run/I"]
read_variables += [
            "nMuon/I","nElectron/I","nJet/I",'reweightPU/F', 'Pileup_nTrueInt/F','reweightLeptonSF/F', 'reweightBTag_SF/F','reweightL1Prefire/F','reweightnISR/F', 'reweightwPt/F',
            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O, genPartIdx/I,genPartFlav/b]"

            ]

sequence = []
def getLeptonSelection( mode ):
	if   mode == 'mu': return "abs(l1_pdgId)==13"
	elif mode == 'e' : return "abs(l1_pdgId)==11"

yields   = {}
allPlots = {}
allModes = ['mu','e']
WJetsToLNu_HT_16APV.texName += "_preVFP"
for index, mode in enumerate(allModes):
	yields[mode] = {}
	weight_ = lambda event, sample: event.weight*event.reweightHEM

	for sample in samples:
		sample.weight         = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightLeptonSF * event.reweightwPt 
		sample.setSelectionString([getFilterCut(isData=False, year=2016, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
	WJetsToLNu_HT_16APV.style = styles.lineStyle(ROOT.kBlue)
	#WJetsToLNu_HT_16.scale = 16.5 
	#WJetsToLNu_HT_16APV.scale = 19.5 
	WJetsToLNu_HT_16.style = styles.lineStyle(ROOT.kRed)
	stack_ = Stack( *list([s] for s in samples)) 


	# Use some defaults
	Plot.setDefaults(stack = stack_, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper', histo_class=ROOT.TH1D)
	Plot2D.setDefaults( weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection) )
	plots   = []
	plots2D = []

	plots.append(Plot(
	    texX = '(l_{1} dR reco w/ gen) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_dRgen/F" ),
	    binning=[10,-1,1],
	  ))
	plots.append(Plot(
	    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_pt/F" ),
	    binning=[40,0,200],
	  ))
	plots.append(Plot(
	    texX = '#eta(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_eta/F" ),
	    binning=[15,-3,3],
	  ))
	plots.append(Plot(
	    texX = '#phi(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_phi/F" ),
	    binning=[20,-pi,pi],
	  ))
	plots.append(Plot(
	    texX = 'dxy(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_dxy/F" ),
	    binning=[20,-.02,.02],
	  ))
	plots.append(Plot(
	    texX = 'dz(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_dz/F" ),
	    binning=[20,-.1,.1],
	  ))
	plots.append(Plot(
	    texX = 'relIso03_all(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_relIso03/F" ),
	    binning=[30,0,5],
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
	    binning=[40,200,1000],
	  ))
	plots.append(Plot(
	    texX = '#phi MET (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "met_phi/F" ),
	    binning=[20,-pi,pi],
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
	#plots.append(Plot(
	#    texX = 'M_{T} (GeV)', texY = 'Number of Events / 20 GeV',
	#    name = 'mt_mod', attribute = lambda event, sample: event.mtmod,
	#    binning=[40,0,300],
	#  ))

	plots.append(Plot(
	    texX = 'cos(#Delta#phi(l_{1},E_{T}^{miss})) (GeV)', texY = 'Number of Events ',
	    name = 'coslmetphi', attribute = lambda event, sample: cos(event.l1_phi - event.met_phi),
	    binning=[10,-1,1],
	  ))
	plots.append(Plot(
	    texX = '#Delta#phi(l_{1},E_{T}^{miss}) (GeV)', texY = 'Number of Events ',
	    name = 'dphilmet', attribute = lambda event, sample: event.l1_phi - event.met_phi,
	    binning=[20,-pi,pi],
	  ))
	plots.append(Plot(
	    texX = '#Delta#phi(l_{1},E_{T}^{miss}) (GeV)', texY = 'Number of Events ',
	    name = 'deltaPhilmet', attribute = lambda event, sample: deltaPhi(event.l1_phi ,event.met_phi),
	    binning=[20,0,pi],
	  ))
	plots.append(Plot(
	    texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
	    name = 'jet1_pt', attribute = lambda event, sample: event.JetGood_pt[0],
	    binning=[45,100,1000],
	  ))
	plots.append(Plot(
	    texX = '#eta(leading jet) (GeV)', texY = 'Number of Events',
	    name = 'jet1_eta', attribute = lambda event, sample: event.JetGood_eta[0],
	    binning=[10,-3,3],
	  ))
	plots.append(Plot(
	    texX = '#phi(leading jet) (GeV)', texY = 'Number of Events',
	    name = 'jet1_phi', attribute = lambda event, sample: event.JetGood_phi[0],
	    binning=[10,-pi,pi],
	  ))
	plots.append(Plot(
	    texX = 'log(1+HI)/log(1+5)', texY = 'Number of Events',
	    name = 'hybridIsolation', attribute = lambda event, sample: log(1+(event.l1_relIso03*(min(event.l1_pt,25))))/log(1+5),
	    binning=[20,0,4],
	  ))
	plots.append(Plot(
	    texX = 'pt Ratio between l1 and leading JetGood', texY = 'Number of Events ',
	    name = 'ptRatio', attribute = lambda event, sample: (event.JetGood_pt[0] / event.l1_pt),
	    binning=[10,0,10],
	  ))
	#plots.append(Plot(
	#    texX = 'p_{T}(clean-leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
	#    name = 'cleanjet1_pt', attribute = lambda event, sample: event.cleanJets_pt,
	#    binning=[45,100,1000],
	#  ))
	#plots.append(Plot(
	#    texX = '#eta(clean-leading jet) (GeV)', texY = 'Number of Events',
	#    name = 'cleanjet1_eta', attribute = lambda event, sample: event.cleanJets_eta,
	#    binning=[10,-3,3],
	#  ))
	#plots.append(Plot(
	#    texX = '#phi(clean-leading jet) (GeV)', texY = 'Number of Events',
	#    name = 'cleanjet1_phi', attribute = lambda event, sample: event.cleanJets_phi,
	#    binning=[10,-pi,pi],
	#  ))
	#plots.append(Plot(
	#    texX = 'number of clean jets', texY = 'Number of Events',
	#    name = 'nJetsClean', attribute = lambda event, sample: event.nJetsClean,
	#    binning=[10,0,10],
	#  ))
	if args.selection.count('njet2'):
		plots.append(Plot(
		    texX = 'p_{T}(sub-leading jet) (GeV)', texY = 'Number of Events ',
		    name = 'jet2_pt', attribute = lambda event, sample: event.JetGood_pt[1],
		    binning=[45,0,1000],
		  ))
		plots.append(Plot(
		    texX = '#eta(sub-leading jet) (GeV)', texY = 'Number of Events',
		    name = 'jet2_eta', attribute = lambda event, sample: event.JetGood_eta[1],
		    binning=[10,-3,3],
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

#	plots2D.append(Plot2D(
#		name = "Data_Jet_eta_vs_phi",
#		texX  = '#eta', texY = "#phi",
#		stack = Stack ([data_sample]),
#		attribute = (
#			lambda event, sample: event.JetGood_eta[0],
#			lambda event, sample: event.JetGood_phi[0],
#			),
#		binning = [10,-3,3, 10,-pi,pi],
#	  ))
#	plots2D.append(Plot2D(
#		name = "MC_Jet_eta_vs_phi",
#		texX  = '#eta', texY = "#phi",
#		stack = Stack (samples),
#		attribute = (
#			lambda event, sample: event.JetGood_eta[0],
#			lambda event, sample: event.JetGood_phi[0],
#			),
#		binning = [10,-3,3, 10,-pi,pi],
#	  ))
#	plots2D.append(Plot2D(
#		name = "Data_l1_eta_vs_phi",
#		texX  = '#eta', texY = "#phi",
#		stack = Stack ([data_sample]),
#		attribute = (
#			TreeVariable.fromString( "l1_eta/F" ),
#			TreeVariable.fromString( "l1_phi/F" ),
#			),
#		binning = [10,-3,3, 10,-pi,pi],
#	  ))
#	plots2D.append(Plot2D(
#		name = "MC_l1_eta_vs_phi",
#		texX  = '#eta', texY = "#phi",
#		stack = Stack (samples),
#		attribute = (
#			TreeVariable.fromString( "l1_eta/F" ),
#			TreeVariable.fromString( "l1_phi/F" ),
#			),
#		binning = [10,-3,3, 10,-pi,pi],
#	  ))
#	plots2D.append(Plot2D(
#		name = "Data_MET_eta_vs_phi",
#		texX  = 'MET #eta', texY = "MET #phi",
#		stack = Stack ([data_sample]),
#		attribute = (
#			lambda event, sample: event.MET_eta,
#			TreeVariable.fromString( "met_phi/F" ),
#			),
#		binning = [10,-3,3, 10,-pi,pi],
#	  ))
#	plots2D.append(Plot2D(
#		name = "MC_MET_eta_vs_phi",
#		texX  = 'MET #eta', texY = "MET #phi",
#		stack = Stack (samples),
#		attribute = (
#			lambda event, sample: event.met_eta,
#			TreeVariable.fromString( "met_phi/F" ),
#			),
#		binning = [10,-3,3, 10,-pi,pi],
#	  ))
#	plots2D.append(Plot2D(
#		name = "Data_cosdphi_vs_Mt",
#		texX  = 'cos(#Delta#phi(l_{1},E_{T}^{miss}))', texY = "M_{t} (GeV)",
#		stack = Stack ([data_sample]),
#		attribute = (
#			lambda event, sample: cos(event.l1_phi - event.met_phi),
#			TreeVariable.fromString( "mt/F" ),
#			),
#		binning = [20,-1,1, 40,0,300],
#	  ))
#	plots2D.append(Plot2D(
#		name = "MC_cosdphi_vs_Mt",
#		texX  = 'cos(#Delta#phi(l_{1},E_{T}^{miss}))', texY = "M_{t} (GeV)",
#		stack = Stack (samples),
#		attribute = (
#			lambda event, sample: cos(event.l1_phi - event.met_phi),
#			TreeVariable.fromString( "mt/F" ),
#			),
#		binning = [20,-1,1, 40,0,300],
#	  ))


	plotting.fill(plots+plots2D, read_variables = read_variables, sequence = sequence)

	#Get normalization yields from yield histogram
	for plot in plots:
	    if plot.name == "yield":
	      for i, l in enumerate(plot.histos):
		for j, h in enumerate(l):
		  yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
		  h.GetXaxis().SetBinLabel(1, "#mu")
		  h.GetXaxis().SetBinLabel(2, "e")
	yields[mode]["MC"] = sum(yields[mode][s.name] for s in samples)
	#dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
	## if plotting only MC
	dataMCScale = 1

	drawPlots(plots, mode, dataMCScale)
	
	for plot in plots2D:
		plotting.draw2D(
				plot=plot,
				plot_directory=os.path.join(plot_directory, 'analysisPlots', args.targetDir, args.era ,mode+"log",args.selection) ,
				logX = False, logY = False, logZ = True,
				drawObjects = drawObjects( True, float('nan')),
				)

	allPlots[mode] = plots

# Add the different channels into all	
yields['all'] = {}
for y in yields[allModes[0]]:
	try:	yields['all'][y] = sum(yields[c][y] for c in (['mu','e']))
	except: yields['all'][y] = 0
#dataMCScale = yields['all']["data"]/yields['all']["MC"] if yields['all']["MC"] != 0 else float('nan')
## if only plotting MC and data
dataMCScale = 1
for plot in allPlots['mu']:
	for plot2 in (p for p in allPlots['e'] if p.name == plot.name): 
		for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
			for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
				if i==k:
					j.Add(l)
drawPlots(allPlots['mu'], 'all', dataMCScale)
