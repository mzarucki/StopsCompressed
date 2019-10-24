''' FWLite example
'''
# Standard imports
import ROOT, os
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import pi, sqrt, sin, cos
small = False
from Analysis.Tools.GenSearch import *
from RootTools.core.standard import *
from StopsCompressed.samples.signals import *

from StopsCompressed.tools.user import plot_directory
signal = fwlite_signals_fastSim_Stops2l_200k                   # fwlite_signals_DisplacedStops_250_200                       #fwlite_signals_fastSim_Stops2l_200k #fwlite_signals_DisplacedStops_500_0p2
print "loading files"
path = '/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest'
if not os.path.exists( path ):
    os.makedirs(path)
# example file
#events = Events(['file:/afs/hephy.at/work/r/rschoefbeck/CMS/tmp/CMSSW_10_2_12_patch1/src/SUS-RunIIAutumn18FSPremix-00052.root'])
#events = Events(['file:/afs/hephy.at/work/p/phussain/backup/CMSSW_10_2_12_patch1/src/StopsCompressed/Generation/cfg/SUS-RunIIAutumn18FSPremix-00052.root'])
#events = Events(['file:/afs/hephy.at/data/cms07/StopsCompressed/fwlite_signals_fastSim/small_2k_test.root'])
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

def dxy(x, y, px, py):
    ''' calculating impact parameters '''
    IP = abs((y*px) - (x*py)) / sqrt(px**2 + py**2)
    print "dxy is", IP
    return IP

def deltaPhi(phi1, phi2):
    dphi = phi2 - phi1
    if  dphi > pi:
        #print "dphi>pi"
        dphi -= 2.0*pi
    if dphi <= -pi:
        dphi += 2.0*pi
    return abs(dphi)

def deltaR(phi1,eta1,phi2,eta2):
    dR = deltaPhi(phi1,phi2)**2 + (eta2 - eta1)**2
    delR = sqrt(dR)
    #print  "deltaR between particles(stops)", dR
    return delR


histo   = ROOT.TH1F("histo","Stops Transverse decay length (13 TeV);Lxy[cm];number of events",500,0.00,10.0)
histodphi   = ROOT.TH1F("histodphi","delta phi between stops (13 TeV);dphi;number of events",50,0.0,4.00)
histolepdphi   = ROOT.TH1F("histolepdphi","delta phi between leptons (13 TeV);dphi;number of events",50,0.0,4.00)
histol  = ROOT.TH1F("histol","Leptons Transverse decay length (13 TeV);Lxy[cm];number of events",50,0.0,0.2)
histot  = ROOT.TH1F("histot","Proper time of stops (13 TeV);proper time[cm];number of events",50,0.0,0.09)
histotn = ROOT.TH1F("histotn","Proper time of stops with neutralinos (13 TeV);proper time[cm];number of events",1000,0.0,100.0)
histopt = ROOT.TH1F("histopt","Transverse Momentum of Leptons (13 TeV);pT[GeV];number of events",50,0.0,50.0)
histostopspt = ROOT.TH1F("histostopspt","Transverse Momentum of Stops (13 TeV);pT[GeV];number of events",100,0.0,700.0)
histonlpt = ROOT.TH1F("histonlpt","Transverse Momentum of Neutralinos (13 TeV);pT[GeV];number of events",100,0.0,700.0)
histonpt = ROOT.TH1F("histonpt","Transverse Momentum of Neutrinos (13 TeV);pT[GeV];number of events",50,0.0,100.0)
histod0 = ROOT.TH1F("histod0","Impact Parameters of leptons (13 TeV);d0[cm];number of events",50,0.0,10.0)
canvasl= ROOT.TCanvas("canvasl", "Stops decay length ", 1000, 600)
#nevents = 1
r = signal.fwliteReader(products = edmCollections)
r.start()
runs = set()
i = 0
while r.run():
  #print r.event.evt, r.event.lumi, r.event.run
  genparticles = r.event.genParticles
  i += 1
  stops = []
  leptons = []

