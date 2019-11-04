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
argParser.add_argument('--targetDir',          action='store',      default='v01')
argParser.add_argument('--signal',       action='store',      default='fwlite_signals_fastSim_Stops2l_200k',choices=['fwlite_signals_DisplacedStops_250_0p001','fwlite_signals_DisplacedStops_250_0p01','fwlite_signals_DisplacedStops_250_0p1','fwlite_signals_DisplacedStops_250_0p2','fwlite_signals_DisplacedStops_250_200'], help='generated signal samples we get plots for')

args = argParser.parse_args()

#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

if args.small: args.signal += "_small"
plot_directory = os.path.join(plot_directory,'gen', args.targetDir,args.signal)
if not os.path.exists( plot_directory ):
    os.makedirs(plot_directory)
    logger.info( "Created plot directory %s", plot_directory )
from StopsCompressed.samples.signals import *

sample = fwlite_signals_DisplacedStops_250_0p2 # fwlite_signals_DisplacedStops_250_200 #fwlite_signals_fastSim_Stops2l_200k #fwlite_signals_DisplacedStops_500_0p2
print "loading files"
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

histo   = ROOT.TH1F("histo","Stops Transverse decay length (13 TeV);Lxy[cm];number of events",500,0.00,10.0)
histodphi   = ROOT.TH1F("histodphi","delta phi between stops (13 TeV);dphi;number of events",50,0.0,4.00)
histolepdphi   = ROOT.TH1F("histolepdphi","delta phi between leptons (13 TeV);dphi;number of events",50,0.0,4.00)
histoMET_dilep_1_dphi   = ROOT.TH1F("histo_dilep_1_dphi","delta phi between 1st lepton and MET(dilep) (13 TeV);dphi;number of events",50,0.0,4.00)
histoMET_dilep_2_dphi   = ROOT.TH1F("histo_dilep_2_dphi","delta phi between 2nd lepton and MET(dilep) (13 TeV);dphi;number of events",50,0.0,4.00)
histoDR   = ROOT.TH1F("histoDR","deltaR between stops (13 TeV);dphi;number of events",50,0.0,4.00)
histoDRlep   = ROOT.TH1F("histoDRlep","deltaR between leptons (13 TeV);dphi;number of events",50,0.0,4.00)
histol  = ROOT.TH1F("histol","Leptons Transverse decay length (13 TeV);Lxy[cm];number of events",50,0.0,0.2)
histot  = ROOT.TH1F("histot","Proper time of stops (13 TeV);proper time[cm];number of events",50,0.0,0.09)
histotn = ROOT.TH1F("histotn","Proper time of stops with neutralinos (13 TeV);proper time[cm];number of events",1000,0.0,100.0)
histopt = ROOT.TH1F("histopt","Transverse Momentum of Leptons (13 TeV);pT[GeV];number of events",50,0.0,50.0)
histostopspt = ROOT.TH1F("histostopspt","Transverse Momentum of Stops (13 TeV);pT[GeV];number of events",100,0.0,700.0)
histonlpt = ROOT.TH1F("histonlpt","Transverse Momentum of Neutralinos (13 TeV);pT[GeV];number of events",100,0.0,700.0)
histonpt = ROOT.TH1F("histonpt","Transverse Momentum of Neutrinos (13 TeV);pT[GeV];number of events",50,0.0,100.0)
histoMET_dilep = ROOT.TH1F("histoMET_dilep","MET dilep (13 TeV);pT[GeV];number of events",50,0.0,700.0)
histod0 = ROOT.TH1F("histod0","Impact Parameters of leptons (13 TeV);d0[cm];number of events",50,0.0,10.0)
histod02D = ROOT.TH2F("histod02D","Impact Parameters of leptons in dilepton state (13 TeV); first lepton d0[cm]; 2nd lepton d0[cm]",10,0.0,0.5,10,0.0,0.5)
#graph = ROOT.TGraph(50)
canvasl= ROOT.TCanvas("canvasl", "Stops decay length ", 1000, 600)
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
  i += 1
  stops = []
  leptons = []
  MET = []
  MET_di = []
  neutrino = {"pdgId": 0 ,"px": float('nan') , "py": float('nan')}
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
                            lep = {"pdgId": d.pdgId() ,"phi": d.phi() , "eta":d.eta(), "d0": IP}
                            leptons.append(lep)
                        else:
                            npt= d.pt()
                            phin=d.phi()
                            #print "neutrino", d.pdgId(), d.pt()
                            histonpt.Fill(npt)
                            px = npt * cos (phin)
                            py = npt * sin (phin)
                            neutrino = {"pdgId": d.pdgId(), "px": px , "py": py}
                            MET.append(neutrino) 
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
            nlphi= p.phi()
            nlpx= nlpt * cos (nlphi)
            nlpy= nlpt * sin (nlphi)
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
            
            neutralino = {"pdgId": p.pdgId(),"px": nlpx,"py":nlpy }
            MET.append(neutralino)
            #print "stops proper time", tn, "decay length of stops", l
            #print "Lxy from neutralino" , vn.rho(), "mass of stop", m.pdgId(), m.mass(), m.pt() 
    elif abs(p.pdgId()) == 1000006 and p.status() == 22:
        stop = {"phi":p.phi(), "eta":p.eta()}
        stops.append(stop)
        #v= p.vertex()
        #print "stops: ",p.pdgId(), "pt: ", p.pt(), "phi:" ,p.phi(), "eta: ", p.eta()
        #print "stops phi", p.phi()
  DR = deltaR(stops[0]["phi"], stops[0]["eta"], stops[1]["phi"],stops[1]["eta"])
  dphi = deltaPhi(stops[0]["phi"], stops[1]["phi"] )
  histodphi.Fill(dphi)
  histoDR.Fill(DR)
  if len(leptons) == 2:
        dphilep = deltaPhi(leptons[0]["phi"],leptons[1]["phi"])
        DRlep = deltaR(leptons[0]["phi"], leptons[0]["eta"], leptons[1]["phi"],leptons[1]["eta"])
        #print "deltphi of leptons", dphilep
        histolepdphi.Fill(dphilep)
        histoDRlep.Fill(DRlep)
        d0l1.append(leptons[0]["d0"])
        d0l2.append(leptons[1]["d0"])       
        histod02D.Fill(leptons[0]["d0"], leptons[1]["d0"])
        #if abs(leptons[0]["pdgId"]) == 13:
        #    histod02D.Fill(leptons[0]["d0"], leptons[1]["d0"])
        #    print "should be muon", leptons[0]["pdgId"],"should be el", leptons[1]["pdgId"]
        #else:
        #    histod02D.Fill(leptons[1]["d0"], leptons[0]["d0"]) 
        #    print "should be muon", leptons[1]["pdgId"],"should be el", leptons[0]["pdgId"]
  if len(MET) == 4:
      dilep_MET, dilep_MET_phi = MET_dilep(MET[0]["px"],MET[0]["py"],MET[1]["px"], MET[1]["py"] ,MET[2]["px"],MET[2]["py"],MET[3]["px"],MET[3]["py"])      
      dphi_MET_1l = deltaPhi(leptons[0]["phi"],dilep_MET_phi)
      dphi_MET_2l = deltaPhi(leptons[1]["phi"],dilep_MET_phi)
      histoMET_dilep.Fill(dilep_MET)
      histoMET_dilep_1_dphi.Fill(dphi_MET_1l)
      histoMET_dilep_2_dphi.Fill(dphi_MET_2l)
  #elif len(MET) == 3:
  #    semilep_MET, semilep_MET_phi = MET_semilep(MET[0]["px"],MET[0]["py"],MET[1]["px"], MET[1]["py"] ,MET[2]["px"],MET[2]["py"])
  #    #print MET[0]['pdgId'] , MET[1]['pdgId'], MET[2]['pdgId']
  #    #print "semilep MET:" ,semilep_MET, "semilep dphi:" , semilep_MET_phi       
  #elif len(MET) == 2:
  #    MET_nl , MET_nl_phi = MET_chi(MET[0]["px"],MET[0]["py"],MET[1]["px"], MET[1]["py"] )
  #    #print MET[0]['pdgId'] , MET[1]['pdgId']
  #    #print "neutralino MET:" , MET_nl, "neutralino MET dphi:" , MET_nl_phi

  #print len(MET)
  if i% 1000==0:
    print "1000 events passed"
