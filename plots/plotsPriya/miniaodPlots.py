''' Plot script for miniAOD signal plots for dilepton compressed
'''

# Standard imports
import ROOT, os, array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math   import pi, sqrt, sin, cos, atan2
from RootTools.core.standard import *
from Analysis.Tools.GenSearch import *
from RootTools.core.standard import *

from StopsCompressed.tools.user         import plot_directory

#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v02_dR0p3')

args = argParser.parse_args()
#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

#importing miniAOD samples from Samples repository
from Samples.miniAOD.Autumn18_Fast_miniAODv1 import DisplacedStops_mStop_250_ctau_0p01
sample = DisplacedStops_mStop_250_ctau_0p01
print "loading files"
print sample.name

if args.small: args.targetDir += "_small"
plot_directory = os.path.join(plot_directory,'miniAOD', args.targetDir, sample.name , 'log')
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

def reco_matched(gen_muon_phi,gen_muon_eta, recoList, threshold ):
    '''finding the closest reco muon for given gen muon'''
    matches = []
    gmu_eta = gen_muon_eta
    gmu_phi = gen_muon_phi
    for i,rm in enumerate(recoList):
        dR = deltaR(rm.phi(),rm.eta(),gmu_phi,gmu_eta)
        if dR < threshold:
            deta = abs(gmu_eta - rm.eta() )
            dphi = deltaPhi( rm.phi(), gmu_phi )
            matches.append({'idx':i, 'deltaR':dR,'deta':deta,'dphi': dphi,'muon':rm})

    return sorted(matches, key=lambda dic:dic['deltaR'])
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


# miniAOD
products = {
#    'pfCands':{'type':'vector<pat::PackedCandidate>', 'label':"packedPFCandidates"},
#    'pfJets':{'type':'vector<pat::Jet>', 'label': ("slimmedJets")},
#    'pfMet':{'type':'vector<pat::MET>','label':( "slimmedMETs" )},
#    'electrons':{'type':'vector<pat::Electron>','label':( "slimmedElectrons" )},
    'genParticles':{'type':'vector<reco::GenParticle>', 'label':("prunedGenParticles") },
    'muons':{'type':'vector<pat::Muon>', 'label':("slimmedMuons") },
}

histomud0 = ROOT.TH1F("histomud0","Impact Parameters of reco muons (13 TeV);d0[cm];number of events",50,0.0,10.0)
histomulxy = ROOT.TH1F("histomulxy","Transverse decay length of reco muons (13 TeV); Lxy[cm];number of events",50,0.0,10.0)
histogenmud0 = ROOT.TH1F("histogenmud0","Impact Parameters of gen muons (13 TeV);d0[cm];number of events",50,0.0,50.0)
histogenmulxy = ROOT.TH1F("histogenmulxy","Transverse decay length of gen muons (13 TeV); Lxy[cm];number of events",50,0.0,10.0)
histo2Dgenmu = ROOT.TH2F("histo2Dgenmu","Impact Parameter and transverse decay length of gen muons (13 TeV);  d0 gen muons[cm]; gen_Lxy [cm]",50,0.0,10.0,50,0.0,10.0)
histo2Drecomu = ROOT.TH2F("histo2Drecomu","Impact Parameter and transverse decay length of matched RECO muons(13 TeV);  d0 reco muons[cm]; reco Lxy [cm]",50,0.0,10.0,50,0.0,10.0)
histo2Dallrecomu = ROOT.TH2F("histo2Dallrecomu","Impact Parameter and transverse decay length of all RECO muons(13 TeV);  d0 reco muons[cm]; reco Lxy [cm]",50,0.0,10.0,50,0.0,10.0)
histo2Dmatchmu = ROOT.TH2F("histo2Dmatchmu","Impact Parameter and transverse decay length of RECO(matched) muons(13 TeV);  gen_d0 muons[cm]; gen_Lxy [cm]",50,0.0,10.0,50,0.0,10.0)
histo2Dmatchgen = ROOT.TH2F("histo2Dmatchgen","Impact Parameter and transverse decay length of RECO(matched) with gen muons(13 TeV);  gen_d0 muons[cm]; gen_Lxy [cm]",50,0.0,10.0,50,0.0,10.0)
histo2D = ROOT.TH2I("histo2D", "number of gen vs reco muons; gen muons;reco muons", 2,0,2,2,0,2)

historecomud0 = ROOT.TH1F("historecomud0","Impact Parameters of reco(matched) muons (13 TeV); gen d0[cm];number of events",50,0.0,50.0)
historecomulxy = ROOT.TH1F("historecomulxy","Transverse decay length of reco(matched) muons (13 TeV); gen Lxy[cm];number of events",50,0.0,10.0)

