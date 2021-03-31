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
#from Analysis.Tools.metFilters              import getFilterCut
from StopsCompressed.Tools.cutInterpreter   import cutInterpreter
from Analysis.Tools.puProfileCache import *
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
argParser.add_argument('--targetDir',          		action='store',      default='v5_Data')
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300-isPrompt')
argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
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
    samples = [WJetsToLNu_HT_16, Top_pow_16 , Fakes_16, singleTop_16, DY_HT_LO_16,VV_16, TTX_16]
    #samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16, VV_16, TTX_16]
    from StopsCompressed.samples.nanoTuples_Run2016_17July2018_postProcessed import *
    from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import *
    #signals = [T2tt_375_365,T2tt_500_470]
    #signals = [T2tt_375_365,T2tt_500_470, T2tt_500_420 ]
    signals = []
    #if args.reweightPU:
    #	    nTrueInt_puRW = getReweightingFunction(data="PU_2016_35920_XSec%s"%args.reweightPU, mc="Summer16")
elif "2017" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Fall17_postProcessed import *
    #samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17,QCD_Ele_17,QCD_Mu_17, VV_17, TTX_17]
    #samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, VV_17, TTX_17]
    samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, QCD_HT_17, VV_17, TTX_17]
    #from StopsCompressed.samples.nanoTuples_Run2017_14Dec2018_postProcessed import *
    from StopsCompressed.samples.nanoTuples_Run2017_nanoAODv6_postProcessed import *
    signals = []
    #if args.reweightPU:
	    # need sample based weights
    #	    pass
elif "2018" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import *
    #samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, QCD_Ele_18, QCD_Mu_18, VV_18, TTX_18]
    #samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, VV_18, TTX_18]
    samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, QCD_HT_18, VV_18, TTX_18]
    from StopsCompressed.samples.nanoTuples_Run2018_nanoAODv6_postProcessed import *
    signals = []
    #if args.reweightPU:
	#    nTrueInt_puRW = getReweightingFunction(data="PU_2018_58830_XSec%s"%args.reweightPU, mc="Autumn18")
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
    
    plot_directory_ = os.path.join(plot_directory, 'fakeStudies',args.targetDir, args.era ,mode +("log" if log else ""), args.selection)
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
            "weight/F", "l1_pt/F", "l1_eta/F" , "l1_phi/F", "l1_pdgId/I", "l1_muIndex/I", "reweightHEM/F","l1_miniRelIso/F", "l1_relIso03/F", "nlep/I","l1_isPrompt/O","l1_dRgen/F", 
	    "lep[pt/F, eta/F, phi/F]",
            "JetGood[pt/F, eta/F, phi/F, genPt/F]", 
            "Jet[pt/F, eta/F, phi/F, jetId/I]", 
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", 'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I","event/I","run/I"]
read_variables += [
            "nMuon/I","nElectron/I","nJet/I",
            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O]"

            ]
#for s in samples:
#    s.read_variables += ["genWeight/F",'reweightPU/F', 'Pileup_nTrueInt/F','reweightBTag_SF/F', 'GenMET_pt/F', 'GenMET_phi/F', 'Muon[genPartIdx/I,genPartFlav/b]']

#genfilter efficiency
genFilter = genFilter(year=year)


sequence = []

def mtwithdphi(event, sample):
	event.mtmod = float('nan')
	if deltaPhi(event.l1_phi ,event.met_phi) < 1.7: 
		event.mtmod            = sqrt (2 * event.l1_pt * event.met_pt * (1 - cos(event.l1_phi - event.met_phi) ) )
def delR(event,sample):
	event.dR = float("nan")
	event.dR = sqrt(((deltaPhi(event.l1_phi,event.JetGood_phi[0])**2) + ((event.l1_eta - event.JetGood_eta[0])**2)))