#  if i ==100000:
#    break  
#print  "Found the following run(s): %s", ",".join(str(run) for run in runs)
#scale = 1 / histol.Integral()
scales = 1 / histo.Integral()
scaletn = 1 / histotn.Integral()
scaledphi = 1 / histodphi.Integral()
scalelepdphi = 1 / histolepdphi.Integral()
scaled0 = 1 / histod0.Integral()
scaled02D = 1 / histod02D.Integral()
scalept = 1 / histopt.Integral()
scalenlpt = 1 / histonlpt.Integral()
scalenpt = 1 / histonpt.Integral()
scalestopspt = 1 / histostopspt.Integral()
scaleDR = 1 / histoDR.Integral()
scaleDRlep = 1 / histoDRlep.Integral()
scaleMET_dilep = 1/ histoMET_dilep.Integral()
scaleMET_dilep_1l = 1/histoMET_dilep_1_dphi.Integral()
scaleMET_dilep_2l = 1/histoMET_dilep_2_dphi.Integral()

canvasd02D= ROOT.TCanvas("canvasd02D", "ImpactParameter ", 1000, 600)
print len(d0l1)
print len(d0l2)
graph = ROOT.TGraph(len(d0l1), d0l1, d0l2)
graph.SetTitle("Impact Parameter of leptons in dilepton final state")
graph.GetXaxis().SetTitle("1st lepton d0 [cm]")
graph.GetYaxis().SetTitle("2nd lepton d0 [cm]")
graph.SetMarkerStyle(21)
graph.Draw("ap")
canvasd02D.SaveAs(os.path.join(plot_directory,'scatterplot_d0.png'))
canvasd02D.SaveAs(os.path.join(plot_directory,'scatterplot_d0.root'))