histolepdphi   = ROOT.TH1F("histolepdphi","delta phi between gen and reco muons (13 TeV);dphi;number of events",200,0.0,0.5)
histolepdeta   = ROOT.TH1F("histolepdeta","delta eta between gen and reco muons (13 TeV);deta;number of events",200,0.0,0.5)
histoDRlep   = ROOT.TH1F("histoDRlep","deltaR between gen and reco muons (13 TeV);dR;number of events",200,0.0,0.5)
histoDRweighted   = ROOT.TH1F("histoDRweighted","deltaR(weighted) between gen and reco(matched) muons (13 TeV);dR;number of events",200,0.0,0.5)
#histoDR   = ROOT.TH1F("histoDR","deltaR between gen and reco(matched) muons (13 TeV);dR;number of events",100,0.0,4.0)
histo2Ddetadphi = ROOT.TH2F("histo2Ddetadphi","dEta vs dPhi of RECO(matched) muons and gen muons (13 TeV);  dEta; dPhi",100,0.0,0.5,100,0.0,0.5)

histounpt = ROOT.TH1F("histounpt","Transverse Momentum of unmatched reco muons (13 TeV);pT[GeV];number of events",100,0.0,50.0)
histouneta   = ROOT.TH1F("histouneta","eta of unmatched reco muons (13 TeV);deta;number of events",200,0.0,0.5)
histounphi   = ROOT.TH1F("histounphi","phiof unmatched reco muons (13 TeV);dphi;number of events",200,0.0,0.5)
histound0 = ROOT.TH1F("histound0","Impact Parameters of unmatched reco muons (13 TeV);d0[cm];number of events",50,0.0,10.0)
histounlxy = ROOT.TH1F("histounlxy","Transverse decay length of unmatched reco muons (13 TeV); Lxy[cm];number of events",50,0.0,10.0)
r = sample.fwliteReader(products = products)
r.start()
runs = set()
i=0
while r.run():
  #print r.event.evt, r.event.lumi, r.event.run
  muons = r.event.muons
  genparticles = r.event.genParticles
  i += 1
  gen_mu = []
  matched_muon = []
  matched_gen = []
  for p in genparticles:
    g = GenSearch(p)
    if abs(p.pdgId()) == 1000006 and g.isLast(p):
        daughters = g.daughters(p)
        #print [ds.pdgId() for ds in daughters]
        for ds in daughters:
            if abs(ds.pdgId()) == 24 and g.isLast(ds):
                #print "w coming from stop",ds.pdgId()
                daughter=g.daughters(ds)
                for d in daughter:
                    #print "genparticle", d.pdgId()
                    if abs(d.pdgId()) in [11,13,12,14]  and g.isFirst(d):
                        #print "leptons coming from W coming from a stop", d.pdgId()
                        if abs(d.pdgId()) == 13 and d.pt() > 5 and abs(d.eta()) < 2.1:
                            ptl = d.pt()
                            v = d.vertex()
                            x = v.x()
                            y = v.y()
                            phil= d.phi()
                            px = ptl * cos (phil)
                            py = ptl * sin (phil)
                            ll= v.rho()
                            #print "pt, phi,lxy of muon: ",ptl,phil,ll
                            IP = dxy(x,y,px,py)
                            gmu = {"phi": d.phi(), "eta": d.eta(), "Lxy": v.rho(), "d0": IP}
                            gen_mu.append(gmu)
                            histogenmud0.Fill(IP)
                            histogenmulxy.Fill(v.rho())
                            histo2Dgenmu.Fill(IP,v.rho())
                            
  for gmu in range(len(gen_mu)):
    phigmu = gen_mu[gmu]["phi"]
    etagmu = gen_mu[gmu]["eta"]
    d0gmu  = gen_mu[gmu]["d0"]
    Lxygmu = gen_mu[gmu]["Lxy"]
    matchedRecoMuons=reco_matched(phigmu,etagmu,muons,threshold=0.3)
    if len( matchedRecoMuons)>0 and gen_mu not in matched_gen:
        #print gen_mu
        #print "matched muons" , len( matchedRecoMuons)
        rm = matchedRecoMuons[0]['muon']
        histo2Dmatchgen.Fill(d0gmu , Lxygmu)
        historecomud0.Fill(d0gmu)
        historecomulxy.Fill(Lxygmu)
        dR = matchedRecoMuons[0]['deltaR']
        norm = 1/dR
        histoDRlep.Fill(dR)
        histoDRweighted.Fill(dR,norm)
        histolepdphi.Fill(matchedRecoMuons[0]['dphi'])
        histolepdeta.Fill(matchedRecoMuons[0]['deta'])
        histo2Ddetadphi.Fill(matchedRecoMuons[0]['deta'],matchedRecoMuons[0]['dphi'])
        #print "deltaR of matched reco&gen should be less than threshold 0.002",matchedRecoMuons[0]['deltaR'] 
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
        histomud0.Fill(IPrmu)
        histomulxy.Fill(lrmu)
        matched_gen.append(gen_mu)
        #print len(matched_gen)
    for m in muons:
        for j,mm in enumerate(matchedRecoMuons):
            if m != matchedRecoMuons[j]['muon'] :
                #print m.pt(), m.phi(),m.eta()
                histounpt.Fill(m.pt())
                histounphi.Fill(m.phi())
                histouneta.Fill(abs(m.eta()))
                vm = m.vertex()
                #print m.px(), m.py()
                histounlxy.Fill(vm.rho())
                IPunm=dxy(vm.x(),vm.y(),m.px(),m.py())
                histound0.Fill(IPunm)
