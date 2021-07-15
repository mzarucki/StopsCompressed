# standard importd
import ROOT
import os
import pickle

# RootTools
from RootTools.core.standard import *

# argParser
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel', 
      action='store',
      nargs='?',
      choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],
      default='INFO',
      help="Log level for logging"
)
#argParser.add_argument('--signal',             action='store',      default=None,            nargs='?', choices=[None, "T2tt", "DM", "T8bbllnunu", "compilation"], help="Add signal to plot")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--overwrite',                               action='store_true',     help='Overwrite?', )
argParser.add_argument('--year',               action='store', type=int,      default=2016, choices = [2016, 2017, 2018])
#argParser.add_argument('--selection',          action='store',      default='lepSel-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1')
#argParser.add_argument('--plot_directory',     action='store',      default='v0p3')
args = argParser.parse_args()

# Logging
import Analysis.Tools.logger as logger
logger = logger.get_logger( "INFO", logFile=None)
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger( "INFO", logFile=None )

from StopsCompressed.Tools.genFilter import genFilter
genFilter = genFilter(year=args.year)
#Samples
if args.year == 2016:
    from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import *
    signals = [T2tt_500_490,T2tt_500_480,T2tt_500_470,T2tt_500_460,T2tt_500_450,T2tt_500_440,T2tt_500_430,T2tt_500_420, T2tt_375_365, T2tt_375_335] 
    from StopsCompressed.samples.nanoTuples_Summer16_postProcessed import *
    samples = [ WJetsToLNu_HT_16, Top_pow_16, DY_HT_LO_16, ZInv_16, singleTop_16 , QCD_HT_16, VV_16, TTX_16]
    from StopsCompressed.samples.nanoTuples_Run2016_17July2018_postProcessed import Run2016
    #samples = [ WJetsToLNu_HT_16 ]
    #samples = []
    lumiFac = 35.9
    data_sample = Run2016
elif args.year == 2017:
    from StopsCompressed.samples.nanoTuples_Fall17_postProcessed import *
    samples = [ WJetsToLNu_HT_16, TTLep_pow_16 , TTSingleLep_pow_16 , DY_HT_LO_16, ZInv_16, singleTop_16 , QCD_HT_16, VV_16, TTX_16]
    from StopsCompressed.samples.nanoTuples_Run2017_nanoAODv6_postProcessed import *
    #samples = [ WJetsToLNu_HT_16 ]
    lumiFac = 41.5
    data_sample = Run2017

logger.info( "Loaded data for year %i", args.year )
#allsamples = samples + [data_sample]
allsamples = signals 
if args.small:
    for sample in allsamples:
        sample.reduceFiles( to = 1)


cuts=[
  ("no cuts",			          "no cuts",				     "(1)"),
  #("l1_Prompt",				  "$l1_isPrompt>0$",			     "l1_isPrompt>0"),
  ("MET>200",                            "$E_{T}^{miss}>200$",                       "met_pt>200"),
  ("HT>300",                             "$H_{T}>300$",                              "HT>300"),
  ##change HT>400, nISR>=1, l1_eta<1.5, CT1>300, l1_charge=-1 for SR1
  (">=1 ISR Jet",                         "n_{ISR}>=1",                              "nISRJets>=1"),
  #("l1_Prompt",				  "$l1_isPrompt>0$",			     "l1_isPrompt>0"),
  #("l1_Prompt",				  "$l1_isPrompt>0$",			     "l1_isPrompt>0"),
  ("dphij0j1<2.5",                        "$dphiJets<2.5$rad",                       "dphij0j1<2.5"),
  #("3Jet Veto ",                       	  "$3^{rd}$ Jet Veto mod",                  "(nJetGood<=2||Alt$(JetGood_pt[2],0)<60)"),
  ("nHardJetsTo2",			  "n_{HardJets}<=2",			     "Sum$(JetGood_pt>=60&&abs(Jet_eta)<2.4)<=2"),
  ("tau Veto",                            "$n_{Tau}==0$",                            "nGoodTaus==0"),
  ("N(lep)>=1",				  "$n_{lep}>=1$",			     "nlep>=1"),
  (" l1_pt>0 ",                 	  "$l1(p_{T})>0 $",       		     "l1_pt>0"),
  (" (lep_pt>20)<=2 ",            	  "$(nlep_{pt}>20)<=1$",       		     "Sum$(lep_pt>20)<=2"),
  ("l1_pt<30",				  "$l_{1} p_{t}<30$",			     "l1_pt<30"),
  ("bjets = 0",				  "$n_{bJets}=0$",			     "nBTag==0"),
  ("CT1>300",                             "$CT_{1}>300$",                            "CT1>300"),
  ("abs(l1_eta)<1.5",                     "$|l1_{eta}|<1.5$",                        "abs(l1_eta)<1.5"),
  ("CT1<400",                             "$CT_{1}<400$",                            "CT1<400"),
  #("l1 charge = -1",                      "$l1_{charge}=-1$",                        "l1_charge==-1"),
  #("CT1>400",                             "$CT_{1}>400$",                            "CT1>400"),
  #("HT>300",                             "$H_{T}>300$",                              "HT>300"),
  #("abs(l1_eta)<2.4",                     "$|l1_{eta}|<2.4$",                        "abs(l1_eta)<2.4"),
  #("ISR Jet Pt>325",                      "$ISR_{pt}>325$",                          "ISRJets_pt>325"),
  #("sofbjets>=1,nHardbjets = 0",	  "$n_{softbJets}>=1 and n_{HardbJets}=0$",  "nSoftBJets>=1&&nHardBJets==0"),
  #("CT2>300",                             "$CT_{2}>300$",                            "CT2>300"),
  ##("CT2<400",                             "$CT_{2}<400$",                            "CT2<400"),
  #("CT2>400",                             "$CT_{2}>400$",                            "CT2>400"),
  #("mt<60",				  "$m_{T}<60$",			    	     "mt<60"),
  #("60<mt<95",				  "$60<m_{T}<95$",			     "mt<=95&&mt>=60"),
  ("mt>95",				  "$m_{T}>95$",			      	     "mt>95"),


  #("sofbjets,nHardbjets = 0",		  "$n_{softbJets}=0 and n_{HardbJets}=0$",  "nSoftBJets==0&&nHardBJets==0"),
  #(" (lep_pt>20)<=2,l1_pt>0 ",            "$(nlep_{pt}>20)<=1,l1(p_{T})>0 $",       "Sum$(lep_pt>20)<=2&&l1_pt>0"),
  #("electrons",				  "abs(l1_pdgId)==11",			    "abs(l1_pdgId)==11"),
  #("muons",				  "abs(l1_pdgId)==13",			    "abs(l1_pdgId)==13"),
  #("Ele channel",			  "$nGoodMuons==0&&nGoodElectrons>=1$",	    "nGoodMuons==0&&nGoodElectrons>=1"),
  #("1== nJet",				  "$nJet ==1$",				    "nJetGood ==1"),
  #("l1_pt<50",				  "$l_{1} p_{t}<50$",			    "l1_pt<50"),
  #("mt>=150",				  "$m_{T}>=150$",			    "mt>=150"),
    ]