histo.Scale(scales)
histo.Draw()
myPad=canvasl.GetPad(1)
canvasl.SetLogy()
histo.GetMean()
canvasl.Modified()
canvasl.Print(os.path.join(plot_directory,'histostops.png'))
canvasl.SaveAs(os.path.join(plot_directory,'histostops.root'))

canvast= ROOT.TCanvas("canvast", "Stops proper time ", 1000, 600)
histotn.Scale(scaletn)
histotn.Draw()
canvast.SetLogy()
histotn.GetMean()
#print "RMS is" ,histotn.GetRMS()
#print "Mean is", histotn.GetMean()
canvast.Modified()
canvast.SaveAs(os.path.join(plot_directory,'histotime.png'))
canvast.SaveAs(os.path.join(plot_directory,'histotime.root'))

canvasd0= ROOT.TCanvas("canvasd0", "ImpactParameter ", 1000, 600)
histod0.Scale(scaled0)
histod0.Draw()
histod0.GetMean()
canvasd0.SetLogy()
canvasd0.Modified()
canvasd0.Print(os.path.join(plot_directory,'ImpactParameter.png'))
canvasd0.SaveAs(os.path.join(plot_directory,'ImpactParameter.root'))

canvaspt= ROOT.TCanvas("canvaspt", "Leptons pt ", 1000, 600)
histopt.Scale(scalept)
histopt.Draw()
histopt.GetMean()
canvaspt.SetLogy()
canvaspt.Modified()
canvaspt.Print(os.path.join(plot_directory,'leptonspT.png'))
canvaspt.SaveAs(os.path.join(plot_directory,'leptonspT.root'))

canvasnlpt= ROOT.TCanvas("canvasnlpt", "Neutralinos pt ", 1000, 600)
histonlpt.Scale(scalenlpt)
histonlpt.Draw()
histonlpt.GetMean()
canvasnlpt.SetLogy()
canvasnlpt.Modified()
canvasnlpt.Print(os.path.join(plot_directory,'neutralinospT.png'))
canvasnlpt.SaveAs(os.path.join(plot_directory,'neutralinospT.root'))

canvasnpt= ROOT.TCanvas("canvasnpt", "Neutrinos pt ", 1000, 600)
histonpt.Scale(scalenpt)
histonpt.Draw()
histonpt.GetMean()
canvasnpt.SetLogy()
canvasnpt.Modified()
canvasnpt.Print(os.path.join(plot_directory,'neutrino_pT.png'))
canvasnpt.SaveAs(os.path.join(plot_directory,'neutrino_pT.root'))

canvasstopspt= ROOT.TCanvas("canvasstopspt", "Stops pt ", 1000, 600)
histostopspt.Scale(scalestopspt)
histostopspt.Draw()
histostopspt.GetMean()
canvasstopspt.SetLogy()
canvasstopspt.Modified()
canvasstopspt.Print(os.path.join(plot_directory,'stops_pT.png'))
canvasstopspt.SaveAs(os.path.join(plot_directory,'stops_pT.root'))