#  muon_match=[]                      
#  for m in muons:
#    v=m.vertex()
#    print v.rho()    
#    gp = m.genParticle()
   # try:
   #     gpv = gp.vertex()
   #     print "gen particle associated with pat muon rho", gpv.rho(), gp.pdgId()
   #     muon_match.append(gp)
   # except ReferenceError:
   #     print "null pointer"
  #print len(muon_match)       
  if i%1000==0:
      print "1000 events passed"
  if args.small:
    if i==1000:
        break


canvasefflxy = ROOT.TCanvas("canvasefflxy", "Efficiency of matched reco and gen muons Lxy", 1000, 600)
histoefflxy = ROOT.TEfficiency(historecomulxy,histogenmulxy)
histoefflxy.Draw()
canvasefflxy.Print(os.path.join(plot_directory,'Efficiency_Lxy.png'))
canvasefflxy.SaveAs(os.path.join(plot_directory,'Efficiency_Lxy.root'))

canvaseffd0 = ROOT.TCanvas("canvaseffd0", "Efficiency of matched reco and gen muons d0", 1000, 600)
histoeffd0 = ROOT.TEfficiency(historecomud0,histogenmud0)
histoeffd0.Draw()
canvaseffd0.Print(os.path.join(plot_directory,'Efficiency_d0.png'))
canvaseffd0.SaveAs(os.path.join(plot_directory,'Efficiency_d0.root'))

scalegend0 = 1 / histogenmud0.Integral()
scalegenlxy = 1 / histogenmulxy.Integral()
scaled0 = 1 / histomud0.Integral()
scalelxy = 1 / histomulxy.Integral()
scalelepdeta = 1 / histolepdeta.Integral()
scalelepdphi = 1 / histolepdphi.Integral()
scaleDRlep = 1 / histoDRlep.Integral()
scaleDRw = 1 / histoDRweighted.Integral()

scalerecod0 = 1 / historecomud0.Integral()
scalerecolxy = 1 / historecomulxy.Integral()

scaleunpt=1/histounpt.Integral()
scaleunphi=1/histounphi.Integral()
scaleuneta=1/histouneta.Integral()
scaleund0=1/histound0.Integral()
scaleunlxy=1/histounlxy.Integral()

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

canvasrecomulxy= ROOT.TCanvas("canvasrecomulxy", "Lxy of reco matched muons", 1000, 600)
historecomulxy.Scale(scalerecolxy)
historecomulxy.Draw()
myPad=canvasrecomulxy.GetPad(1)
canvasrecomulxy.SetLogy()
historecomulxy.GetMean()
canvasrecomulxy.Modified()
canvasrecomulxy.Print(os.path.join(plot_directory,'Lxy_Matchedreco.png'))
canvasrecomulxy.SaveAs(os.path.join(plot_directory,'Lxy_Matchedreco.root'))


canvasrecomud0= ROOT.TCanvas("canvasrecomud0", "d0 of reco matched muons", 1000, 600)
historecomud0.Scale(scalerecod0)
historecomud0.Draw()
myPad=canvasrecomud0.GetPad(1)
canvasrecomud0.SetLogy()
historecomud0.GetMean()
canvasrecomulxy.Modified()
canvasrecomud0.Print(os.path.join(plot_directory,'d0_Matchedreco.png'))
canvasrecomud0.SaveAs(os.path.join(plot_directory,'d0_Matchedreco.root'))


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
histoeff = ROOT.TEfficiency(histo2Dmatchgen,histo2Dgenmu)
histoeff.Draw("COLZ")
canvaseff.Print(os.path.join(plot_directory,'Efficiency.png'))
canvaseff.SaveAs(os.path.join(plot_directory,'Efficiency.root'))

canvaslepdphi= ROOT.TCanvas("canvaslepdphi", "deltaphi between reco and gen muons", 1000, 600)
histolepdphi.Scale(scalelepdphi)
histolepdphi.Draw()
histolepdphi.GetMean()
canvaslepdphi.SetLogy()
canvaslepdphi.Modified()
canvaslepdphi.Print(os.path.join(plot_directory,'reco_matched_gen_dphi.png'))
canvaslepdphi.SaveAs(os.path.join(plot_directory,'reco_matched_gen_dphi.root'))


