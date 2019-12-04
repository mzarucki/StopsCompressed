''' FWLite example
'''
# Standard imports
import ROOT, os, array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import pi, sqrt, sin, cos, atan2
small = False
from Analysis.Tools.GenSearch import *
from RootTools.core.standard import *

from StopsCompressed.tools.user import plot_directory
#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='eff_v03test')
#argParser.add_argument('--signal',       action='store',      default='fwlite_signals_fastSim_Stops2l_200k',choices=['fwlite_signals_DisplacedStops_250_0p001','fwlite_signals_DisplacedStops_250_0p01','fwlite_signals_DisplacedStops_250_0p1','fwlite_signals_DisplacedStops_250_0p2','fwlite_signals_DisplacedStops_250_200'], help='generated signal samples we get plots for')

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

from StopsCompressed.samples.signals import *

sample = fwlite_signals_DisplacedStops_250_0p1 #fwlite_signals_DisplacedStops_250_200 #fwlite_signals_fastSim_Stops2l_200k #fwlite_signals_DisplacedStops_500_0p2

#if args.small: sample.name += "_small"
if args.small:
    plot_directory = os.path.join(plot_directory,'gen', args.targetDir, sample.name, 'small')
else:
    plot_directory = os.path.join(plot_directory,'gen', args.targetDir, sample.name)
if not os.path.exists( plot_directory ):
    os.makedirs(plot_directory)
    logger.info( "Created plot directory %s", plot_directory )
print "loading files"
print sample.name
#if args.small:
#        sample.reduceFiles( to = 1 )
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
products = {
#    'pfCands':{'type':'vector<pat::PackedCandidate>', 'label':"packedPFCandidates"},
#    'pfJets':{'type':'vector<pat::Jet>', 'label': ("slimmedJets")},
#    'pfMet':{'type':'vector<pat::MET>','label':( "slimmedMETs" )},
#    'electrons':{'type':'vector<pat::Electron>','label':( "slimmedElectrons" )},
    'muons':{'type':'vector<pat::Muon>', 'label':("slimmedMuons") },
}

