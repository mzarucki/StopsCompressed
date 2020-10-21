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
#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           		action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--era',                		action='store',      default="Run2018",  	type=str )
argParser.add_argument('--eos',                		action='store_true', 			help='change sample directory to location eos directory' )
argParser.add_argument('--small',              		action='store_true', 			help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          		action='store',      default='v_32')
argParser.add_argument('--selection',          		action='store',      default='nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300')
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
if args.postHEM:                      args.targetDir += "_postHEM"

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
    # bkg MC
	from StopsCompressed.samples.nanoTuples_Summer16_postProcessed import *
    # samples = [WJetsToLNu_HT_16, Top_pow_16, singleTop_16, ZInv_16, DY_HT_LO_16, QCD_HT_16, VV_16, TTX_16]
	samples = [QCD_HT_16]
	prediction = [copy.deepcopy(QCD_HT_16)]
	prediction[0].texName = "QCD-predcited" 
	prediction[0].color = ROOT.kCyan 
	prediction[0].SetFillColorAlpha = (ROOT.kCyan,0.3) 
	prediction[0].name = "QCD_HTcopy"
	# data
	from StopsCompressed.samples.nanoTuples_Run2016_17July2018_postProcessed import *
    
	# signal MC
	#from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import *
    #signals = [T2tt_375_365,T2tt_500_470 ]
	signals = []
    #if args.reweightPU:
    #	    nTrueInt_puRW = getReweightingFunction(data="PU_2016_35920_XSec%s"%args.reweightPU, mc="Summer16")
elif "2017" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Fall17_postProcessed import *
    #samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17,QCD_Ele_17,QCD_Mu_17, VV_17, TTX_17]
    samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, VV_17, TTX_17]
    #samples = [WJetsToLNu_HT_17, Top_pow_17, singleTop_17, ZInv_17, DY_HT_LO_17, QCD_HT_17, VV_17, TTX_17]
    #from StopsCompressed.samples.nanoTuples_Run2017_14Dec2018_postProcessed import *
    from StopsCompressed.samples.nanoTuples_Run2017_nanoAODv6_postProcessed import *
    signals = []
    #if args.reweightPU:
	    # need sample based weights
    #	    pass
elif "2018" in args.era and not args.eos:
    from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed import *
    #samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, QCD_Ele_18, QCD_Mu_18, VV_18, TTX_18]
    samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, VV_18, TTX_18]
    #samples =[WJetsToLNu_HT_18, Top_pow_18, singleTop_18, ZInv_18, DY_HT_LO_18, QCD_HT_18, VV_18, TTX_18]
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
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots,mode, dataMCScale):
  	for log in [False, True]:
		plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.targetDir, args.era ,mode +("log" if log else ""), args.selection)
		for plot in plots:
			_drawObjects = []
			plotting.draw(
				plot,
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
            "met_pt/F", "met_phi/F","CT1/F", "HT/F","mt/F", 'l1_dxy/F', 'l1_dz/F', 'dphij0j1/F','ISRJets_pt/F', 'nISRJets/I','nSoftBJets/I','nHardBJets/I', "nBTag/I", "nJetGood/I", "PV_npvsGood/I","event/I","run/I"]
read_variables += [
            "nMuon/I","nElectron/I","nJet/I",
            "Muon[dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,ip3d/F,jetRelIso/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/b,inTimeMuon/O,isGlobal/O,isPFcand/O,isTracker/O,mediumId/O,mediumPromptId/O,miniIsoId/b,multiIsoId/b,mvaId/b,pfIsoId/b,softId/O,softMvaId/O,tightId/O,tkIsoId/b,triggerIdLoose/O]"
            ]

sequence = []

FR_file = ROOT.TFile("/users/janik.andrejkovic/public/HEPHY_Analysis/CMSSW_10_2_18/src/tWZ/plots/plotsJanik/fakes/FR.root")
TightToLoose = FR_file.Get("TightToLoose")
def mtwithdphi(event, sample):
	event.mtmod = float('nan')
	if deltaPhi(event.l1_phi ,event.met_phi) < 1.7: 
		event.mtmod            = sqrt (2 * event.l1_pt * event.met_pt * (1 - cos(event.l1_phi - event.met_phi) ) )
