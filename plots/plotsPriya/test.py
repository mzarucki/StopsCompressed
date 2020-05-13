''' FWLite example
'''
# Standard imports
import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import sqrt
small = False
#from RootTools.core.standard import *
#s2 = FWLiteSample.fromDAS("stops2l","/Stops2l/schoef-Stops2l-393b4278a04aeb4c6106d6aae1db462e/USER",instance = 'phys03',prefix='root://hephyse.oeaw.ac.at/', maxN = 1) 
# example file
#events = Events(['file:/afs/hephy.at/work/r/rschoefbeck/CMS/tmp/CMSSW_10_2_12_patch1/src/SUS-RunIIAutumn18FSPremix-00052.root'])
#events = Events(['file:/afs/hephy.at/work/p/phussain/backup/CMSSW_10_2_12_patch1/src/StopsCompressed/Generation/cfg/SUS-RunIIAutumn18FSPremix-00052.root'])
events = Events(['file:/afs/hephy.at/data/cms07/StopsCompressed/fwlite_signals_fastSim/small_2k_test.root'])
# Use 'edmDumpEventContent <file>' to list all products. Then, make a simple dictinary as below for the products you want to read.
# These are the PF rechit collections:
#vector<reco::PFRecHit>                "particleFlowRecHitECAL"    "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitHBHE"    "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitHF"      "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitHO"      "Cleaned"         "reRECO"   
#vector<reco::PFRecHit>                "particleFlowRecHitPS"      "Cleaned"         "reRECO" 


# RECO
edmCollections = { 
'muons':{'type':'vector<reco:Muon>', 'label': ( "muons", "", "RECO" ) },
'genParticles':{'type':'vector<reco:GenParticle>', 'label': ( "genParticles", "", "RECO" ) },
'inclusiveSecondaryVertices':{'type':'vector<reco:Vertex>', 'label': ( "inclusiveSecondaryVertices", "", "RECO" ) },
'offlinePrimaryVerticesWithBS':{'type':'vector<reco:Vertex>', 'label': ( "offlinePrimaryVerticesWithBS", "", "RECO" ) },
'inclusiveCandidateSecondaryVertices':{'type':'vector<reco:VertexCompositePtrCandidate>', 'label': ( "inclusiveCandidateSecondaryVertices", "", "RECO" ) },
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
histo = ROOT.TH1F("histo","Stops Transverse decay length (13 TeV);Lxy[cm];number of events",10,0.04,0.05)
histol = ROOT.TH1F("histol","Leptons Transverse decay length (13 TeV);Lxy[cm];number of events",50,0.0,0.2)
histo.Sumw2()
histol.Sumw2()
canvas= ROOT.TCanvas("canvas", "Stops decay length ", 1000, 600)
mothers = []
#while r.run():
for i in range(nevents):
  events.to(i)
  #runs.add(r.evt[0])
  eaux  = events.eventAuxiliary()
  #genparticles = r.event.genParticles
  #muons = r.event.muons
  #secondaryVertices = r.event.inclusiveSecondaryVertices
  #primaryVertices = r.event.offlinePrimaryVerticesWithBS
  #incSecondaryVertices = r.event.inclusiveCandidateSecondaryVertices
  #print genparticles.size() 
  #print muons.size() 
  #print secondaryVertices.size() 
  #print primaryVertices.size() 
  #print incSecondaryVertices.size()
#  # run/lumi/event
  run   = eaux.run()
  event = eaux.event()
  lumi  = eaux.luminosityBlock()
  #print r.event.evt, r.event.lumi, r.event.run
#
  #read all products as specifed in edmCollections
  products = {}
  for k, v in edmCollections.iteritems():
    events.getByLabel(v['label'], v['handle'])
    products[k] = v['handle'].product()
  for m in muons:
    v = m.vertex()
    print "Lxy", v.rho(),"v.x",v.x(), "v.y",v.y(),"pdgId", m.pdgId() , "phi", m.phi(), "pt", m.pt()
#
#  print run,lumi,event
#  for p in genparticles:
#   #if abs(p.pdgId()) in [11, 13 ] and p.status()==1:
#   #if abs(p.pdgId()) in [11, 13,15] and p.status()==1:
#    if abs(p.pdgId()) in [11, 13 ] and p.status()==1:
#        print p.pdgId(), p.pt(), p.eta(), p.phi()
#        m = p.mother()
#        print "mother of lepton", m.pdgId()
#        while abs(m.pdgId()) != 2212:
#            if abs(m.pdgId()) != 1000006:
#                m = m.mother()
#                print "mother particle pdgId", m.pdgId()
#            else:
#                print "should be a stop", m.pdgId()
#                v = m.vertex()
#                
#                break
    #    #v = p.vertex()
    #    #print "Lxy", v.rho()
    #  #  d = p.daughter(0)
    #  #  print "daughter pdgId", d.pdgId()
      #  m = p.mother()
      #  print "mother pdgId", m.pdgId()
      #  if abs(m.pdgId()) >37 and abs(m.pdgId()) <1000 : continue
      #  else:
      #      print"lepton coming from W",  m.pdgId()
      #      gm = m.mother()
      #      if abs(gm.pdgId()) != 1000006 or abs(gm.pdgId()) != 24: continue
      #      else:
      #          print "W coming from stop", gm.pdgId()
      #          v = p.vertex()
      #          x= v.x()
      #          y= v.y()
      #          lc = sqrt((x*x)+(y*y))
      #          ll= v.rho()
      #          gv= gm.vertex()
      #          gx= gv.x()
      #          gy= gv.y()
      #          lsc= sqrt((gx*gx)+(gy*gy))
      #          ls= gv.rho()
      #          print "lxy of leptons", ll, "lxy computed", lc
      #          print "lxy of stopss", ls, "lxy computed stops", lsc
      #          histol.Fill(ll)
      #  while abs(m.pdgId()) != 2212:
      #      if abs(m.pdgId()) != 1000006:
      #          if abs(m.pdgId()) != 24: continue
      #          m = m.mother()
      #          print "mother particles",m.pdgId()
      #      else:
      #          print "should be a b quark",m.pdgId(), m.pt() 
       #         vp = p.vertex()
       #         vm = m.vertex()
       #         print "Lxy of the stop vertex", vm.rho(), "Lxy of leptons", vp.rho()
       #         print "dx of the stop vertex", vm.x(), "dx of leptons", vp.x()
       #         break
   # elif abs(p.pdgId()) == 1000006:
   #     print p.pdgId()
   #     v = p.vertex()
   #     print "Lxy of stops", v.rho()
   #     l = v.rho()
   #     print l
   #     histo.Fill(l) 
   #     break
#histo.Draw('E')
#histo.GetEntries()
#scale = 1 / histol.Integral()
#histo.Scale(scale)
#histol.Scale(scale)
#histol.Draw()
#canvas.Print('/afs/hephy.at/user/p/phussain/www/histoleptonleptondecay.png')
#histo.Draw('E')
#histo.Draw()
#canvas.Print('/afs/hephy.at/user/p/phussain/www/histo2.png')       
#  #print RecHits
#  for i, cl in enumerate(products["clusterHCAL"]):
#    print "cluster   n %i E %3.2f"%(i, cl.energy())
#  #for i, rh in enumerate(products["caloRecHits"]):
#  #  print "caloRechit n %i E %3.2f"%(i, rh.energy())