#  print run,lumi,event
  for p in genparticles:
    g = GenSearch(p)
    #if abs(p.pdgId()) in [11, 13 ] and p.status()==1:
    #if abs(p.pdgId()) in [11, 13,15] and p.status()==1:
    if abs(p.pdgId()) == 1000006 and g.isLast(p): # and p.status() == 22 and g.isLast(p):
        daughters = g.daughters(p)
        #print [ds.pdgId() for ds in daughters]
        #if 24 in [abs(ds.pdgId()) for ds in daughters]:
        for ds in daughters:
            if abs(ds.pdgId()) == 24 and g.isLast(ds): 
                daughter=g.daughters(ds)
                #print "w coming from stop",ds.pdgId()
                for d in daughter:
                    #print d.pdgId()
                    if abs(d.pdgId()) in [11,13,12,14]  and g.isFirst(d):
                        #print "leptons coming from W coming from a stop", d.pdgId()
                        if abs(d.pdgId()) in [11,13]:
                            ptl = d.pt()
                            #print "electron,muon", d.pdgId()
                            histopt.Fill(ptl) 
                            v = d.vertex()
                            x = v.x()
                            y = v.y()
                            phil= d.phi()
                            px = ptl * cos (phil)
                            py = ptl * sin (phil)
                            IP = dxy(x,y,px,py)
                            #print 'impact parameter is', IP
                            histod0.Fill(IP)
                            lep = {"phi": d.phi() , "eta":d.eta()}
                            leptons.append(lep)
                        else:
                            npt= d.pt()
                            #print "neutrino", d.pdgId(), d.pt()
                            histonpt.Fill(npt)
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
            nlpt= p.pt()
            histonlpt.Fill(nlpt)
            #print "should be a neutralino", p.pdgId(), p.pt()
            lc = ln - ls
            l = sqrt((nx-sx)**2 + (ny-sy)**2)
            smass = m.mass()
            #print histotn
            tn = (smass * l) / spt
            histotn.Fill(float(tn))
            histo.Fill(l)
            histostopspt.Fill(spt)
            #print "stops proper time", tn, "decay length of stops", l
            #print "Lxy from neutralino" , vn.rho(), "mass of stop", m.pdgId(), m.mass(), m.pt() 
    elif abs(p.pdgId()) == 1000006 and p.status() == 22:
        stop = {"phi":p.phi(), "eta":p.eta()}
        stops.append(stop)
        v= p.vertex()
        #print "stops: ",p.pdgId(), "pt: ", p.pt(), "phi:" ,p.phi(), "eta: ", p.eta()
  DR = deltaR(stops[0]["phi"], stops[0]["eta"], stops[1]["phi"],stops[1]["eta"])
  dphi = deltaPhi(stops[0]["phi"], stops[1]["phi"] )
  histodphi.Fill(dphi)
  if len(leptons) == 2:
        dphilep = deltaPhi(leptons[0]["phi"],leptons[1]["phi"])
        #print "deltphi of leptons", dphilep
        histolepdphi.Fill(dphilep)
  if i% 1000==0:
    print "1000 events passed"
