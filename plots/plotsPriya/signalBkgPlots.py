''' Plot script for signal and background plots for dilepton compressed
'''

# Standard imports
import ROOT, os, array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import pi, sqrt, sin, cos, atan2
from RootTools.core.standard import *
from StopsCompressed.Tools.user         import plot_directory

#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v11')#v08

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)


#Plotting directory
#path = '/afs/hephy.at/user/p/phussain/www/stopsCompressed/v01/reco/'

if args.small: args.targetDir += "_small"
plot_directory = os.path.join(plot_directory,'reco', args.targetDir, 'signal_bkg', 'wo_dxy0p1_inclusive_range')
if not os.path.exists( plot_directory ):
    os.makedirs(plot_directory)
    logger.info( "Created plot directory %s", plot_directory )

# Text on the plots
#
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextSize(0.04)
tex.SetTextAlign(11) # align right

def drawObjects( plotData ):
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation       L=138.4 fb{}^{-1}'), 
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def getVarValue(c, var, n=-1):
    try:
        att = getattr(c, var)
    except AttributeError:
        return float('nan')
    if n>=0:
#    print "getVarValue %s %i"%(var,n)
        if n<att.__len__():
            return att[n]
        else:
            return float('nan')
    return att

def getObjDict(c, prefix, variables, i):
    return {var: getVarValue(c, prefix+var, i) for var in variables}
def getCollection(c, prefix, variables, counter_variable):
    return [getObjDict(c, prefix+'_', variables, i) for i in range(int(getVarValue(c, counter_variable)))]

def eleSelector( p ):
    return p['pt']>5 and abs(p['eta'])<2.4 and p['miniPFRelIso_all']<0.2  #and abs(p['dxy'])>0.1

def muSelector( p ):
    return p['pt']>5 and abs(p['eta'])<2.4 and p['miniPFRelIso_all']<0.2 #and abs(p['dxy']) > 0.1

# importing background samples
from Samples.nanoAOD.Autumn18_private_legacy_v1 import TTLep_pow
from Samples.nanoAOD.Autumn18_private_legacy_v1 import TTSingleLep_pow, WJetsToLNu
from Samples.nanoAOD.Autumn18_private_legacy_v1 import DisplacedStops_mStop_250_ctau_0p01
from Samples.nanoAOD.Autumn18_private_legacy_v1 import DisplacedStops_mStop_250_ctau_0p1

#define the sample
sample = [TTLep_pow]+[TTSingleLep_pow] + [WJetsToLNu] + [DisplacedStops_mStop_250_ctau_0p01] + [DisplacedStops_mStop_250_ctau_0p1] 
#TTLep_pow.style = styles.errorStyle(ROOT.kRed)
#TTSingleLep_pow.style = styles.errorStyle(ROOT.kMagenta)
#WJetsToLNu.style = styles.errorStyle(ROOT.kMagenta)
#DisplacedStops_mStop_250_ctau_0p01.style = styles.errorStyle(ROOT.kBlue)
#DisplacedStops_mStop_250_ctau_0p1.style = styles.errorStyle(ROOT.kGreen)
TTLep_pow.style = styles.lineStyle(ROOT.kRed)
TTSingleLep_pow.style = styles.lineStyle(ROOT.kMagenta)
WJetsToLNu.style = styles.lineStyle(ROOT.kYellow)
DisplacedStops_mStop_250_ctau_0p01.style = styles.lineStyle(ROOT.kBlue)
DisplacedStops_mStop_250_ctau_0p1.style = styles.lineStyle(ROOT.kGreen)
if args.small:
    for s in sample:
        s.reduceFiles( to = 10 )
        #print s.normalization
#defining variables for the leptons in dilep
electronVars = [ 'pt', 'eta','phi', 'pdgId', 'dxy','dxyErr', 'dz', 'charge', 'miniPFRelIso_all', 'pfRelIso03_all', 'sip3d']
muonVars = [ 'pt', 'eta','phi', 'pdgId', 'dxy','dxyErr' ,'dz', 'charge', 'miniPFRelIso_all', 'pfRelIso03_all', 'mediumId','sip3d']

def getMuons(c, collVars=muonVars):
    return [getObjDict(c, 'Muon_', collVars, i) for i in range(int(getVarValue(c, 'nMuon')))]
def getElectrons(c, collVars=electronVars):
    return [getObjDict(c, 'Electron_', collVars, i) for i in range(int(getVarValue(c, 'nElectron')))]

#variables to be read from Tree
read_variables = [ \
    TreeVariable.fromString('nElectron/I'), 
    VectorTreeVariable.fromString('Electron[pt/F,eta/F,phi/F,pdgId/I,cutBased/I,miniPFRelIso_all/F,pfRelIso03_all/F,dxy/F,dxyErr/F,dz/F,charge/I, sip3d/F]'),
    TreeVariable.fromString('nMuon/I'),
    VectorTreeVariable.fromString('Muon[pt/F,eta/F,phi/F,pdgId/I,mediumId/O,miniPFRelIso_all/F,pfRelIso03_all/F,sip3d/F,dxy/F,dxyErr/F,dz/F,charge/I]'),
    TreeVariable.fromString('genWeight/F'),
    TreeVariable.fromString('nJet/I'),
    VectorTreeVariable.fromString('Jet[pt/F,eta/F,phi/F]'),
    TreeVariable.fromString('MET_pt/F'),
]