canvasdphistop= ROOT.TCanvas("canvasdphistop", "deltaphi between Stops ", 1000, 600)
histodphi.Scale(scaledphi)
histodphi.Draw()
histodphi.GetMean()
canvasdphistop.SetLogy()
canvasdphistop.Modified()
canvasdphistop.Print(os.path.join(plot_directory,'stops_dphi.png'))
canvasdphistop.SaveAs(os.path.join(plot_directory,'stops_dphi.root'))

canvaslepdphi= ROOT.TCanvas("canvaslepdphi", "deltaphi between Leptons", 1000, 600)
histolepdphi.Scale(scalelepdphi)
histolepdphi.Draw()
histolepdphi.GetMean()
canvaslepdphi.SetLogy()
canvaslepdphi.Modified()
canvaslepdphi.Print(os.path.join(plot_directory,'leptons_dphi.png'))
canvaslepdphi.SaveAs(os.path.join(plot_directory,'leptons_dphi.root'))

canvasDR= ROOT.TCanvas("canvasDR", "deltaR between Stops", 1000, 600)
histoDR.Scale(scaleDR)
histoDR.Draw()
histoDR.GetMean()
canvasDR.SetLogy()
canvasDR.Modified()
canvasDR.Print(os.path.join(plot_directory,'stops_dR.png'))
canvasDR.SaveAs(os.path.join(plot_directory,'stops_dR.root'))

canvasDRlep= ROOT.TCanvas("canvasDRlep", "deltaR between Leptons", 1000, 600)
histoDRlep.Scale(scaleDRlep)
histoDRlep.Draw()
histoDRlep.GetMean()
canvasDRlep.SetLogy()
canvasDRlep.Modified()
canvasDRlep.Print(os.path.join(plot_directory,'leptons_dR.png'))
canvasDRlep.SaveAs(os.path.join(plot_directory,'leptons_dR.root'))

canvasMET_dilep= ROOT.TCanvas("canvasMET_dilep", "MET_dilep ", 1000, 600)
histoMET_dilep.Scale(scaleMET_dilep)
histoMET_dilep.Draw()
histoMET_dilep.GetMean()
canvasMET_dilep.SetLogy()
canvasMET_dilep.Modified()
canvasMET_dilep.Print(os.path.join(plot_directory,'MET_dilep.png'))
canvasMET_dilep.SaveAs(os.path.join(plot_directory,'MET_dilep.root'))

canvasdphiMET_dilep_1l= ROOT.TCanvas("canvasdphiMET_dilep_1l", "deltaphi between dilep MET and 1stl ", 1000, 600)
histoMET_dilep_1_dphi.Scale(scaleMET_dilep_1l)
histoMET_dilep_1_dphi.Draw()
histoMET_dilep_1_dphi.GetMean()
canvasdphiMET_dilep_1l.SetLogy()
canvasdphiMET_dilep_1l.Modified()
canvasdphiMET_dilep_1l.Print(os.path.join(plot_directory,'METdilep_1l_dphi.png'))
canvasdphiMET_dilep_1l.SaveAs(os.path.join(plot_directory,'METdilep_1l_dphi.root'))

canvasdphiMET_dilep_2l= ROOT.TCanvas("canvasdphiMET_dilep_2l", "deltaphi between dilep MET and 2ndl ", 1000, 600)
histoMET_dilep_2_dphi.Scale(scaleMET_dilep_2l)
histoMET_dilep_2_dphi.Draw()
histoMET_dilep_2_dphi.GetMean()
canvasdphiMET_dilep_2l.SetLogy()
canvasdphiMET_dilep_2l.Modified()
canvasdphiMET_dilep_2l.Print(os.path.join(plot_directory,'METdilep_2l_dphi.png'))
canvasdphiMET_dilep_2l.SaveAs(os.path.join(plot_directory,'METdilep_2l_dphi.root'))

canvasd02Dhist= ROOT.TCanvas("canvasd02Dhist", "ImpactParameter of leptons in dilepton state", 1000, 600)
histod02D.Scale(scaled02D)
histod02D.Draw("COLZ")
histod02D.GetMean()
canvasd02Dhist.SetLogz()
#canvasd02Dhist.Modified()
canvasd02Dhist.Print(os.path.join(plot_directory,'ImpactParameter2D.png'))
canvasd02Dhist.SaveAs(os.path.join(plot_directory,'ImpactParameter2D.root'))
#
#histo.Draw('E')
#histo.Draw()
#canvas.Print('/afs/hephy.at/user/p/phussain/www/histo2.png')       