# RECO
edmCollections = { 
'muons':{'type':'vector<reco:Muon>', 'label': ( "muons", "", "RECO" ) },
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
    #print "dxy is", IP
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

def MET_dilep(n1_px,n1_py,n2_px,n2_py,nl1_px,nl1_py,nl2_px,nl2_py):
    MET_dilep = sqrt( (n1_px+n2_px+nl1_px+nl2_px)**2 + (n1_py+n2_py+nl1_py+nl2_py)**2)
    MET_dilep_phi = atan2( (n1_px+n2_px+nl1_px+nl2_px) , (n1_py+n2_py+nl1_py+nl2_py))
    #print "MET for dilep decay", MET_dilep
    return MET_dilep, MET_dilep_phi

def MET_semilep(n1_px,n1_py,nl1_px,nl1_py,nl2_px,nl2_py):
    MET_semilep = sqrt( (n1_px+nl1_px+nl2_px)**2 + (n1_py+nl1_py+nl2_py)**2)
    MET_semilep_phi = atan2( (n1_px+nl1_px+nl2_px) , (n1_py+nl1_py+nl2_py))
    #print "MET for semilep decay", MET_dilep
    return MET_semilep, MET_semilep_phi

def MET_chi(nl1_px,nl1_py,nl2_px,nl2_py):
    MET_chi = sqrt( (nl1_px+nl2_px)**2 + (nl1_py+nl2_py)**2)
    MET_chi_phi = atan2( (nl1_px+nl2_px) , (nl1_py+nl2_py))
    #print "MET for semilep decay", MET_dilep
    return MET_chi, MET_chi_phi

histomud0 = ROOT.TH1F("histomud0","Impact Parameters of reco muons (13 TeV);d0[cm];number of events",50,0.0,50.0)
histomulxy = ROOT.TH1F("histomulxy","Transverse decay length of reco muons (13 TeV); Lxy[cm];number of events",50,0.0,100.0)
histogenmud0 = ROOT.TH1F("histogenmud0","Impact Parameters of gen muons (13 TeV);d0[cm];number of events",50,0.0,50.0)
histogenmulxy = ROOT.TH1F("histogenmulxy","Transverse decay length of gen muons (13 TeV); Lxy[cm];number of events",50,0.0,100.0)
histo2Dgenmu = ROOT.TH2F("histo2Dgenmu","Impact Parameter and transverse decay length of gen muons (13 TeV);  d0 gen muons[cm]; gen_Lxy [cm]",50,0.0,50.0,50,0.0,100.0)
histo2Drecomu = ROOT.TH2F("histo2Drecomu","Impact Parameter and transverse decay length of matched RECO muons(13 TeV);  d0 reco muons[cm]; reco Lxy [cm]",50,0.0,50.0,50,0.0,100.0)
histo2Dallrecomu = ROOT.TH2F("histo2Dallrecomu","Impact Parameter and transverse decay length of all RECO muons(13 TeV);  d0 reco muons[cm]; reco Lxy [cm]",50,0.0,50.0,50,0.0,100.0)
histo2Dmatchmu = ROOT.TH2F("histo2Dmatchmu","Impact Parameter and transverse decay length of RECO(matched) muons(13 TeV);  gen_d0 muons[cm]; gen_Lxy [cm]",50,0.0,50.0,50,0.0,100.0)
histo2Dmatchgen = ROOT.TH2F("histo2Dmatchgen","Impact Parameter and transverse decay length of RECO(matched) with gen muons(13 TeV);  gen_d0 muons[cm]; gen_Lxy [cm]",50,0.0,50.0,50,0.0,100.0)
histo2D = ROOT.TH2I("histo2D", "number of gen vs reco muons; gen muons;reco muons", 2,0,2,2,0,2)
#histoeff = ROOT.TEfficiency ("histoeff","Efficiency Reco vs gen muons (13 TeV);  d0 [cm]; Lxy [cm]",50,0.0,50.0,50,0.0,100.0)
#histod02D = ROOT.TH2F("histod02D","Impact Parameters of leptons in dilepton state (13 TeV); first lepton d0[cm]; 2nd lepton d0[cm]",50,0.0,200.0,50,0.0,200.0)
#graph = ROOT.TGraph(50)
#canvasl= ROOT.TCanvas("canvasl", "Stops decay length ", 1000, 600)
#nevents = 1
r = sample.fwliteReader(products = edmCollections)
r.start()
runs = set()
d0l1=array.array('d')
d0l2=array.array('d')
i = 0

while r.run():
  #print r.event.evt, r.event.lumi, r.event.run
  genparticles = r.event.genParticles
  muons = r.event.muons
  i += 1
 

 # gen_mu = [ g for g in r.event.genParticles if g.status()==1 and abs(g.pdgId()) == 13]
 # reco_mu = [m for m in r.event.muons if m.pt()>5 and m.isolationR03().sumPt+m.isolationR03().emEt+m.isolationR03().hadEt < 0.15*m.pt()]

 # for m in reco_mu:
 #     for gm in gen_mu:
 #         if deltaR( m.phi(), m.eta(), gm.phi(), gm.eta() )<0.2:
 #             m.gen_gen_match = gm
 #             print "Found gen_match"
 #             assert False, ""
 #             break
        
  gen_mu = []
  reco = [] 
  matched_muon = []
  matched_gen = []
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
                            v = d.vertex()
                            x = v.x()
                            y = v.y()
                            phil= d.phi()
                            px = ptl * cos (phil)
                            py = ptl * sin (phil)
                            IP = dxy(x,y,px,py)
                            #print 'impact parameter is', IP
                            #if abs(d.pdgId()) == 13 and abs(d.eta())<2.1 and d.pt() > 5:
                            if abs(d.pdgId()) == 13:
                                #print d.phi()
                                gmu = {"phi": d.phi(), "eta": d.eta(), "Lxy": v.rho(), "d0": IP}
                                gen_mu.append(gmu)
                                histogenmud0.Fill(IP)
                                histogenmulxy.Fill(v.rho())
                                histo2Dgenmu.Fill(IP,v.rho()) 
                                #print "gen d0", IP, "gen Lxy", v.rho()
  for gmu in range(len(gen_mu)):
    phigmu = gen_mu[gmu]["phi"]
    etagmu = gen_mu[gmu]["eta"]
    d0gmu  = gen_mu[gmu]["d0"]
    Lxygmu = gen_mu[gmu]["Lxy"]
    for rm in muons:
        phirmu = rm.phi()
        etarmu = rm.eta()
        vrmu = rm.vertex()
        xrmu = vrmu.x()
        yrmu = vrmu.y()
        lrmu = vrmu.rho()
        ptrmu = rm.pt()
        pxrmu= ptrmu * cos(phirmu)
        pyrmu= ptrmu * cos(phirmu)
        IPrmu= dxy(xrmu,yrmu,pxrmu,pyrmu)
        dR = deltaR( phirmu, etarmu, phigmu, etagmu ) 
        if dR < 0.3:
            if gmu not in matched_gen:
                histo2Dmatchgen.Fill(d0gmu , Lxygmu)
            matched_gen.append(gmu)        

  for m in muons:
    #if abs(m.eta())<2.1 and m.pt() > 5 and m.isolationR03().sumPt+m.isolationR03().emEt+m.isolationR03().hadEt < 0.15*m.pt():
    vmu= m.vertex()
    #print i , "reco muon"
    reco_phi = m.phi()
    reco_eta = m.eta()
    for gm in range(len(gen_mu)):
        gen_phi = gen_mu[gm]["phi"]
        gen_eta = gen_mu[gm]["eta"]
        gen_d0 = gen_mu[gm]["d0"]
        gen_Lxy = gen_mu[gm]["Lxy"]
        xmu= vmu.x()
        ymu= vmu.y()
        lmu= vmu.rho()
        phimu= m.phi()
        ptmu= m.pt()
        pxmu= ptmu * cos(phimu)
        pymu= ptmu * cos(phimu)
        IPmu= dxy(xmu,ymu,pxmu,pymu)
        histo2Dallrecomu.Fill(IPmu,lmu) 
        dR = deltaR( m.phi(), m.eta(), gen_phi, gen_eta )
        if dR<0.3:
            #print "gen d0", gen_d0, "gen Lxy", gen_Lxy, "reco Lxy", vmu.rho(), "dR between gena nd reco", dR
            histomud0.Fill(IPmu)
            histomulxy.Fill(lmu)
            histo2Drecomu.Fill(IPmu,lmu)
            if gen_Lxy not in matched_muon:
                #print "matched d0", gen_d0, "matched Lxy", gen_Lxy
                histo2Dmatchmu.Fill(gen_d0,gen_Lxy)
            matched_muon.append(gen_Lxy) #using gen Lxy reduces any other gen muon with same Lxy, because we have dilepton cases #Fix it!!
            reco.append(m)
  #print "reco muons matched", len(reco), "gen muons", len(gen_mu)
  histo2D.Fill(len(gen_mu),len(reco))
  
  #print len(MET)
#  if i% 1000==0:
#    print "1000 events passed"
  if args.small:
      print "number of event", i
      if i == 5000:
        break  
#print  "Found the following run(s): %s", ",".join(str(run) for run in runs)
#scale = 1 / histol.Integral()
scalegend0 = 1 / histogenmud0.Integral()
scalegenlxy = 1 / histogenmulxy.Integral()
#scale2Dgen = 1 / histo2Dgenmu.Integral()
scaled0 = 1 / histomud0.Integral()
scalelxy = 1 / histomulxy.Integral()
#scale2Dmu = 1 / histo2Dmu.Integral()

canvasd0= ROOT.TCanvas("canvasd0", "Impact parameter reco  muons ", 1000, 600)
histomud0.Scale(scaled0)
histomud0.Draw()
myPad=canvasd0.GetPad(1)
canvasd0.SetLogy()
histomud0.GetMean()
canvasd0.Modified()
canvasd0.Print(os.path.join(plot_directory,'ImpactParameter_reco.png'))
canvasd0.SaveAs(os.path.join(plot_directory,'ImpactParameter_reco.root'))

canvasgend0= ROOT.TCanvas("canvasgend0", "Impact parameter gen  muons ", 1000, 600)
histogenmud0.Scale(scalegend0)
histogenmud0.Draw()
myPad=canvasgend0.GetPad(1)
canvasgend0.SetLogy()
histogenmud0.GetMean()
canvasgend0.Modified()
canvasgend0.Print(os.path.join(plot_directory,'ImpactParameter_gen.png'))
canvasgend0.SaveAs(os.path.join(plot_directory,'ImpactParameter_gen.root'))


canvaslxy= ROOT.TCanvas("canvaslxy", "Transverse decay length reco  muons ", 1000, 600)
histomulxy.Scale(scalelxy)
histomulxy.Draw()
myPad=canvaslxy.GetPad(1)
canvaslxy.SetLogy()
histomulxy.GetMean()
canvaslxy.Modified()
canvaslxy.Print(os.path.join(plot_directory,'Lxy_reco.png'))
canvaslxy.SaveAs(os.path.join(plot_directory,'Lxy_reco.root'))


canvasgenlxy= ROOT.TCanvas("canvasgenlxy", "Transverse Decay length gen  muons ", 1000, 600)
histogenmulxy.Scale(scalegenlxy)
histogenmulxy.Draw()
myPad=canvasgenlxy.GetPad(1)
canvasgenlxy.SetLogy()
histogenmulxy.GetMean()
canvasgenlxy.Modified()
canvasgenlxy.Print(os.path.join(plot_directory,'Lxy_gen.png'))
canvasgenlxy.SaveAs(os.path.join(plot_directory,'Lxy_gen.root'))

canvas2Dgen= ROOT.TCanvas("canvas2Dgen", "Impact Parameter and Lxy of gen muons", 1000, 600)
#histo2Dgenmu.Scale(scale2Dgen)
histo2Dgenmu.Draw("COLZ")
histo2Dgenmu.GetMean()
canvas2Dgen.SetLogz()
canvas2Dgen.Print(os.path.join(plot_directory,'ImpactParameterLxy_gen.png'))
canvas2Dgen.SaveAs(os.path.join(plot_directory,'ImpactParameterLxy_gen.root'))

canvas2Drecomu= ROOT.TCanvas("canvas2Drecomu", "Impact Parameter and Lxy of reco muons", 1000, 600)
#histo2Dmu.Scale(scale2Dmu)
histo2Drecomu.Draw("COLZ")
histo2Drecomu.GetMean()
canvas2Drecomu.SetLogz()
canvas2Drecomu.Print(os.path.join(plot_directory,'ImpactParameterLxy_reco.png'))
canvas2Drecomu.SaveAs(os.path.join(plot_directory,'ImpactParameterLxy_reco.root'))

canvas2Dallrecomu= ROOT.TCanvas("canvas2Dallrecomu", "Impact Parameter and Lxy of ALL reco muons", 1000, 600)
histo2Dallrecomu.Draw("COLZ")
histo2Dallrecomu.GetMean()
canvas2Dallrecomu.SetLogz()
canvas2Dallrecomu.Print(os.path.join(plot_directory,'ImpactParameterLxy_ALLreco.png'))
canvas2Dallrecomu.SaveAs(os.path.join(plot_directory,'ImpactParameterLxy_ALLreco.root'))

canvas2Dmu= ROOT.TCanvas("canvas2Dmu", "Impact Parameter and Lxy of matched reco muons", 1000, 600)
#histo2Dmu.Scale(scale2Dmu)
histo2Dmatchmu.Draw("COLZ")
histo2Dmatchmu.GetMean()
canvas2Dmu.SetLogz()
canvas2Dmu.Print(os.path.join(plot_directory,'ImpactParameterLxy_matched_reco.png'))
canvas2Dmu.SaveAs(os.path.join(plot_directory,'ImpactParameterLxy_matched_reco.root'))


canvas2Dmugenmatch= ROOT.TCanvas("canvas2Dmugenmatch", "Impact Parameter and Lxy of matched reco muons with gen", 1000, 600)
#histo2Dmu.Scale(scale2Dmu)
histo2Dmatchgen.Draw("COLZ")
histo2Dmatchgen.GetMean()
canvas2Dmugenmatch.SetLogz()
canvas2Dmugenmatch.Print(os.path.join(plot_directory,'ImpactParameterLxy_matched_reco_w_gen.png'))
canvas2Dmugenmatch.SaveAs(os.path.join(plot_directory,'ImpactParameterLxy_matched_reco_w_gen.root'))

canvas2D= ROOT.TCanvas("canvas2D", "gen and reco muons", 1000, 600)
#histo2Dmu.Scale(scale2Dmu)
histo2D.Draw("COLZ")
histo2D.GetMean()
canvas2D.SetLogz()
canvas2D.Print(os.path.join(plot_directory,'gen_reco_muons.png'))
canvas2D.SaveAs(os.path.join(plot_directory,'gen_reco_muons.root'))

canvaseff = ROOT.TCanvas("canvaseff", "Efficiency of reco and gen muons", 1000, 600)
histoeff = ROOT.TEfficiency(histo2Dmatchmu,histo2Dgenmu)
histoeff.Draw("COLZ")
canvaseff.Print(os.path.join(plot_directory,'Efficiency.png'))
canvaseff.SaveAs(os.path.join(plot_directory,'Efficiency.root'))