#make a sequence for your leptons selection
sequence = []
def makeLeptons( event, sample ):
    electrons_ = getElectrons( event )

    electrons = filter( eleSelector, electrons_)
    #muons     = filter( muSelector, muons)

    muons_     = getMuons( event )
    muons      = filter (muSelector, muons_)
    muons.sort(key = lambda p:-p['pt'])
    leptons = electrons + muons
    leptons.sort(key = lambda p:-p['pt'])
    event.all_muons = muons    
    event.nlep = len(leptons)
    event.mu1 = -999
    event.mu1pt = -999
    event.mu1sip3d = -999
    mu1IPsig = -999
    if len(muons) >= 1: 
        event.mu1 = abs(muons[0]['dxy'])
        event.mu1pt = abs(muons[0]['pt'])
        event.mu1sip3d = abs(muons[0]['sip3d'])
        if abs(muons[0]['dxyErr']) > 0: #and abs(muons[1]['dxyErr']) >0:
            event.mu1IPsig = abs(muons[0]['dxy']) / abs(muons[0]['dxyErr'])
sequence.append(makeLeptons)

def makeweight (event, sample):
    if "Displ" in sample.name:
        event.weight = ((24.8*1000)/ sample.normalization)* event.genWeight * 138.4
    else:
        event.weight = ((sample.xSection*1000)/ sample.normalization)* event.genWeight * 138.4
sequence.append(makeweight)
        
i = 0

weight_ = lambda event, sample: event.weight

stack = Stack( TTLep_pow, TTSingleLep_pow, WJetsToLNu , DisplacedStops_mStop_250_ctau_0p01 , DisplacedStops_mStop_250_ctau_0p1)

#Plot.setDefaults(stack = stack, weight=staticmethod( weight_ ),selectionString = 'Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2)>1', addOverFlowBin='upper' , histo_class=ROOT.TH1D)
#Plot.setDefaults(stack = stack, weight=staticmethod( weight_ ),selectionString = 'Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&(abs(Muon_dxy)>0.1))==2', addOverFlowBin='upper' , histo_class=ROOT.TH1D)
Plot.setDefaults(stack = stack, weight=staticmethod( weight_ ),)

plots = []
plots.append(Plot( name = "leading_muon_dxy", texX = "dxy of leading muon (cm)", texY = "Number of events", attribute = lambda event, sample: event.mu1, binning=[100,0.0,10.0]),)
#plots.append(Plot( name = "leading_muon_dxy_sig", texX = "dxy significance of leading muon ", texY = "Number of events", attribute = lambda event, sample: event.mu1IPsig, binning=[100,0.0,200.0]),)
plots.append(Plot( name = "leading_muon_sip3d", texX = "dxy significance(sip3D) of leading muon ", texY = "Number of events", attribute = lambda event, sample: event.mu1sip3d, binning=[100,0.0,200.0]),)
plots.append(Plot( name = "leading_muon_pt_dxy", texX = "pt of leding muon (GeV)", texY = "Number of events", attribute = lambda event, sample: event.mu1pt, binning=[120,0.0,60.0]),)
plots.append(Plot( name = "Met_pt", texX = "MET pt (GeV)", texY = "Number of events", attribute = TreeVariable.fromString( "MET_pt/F" ), binning=[50,0.0,400.0]),)

plots.append(Plot( name = "all_muons_dxy", texX = "dxy of all muons (cm)", texY = "Number of events", attribute = lambda event, sample: [ m['dxy'] for m in event.all_muons ], binning=[100,0.0,10.0]),)

#plots2D = []
#plots2D.append(Plot2D( name = "ctau_0p01_all_muons_dxy_vs_pt", texX = "dxy of all muons (cm)", texY = "pt of all muons", stack = Stack([DisplacedStops_mStop_250_ctau_0p01]), attribute =(lambda event, sample: [ m['dxy'] for m in event.all_muons ], lambda event, sample: [ m['pt'] for m in event.all_muons ]), binning=[100,0.0,5.0,120,0.0,60.0], weight= weight_ ))
#
#plot = plots + plots2D
#plotting.fill(plots , read_variables = read_variables, sequence = sequence, max_events=100)

plotting.fill(plots, read_variables = read_variables, sequence = sequence)

for plot in plots:
    plotting.draw(plot, plot_directory = plot_directory, logX = False, logY = True,  sorting = False, ratio = None, drawObjects = drawObjects( False )  )

#for plot2 in plots2D:
#    plotting.draw2D(plot2, plot_directory = plot_directory, logX = False, logY = True, logZ = True,zRange = (1,10**7), drawObjects = drawObjects( False )  )
