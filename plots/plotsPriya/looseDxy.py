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

from math   import pi, sqrt, sin, cos, atan2, log, isnan
from RootTools.core.standard import *
from StopsCompressed.Tools.user             import plot_directory
from Analysis.Tools.metFilters              import getFilterCut
from StopsCompressed.Tools.cutInterpreter   import cutInterpreter
#from Analysis.Tools.puProfileCache import *
from StopsCompressed.Tools.helpers           import deltaR, deltaPhi,ptRatio
from StopsCompressed.Tools.objectSelection   import muonSelector, eleSelector,  getGoodMuons, getGoodElectrons, getGoodTaus, getAllJets, matchLep
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
#argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
argParser.add_argument('--selection',          		action='store',      default='')
argParser.add_argument('--reweightPU',         		action='store',      default=None, 		  choices=['VDown', 'Down', 'Central', 'Up', 'VUp', 'VVUp'])
argParser.add_argument('--badMuonFilters',     		action='store',      default="Summer2016",  	  help="Which bad muon filters" )
argParser.add_argument('--noBadPFMuonFilter',           action='store_true', default=False)
argParser.add_argument('--noBadChargedCandidateFilter', action='store_true', default=True)
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

if  "2016" in args.era:
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
    
    
elif args.era == "Run2016preVFP" and not args.eos:
    from StopsCompressed.samples.nanoTuples_UL16APV_postProcessed import *
    samples = [WJetsToLNu_HT_16APV, Top_pow_16APV, singleTop_16APV, ZInv_16APV, DY_HT_LO_16APV, QCD_HT_16APV, VV_16APV, TTX_16APV]
    from StopsCompressed.samples.nanoTuples_RunUL16APV_postProcessed import *
    data_sample = Run2016preVFP
    from StopsCompressed.samples.nanoTuples_UL16APV_FullSimSignal_postProcessed import *
    #from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import *
    #signals = [T2tt_375_365,T2tt_500_470]
    #signals = [T2tt_375_365,T2tt_500_470, T2tt_500_420 ]
    signals = [T2tt_500_420, T2tt_500_470 ]
elif args.era == "Run2016postVFP" and not args.eos:
    from StopsCompressed.samples.nanoTuples_UL16_postProcessed import *
    #samples = [WJetsToLNu_HT_16, TTJets_1l_16, singleTop_16, ZInv_16, DY_HT_LO_16, QCD_HT_16, VV_16, TTX_16]
    #samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16, QCD_HT_16, VV_16, TTX_16]
    #samples = [WJetsToLNu_HT_16]
    samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16,QCD_HT_16, VV_16, TTX_16]
    from StopsCompressed.samples.nanoTuples_RunUL16_postProcessed import *
    data_sample = Run2016postVFP
    from StopsCompressed.samples.nanoTuples_UL16_FullSimSignal_postProcessed import *
    #from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import *
    #signals = [T2tt_375_365,T2tt_500_470]
    #signals = [T2tt_375_365,T2tt_500_470, T2tt_500_420 ]
    signals = [T2tt_500_420, T2tt_500_470, T2tt_LL_300_290, T2tt_LL_400_380, T2tt_LL_350_335]
    #if args.reweightPU:
    #	    nTrueInt_puRW = getReweightingFunction(data="PU_2016_35920_XSec%s"%args.reweightPU, mc="Summer16")
elif  args.era == "Run2016" and not args.eos:
    from StopsCompressed.samples.nanoTuples_UL16_36fb_postProcessed_v2 import *
    from StopsCompressed.samples.nanoTuples_UL16_36fb_FullSimSignal_postProcessed import *
    #samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_M50_LO_16, QCD_HT_16, VV_16, WWToLNuQQ_16, TTX_16]
    samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16, QCD_HT_16, VV_16, TTX_16]
    #samples = [QCD_HT_16]
    #samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_M50_LO_16, QCD_HT_16, TTX_16]
    data_sample = RunUL16_36fb
    signals = [T2tt_500_470, T2tt_500_420]
    #signals = [T2tt_500_420, T2tt_500_490]