path = "/users/priya.hussain/www/StopsCompressed/www/cutFlow/%i/signalT2tt"%args.year
if not os.path.exists( path ):
    os.makedirs(path)

prefix = 'small_' if args.small else ''

cutFlowFile = os.path.join( path, prefix+'cutFlow_%i.tex'%args.year  )
pklFile = os.path.join( path, prefix+'cutFlow_%i.pkl'%args.year  )
print cutFlowFile
if not os.path.exists(pklFile) or args.overwrite:
    values={}
    for i_cut, cut in enumerate(cuts):
        values[i_cut]={}
	for sample in allsamples :
	    if "Run" in sample.name :
		    weight_string = 'weight*reweightHEM'
		    values[i_cut][sample.name] = sample.getYieldFromDraw(selectionString = "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]]), weightString = weight_string)['val'] 
	    elif "T2tt" in sample.name:
		    mStop= int(sample.name.split('_')[1])
		    mNeu= int(sample.name.split('_')[2])
		    genEff = genFilter.getEff(mStop,mNeu)
		    #print "signal name: ",sample.name, "mStop: ", mStop, "mNeu: ", mNeu,"genEff: " ,genEff
		    #sample.read_variables += [ 'reweight_nISR/F']
		    weight_string = 'weight*reweightBTag_SF*reweightL1Prefire*reweightLeptonSF*reweight_nISR'
		    selectionString = "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]])
		    values[i_cut][sample.name] = genEff*lumiFac*sample.getYieldFromDraw(selectionString = "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]]), weightString = weight_string)['val']

	    else:
		    weight_string = 'weight*reweightHEM*reweightBTag_SF*reweightL1Prefire*reweightwPt*reweightLeptonSF'
		    values[i_cut][sample.name] = lumiFac*genEff*sample.getYieldFromDraw(selectionString = "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]]), weightString = weight_string)['val'] 

       #logger.debug("I had a problem here: %s", "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]]) )

    pickle.dump( values, file(pklFile,'w'))
    logger.info("Written values to pklFile %s", pklFile)
else:
    values = pickle.load(file(pklFile))
    logger.info("Loaded values from pklFile %s", pklFile)
    


#cutFlowFile =f'/afs/hephy.at/user/p/phussain/www/stopsDilepton/analysisPlots/2016/ {args.year}cutflowmod.tex'

with open(cutFlowFile, "w") as cf:

    cf.write("\\begin{tabular}{r|"+"|l"*len(allsamples)+"} \n")
    cf.write( 30*" "+"& "+ " & ".join([ "%13s"%s.texName for s in allsamples ] )+"\\\\\\hline\n" )
    print 30*" "+ "".join([ "%13s"%s.name for s in allsamples ] )

    for i in range(len(cuts)):
        r=[]
        for s in allsamples:
            #selection = "&&".join(c[2] for c in cuts[:i+1])
            #selection = "&&".join(c[2] for c in cuts)
            #if selection=="":selection="(1)"

            y = values[i][s.name]
            #n = s.getYieldFromDraw( selection, '(1)')
            r.append(y)
        cf.write("%30s"%cuts[i][1]+ "& "+" & ".join([ " %12.2f"%r[j] for j in range(len(r))] )+"\\\\\n")
        print "%30s"%cuts[i][0]+ "".join([ " %12.2f"%r[j] for j in range(len(r))] )

    cf.write("\\end{tabular} \n")
    if args.year == 2016:
        cf.write("\\2016{ Cutflow.} \n")
    elif args.year == 2017:
        cf.write("\\2017{ Cutflow.} \n")
    else:
        cf.write("\\2018{ Cutflow.} \n")