def delR(event,sample):
	event.dR = float("nan")
	event.dR = sqrt(((deltaPhi(event.l1_phi,event.JetGood_phi[0])**2) + ((event.l1_eta - event.JetGood_eta[0])**2)))
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
def frHybridIso(event,sample) :
	if event.l1_pt <= 25 :
		event.HI = event.l1_relIso03*event.l1_pt
	else :
		event.HI = event.l1_relIso03*25.

	event.tight = 0.
	event.loose = 0.
	event.TLratio = 1.
	if event.HI <= 5 :
		event.tight = 1.
	elif event.HI > 5 :
		event.loose = 1.
		event.TLratio = TightToLoose.GetBinContent(TightToLoose.GetXaxis().FindBin(event.l1_pt),TightToLoose.GetYaxis().FindBin(event.l1_eta))
		
def getLeptonSelection( mode ):
	if   mode == 'mu': return "abs(l1_pdgId)==13"
	elif mode == 'e' : return "abs(l1_pdgId)==11"
def IsoCutWeight (Tight=True, inclusive=False, TL=False) :
    def myIsoWeight(event, sample ):
        if inclusive :
            return event.weight
        else :
            if event.HI <= 5 and Tight == True:
                return event.weight
            elif event.HI > 5 and Tight == False:
				if TL :
					return event.weight * event.TLratio
				else :
					return event.weight        
            else:
                return 0
        
    return myIsoWeight