elif "2017" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_UL17_postProcessed import *
    #samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17,QCD_Ele_17,QCD_Mu_17, VV_17, TTX_17]
    #samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, VV_17, TTX_17]
    samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, QCD_HT_17, VV_17, TTX_17]
    #from StopsCompressed.samples.nanoTuples_Run2017_14Dec2018_postProcessed import *
    from StopsCompressed.samples.nanoTuples_RunUL17_postProcessed import *
    data_sample = Run2017
    from StopsCompressed.samples.nanoTuples_UL17_FullSimSignal_postProcessed import *
    signals = [T2tt_500_420, T2tt_500_470]
    #if args.reweightPU:
	    # need sample based weights
    #	    pass
elif "2018" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_UL18_postProcessed import *
    #samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, QCD_Ele_18, QCD_Mu_18, VV_18, TTX_18]
    #samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, VV_18, TTX_18]
    samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, QCD_HT_18, VV_18, TTX_18]
    from StopsCompressed.samples.nanoTuples_RunUL18_postProcessed import *
    data_sample = Run2018
    from StopsCompressed.samples.nanoTuples_UL18_FullSimSignal_postProcessed import *
    signals = [T2tt_500_420, T2tt_500_470]
    #if args.reweightPU:
	#    nTrueInt_puRW = getReweightingFunction(data="PU_2018_58830_XSec%s"%args.reweightPU, mc="Autumn18")
if args.era != "Run2016" and not args.eos:
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
lumi_scale = 35.9

def drawObjects( plotData, dataMCScale):
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, ' L=%3.1f fb{}^{-1}(13 TeV) Scale %3.2f'% ( lumi_scale , dataMCScale) )
      #(0.45, 0.95, ' (13 TeV) Scale %3.2f'% ( dataMCScale) )
      #(0.15, 0.95, ' L=%3.1f fb{}^{-1}(13 TeV) Scale %3.2f Integral %3.2f'% ( lumi_scale , dataMCScale, mcIntegral) )
      #(0.15, 0.95, 'Scale %3.2f MCIntegral %3.2f DataIntegral %3.2f'% ( dataMCScale, mcIntegral, mcIntegral) )
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots,mode, dataMCScale):
  for log in [False, True]:
    
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', 'looseDxy' , args.targetDir, args.era ,mode +("log" if log else ""), args.selection)
    for plot in plots:
      #print "data?? : ", plot.histos[1], "mc:?? ", plot.histos[0]
      #if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
#      for l in plot.histos:
#	if len(l)>1: print "samples list in plot histo", [ l[x].GetName() for x in range(len(l))]
#	
#	if len(l)>1: 
#		mc_integral=  sum([ l[x].Integral() for x in range(len(l))]) 
#		print "integral: ", mc_integral
#      print l[0].GetName()
#      print "integral: ", l[0].Integral()

      
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
            "weight/F", "l1_pt/F", "l1_eta/F" , "l1_phi/F", "l1_pdgId/I", "l1_muIndex/I", "reweightHEM/F","l1_miniRelIso/F", "l1_relIso03/F", "nlep/I",
	    "lep[pt/F, eta/F, phi/F]",
            "JetGood[pt/F, eta/F, phi/F, genPt/F]", 
            "Jet[pt/F, eta/F, phi/F, jetId/I]", 
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", 'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I","event/I","run/I", "Flag_BadPFMuonDzFilter/O"]
read_variables += [
            "nMuon/I","nElectron/I","nJet/I", "dPhiMetJet/F", "metJet/I",
            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,genPartFlav/b,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O]",
	    "LowPtElectron[pt/F]",
            ]
#for s in samples:
#    s.read_variables = ["genWeight/F",'reweightPU/F', 'Pileup_nTrueInt/F','reweightBTag_SF/F', 'GenMET_pt/F', 'GenMET_phi/F', 'Muon[genPartIdx/I,genPartFlav/b]', "GenPart[pt/F,eta/F,phi/F]", "nGenPart/I"]

#genfilter efficiency
genFilter = genFilter(year=year)


sequence = []
ele_selector_nodxydz = eleSelector("noDxyDz", year=year)
mu_selector_nodxydz = muonSelector("noDxyDz", year=year)

ele_selector_nodxy = eleSelector("noDxy", year=year)
mu_selector_nodxy = muonSelector("noDxy", year=year)

