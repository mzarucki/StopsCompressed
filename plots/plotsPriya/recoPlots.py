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
argParser.add_argument('--targetDir',          action='store',      default='v02_log')

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)


#Plotting directory
#path = '/afs/hephy.at/user/p/phussain/www/stopsCompressed/v01/reco/'

if args.small: args.targetDir += "_small"
plot_directory = os.path.join(plot_directory,'reco', args.targetDir)
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
if args.small:
    for s in sample:
        s.reduceFiles( to = 10 )
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
]

##writing lep variables
#lepVars         = ['pt/F','eta/F','phi/F','pdgId/I','cutBased/I','miniPFRelIso_all/F','pfRelIso03_all/F','dxy/F','dz/F','charge/I','mediumId/I','eleIndex/I','muIndex/I']
#lepVarNames     = [x.split('/')[0] for x in lepVars]

##new variables to be used
#new_variables = ['nlep/I','nGoodMuons/I', 'nGoodElectrons/I', 'nGoodLeptons/I','l1_pt/F', 'l1_eta/F', 'l1_phi/F', 'l1_pdgId/I', 'l1_index/I','l1_miniRelIso/F', 'l1_relIso03/F', 'l1_dxy/F', 'l1_dz/F','l1_eleIndex/I', 'l1_muIndex/I','l2_pt/F', 'l2_eta/F', 'l2_phi/F', 'l2_pdgId/I', 'l2_index/I','l2_miniRelIso/F', 'l2_relIso03/F', 'l2_dxy/F', 'l2_dz/F','l2_eleIndex/I', 'l2_muIndex/I','isEE/I', 'isMuMu/I', 'isEMu/I', 'isOS/I'] 



## Define a reader
def makeLeptons( event, sample ):
    electrons = getElectrons( event )

    #electrons = filter( eleSelector, electrons)
    #muons     = filter( muSelector, muons)

    muons_     = getMuons( event )
    muons      = filter (muSelector, muons_)
    leptons = electrons + muons

    #print leptons
    #print muons

    leptons.sort(key = lambda p:-p['pt'])
    
    ##fill_vector_collection( event, "lep", lepVarNames, leptons) #thinking about it 
    event.nlep = len(leptons)
    if len(muons) > 1 and event.nlep >= 1:
        dl1.Fill(abs(muons[0]['dxy']))
        dl2.Fill(abs(muons[1]['dxy']))
        d2.Fill(abs(muons[0]['dxy']),abs(muons[1]['dxy'])) 
        #print event.nlep , leptons[0]['dxy']
    else: pass
sequence = [makeLeptons]
i = 0
for s in sample:
    sname = s.name
    dl1 = ROOT.TH1F('1stmuon dxy','Impact Parameter of 1st muon',50,0.0,1.5)
    dl2 = ROOT.TH1F('2ndmuon dxy','Impact Parameter of 1st muon',50,0.0,1.5)
    d2 = ROOT.TH2F('dxy','Impact Parameters of leptons in dilepton state (13 TeV); first lepton d0[cm]; 2nd lepton d0[cm]',50,0.0,1.0,50,0.0,1.0)
    r = s.treeReader( \
        variables = read_variables ,
        #selectionString = "&&".join(skimConds)
        sequence = sequence,
        )

    r.start()
    while r.run():
        i += 1
        pass
    plotl1 = Plot.fromHisto(name = "1st_muon_dxy_%s_10"%sname, histos = [[dl1]], texX = "dxy of 1st muon (cm)", texY = "Number of events" )
    plotl2 = Plot.fromHisto(name = "2nd_muon_dxy_%s_10"%sname, histos = [[dl2]], texX = "dxy of 2nd muon(cm)", texY = "Number of events" )
    plot1 = Plot2D.fromHisto(name = "dxy_of_Muons_%s_2D_10"%sname, histos = [[d2]], texX = "dxy 1st muon (cm)", texY = "dxy 2nd muon(cm)" )
    plotting.draw(plotl1, plot_directory = plot_directory, logX = False, logY = True, sorting = False, ratio = None, drawObjects = drawObjects( False )  )
    plotting.draw(plotl2, plot_directory = plot_directory, logX = False, logY = True, sorting = False, ratio = None ,drawObjects = drawObjects( False ) )
    plotting.draw2D(plot1, plot_directory = plot_directory, logX = False, logY = False,logZ = True , drawObjects = drawObjects( False ))
