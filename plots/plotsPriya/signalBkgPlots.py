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

def drawObjects( plotData ):
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
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

#def eleSelector( p ):
#    return p['pt']>5 and abs(p['eta'])<2.4 and p['miniPFRelIso_all']<0.1

def muSelector( p ):
    return p['pt']>5 and abs(p['eta'])<2.4 and p['miniPFRelIso_all']<0.2

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
#defining variables for the leptons in dilep
electronVars = [ 'pt', 'eta','phi', 'pdgId', 'dxy', 'dz', 'charge', 'miniPFRelIso_all', 'pfRelIso03_all']
muonVars = [ 'pt', 'eta','phi', 'pdgId', 'dxy', 'dz', 'charge', 'miniPFRelIso_all', 'pfRelIso03_all', 'mediumId']

def getMuons(c, collVars=muonVars):
    return [getObjDict(c, 'Muon_', collVars, i) for i in range(int(getVarValue(c, 'nMuon')))]
def getElectrons(c, collVars=electronVars):
    return [getObjDict(c, 'Electron_', collVars, i) for i in range(int(getVarValue(c, 'nElectron')))]

#variables to be read from Tree
read_variables = [ \
    TreeVariable.fromString('nElectron/I'), 
    VectorTreeVariable.fromString('Electron[pt/F,eta/F,phi/F,pdgId/I,cutBased/I,miniPFRelIso_all/F,pfRelIso03_all/F,dxy/F,dz/F,charge/I]'),
    TreeVariable.fromString('nMuon/I'),
    VectorTreeVariable.fromString('Muon[pt/F,eta/F,phi/F,pdgId/I,mediumId/O,miniPFRelIso_all/F,pfRelIso03_all/F,sip3d/F,dxy/F,dz/F,charge/I]'),
    TreeVariable.fromString('genWeight/F'),
    TreeVariable.fromString('nJet/I'),
    VectorTreeVariable.fromString('Jet[pt/F,eta/F,phi/F]')
]

#make a sequence for your leptons selection
sequence = []
def makeLeptons( event, sample ):
    electrons = getElectrons( event )

    #electrons = filter( eleSelector, electrons)
    #muons     = filter( muSelector, muons)

    muons_     = getMuons( event )
    muons      = filter (muSelector, muons_)

    leptons = electrons + muons
    leptons.sort(key = lambda p:-p['pt'])
    
    event.nlep = len(leptons)
    event.mu1 = -999
    event.mu2 = -999
    if len(muons) > 1 and event.nlep >= 1:
        event.mu1 = abs(muons[0]['dxy'])
        event.mu2 = abs(muons[1]['dxy'])
        #d2.Fill(abs(muons[0]['dxy']),abs(muons[1]['dxy'])) 
    else: pass
sequence.append(makeLeptons)#def makeweight (event, sample):

def makeweight (event, sample):
    #print event.genWeight 
    if "TTLep" in sample.name:
        event.weight = ((sample.xSection*1000)/ sample.normalization)* event.genWeight
        print sample.xSection, sample.normalization, event.genWeight
        #print event.weight, sample.name
    elif "Displ" in sample.name:
        event.weight = ((24.8*1000)/ sample.normalization)* event.genWeight
        print sample.name,  sample.normalization , event.genWeight
        #print event.weight, sample.name
sequence.append(makeweight)
weight_TT   = '((87.315047712*1000)/4635769526.2) * 72.6983032227'
weight_0p01 = '((24.8*1000)/223923)'
weight_0p1  =' ((24.8*1000)/164370)'
#for s in sample:
#    if "TTLep" in s.name:
#        print s.name, s.getYieldFromDraw(selectionString='Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&abs(Muon_dxy)>0.1)==2',weightString = weight_TT)['val']
#    elif s.name == 'DisplacedStops_mStop_250_ctau_0p01':
#        print s.name, s.getYieldFromDraw(selectionString='Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&abs(Muon_dxy)>0.1)==2',weightString = weight_0p01)['val']
#    elif s.name == 'DisplacedStops_mStop_250_ctau_0p1':
#        print s.name, s.getYieldFromDraw(selectionString='Sum$(Muon_pt>5&&abs(Muon_eta)<2.4&&Muon_miniPFRelIso_all<.2&&abs(Muon_dxy)>0.1)==2',weightString = weight_0p1)['val']
    #s.weight = lambda event,sample: event.weight
    #print s.weight
        
#sequence = [makeLeptons]
i = 0

weight_ = lambda event, sample: event.weight

stack = Stack( TTLep_pow, DisplacedStops_mStop_250_ctau_0p01 , DisplacedStops_mStop_250_ctau_0p1)

Plot.setDefaults(stack = stack, weight=staticmethod( weight_ ), histo_class=ROOT.TH1D)
plots = []
plots.append(Plot( name = "1st_muon_dxy", texX = "dxy of 1st muon (cm)", texY = "Number of events", attribute = lambda event, sample: event.mu1, binning=[100,0.0,10.0]),)
plots.append(Plot( name = "2nd_muon_dxy", texX = "dxy of 2nd muon (cm)", texY = "Number of events", attribute = lambda event, sample: event.mu2, binning=[100,0.0,10.0]),)

plotting.fill(plots, read_variables = read_variables, sequence = sequence, max_events=1)

#for plot in plots:
#    plotting.draw(plot, plot_directory = plot_directory, logX = False, logY = True, sorting = False, ratio = None, drawObjects = drawObjects( False )  )