ele_selector_hybridIso = eleSelector("hybridIso", year=year)
mu_selector_hybridIso = muonSelector("hybridIso", year=year)
def lepLooseDxy(event, sample):
	event.l1_pt_nodxydz   = -999 
	event.l1_eta_nodxydz  = -999 
	event.l1_phi_nodxydz  = -999 
	event.l1_dxy_nodxydz  = -999
	event.l1_dz_nodxydz   = -999 
	event.l1_pfRelIso03_all_nodxydz   = -999
	event.l1_abs_dxy_nodxydz = -999
	event.l1_abs_dz_nodxydz  = -999
	event.isPrompt	= 0
	noDxyDzLeptons = getGoodElectrons( event, ele_selector = ele_selector_nodxydz) + getGoodMuons(event, mu_selector = mu_selector_nodxydz)
	noDxyDzLeptons.sort(key = lambda p:-p['pt'])
	for l in noDxyDzLeptons:
		if  matchLep(l) == True:
			event.isPrompt = 1
	if len(noDxyDzLeptons) > 0 :
		event.l1_pt_nodxydz   = noDxyDzLeptons[0]['pt'] 
		event.l1_eta_nodxydz  = noDxyDzLeptons[0]['eta'] 
		event.l1_phi_nodxydz  = noDxyDzLeptons[0]['phi']
		event.l1_dxy_nodxydz  = noDxyDzLeptons[0]['dxy'] 
		event.l1_dz_nodxydz   = noDxyDzLeptons[0]['dz'] 
		event.l1_pfRelIso03_all_nodxydz   = noDxyDzLeptons[0]['pfRelIso03_all'] 
		event.l1_abs_dxy_nodxydz  = abs(noDxyDzLeptons[0]['dxy'])
		event.l1_abs_dz_nodxydz   = abs(noDxyDzLeptons[0]['dz']) 


	event.l1_pt_nodxy   = -999
	event.l1_eta_nodxy  = -999
	event.l1_phi_nodxy  = -999 
	event.l1_dxy_nodxy  = -999
	event.l1_dz_nodxy   = -999
	event.l1_dxy_nodxy  = -999
	event.l1_dz_nodxy   = -999
	event.l1_pfRelIso03_all_nodxy   = float('nan')
	noDxyLeptons = getGoodElectrons( event, ele_selector = ele_selector_nodxy) + getGoodMuons(event, mu_selector = mu_selector_nodxy)
	noDxyLeptons.sort(key = lambda p:-p['pt'])
	if len(noDxyLeptons) > 0:
		event.l1_pt_nodxy   = noDxyLeptons[0]['pt'] 
		event.l1_eta_nodxy  = noDxyLeptons[0]['eta'] 
		event.l1_phi_nodxy  = noDxyLeptons[0]['phi']
		event.l1_dxy_nodxy  = noDxyLeptons[0]['dxy'] 
		event.l1_dz_nodxy     = noDxyLeptons[0]['dz'] 
		event.l1_pfRelIso03_all_nodxy     = noDxyLeptons[0]['pfRelIso03_all'] 

	
	event.l1_eta_hybridIso  = float('nan')
	hybridIsoLeptons = getGoodElectrons( event, ele_selector = ele_selector_hybridIso) + getGoodMuons(event, mu_selector = mu_selector_hybridIso)
	hybridIsoLeptons.sort(key = lambda p:-p['pt'])
	if len(hybridIsoLeptons) > 0:
		event.l1_eta_hybridIso = hybridIsoLeptons[0]['eta']

sequence.append (lepLooseDxy)

def getLeptonSelection( mode ):
	if   mode == 'mu': return "abs(l1_pdgId)==13"
	elif mode == 'e' : return "abs(l1_pdgId)==11"