sequence.append(delR)
def jetToLeptonRatio (event, sample):
	event.cleanJets_pt  = float ('nan')
	event.cleanJets_eta = float ('nan')
	event.cleanJets_phi  = float ('nan')
	Electrons =  getGoodElectrons(event, ele_selector = eleSelector("hybridIso", year=year))	
	Muons =  getGoodMuons(event, mu_selector = muonSelector("hybridIso", year=year))	
	leptons = Electrons + Muons
	leptons.sort(key = lambda p:-p['pt'])
	jets = getAllJets(event, leptons, ptCut=30, absEtaCut=2.4,jetVars= ['pt','eta','phi', 'jetId'] , jetCollections=["Jet"], idVar='jetId')
	event.nJetsClean = len(jets)
	if event.nJetsClean >0:
		event.cleanJets_pt  = jets[0]['pt']
		event.cleanJets_eta = jets[0]['eta']
		event.cleanJets_phi = jets[0]['phi']
#	for i,jet in enumerate(jets):
#		event.cleanJets_pt  = jet['pt']
#		event.cleanJets_eta = jet['eta']
#		event.cleanJets_phi = jet['phi']

#def make_weight (event, sample):
#	print event.weight, event.reweightHEM
#sequence.append (make_weight)


def getLeptonSelection( mode ):
	if   mode == 'mu': return "abs(l1_pdgId)==13"
	elif mode == 'e' : return "abs(l1_pdgId)==11"