canvaslepdeta= ROOT.TCanvas("canvaslepdeta", "deltaeta between reco and gen muons", 1000, 600)
histolepdeta.Scale(scalelepdeta)
histolepdeta.Draw()
histolepdeta.GetMean()
canvaslepdeta.SetLogy()
canvaslepdeta.Modified()
canvaslepdeta.Print(os.path.join(plot_directory,'reco_matched_gen_deta.png'))
canvaslepdeta.SaveAs(os.path.join(plot_directory,'reco_matched_gen_deta.root'))

canvasDRlep= ROOT.TCanvas("canvasDRlep", "deltaR between reco and gen muons", 1000, 600)
histoDRlep.Scale(scaleDRlep)
histoDRlep.Draw()
histoDRlep.GetMean()
canvasDRlep.SetLogy()
canvasDRlep.Modified()
canvasDRlep.Print(os.path.join(plot_directory,'reco_gen_muons_dR.png'))
canvasDRlep.SaveAs(os.path.join(plot_directory,'reco_gen_muons_dR.root'))

canvasDRw= ROOT.TCanvas("canvasDRw", "deltaR(weighted) between reco and gen muons", 1000, 600)
histoDRweighted.Scale(scaleDRw)
histoDRweighted.Draw()
histoDRweighted.GetMean()
canvasDRw.SetLogy()
canvasDRw.Modified()
canvasDRw.Print(os.path.join(plot_directory,'reco_gen_muons_dR_weighted.png'))
canvasDRw.SaveAs(os.path.join(plot_directory,'reco_gen_muons_dR_weighted.root'))

canvas2Detaphi= ROOT.TCanvas("canvas2Detaphi", "gen and reco muons deta vs dphi", 1000, 600)
histo2Ddetadphi.Draw("COLZ")
histo2Ddetadphi.GetMean()
canvas2Detaphi.SetLogz()
canvas2Detaphi.Print(os.path.join(plot_directory,'gen_reco_deta_vs_dphi.png'))
canvas2Detaphi.SaveAs(os.path.join(plot_directory,'gen_reco_deta_vs_dphi.root'))

canvasunpt= ROOT.TCanvas("canvasunpt", "Unmatched reco muons pt ", 1000, 600)
histounpt.Scale(scaleunpt)
histounpt.Draw()
histounpt.GetMean()
canvasunpt.SetLogy()
canvasunpt.Modified()
canvasunpt.Print(os.path.join(plot_directory,'unmatched_recomuon_pT.png'))
canvasunpt.SaveAs(os.path.join(plot_directory,'unmatched_recomuon_pT.root'))


canvasunphi= ROOT.TCanvas("canvasunphi", "Unmatched reco muons phi ", 1000, 600)
histounphi.Scale(scaleunphi)
histounphi.Draw()
histounphi.GetMean()
canvasunphi.SetLogy()
canvasunphi.Modified()
canvasunphi.Print(os.path.join(plot_directory,'unmatched_recomuon_phi.png'))
canvasunphi.SaveAs(os.path.join(plot_directory,'unmatched_recomuon_phi.root'))

canvasuneta= ROOT.TCanvas("canvasuneta", "Unmatched reco muons eta ", 1000, 600)
histouneta.Scale(scaleuneta)
histouneta.Draw()
histouneta.GetMean()
canvasuneta.SetLogy()
canvasuneta.Modified()
canvasuneta.Print(os.path.join(plot_directory,'unmatched_recomuon_eta.png'))
canvasuneta.SaveAs(os.path.join(plot_directory,'unmatched_recomuon_eta.root'))


canvasund0= ROOT.TCanvas("canvasund0", "Unmatched reco muons Impact Parameter ", 1000, 600)
histound0.Scale(scaleund0)
histound0.Draw()
histound0.GetMean()
canvasund0.SetLogy()
canvasund0.Modified()
canvasund0.Print(os.path.join(plot_directory,'unmatched_recomuon_d0.png'))
canvasund0.SaveAs(os.path.join(plot_directory,'unmatched_recomuon_d0.root'))

canvasunlxy= ROOT.TCanvas("canvasunlxy", "Unmatched reco muons Lxy ", 1000, 600)
histounlxy.Scale(scaleunlxy)
histounlxy.Draw()
histounlxy.GetMean()
canvasunlxy.SetLogy()
canvasunlxy.Modified()
canvasunlxy.Print(os.path.join(plot_directory,'unmatched_recomuon_lxy.png'))
canvasunlxy.SaveAs(os.path.join(plot_directory,'unmatched_recomuon_lxy.root'))
