''' FWLite example
'''
# Standard imports
import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import sqrt
small = False
from RootTools.core.standard import *
s2 = FWLiteSample.fromDAS("stops2l","/Stops2l/schoef-Stops2l-393b4278a04aeb4c6106d6aae1db462e/USER",instance = 'phys03',prefix='root://hephyse.oeaw.ac.at/', maxN = 1)
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
'genParticles':{'type':'vector<reco:GenParticle>', 'label': ( "genParticles" ) },
#'jets':{'type':'vector<pat::Jet>', 'label': ( "slimmedJets" ) },
#    'pfMet':        { 'label':('pfMet'), 'type':'vector<reco::PFMET>'},
    #'pfRecHitsHBHE':{ 'label':("particleFlowRecHitHBHE"), 'type':"vector<reco::PFRecHit>"},
    #'caloRecHits':  { 'label':("reducedHcalRecHits"), 'type':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
#    'clusterHCAL':  {  'label': "particleFlowClusterHCAL", "type":"vector<reco::PFCluster>"},
#    'pf':           { 'label':('particleFlow'), 'type':'vector<reco::PFCandidate>'},
   #'ecalBadCalibFilter':{'label':( "ecalBadCalibFilter",  "", "USER"), 'type':'bool'}
 
   }

r = s2.fwliteReader(products = edmCollections)
r.start()

histo = ROOT.TH1F("histo","Stops Transverse decay length (13 TeV);Lxy[cm];number of events",50,0.00,1.0)
histol = ROOT.TH1F("histol","Leptons Transverse decay length (13 TeV);Lxy[cm];number of events",50,0.0,0.2)
histot = ROOT.TH1F("histot","Proper time of stops (13 TeV);proper time[cm];number of events",50,0.0,0.09)
histotn = ROOT.TH1F("histotn","Proper time of stops with neutralinos (13 TeV);proper time[cm];number of events",50,0.0,100.0)
histo.Sumw2()
histol.Sumw2()
histot.Sumw2()
canvasl= ROOT.TCanvas("canvasl", "Stops decay length ", 1000, 600)
mothers = []
#nevents = 1
runs = set()
while r.run():
  print r.event.evt, r.event.lumi, r.event.run
  genparticles = r.event.genParticles
  
#  print run,lumi,event
  for p in genparticles:
    #if abs(p.pdgId()) in [11, 13 ] and p.status()==1:
    #if abs(p.pdgId()) in [11, 13,15] and p.status()==1:
    if abs(p.pdgId()) in [11, 13 ] and p.status()==1:
        m = p.mother()
        #print "mother pdgId", m.pdgId()
        if abs(m.pdgId()) != 24 : continue
        else:
            #print"lepton coming from W",  m.pdgId()
            gm = m.mother()
            if abs(gm.pdgId()) != 1000006: continue
            else:
                #print "W coming from stop", gm.pdgId()
                v = p.vertex()
                x= v.x()
                y= v.y()
                lc = sqrt((x*x)+(y*y))
                ll= v.rho()
                m = gm.mass()
                pt = gm.pt()
                t = (pt * ll) / m
                #gv= gm.vertex()
                #ls= gv.rho()
                #print "lxy of leptons", ll, "lxy computed", lc
                histol.Fill(ll)
                histot.Fill(t)
                #print gm.pdgId(), p.pdgId(), gm.mass()

    elif abs(p.pdgId()) == 1000022 :
        m= p.mother()
        #print "neutralino pdgId", p.pdgId(),"mother pdgId", m.pdgId()
        if abs(m.pdgId()) != 1000006: continue
        else:
            vn = p.vertex()
            ln = vn.rho()
            nx = vn.x()
            ny = vn.y()
            vs = m.vertex()
            ls = vs.rho()
            sx = vs.x()
            sy = vs.y() 
            spt= m.pt()
            lc = ln - ls
            l = sqrt((nx-sx)**2 + (ny-sy)**2)
            smass = m.mass()
            tn = (spt * l) / smass
            histotn.Fill(tn)
            histo.Fill(l)
            #print "stops time", tn, "decay length of stops", l, lc
            #print "Lxy from neutralino" , vn.rho(), "mass of stop", m.pdgId(), m.mass(), m.pt() 
       # while abs(m.pdgId()) != 2212:
       #     if abs(m.pdgId()) != 1000006:
       #         if abs(m.pdgId()) != 24: continue
       #         m = m.mother()
       #         print "mother particles",m.pdgId()
       #     else:
       #         print "should be a b quark",m.pdgId(), m.pt() 
       #         vp = p.vertex()
       #         vm = m.vertex()
       #         print "Lxy of the stop vertex", vm.rho(), "Lxy of leptons", vp.rho()
       #         print "dx of the stop vertex", vm.x(), "dx of leptons", vp.x()
       #         break
   # if abs(p.pdgId()) == 1000006:
   #     print p.pdgId(), p.pt(), p.mass()
   #     v = p.vertex()
   #     print "Lxy of stops", v.rho()
   #     l = v.rho()
   #     print l
   #     t = (p.pt()* l )/ p.mass() 
   #     print "proper time",t
   #     histot.Fill(t) 
   #     break
#histo.Draw('E')
#histo.GetEntries()
print  "Found the following run(s): %s", ",".join(str(run) for run in runs)
scale = 1 / histol.Integral()
scales = 1 / histo.Integral()
scaletn = 1 / histotn.Integral()
##histo.Scale(scale)
#histotn.Scale(scale)
#histotn.Draw()
#histotn.GetMean()
histo.Scale(scales)
histo.Draw()
#histo.GetMean()
canvasl.Print('/afs/hephy.at/user/p/phussain/www/histostops2k.png')
canvast= ROOT.TCanvas("canvast", "Stops proper time ", 1000, 600)

histotn.Scale(scaletn)
histotn.Draw()
histotn.GetMean()
print "RMS is" ,histotn.GetRMS()
print "Mean is", histotn.GetMean()
canvast.SaveAs('/afs/hephy.at/user/p/phussain/www/histotimetry2k.png')
#histo.Draw('E')
#histo.Draw()
#canvas.Print('/afs/hephy.at/user/p/phussain/www/histo2.png')       
