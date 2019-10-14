''' FWLite example
'''
# Standard imports
import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False

# example file
events = Events(['file:/afs/hephy.at/work/r/rschoefbeck/CMS/tmp/CMSSW_10_2_12_patch1/src/SUS-RunIIAutumn18FSPremix-00052.root'])

# Use 'edmDumpEventContent <file>' to list all products. Then, make a simple dictinary as below for the products you want to read.
# These are the PF rechit collections:
#vector<reco::PFRecHit>                "particleFlowRecHitECAL"    "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitHBHE"    "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitHF"      "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitHO"      "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitPS"      "Cleaned"         "reRECO" 

# miniAOD
#products = {
#    'pfCands':{'type':'vector<pat::PackedCandidate>', 'label':"packedPFCandidates"},
#    'pfJets':{'type':'vector<pat::Jet>', 'label': ("slimmedJets")},
#    'pfMet':{'type':'vector<pat::MET>','label':( "slimmedMETs" )},
#    'electrons':{'type':'vector<pat::Electron>','label':( "slimmedElectrons" )},
#    'muons':{'type':'vector<pat::Muon>', 'label':("slimmedMuons") },
#}

# RECO
edmCollections = { 
'genParticles':{'type':'vector<reco:GenParticle>', 'label': ( "genParticles", "", "RECO" ) },
#'jets':{'type':'vector<pat::Jet>', 'label': ( "slimmedJets" ) },
#    'pfMet':        { 'label':('pfMet'), 'type':'vector<reco::PFMET>'},
    #'pfRecHitsHBHE':{ 'label':("particleFlowRecHitHBHE"), 'type':"vector<reco::PFRecHit>"},
    #'caloRecHits':  { 'label':("reducedHcalRecHits"), 'type':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
#    'clusterHCAL':  {  'label': "particleFlowClusterHCAL", "type":"vector<reco::PFCluster>"},
#    'pf':           { 'label':('particleFlow'), 'type':'vector<reco::PFCandidate>'},
   #'ecalBadCalibFilter':{'label':( "ecalBadCalibFilter",  "", "USER"), 'type':'bool'}
 
   }

# add handles
for k, v in edmCollections.iteritems():
    v['handle'] = Handle(v['type'])

nevents = 1 if small else events.size()

for i in range(nevents):
  events.to(i)

  eaux  = events.eventAuxiliary()

  # run/lumi/event
  run   = eaux.run()
  event = eaux.event()
  lumi  = eaux.luminosityBlock()

  #read all products as specifed in edmCollections
  products = {}
  for k, v in edmCollections.iteritems():
    events.getByLabel(v['label'], v['handle'])
    products[k] = v['handle'].product()

  print run,lumi,event
  for p in products['genParticles']:
    if abs(p.pdgId()) in [11, 13 ] and p.status()==1:
        print p.pdgId(), p.pt(), p.eta(), p.phi() 


#  #print RecHits
#  for i, cl in enumerate(products["clusterHCAL"]):
#    print "cluster   n %i E %3.2f"%(i, cl.energy())
#  #for i, rh in enumerate(products["caloRecHits"]):
#  #  print "caloRechit n %i E %3.2f"%(i, rh.energy())