yields   = {}
allPlots = {}
allModes = ['mu','e']
for index, mode in enumerate(allModes):
	yields[mode] = {}
	if args.era == "Run2016":
		data_sample.setSelectionString([getFilterCut(isData=True, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
		lumi_scale                 = data_sample.lumi/1000
		#print "lumi for each set: ", lumi_scale
		data_sample.scale          = 1.
		data_sample.style          = styles.errorStyle(ROOT.kBlack)
		data_sample.name 	   = "data"
	else:
		data_sample.setSelectionString([getFilterCut(isData=True, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
		if args.preHEM:
			data_sample.addSelectionString("run<319077")
		if args.postHEM:
			data_sample.addSelectionString("run>=319077")
		lumi_scale                 = data_sample.lumi/1000
		#print "lumi: ", lumi_scale
		if args.preHEM:   lumi_scale *= 0.37
		if args.postHEM:  lumi_scale *= 0.63
		data_sample.scale          = 1.
		data_sample.style          = styles.errorStyle(ROOT.kBlack)
		data_sample.name 	   = "data"
	if signals:
	    T2tt_500_470.color = ROOT.kPink+6
	    T2tt_500_420.color = ROOT.kCyan+2
	    T2tt_LL_300_290.color = ROOT.kYellow
	    T2tt_LL_400_380.color = ROOT.kRed
	    T2tt_LL_350_335.color = ROOT.kBlue
	
	weight_ = lambda event, sample: event.weight*event.reweightHEM

	for sample in samples + signals:

		sample.read_variables = ['reweightPU/F', 'Pileup_nTrueInt/F','reweightLeptonSF/F', 'reweightBTag_SF/F','reweightL1Prefire/F','reweightnISR/F', 'reweightwPt/F',]
		sample.read_variables += ['reweightPU%s/F'%args.reweightPU if args.reweightPU != "Central" else "reweightPU/F"]
		#pu_getter = operator.attrgetter('reweightPU' if args.reweightPU=='Central' else "reweightPU%s"%args.reweightPU)
		if args.era == "Run2016":
			if "T2tt" in sample.name:
				mStop= int(sample.name.split('_')[1])
				mNeu= int(sample.name.split('_')[2])
				#print sample.name.split('_')[1], sample.name.split('_')[2]
				genEff = genFilter.getEff(mStop,mNeu)
				#print "signal name: ",sample.name, "mStop: ", mStop, "mNeu: ", mNeu,"genEff: " ,genEff
				#sample.read_variables += [ 'reweight_nISR/F']
				sample.read_variables += [ 'year/I']
				sample.weight         = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightwPt * event.reweightLeptonSF * genEff * lumi_year[event.year]/1000
				#sample.weight         = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire  * event.reweightLeptonSF 
				sample.style = styles.errorStyle( color=sample.color, markerSize = 0.6)
				sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])

			else:
				sample.read_variables += ['year/I', ]
				sample.weight         = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightLeptonSF * event.reweightwPt * lumi_year[event.year]/1000  
				sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
				sample.style = styles.fillStyle(sample.color)
		else:
			if "T2tt" in sample.name:
				sample.style = styles.errorStyle( color=sample.color, markerSize = 0.6)
				sample.weight         = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightLeptonSF * event.reweightwPt
				sample.scale = lumi_scale
				sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode),])
			else:

				sample.weight = lambda event, sample: event.reweightPU * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightLeptonSF * event.reweightwPt
				sample.scale = lumi_scale
				sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode),])
			
				sample.style = styles.fillStyle(sample.color)
	#stack_ = Stack( samples, data_sample ) 
	#stack_ = Stack( samples )
	#stack_ = Stack( samples, T2tt_500_470, T2tt_500_420 )
	stack_ = Stack( samples, data_sample, T2tt_500_470,  T2tt_LL_400_380, T2tt_LL_350_335)

	if args.small:
		for sample in samples + [data_sample] + signals:
			sample.normalization = 1.
			sample.reduceFiles( factor = 70 )
			#sample.scale /= sample.normalization

	# Use some defaults
	Plot.setDefaults(stack = stack_, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper', histo_class=ROOT.TH1D)
	#Plot2D.setDefaults( weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection) )
	plots   = []
	plots2D = []

	plots.append(Plot(
	    texX = 'l1_pt w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_pt_nodxydz', attribute = lambda event, sample: event.l1_pt_nodxydz,
	    binning=[40,0,200],
	  ))
	plots.append(Plot(
	    texX = 'l1_eta w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_eta_nodxydz', attribute = lambda event, sample: event.l1_eta_nodxydz,
	    binning=[20,-4,4],
	  ))
	plots.append(Plot(
	    texX = 'l1_phi w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_phi_nodxydz', attribute = lambda event, sample: event.l1_phi_nodxydz,
	    binning=[20,-pi,pi],
	  ))
	plots.append(Plot(
	    texX = 'l1_dxy w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_dxy_nodxydz', attribute = lambda event, sample: event.l1_dxy_nodxydz,
	    binning=[50,-10,10],
	  ))
	plots.append(Plot(
	    texX = 'l1_dz w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_dz_nodxydz', attribute = lambda event, sample: event.l1_dz_nodxydz,
	    binning=[50,-12,12],
	  ))
	plots.append(Plot(
	    texX = 'l1_dxy w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_dxy_nodxydz', attribute = lambda event, sample: event.l1_abs_dxy_nodxydz,
	    binning=[50,0,10],
	  ))
	plots.append(Plot(
	    texX = 'l1_abs_dz w/o dxy and dz', texY = 'Number of events',
	    name = 'l1_abs_dz_nodxydz', attribute = lambda event, sample: event.l1_abs_dz_nodxydz,
	    binning=[24,0,12],
	  ))


	plots.append(Plot(
	    texX = 'l1_pt w/o dxy ', texY = 'Number of events',
	    name = 'l1_pt_nodxy', attribute = lambda event, sample: event.l1_pt_nodxy,
	    binning=[40,0,200],
	  ))
	plots.append(Plot(
	    texX = 'l1_eta w/o dxy and ', texY = 'Number of events',
	    name = 'l1_eta_nodxy', attribute = lambda event, sample: event.l1_eta_nodxy,
	    binning=[20,-4,4],
	  ))
	plots.append(Plot(
	    texX = 'l1_phi w/o dxy', texY = 'Number of events',
	    name = 'l1_phi_nodxy', attribute = lambda event, sample: event.l1_phi_nodxy,
	    binning=[20,-pi,pi],
	  ))
	plots.append(Plot(
	    texX = 'l1_dxy w/o dxy', texY = 'Number of events',
	    name = 'l1_dxy_nodxy', attribute = lambda event, sample: event.l1_dxy_nodxy,
	    binning=[50,-10,10],
	  ))
	plots.append(Plot(
	    texX = 'l1_dz w/o dxy ', texY = 'Number of events',
	    name = 'l1_dz_nodxy', attribute = lambda event, sample: event.l1_dz_nodxy,
	    binning=[50,-12,12],
	  ))
	plots.append(Plot(
	    name = 'yield', texX = 'yield', texY = 'Number of Events',
	    attribute = lambda event, sample: 0.5 + index ,
	    binning=[3, 0, 3],
	  ))

	plots.append(Plot(
	    texX = 'l1_eta hybridIso ', texY = 'Number of events',
	    name = 'l1_eta_hybridiso', attribute = lambda event, sample: event.l1_eta_hybridIso,
	    binning=[20,-4,4],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'WJets pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (samples[0]),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_dz w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'WJets l1_dz vs dxy nodxydz', 
	    stack = Stack (samples[0]),
	    attribute = (
		    lambda event, sample: event.l1_dz_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[50,-12,12, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dz w/o dxy and dz',
	    name = 'WJets pfRelIso03_all vs dz nodxydz', 
	    stack = Stack (samples[0]),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dz_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_500_420 pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (T2tt_500_420),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dz w/o dxy and dz',
	    name = 'T2tt_500_420 pfRelIso03_all vs dz nodxydz', 
	    stack = Stack (T2tt_500_420),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dz_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_dz w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_500_420_l1_dz vs dxy nodxydz', 
	    stack = Stack (T2tt_500_420),
	    attribute = (
		    lambda event, sample: event.l1_dz_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[50,-12,12, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_500_470 pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (T2tt_500_470),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dz w/o dxy and dz',
	    name = 'T2tt_500_470 pfRelIso03_all vs dz nodxydz', 
	    stack = Stack (T2tt_500_470),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dz_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_dz w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_500_470_l1_dz vs dxy nodxydz', 
	    stack = Stack (T2tt_500_470),
	    attribute = (
		    lambda event, sample: event.l1_dz_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[50,-12,12, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_LL_300_290 pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (T2tt_LL_300_290),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dz w/o dxy and dz',
	    name = 'T2tt_LL_300_290 pfRelIso03_all vs dz nodxydz', 
	    stack = Stack (T2tt_LL_300_290),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dz_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_LL_400_380 pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (T2tt_LL_400_380),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_dz w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_LL_400_380_l1_dz vs dxy nodxydz', 
	    stack = Stack (T2tt_LL_400_380),
	    attribute = (
		    lambda event, sample: event.l1_dz_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[50,-12,12, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dz w/o dxy and dz',
	    name = 'T2tt_LL_400_380 pfRelIso03_all vs dz nodxydz', 
	    stack = Stack (T2tt_LL_400_380),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dz_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_LL_350_335 pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (T2tt_LL_350_335),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[30,0,5, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz (noPrompt)', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_LL_350_335 pfRelIso03_all vs dxy nodxydz_noPRompt', 
	    stack = Stack (T2tt_LL_350_335),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    binning=[30,0,5, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_dz w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'T2tt_LL_350_335_l1_dz vs dxy nodxydz', 
	    stack = Stack (T2tt_LL_350_335),
	    attribute = (
		    lambda event, sample: event.l1_dz_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    weight = lambda event, sample: event.isPrompt,
	    binning=[50,-12,12, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'QCD pfRelIso03_all vs dxy nodxydz', 
	    stack = Stack (samples[5]),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    binning=[30,0,5, 50,-10,10],
	  ))

	plots2D.append(Plot2D(
	    texX = 'l1_pfRelIso_03_all w/o dxy and dz', texY = 'dz w/o dxy and dz',
	    name = 'QCD pfRelIso03_all vs dz nodxydz', 
	    stack = Stack (samples[5]),
	    attribute = (
		    lambda event, sample: event.l1_pfRelIso03_all_nodxydz,
		    lambda event, sample: event.l1_dz_nodxydz,
		    ),
	    binning=[30,0,5, 50,-10,10],
	  ))
	plots2D.append(Plot2D(
	    texX = 'l1_dz w/o dxy and dz', texY = 'dxy w/o dxy and dz',
	    name = 'QCD_l1_dz vs dxy nodxydz', 
	    stack = Stack (samples[5]),
	    attribute = (
		    lambda event, sample: event.l1_dz_nodxydz,
		    lambda event, sample: event.l1_dxy_nodxydz,
		    ),
	    binning=[50,-12,12, 50,-10,10],
	  ))
	plotting.fill(plots+plots2D, read_variables = read_variables, sequence = sequence)
	#plotting.fill(plots, read_variables = read_variables, sequence = sequence)

	#Get normalization yields from yield histogram
	for plot in plots:
		if plot.name == "yield":
			for i, l in enumerate(plot.histos):
				for j, h in enumerate(l):
					yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
					h.GetXaxis().SetBinLabel(1, "#mu")
					h.GetXaxis().SetBinLabel(2, "e")
	for s in samples:
		print "INFO: Yield for %s: %f" % (s.name, yields[mode][s.name])
	yields[mode]["MC"] = sum(yields[mode][s.name] for s in samples)
	if isnan(yields[mode]["MC"]):
		print "ERROR: MC Yield is nan"
		dataMCScale = 1
	elif yields[mode]["MC"] == 0:
		print "ERROR: MC Yield is 0"
		dataMCScale = 1
	else:
		dataMCScale        = yields[mode]["data"]/yields[mode]["MC"]
	## if plotting only MC
	#dataMCScale = 1

	drawPlots(plots, mode, dataMCScale)
	
	for plot in plots2D:
		plotting.draw2D(
				plot=plot,
				plot_directory=os.path.join(plot_directory, 'analysisPlots', 'looseDxy' , args.targetDir, args.era ,mode+"log",args.selection) ,
				logX = False, logY = False, logZ = True,
				drawObjects = drawObjects( True, float('nan')),
				)

	allPlots[mode] = plots

# Add the different channels into all	
yields['all'] = {}
for y in yields[allModes[0]]:
	try:	yields['all'][y] = sum(yields[c][y] for c in (['mu','e']))
	except: yields['all'][y] = 0

if isnan(yields['all']["MC"]):
	print "ERROR: MC Yield is nan"
	dataMCScale = 1
elif yields['all']["MC"] == 0:
	print "ERROR: MC Yield is 0"
	dataMCScale = 1
else:
	dataMCScale        = yields['all']["data"]/yields['all']["MC"]

## if only plotting MC and data
#dataMCScale = 1
for plot in allPlots['mu']:
	for plot2 in (p for p in allPlots['e'] if p.name == plot.name): 
		for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
			for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
				if i==k:
					j.Add(l)
drawPlots(allPlots['mu'], 'all', dataMCScale)
