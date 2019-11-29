''' Plot script for signal and background plots for dilepton compressed
'''

# Standard imports
import ROOT, os, array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import pi, sqrt, sin, cos, atan2
from RootTools.core.standard import *
from StopsCompressed.tools.user         import plot_directory

#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v01_log')

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)


#Plotting directory
#path = '/afs/hephy.at/user/p/phussain/www/stopsCompressed/v01/reco/'

if args.small: args.targetDir += "_small"
plot_directory = os.path.join(plot_directory,'reco', args.targetDir, 'signal_bkg')
if not os.path.exists( plot_directory ):
    os.makedirs(plot_directory)
    logger.info( "Created plot directory %s", plot_directory )

# Text on the plots
#
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextSize(0.04)
tex.SetTextAlign(11) # align right

# importing background samples
from Samples.nanoAOD.Autumn18_private_legacy_v1 import TTLep_pow
from Samples.nanoAOD.Autumn18_private_legacy_v1 import DisplacedStops_mStop_250_ctau_0p01
from Samples.nanoAOD.Autumn18_private_legacy_v1 import DisplacedStops_mStop_250_ctau_0p1

#define the sample
sample = [TTLep_pow] + [DisplacedStops_mStop_250_ctau_0p01] + [DisplacedStops_mStop_250_ctau_0p1] 
TTLep_pow.style = styles.lineStyle(ROOT.kRed)
DisplacedStops_mStop_250_ctau_0p01.style = styles.lineStyle(ROOT.kBlue)
DisplacedStops_mStop_250_ctau_0p1.style = styles.lineStyle(ROOT.kGreen)
if args.small:
    for s in sample:
        s.reduceFiles( to = 1 )
        #print s.normalization
##defining variables for the leptons in dilep
#electronVars = [ 'pt', 'eta','phi', 'pdgId', 'dxy', 'dz', 'charge', 'miniPFRelIso_all', 'pfRelIso03_all']
#muonVars = [ 'pt', 'eta','phi', 'pdgId', 'dxy', 'dz', 'charge', 'miniPFRelIso_all', 'pfRelIso03_all', 'mediumId']
#
#variables to be read from Tree
read_variables = [ \
    TreeVariable.fromString('nElectron/I'), 
    VectorTreeVariable.fromString('Electron[pt/F,eta/F,phi/F,pdgId/I,cutBased/I,miniPFRelIso_all/F,pfRelIso03_all/F,dxy/F,dz/F,charge/I]'),
    TreeVariable.fromString('nMuon/I'),
    VectorTreeVariable.fromString('Muon[pt/F,eta/F,phi/F,pdgId/I,mediumId/O,miniPFRelIso_all/F,pfRelIso03_all/F,sip3d/F,dxy/F,dz/F,charge/I]'),
    TreeVariable.fromString('genWeight/F'),
    TreeVariable.fromString('nJet/I'),
    VectorTreeVariable.fromString('Jet[pt/F,eta/F,phi/F]'),
    TreeVariable.fromString('MET_pt/F'),
]

#weight_TT   = '((87.315047712*1000)/4635769526.2) * 72.6983032227 * 138.4'
#weight_0p01 = '((24.8*1000)/223923)* 138.4'
#weight_0p1  =' ((24.8*1000)/164370)* 138.4'
weight_TT   = '((87.315047712*1000)/4635769526.2) * 72.6983032227 '
weight_0p01 = '((24.8*1000)/223923)'
weight_0p1  =' ((24.8*1000)/164370)'
#print weight_TT , weight_0p01 , weight_0p1
#nmuon = 'Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&abs(Muon_dxy)>0.1)'
nmuon = 'Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2)'
nisr   = 'Sum$(Jet_pt>100)'
MET    = 'MET_pt>250'
for nLep in [0,1,2]:
    for nisrJet in [0,1]:
        print "nLep", nLep, "nisrJet", nisrJet
        for s in sample:
            selectionString =  nmuon+">=%i"%nLep+"&&"+nisr+">=%i"%nisrJet+"&&"+MET
            print "selection: ", selectionString 
            #print "nLep", nLep, "nisrJet", nisrJet
            if "TTLep" in s.name:
                print s.name , s.getYieldFromDraw()['val'], "0"
                print s.name , s.getYieldFromDraw(selectionString= selectionString, weightString = weight_TT)['val'], "selection and weights"
                print s.name , s.getYieldFromDraw(selectionString= selectionString)['val'], "no weights"
                print s.name , s.getYieldFromDraw( weightString = weight_TT)['val'], "only weights"
            elif s.name == 'DisplacedStops_mStop_250_ctau_0p01':
                print s.name , s.getYieldFromDraw()['val'], "0"
                print s.name , s.getYieldFromDraw(selectionString= selectionString, weightString = weight_0p01)['val'], "selection and weights"
                print s.name , s.getYieldFromDraw(selectionString= selectionString)['val'], "no weights"
                print s.name , s.getYieldFromDraw( weightString = weight_0p01)['val'], "only weights"
            elif s.name == 'DisplacedStops_mStop_250_ctau_0p1':
                print s.name , s.getYieldFromDraw()['val'], "0"
                print s.name , s.getYieldFromDraw(selectionString= selectionString, weightString = weight_0p1)['val'], "selection and weights"
                print s.name , s.getYieldFromDraw(selectionString= selectionString)['val'], "no weights"
                print s.name , s.getYieldFromDraw( weightString = weight_0p1)['val'], "only weights"

#print s.name,"Di muon", s.getYieldFromDraw(selectionString='Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&abs(Muon_dxy)>0.1)==2',weightString = weight_0p1)['val']
#
#print s.name, "Single muon", s.getYieldFromDraw(selectionString='Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&abs(Muon_dxy)>0.1)==1',weightString = weight_0p1)['val']
        
