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


#Samples
if args.year == 2016:
    from StopsCompressed.samples.nanoTuples_Summer16_postProcessed import *
    samples = [TTLep_pow_16 , TTSingleLep_pow_16 , DY_HT_LO_16, singleTop_16 , WJetsToLNu_HT_16 , VV_16, TTX_16]
    #samples = [ WJetsToLNu_HT_16 ]
    lumiFac = 35.9

logger.info( "Loaded data for year %i", args.year )


if args.small:
    for sample in samples:
        sample.reduceFiles( to = 1)

#weight_string = 'weight*reweightLeptonTrackingSF*reweightBTag_SF*reweightLeptonSF*reweightDilepTrigger*reweightPU*reweightL1Prefire'
weight_string = 'weight' 


cuts=[
  ("lepton selection",                "$n_{\\textrm{lep.}==1}$",              "Sum$(lep_pt>20)<=1&&l1_pt>0"),
  ("ISR Jet",                         "n_{ISR}==1",                           "nISRJets==1"),
  ("tau Veto",                        "$n_{Tau}==0$",                         "nGoodTaus==0"),
  ("dphij0j1<2.5",                    "$dphiJets<2.5$rad",                    "dphij0j1<2.5"),
  ("3Jet Veto",                       "$3^{rd}$ Jet Veto",                    "(nJetGood<=2||JetGood_pt[2]<60 )"),
  ("MET>200",                         "$$E_{T}^{miss}>200$",                  "met_pt>=200"),
  ("HT>300",                          "$H_{T}>300$",                          "HT>=300"),
    ]

path = "/afs/hephy.at/user/p/phussain/www/stopsCompressed/analysisPlots/cutFlow/v01/%i"%args.year
if not os.path.exists( path ):
    os.makedirs(path)

prefix = 'small_' if args.small else ''

cutFlowFile = os.path.join( path, prefix+'cutFlow_%i.tex'%args.year  )
pklFile = os.path.join( path, prefix+'cutFlow_%i.pkl'%args.year  )

if not os.path.exists(pklFile) or args.overwrite:
    values={}
    for i_cut, cut in enumerate(cuts):
        values[i_cut]={}
        for sample in samples:
            values[i_cut][sample.name] = lumiFac*sample.getYieldFromDraw(selectionString = "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]]), weightString = weight_string)['val'] 
       #logger.debug("I had a problem here: %s", "&&".join([ '('+c[2]+')' for c in cuts[:i_cut+1]]) )

    pickle.dump( values, file(pklFile,'w'))
    logger.info("Written values to pklFile %s", pklFile)
else:
    values = pickle.load(file(pklFile))
    logger.info("Loaded values from pklFile %s", pklFile)
    


#cutFlowFile =f'/afs/hephy.at/user/p/phussain/www/stopsDilepton/analysisPlots/2016/ {args.year}cutflowmod.tex'

with open(cutFlowFile, "w") as cf:

    cf.write("\\begin{tabular}{r|"+"|l"*len(samples)+"} \n")
    cf.write( 30*" "+"& "+ " & ".join([ "%13s"%s.texName for s in samples ] )+"\\\\\\hline\n" )
    print 30*" "+ "".join([ "%13s"%s.name for s in samples ] )

    for i in range(len(cuts)):
        r=[]
        for s in samples:
            #selection = "&&".join(c[2] for c in cuts[:i+1])
            #selection = "&&".join(c[2] for c in cuts)
            #if selection=="":selection="(1)"

            y = values[i][s.name]
            #n = s.getYieldFromDraw( selection, '(1)')
            r.append(y)
        cf.write("%30s"%cuts[i][1]+ "& "+" & ".join([ " %12.1f"%r[j] for j in range(len(r))] )+"\\\\\n")
        print "%30s"%cuts[i][0]+ "".join([ " %12.1f"%r[j] for j in range(len(r))] )

    cf.write("\\end{tabular} \n")
    if args.year == 2016:
        cf.write("\\2016{ Cutflow.} \n")
    elif args.year == 2017:
        cf.write("\\2017{ Cutflow.} \n")
    else:
        cf.write("\\2018{ Cutflow.} \n")