yields   = {}
allPlots = {}
allModes = ['mu','e']
for index, mode in enumerate(allModes):
	yields[mode] = {}
	data_sample.setSelectionString([getFilterCut(isData=True, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
	if args.preHEM:
		data_sample.addSelectionString("run<319077")
	if args.postHEM:
		data_sample.addSelectionString("run>=319077")
	lumi_scale                 = data_sample.lumi/1000
	if args.preHEM:   lumi_scale *= 0.37
	if args.postHEM:  lumi_scale *= 0.63
	data_sample.scale          = 1.
	data_sample.style          = styles.errorStyle(ROOT.kBlack)
	data_sample.name 	   = "data"
	if signals:
	    T2tt_500_470.color = ROOT.kPink+6
	    #T2tt_500_420.color = ROOT.kCyan
	    T2tt_375_365.color = ROOT.kAzure+1
	
	weight_ = lambda event, sample: event.weight*event.reweightHEM

	for sample in samples + signals:

		sample.read_variables  = ['reweightPU/F', 'Pileup_nTrueInt/F','reweightLeptonSF/F', 'reweightBTag_SF/F','reweightL1Prefire/F','reweightnISR/F', 'reweightwPt/F',]
		sample.read_variables += ['reweightPU%s/F'%args.reweightPU if args.reweightPU != "Central" else "reweightPU/F"]
		pu_getter = operator.attrgetter('reweightPU' if args.reweightPU=='Central' else "reweightPU%s"%args.reweightPU)
		if "T2tt" in sample.name:
			mStop= int(sample.name.split('_')[1])
			mNeu= int(sample.name.split('_')[2])

			#print sample.name.split('_')[1], sample.name.split('_')[2]
			genEff = genFilter.getEff(mStop,mNeu)
			#print "signal name: ",sample.name, "mStop: ", mStop, "mNeu: ", mNeu,"genEff: " ,genEff
			sample.read_variables += [ 'reweight_nISR/F']
			sample.weight         = lambda event, sample: pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightnISR * event.reweightwPt * event.reweightLeptonSF * event.reweight_nISR * genEff
			sample.style = styles.errorStyle( color=sample.color, markerSize = 0.6)
			sample.setSelectionString([getFilterCut(isData=False, isFastSim=True, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
			sample.scale = lumi_scale
	#	elif "T2tt_375_365" in sample.name:
	#		sample.read_variables += [ 'reweight_nISR/F']
	#		sample.weight         = lambda event, sample: pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightnISR * event.reweightwPt * event.reweightLeptonSF * event.reweight_nISR*0.2546
	#		sample.style = styles.errorStyle( color=sample.color, markerSize = 0.6)
	#		sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
	#		sample.scale = lumi_scale
	#	elif "T2tt_500_420" in sample.name:
	#		sample.read_variables += [ 'reweight_nISR/F']
	#		sample.weight         = lambda event, sample: pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightnISR * event.reweightwPt * event.reweightLeptonSF * event.reweight_nISR*0.3520
	#		sample.style = styles.errorStyle( color=sample.color, markerSize = 0.6)
	#		sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
	#		sample.scale = lumi_scale
		else:
			sample.weight         = lambda event, sample: pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightwPt * event.reweightLeptonSF
			sample.scale = lumi_scale 
			sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
	for sample in samples:
		if sample.name == "fakes":
			print sample.name, "better be fake"
			sample.addSelectionString("l1_isPrompt==0")
			sample.style = styles.fillStyle(sample.color)
		else:
			print sample.name, "no fakes"
			sample.addSelectionString("l1_isPrompt>0")
			sample.style = styles.fillStyle(sample.color)

	stack_ = Stack( samples, data_sample ) 
	#stack_ = Stack( samples, data_sample, T2tt_375_365, T2tt_500_470, T2tt_500_420 )
	#stack_ = Stack( samples, data_sample, T2tt_375_365, T2tt_500_470 )

	if args.small:
		for sample in samples + [data_sample] + signals:
			sample.normalization = 1.
			sample.reduceFiles( factor = 40 )
			sample.scale /= sample.normalization

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
	    texX = 'dR between l1 and leading JetGood', texY = 'Number of Events ',
	    name = 'deltaR', attribute = lambda event, sample: event.dR,
	    binning=[10,-1,1],
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

	plots2D.append(Plot2D(
		name = "Data_Jet_eta_vs_phi",
		texX  = '#eta', texY = "#phi",
		stack = Stack ([data_sample]),
		attribute = (
			lambda event, sample: event.JetGood_eta[0],
			lambda event, sample: event.JetGood_phi[0],
			),
		binning = [10,-3,3, 10,-pi,pi],
	  ))
	plots2D.append(Plot2D(
		name = "MC_Jet_eta_vs_phi",
		texX  = '#eta', texY = "#phi",
		stack = Stack (samples),
		attribute = (
			lambda event, sample: event.JetGood_eta[0],
			lambda event, sample: event.JetGood_phi[0],
			),
		binning = [10,-3,3, 10,-pi,pi],
	  ))
	plots2D.append(Plot2D(
		name = "Data_l1_eta_vs_phi",
		texX  = '#eta', texY = "#phi",
		stack = Stack ([data_sample]),
		attribute = (
			TreeVariable.fromString( "l1_eta/F" ),
			TreeVariable.fromString( "l1_phi/F" ),
			),
		binning = [10,-3,3, 10,-pi,pi],
	  ))
	plots2D.append(Plot2D(
		name = "MC_l1_eta_vs_phi",
		texX  = '#eta', texY = "#phi",
		stack = Stack (samples),
		attribute = (
			TreeVariable.fromString( "l1_eta/F" ),
			TreeVariable.fromString( "l1_phi/F" ),
			),
		binning = [10,-3,3, 10,-pi,pi],
	  ))
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
	plots2D.append(Plot2D(
		name = "Data_cosdphi_vs_Mt",
		texX  = 'cos(#Delta#phi(l_{1},E_{T}^{miss}))', texY = "M_{t} (GeV)",
		stack = Stack ([data_sample]),
		attribute = (
			lambda event, sample: cos(event.l1_phi - event.met_phi),
			TreeVariable.fromString( "mt/F" ),
			),
		binning = [20,-1,1, 40,0,300],
	  ))
	plots2D.append(Plot2D(
		name = "MC_cosdphi_vs_Mt",
		texX  = 'cos(#Delta#phi(l_{1},E_{T}^{miss}))', texY = "M_{t} (GeV)",
		stack = Stack (samples),
		attribute = (
			lambda event, sample: cos(event.l1_phi - event.met_phi),
			TreeVariable.fromString( "mt/F" ),
			),
		binning = [20,-1,1, 40,0,300],
	  ))


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
	dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
	## if plotting only MC
	#dataMCScale = 1

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
dataMCScale = yields['all']["data"]/yields['all']["MC"] if yields['all']["MC"] != 0 else float('nan')
## if only plotting MC and data
#dataMCScale = 1
for plot in allPlots['mu']:
	for plot2 in (p for p in allPlots['e'] if p.name == plot.name): 
		for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
			for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
				if i==k:
					j.Add(l)
drawPlots(allPlots['mu'], 'all', dataMCScale)