sequence.append(delR)
sequence.append(frHybridIso)



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
	# if signals:
	#     T2tt_500_470.color = ROOT.kPink+6
	#     T2tt_375_365.color = ROOT.kAzure+1
	
	weight_ = lambda event, sample: event.weight*event.reweightHEM

	for sample in samples :
		sample.read_variables  = ['reweightPU/F', 'Pileup_nTrueInt/F','reweightLeptonSF/F', 'reweightBTag_SF/F','reweightL1Prefire/F','reweightnISR/F', 'reweightwPt/F',]
		sample.read_variables += ['reweightPU%s/F'%args.reweightPU if args.reweightPU != "Central" else "reweightPU/F"]
		pu_getter = operator.attrgetter('reweightPU' if args.reweightPU=='Central' else "reweightPU%s"%args.reweightPU)
		sample.weight         = lambda event, sample: event.tight * pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightnISR * event.reweightwPt * event.reweightLeptonSF
		sample.scale = lumi_scale 
		sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
		sample.style = styles.fillStyle(sample.color)
	
	for sample in prediction :
		sample.read_variables  = ['reweightPU/F', 'Pileup_nTrueInt/F','reweightLeptonSF/F', 'reweightBTag_SF/F','reweightL1Prefire/F','reweightnISR/F', 'reweightwPt/F',]
		sample.read_variables += ['reweightPU%s/F'%args.reweightPU if args.reweightPU != "Central" else "reweightPU/F"]
		pu_getter = operator.attrgetter('reweightPU' if args.reweightPU=='Central' else "reweightPU%s"%args.reweightPU)
		sample.weight         = lambda event, sample: event.loose * event.TLratio * pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightnISR * event.reweightwPt * event.reweightLeptonSF
		sample.scale = lumi_scale 
		sample.setSelectionString([getFilterCut(isData=False, year=year, skipBadPFMuon=args.noBadPFMuonFilter, skipBadChargedCandidate=args.noBadChargedCandidateFilter, skipVertexFilter = True), getLeptonSelection(mode)])
		sample.style = styles.fillStyle(sample.color,alpha=0.3)
	
	
	#stack_ = Stack( samples )
	# stack_ = Stack( samples, data_sample ) 
	stack_ = Stack( samples, data_sample, prediction ) 
	# stack_ = Stack( samples, data_sample, prediction ) 
	#stack_ = Stack( samples, data_sample, T2tt_375_365, T2tt_500_470 )

	
	if args.small:
		for sample in samples + [data_sample] + signals + prediction:
			sample.normalization = 1.
			sample.reduceFiles( factor = 40 )
			sample.scale /= sample.normalization

	# Use some defaults
	Plot.setDefaults(stack = stack_, weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper', histo_class=ROOT.TH1D)
	Plot2D.setDefaults( weight = (staticmethod(weight_)), selectionString = cutInterpreter.cutString(args.selection) )
	plots   = []
	plots2D = []

	plots.append(Plot(
		name = "tightHI_l1pt",
	    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_pt/F" ),
		# weight = lambda event, sample: event.tight * pu_getter(event) * event.reweightBTag_SF * event.reweightL1Prefire * event.reweightnISR * event.reweightwPt * event.reweightLeptonSF,
		# weight=IsoCutWeight(Tight=True, inclusive=False),

		binning=[10,0,50],
	  ))
	plots.append(Plot(
		name = "looseHI_l1pt",
	    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_pt/F" ),
		# weight = lambda event, sample: event.loose,
		# weight=IsoCutWeight(Tight=False, inclusive=False),
	    binning=[10,0,50],
	  ))
	plots.append(Plot(
		name = "pred_l1pt",
	    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events ',
	    attribute = TreeVariable.fromString( "l1_pt/F" ),
		# weight=IsoCutWeight(Tight=False, inclusive=False,TL=True),
	    binning=[10,0,50],
	  ))
	plots.append(Plot(
	    texX = 'log(1+HI)/log(1+5)', texY = 'Number of Events',
	    name = 'hybridIsolation', attribute = lambda event, sample: log(1+(event.l1_relIso03*(min(event.l1_pt,25))))/log(1+5),
	    binning=[20,0,4],
	  ))
	plots.append(Plot(
	    texX = 'log(1+HI)/log(1+5)', texY = 'Number of Events',
	    name = 'hybridIsolationOwn', attribute = lambda event, sample: log(1+event.HI) / log(6),
	    binning=[20,0,4],
	  ))
	  
	plots.append(Plot(
	    name = 'yield', texX = 'yield', texY = 'Number of Events',
	    attribute = lambda event, sample: 0.5 + index ,
	    binning=[3, 0, 3],
	  ))

	# plots2D.append(Plot2D(
	# 	name = "All_Pt_Eta",
	# 	texX  = 'p_{T}', texY = "#eta",
	# 	stack = Stack ([samples[0]]),
	# 	attribute = (
	# 		lambda event, sample: event.l1_pt,
	# 		lambda event, sample: event.l1_eta,
	# 		),
	# 	binning = [10,0,50,6,-3,3],
	# 	weight=IsoCutWeight(Tight=True, inclusive=True)
	#   ))
	# plots2D.append(Plot2D(
	# 	name = "Tight_Pt_Eta",
	# 	texX  = 'p_{T}', texY = "#eta",
	# 	stack = Stack ([samples[0]]),
	# 	attribute = (
	# 		lambda event, sample: event.l1_pt,
	# 		lambda event, sample: event.l1_eta,
	# 		),
	# 	binning = [10,0,50,6,-3,3],
	# 	weight=IsoCutWeight(Tight=True, inclusive=False)
	#   ))
	# plots2D.append(Plot2D(
	# 	name = "Loose_Pt_Eta",
	# 	texX  = 'p_{T}', texY = "#eta",
	# 	stack = Stack ([samples[0]]),
	# 	attribute = (
	# 		lambda event, sample: event.l1_pt,
	# 		lambda event, sample: event.l1_eta,
	# 		),
	# 	binning = [10,0,50,6,-3,3],
	# 	weight=IsoCutWeight(Tight=False, inclusive=False)
	#   ))
	
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
	yields[mode]["QCD-predcited"] = sum(yields[mode][s.name] for s in prediction)
	# dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
	QCDScale        = yields[mode]["QCD-predcited"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
	dataMCScale = 1
	# drawPlots(plots, mode, dataMCScale)
	print "QCD scale {}".format(QCDScale)
	drawPlots(plots, mode, QCDScale)
	
	for plot in plots2D:
		plotting.draw2D(
				plot=plot,
				plot_directory=os.path.join(plot_directory, 'analysisPlots', args.targetDir, args.era ,mode+"log",args.selection) ,
				logX = False, logY = False, logZ = True,
				drawObjects = drawObjects( True, float('nan')),
				)

	allPlots[mode] = plots

	# ffile = ROOT.TFile("PtEtaMap_{}.root".format(mode),"RECREATE")
	# plots2D[0].histos[0][0].Write("PtEtaMap")
	# plots2D[1].histos[0][0].Write("PtEtaMapTight") # tight hybrid iso
	# plots2D[2].histos[0][0].Write("PtEtaMapLoose") # loose hybrid iso

	# ffile.Close()

# Add the different channels into all	
# yields['all'] = {}
# for y in yields[allModes[0]]:
# 	try:	yields['all'][y] = sum(yields[c][y] for c in (['mu','e']))
# 	except: yields['all'][y] = 0
# # s = yields['all']["data"]/yields['all']["MC"] if yields['all']["MC"] != 0 else float('nan')
# dataMCScale = 1
# for plot in allPlots['mu']:
# 	for plot2 in (p for p in allPlots['e'] if p.name == plot.name): 
# 		for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
# 			for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
# 				if i==k:
# 					j.Add(l)
# drawPlots(allPlots['mu'], 'all', dataMCScale)

FR_file.Close()