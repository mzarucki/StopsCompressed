from Samples.nanoAOD.Autumn18_private_legacy_v1 import *

nmuon = "Sum$(Muon_pt>5&&Muon_miniPFRelIso_all<.1&&abs(Muon_dxy)>0.1)"
nisr  = "Sum$(Jet_pt>100)"


samples = [
    ( 0.2, TTLep_pow), 
    ( 15, DisplacedStops_mStop_250_ctau_0p01), 
    ( 15, DisplacedStops_mStop_250_ctau_0p1)
    ]

for nLep in [0,1,2]:
    for nisrJet in [0,1]:
        for norm, sample in samples:
            #sample.reduceFiles(to=1)
            selectionString =  nmuon+">=%i"%nLep+"&&"+nisr+">=%i"%nisrJet
            print "nLep", nLep, "nisrJet", nisrJet
            print sample.name, norm*sample.getYieldFromDraw(selectionString = selectionString)['val'] 