#  if i ==100:
#    break  
#print  "Found the following run(s): %s", ",".join(str(run) for run in runs)
#scale = 1 / histol.Integral()
scales = 1 / histo.Integral()
scaletn = 1 / histotn.Integral()
scaledphi = 1 / histodphi.Integral()
scalelepdphi = 1 / histolepdphi.Integral()
scaled0 = 1 / histod0.Integral()
scalept = 1 / histopt.Integral()
scalenlpt = 1 / histonlpt.Integral()
scalenpt = 1 / histonpt.Integral()
scalestopspt = 1 / histostopspt.Integral()
#
#histo.Scale(scales)
#histo.Draw()
#histo.GetYaxis().SetLogy()
#myPad=canvasl.GetPad(1)
#canvasl.SetLogy()
#histo.GetMean()
#canvasl.Modified()
#canvasl.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/histostops_ctau200_small.png')
#canvasl.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/histostops_ctau200_small.root')
#
#canvast= ROOT.TCanvas("canvast", "Stops proper time ", 1000, 600)
#histotn.Scale(scaletn)
#histotn.Draw()
#canvast.SetLogy()
#histotn.GetMean()
#print "RMS is" ,histotn.GetRMS()
#print "Mean is", histotn.GetMean()
#canvast.Modified()
#canvast.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/histotime_ctau200_small.png')
#canvast.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/histotime_ctau200_small.root')
#
#canvasd0= ROOT.TCanvas("canvasd0", "ImpactParameter ", 1000, 600)
#histod0.Scale(scaled0)
#histod0.Draw()
#histod0.GetMean()
#canvasd0.SetLogy()
#canvasd0.Modified()
#canvasd0.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtestImpactParameter_ctau200_small.png')
#canvasd0.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/ImpactParameter_ctau200_small.root')
#
#canvaspt= ROOT.TCanvas("canvaspt", "Leptons pt ", 1000, 600)
##histopt.GetYaxis().SetLogy()
#histopt.Scale(scalept)
#histopt.Draw()
#histopt.GetMean()
#canvaspt.SetLogy()
#canvaspt.Modified()
#canvaspt.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/leptonspT_ctau200_small.png')
#canvaspt.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/leptonspT_ctau200_small.root')
#
#canvasnlpt= ROOT.TCanvas("canvasnlpt", "Neutralinos pt ", 1000, 600)
##histopt.GetYaxis().SetLogy()
#histonlpt.Scale(scalenlpt)
#histonlpt.Draw()
#histonlpt.GetMean()
#canvasnlpt.SetLogy()
#canvasnlpt.Modified()
#canvasnlpt.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/neutralinospT_ctau200_small.png')
#canvasnlpt.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/neutralinospT_ctau200_small.root')
#
#canvasnpt= ROOT.TCanvas("canvasnpt", "Neutrinos pt ", 1000, 600)
##histon.GetYaxis().SetLogy()
#histonpt.Scale(scalenpt)
#histonpt.Draw()
#histonpt.GetMean()
#canvasnpt.SetLogy()
#canvasnpt.Modified()
#canvasnpt.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/neutrinopT_ctau200_small.png')
#canvasnpt.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/neutrinopT_ctau200_small.root')
#
#canvasstopspt= ROOT.TCanvas("canvasstopspt", "Stops pt ", 1000, 600)
##histostopspt.GetYaxis().SetLogy()
#histostopspt.Scale(scalestopspt)
#histostopspt.Draw()
#histostopspt.GetMean()
#canvasstopspt.SetLogy()
#canvasstopspt.Modified()
#canvasstopspt.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/stopspT_ctau200_small.png')
#canvasstopspt.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/stopspT_ctau200_small.root')

canvasdphistop= ROOT.TCanvas("canvasdphistop", "deltaphi between Stops ", 1000, 600)
histodphi.Scale(scaledphi)
histodphi.Draw()
histodphi.GetMean()
canvasdphistop.SetLogy()
canvasdphistop.Modified()
canvasdphistop.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/stops_dphi_200k.png')
canvasdphistop.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/stops_dphi_200k.root')

canvaslepdphi= ROOT.TCanvas("canvaslepdphi", "deltaphi between Leptons", 1000, 600)
histolepdphi.Scale(scalelepdphi)
histolepdphi.Draw()
histolepdphi.GetMean()
canvaslepdphi.SetLogy()
canvaslepdphi.Modified()
canvaslepdphi.Print('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/leptons_dphi_200k.png')
canvaslepdphi.SaveAs('/afs/hephy.at/user/p/phussain/www/stopsCompressed/vtest/leptons_dphi_200k.root')


#histo.Draw('E')
#histo.Draw()
#canvas.Print('/afs/hephy.at/user/p/phussain/www/histo2.png')       
