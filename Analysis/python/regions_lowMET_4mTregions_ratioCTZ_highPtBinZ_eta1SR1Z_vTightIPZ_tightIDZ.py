from math import pi

from StopsCompressed.Analysis.Region import Region

# Put all sets of regions that are used in the analysis, closure, tables, etc.

# Adding lowMET region Z with 200 < CT < 300 GeV
# NOTE: MET plateau ~ 200 GeV
# NOTE: muon plateau ~ 8 GeV and cut at 6 GeV (~ 85 %)    # NOTE: abs(eta) < 1.5
# NOTE: jet plateau ~ 140 GeV and cut at 130 GeV (~ 90 %) # NOTE: all jets already have abs(eta) < 2.4

# nSR = 312
# nCR = 80
# nSR + nCR = 392 regions

# tight muon selection
tightMuon = Region("abs(l1_dxy)", (0,0.0015)) + Region("abs(l1_dz)", (0,0.003)) + Region("l1_dxyErr", (0,0.0022)) + Region("l1_dzErr", (0,0.004)) + Region("Muon_tightId[l1_muIndex[0]]", (1,1))

### SR1
SR1 = Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) #NOTE: reduced MET and HT cuts in Setup.py 
signalRegions = []
controlRegions = []
region = {}

## SR1a
# SR1aZ
SR1laZ0p6  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio 
SR1maZ0p6  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ0p6  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ0p6 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZ0p7  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZ0p7  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ0p7  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ0p7 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZ0p8  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZ0p8  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ0p8  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ0p8 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZ0p9  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZ0p9  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ0p9  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ0p9 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZ1p0  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZ1p0  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ1p0  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ1p0 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZ1p1  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZ1p1  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ1p1  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ1p1 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZ1p2  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZ1p2  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZ1p2  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZ1p2 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1laZinf  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1maZinf  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1haZinf  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhaZinf = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

# SR1aX
SR1vlaX   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1laX    = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1maX    = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1haX    = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

# SR1aY
SR1vlaY   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1laY    = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1maY    = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1haY    = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## CR1a
CR1aZ0p6  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio
CR1aZ0p7  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aZ0p8  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aZ0p9  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aZ1p0  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aZ1p1  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aZ1p2  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aZinf  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1aX     = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
CR1aY     = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## SR1b
# SR1bZ
SR1lbZ0p6  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio
SR1mbZ0p6  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ0p6  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ0p6 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZ0p7  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZ0p7  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ0p7  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ0p7 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZ0p8  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZ0p8  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ0p8  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ0p8 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZ0p9  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZ0p9  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ0p9  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ0p9 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZ1p0  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZ1p0  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ1p0  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ1p0 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZ1p1  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZ1p1  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ1p1  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ1p1 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZ1p2  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZ1p2  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZ1p2  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZ1p2 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lbZinf  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mbZinf  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hbZinf  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhbZinf = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

# SR1bX
SR1vlbX   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1lbX    = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1mbX    = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1hbX    = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

# SR1bY
SR1vlbY   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1lbY    = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1mbY    = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1hbY    = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## CR1b
CR1bZ0p6  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio
CR1bZ0p7  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bZ0p8  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bZ0p9  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bZ1p0  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bZ1p1  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bZ1p2  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bZinf  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1bX     = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
CR1bY     = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## SR1c
# SR1cZ
SR1lcZ0p6  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio
SR1mcZ0p6  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ0p6  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ0p6 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZ0p7  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZ0p7  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ0p7  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ0p7 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZ0p8  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZ0p8  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ0p8  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ0p8 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZ0p9  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZ0p9  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ0p9  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ0p9 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZ1p0  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZ1p0  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ1p0  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ1p0 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZ1p1  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZ1p1  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ1p1  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ1p1 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZ1p2  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZ1p2  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZ1p2  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZ1p2 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1lcZinf  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mcZinf  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hcZinf  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhcZinf = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

# SR1cX
SR1lcX    = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5)) 
SR1mcX    = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1hcX    = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

# SR1cY
SR1lcY    = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5)) 
SR1mcY    = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1hcY    = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## CR1c
CR1cZ0p6  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon# NOTE: replaced CT1 with MET and HT ratio
CR1cZ0p7  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cZ0p8  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cZ0p9  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cZ1p0  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cZ1p1  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cZ1p2  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cZinf  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon 
CR1cX     = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
CR1cY     = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## SR1d
# SR1dZ
SR1ldZ0p6  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio 
SR1mdZ0p6  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ0p6  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ0p6 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZ0p7  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZ0p7  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ0p7  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ0p7 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZ0p8  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZ0p8  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ0p8  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ0p8 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZ0p9  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZ0p9  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ0p9  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ0p9 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZ1p0  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZ1p0  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ1p0  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ1p0 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZ1p1  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZ1p1  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ1p1  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ1p1 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZ1p2  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZ1p2  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZ1p2  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZ1p2 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

SR1ldZinf  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1mdZinf  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1hdZinf  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
SR1vhdZinf = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon

# SR1dX
SR1ldX    = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1mdX    = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1hdX    = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

# SR1dY
SR1ldY    = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1mdY    = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
SR1hdY    = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

## CR1d
CR1dZ0p6  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0,0.6))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon # NOTE: replaced CT1 with MET and HT ratio
CR1dZ0p7  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dZ0p8  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dZ0p9  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dZ1p0  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (0.9,1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dZ1p1  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1,1.1))    + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dZ1p2  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dZinf  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_eta", (-1, 1)) + tightMuon
CR1dX     = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))
CR1dY     = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("l1_eta", (-1.5, 1.5))

### SR2
SR2 = Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) # NOTE: reduced MET cut in Setup.py

## SR2a
# SR2aZ
SR2laZ0p6  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
SR2maZ0p6  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2haZ0p6  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ0p6 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZ0p7  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZ0p7  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZ0p7  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ0p7 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZ0p8  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZ0p8  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZ0p8  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ0p8 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZ0p9  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZ0p9  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZ0p9  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ0p9 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZ1p0  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZ1p0  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZ1p0  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ1p0 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZ1p1  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZ1p1  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZ1p1  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ1p1 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZ1p2  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZ1p2  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZ1p2  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZ1p2 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2laZinf  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2maZinf  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2haZinf  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhaZinf = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

# SR2aX
SR2vlaX   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2laX    = SR2 + Region("mt", (0,60)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2maX    = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2haX    = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2aY
SR2vlaY   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2laY    = SR2 + Region("mt", (0,60)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2maY    = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2haY    = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2a
CR2aZ0p6  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
CR2aZ0p7  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aZ0p8  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aZ0p9  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aZ1p0  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aZ1p1  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aZ1p2  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aZinf  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
CR2aX     = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
CR2aY     = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 

## SR2b
# SR2bZ
SR2lbZ0p6  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
SR2mbZ0p6  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ0p6  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ0p6 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZ0p7  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZ0p7  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ0p7  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ0p7 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZ0p8  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZ0p8  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ0p8  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ0p8 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZ0p9  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZ0p9  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ0p9  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ0p9 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZ1p0  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZ1p0  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ1p0  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ1p0 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZ1p1  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZ1p1  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ1p1  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ1p1 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZ1p2  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZ1p2  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZ1p2  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZ1p2 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lbZinf  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mbZinf  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hbZinf  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhbZinf = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

# SR2bX
SR2vlbX   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2lbX    = SR2 + Region("mt", (60,95)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mbX    = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hbX    = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2bY
SR2vlbY   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2lbY    = SR2 + Region("mt", (60,95)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mbY    = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hbY    = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2b
CR2bZ0p6  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
CR2bZ0p7  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bZ0p8  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bZ0p9  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bZ1p0  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bZ1p1  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bZ1p2  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bZinf  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2bX     = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2bY     = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2c
# SR2cZ
SR2lcZ0p6  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
SR2mcZ0p6  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ0p6  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ0p6 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZ0p7  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZ0p7  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ0p7  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ0p7 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZ0p8  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZ0p8  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ0p8  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ0p8 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZ0p9  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZ0p9  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ0p9  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ0p9 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZ1p0  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZ1p0  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ1p0  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ1p0 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZ1p1  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZ1p1  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ1p1  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ1p1 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZ1p2  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZ1p2  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZ1p2  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZ1p2 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

SR2lcZinf  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mcZinf  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2hcZinf  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2vhcZinf = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon

# SR2cX
SR2lcX    = SR2 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcX    = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcX    = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2cY
SR2lcY    = SR2 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcY    = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcY    = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2c
CR2cZ0p6  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio 
CR2cZ0p7  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cZ0p8  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cZ0p9  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cZ1p0  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cZ1p1  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cZ1p2  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cZinf  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2cX     = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2cY     = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2d
# SR2dZ
SR2ldZ0p6  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon # NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
SR2mdZ0p6  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ0p6  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ0p6 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZ0p7  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZ0p7  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ0p7  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ0p7 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZ0p8  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZ0p8  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ0p8  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ0p8 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZ0p9  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZ0p9  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ0p9  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ0p9 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZ1p0  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZ1p0  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ1p0  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ1p0 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZ1p1  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZ1p1  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ1p1  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ1p1 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZ1p2  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZ1p2  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZ1p2  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZ1p2 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

SR2ldZinf  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
SR2mdZinf  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2hdZinf  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 
SR2vhdZinf = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,60)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon 

# SR2dX
SR2ldX    = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mdX    = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hdX    = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2dY
SR2ldY    = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mdY    = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hdY    = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2d
CR2dZ0p6  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0,0.6))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon# NOTE: reducing ISR jet pT cut further due to correlation with MET # NOTE: replaced CT2 cut with MET and HT ratio
CR2dZ0p7  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.6,0.7))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dZ0p8  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.7,0.8))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dZ0p9  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.8,0.9))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dZ1p0  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (0.9,1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dZ1p1  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1,1.1))    + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dZ1p2  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.1,1.2))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dZinf  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (60,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("(MET_pt/HT)", (1.2,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) + tightMuon
CR2dX     = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2dY     = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

signalRegions = [ # nSR = 312
             SR1laZ0p6, SR1maZ0p6, SR1haZ0p6, SR1vhaZ0p6,
             SR1laZ0p7, SR1maZ0p7, SR1haZ0p7, SR1vhaZ0p7,
             SR1laZ0p8, SR1maZ0p8, SR1haZ0p8, SR1vhaZ0p8,
             SR1laZ0p9, SR1maZ0p9, SR1haZ0p9, SR1vhaZ0p9,
             SR1laZ1p0, SR1maZ1p0, SR1haZ1p0, SR1vhaZ1p0,
             SR1laZ1p1, SR1maZ1p1, SR1haZ1p1, SR1vhaZ1p1,
             SR1laZ1p2, SR1maZ1p2, SR1haZ1p2, SR1vhaZ1p2,
             SR1laZinf, SR1maZinf, SR1haZinf, SR1vhaZinf,
    SR1vlaX, SR1laX, SR1maX, SR1haX, 
    SR1vlaY, SR1laY, SR1maY, SR1haY,
 
             SR1lbZ0p6, SR1mbZ0p6, SR1hbZ0p6, SR1vhbZ0p6,
             SR1lbZ0p7, SR1mbZ0p7, SR1hbZ0p7, SR1vhbZ0p7,
             SR1lbZ0p8, SR1mbZ0p8, SR1hbZ0p8, SR1vhbZ0p8,
             SR1lbZ0p9, SR1mbZ0p9, SR1hbZ0p9, SR1vhbZ0p9,
             SR1lbZ1p0, SR1mbZ1p0, SR1hbZ1p0, SR1vhbZ1p0,
             SR1lbZ1p1, SR1mbZ1p1, SR1hbZ1p1, SR1vhbZ1p1,
             SR1lbZ1p2, SR1mbZ1p2, SR1hbZ1p2, SR1vhbZ1p2,
             SR1lbZinf, SR1mbZinf, SR1hbZinf, SR1vhbZinf,
    SR1vlbX, SR1lbX, SR1mbX, SR1hbX, 
    SR1vlbY, SR1lbY, SR1mbY, SR1hbY,
 
             SR1lcZ0p6, SR1mcZ0p6, SR1hcZ0p6, SR1vhcZ0p6,
             SR1lcZ0p7, SR1mcZ0p7, SR1hcZ0p7, SR1vhcZ0p7,
             SR1lcZ0p8, SR1mcZ0p8, SR1hcZ0p8, SR1vhcZ0p8,
             SR1lcZ0p9, SR1mcZ0p9, SR1hcZ0p9, SR1vhcZ0p9,
             SR1lcZ1p0, SR1mcZ1p0, SR1hcZ1p0, SR1vhcZ1p0,
             SR1lcZ1p1, SR1mcZ1p1, SR1hcZ1p1, SR1vhcZ1p1,
             SR1lcZ1p2, SR1mcZ1p2, SR1hcZ1p2, SR1vhcZ1p2,
             SR1lcZinf, SR1mcZinf, SR1hcZinf, SR1vhcZinf,
             SR1lcX, SR1mcX, SR1hcX,
             SR1lcY, SR1mcY, SR1hcY, 
             
             SR1ldZ0p6, SR1mdZ0p6, SR1hdZ0p6, SR1vhdZ0p6,
             SR1ldZ0p7, SR1mdZ0p7, SR1hdZ0p7, SR1vhdZ0p7,
             SR1ldZ0p8, SR1mdZ0p8, SR1hdZ0p8, SR1vhdZ0p8,
             SR1ldZ0p9, SR1mdZ0p9, SR1hdZ0p9, SR1vhdZ0p9,
             SR1ldZ1p0, SR1mdZ1p0, SR1hdZ1p0, SR1vhdZ1p0,
             SR1ldZ1p1, SR1mdZ1p1, SR1hdZ1p1, SR1vhdZ1p1,
             SR1ldZ1p2, SR1mdZ1p2, SR1hdZ1p2, SR1vhdZ1p2,
             SR1ldZinf, SR1mdZinf, SR1hdZinf, SR1vhdZinf,
             SR1ldX, SR1mdX, SR1hdX,
             SR1ldY, SR1mdY, SR1hdY, 
             

             SR2laZ0p6, SR2maZ0p6, SR2haZ0p6, SR2vhaZ0p6,
             SR2laZ0p7, SR2maZ0p7, SR2haZ0p7, SR2vhaZ0p7,
             SR2laZ0p8, SR2maZ0p8, SR2haZ0p8, SR2vhaZ0p8,
             SR2laZ0p9, SR2maZ0p9, SR2haZ0p9, SR2vhaZ0p9,
             SR2laZ1p0, SR2maZ1p0, SR2haZ1p0, SR2vhaZ1p0,
             SR2laZ1p1, SR2maZ1p1, SR2haZ1p1, SR2vhaZ1p1,
             SR2laZ1p2, SR2maZ1p2, SR2haZ1p2, SR2vhaZ1p2,
             SR2laZinf, SR2maZinf, SR2haZinf, SR2vhaZinf,
    SR2vlaX, SR2laX, SR2maX, SR2haX, 
    SR2vlaY, SR2laY, SR2maY, SR2haY,
 
             SR2lbZ0p6, SR2mbZ0p6, SR2hbZ0p6, SR2vhbZ0p6,
             SR2lbZ0p7, SR2mbZ0p7, SR2hbZ0p7, SR2vhbZ0p7,
             SR2lbZ0p8, SR2mbZ0p8, SR2hbZ0p8, SR2vhbZ0p8,
             SR2lbZ0p9, SR2mbZ0p9, SR2hbZ0p9, SR2vhbZ0p9,
             SR2lbZ1p0, SR2mbZ1p0, SR2hbZ1p0, SR2vhbZ1p0,
             SR2lbZ1p1, SR2mbZ1p1, SR2hbZ1p1, SR2vhbZ1p1,
             SR2lbZ1p2, SR2mbZ1p2, SR2hbZ1p2, SR2vhbZ1p2,
             SR2lbZinf, SR2mbZinf, SR2hbZinf, SR2vhbZinf,
    SR2vlbX, SR2lbX, SR2mbX, SR2hbX, 
    SR2vlbY, SR2lbY, SR2mbY, SR2hbY,
 
             SR2lcZ0p6, SR2mcZ0p6, SR2hcZ0p6, SR2vhcZ0p6,
             SR2lcZ0p7, SR2mcZ0p7, SR2hcZ0p7, SR2vhcZ0p7,
             SR2lcZ0p8, SR2mcZ0p8, SR2hcZ0p8, SR2vhcZ0p8,
             SR2lcZ0p9, SR2mcZ0p9, SR2hcZ0p9, SR2vhcZ0p9,
             SR2lcZ1p0, SR2mcZ1p0, SR2hcZ1p0, SR2vhcZ1p0,
             SR2lcZ1p1, SR2mcZ1p1, SR2hcZ1p1, SR2vhcZ1p1,
             SR2lcZ1p2, SR2mcZ1p2, SR2hcZ1p2, SR2vhcZ1p2,
             SR2lcZinf, SR2mcZinf, SR2hcZinf, SR2vhcZinf,
             SR2lcX, SR2mcX, SR2hcX,
             SR2lcY, SR2mcY, SR2hcY,
             
             SR2ldZ0p6, SR2mdZ0p6, SR2hdZ0p6, SR2vhdZ0p6,
             SR2ldZ0p7, SR2mdZ0p7, SR2hdZ0p7, SR2vhdZ0p7,
             SR2ldZ0p8, SR2mdZ0p8, SR2hdZ0p8, SR2vhdZ0p8,
             SR2ldZ0p9, SR2mdZ0p9, SR2hdZ0p9, SR2vhdZ0p9,
             SR2ldZ1p0, SR2mdZ1p0, SR2hdZ1p0, SR2vhdZ1p0,
             SR2ldZ1p1, SR2mdZ1p1, SR2hdZ1p1, SR2vhdZ1p1,
             SR2ldZ1p2, SR2mdZ1p2, SR2hdZ1p2, SR2vhdZ1p2,
             SR2ldZinf, SR2mdZinf, SR2hdZinf, SR2vhdZinf,
             SR2ldX, SR2mdX, SR2hdX,
             SR2ldY, SR2mdY, SR2hdY
]

controlRegions= [ # nCR = 80
    CR1aZ0p6, CR1aZ0p7, CR1aZ0p8, CR1aZ0p9, CR1aZ1p0, CR1aZ1p1, CR1aZ1p2, CR1aZinf, CR1aX, CR1aY, 
    CR1bZ0p6, CR1bZ0p7, CR1bZ0p8, CR1bZ0p9, CR1bZ1p0, CR1bZ1p1, CR1bZ1p2, CR1bZinf, CR1bX, CR1bY, 
    CR1cZ0p6, CR1cZ0p7, CR1cZ0p8, CR1cZ0p9, CR1cZ1p0, CR1cZ1p1, CR1cZ1p2, CR1cZinf, CR1cX, CR1cY,
    CR1dZ0p6, CR1dZ0p7, CR1dZ0p8, CR1dZ0p9, CR1dZ1p0, CR1dZ1p1, CR1dZ1p2, CR1dZinf, CR1dX, CR1dY,
    
    CR2aZ0p6, CR2aZ0p7, CR2aZ0p8, CR2aZ0p9, CR2aZ1p0, CR2aZ1p1, CR2aZ1p2, CR2aZinf, CR2aX, CR2aY, 
    CR2bZ0p6, CR2bZ0p7, CR2bZ0p8, CR2bZ0p9, CR2bZ1p0, CR2bZ1p1, CR2bZ1p2, CR2bZinf, CR2bX, CR2bY, 
    CR2cZ0p6, CR2cZ0p7, CR2cZ0p8, CR2cZ0p9, CR2cZ1p0, CR2cZ1p1, CR2cZ1p2, CR2cZinf, CR2cX, CR2cY,
    CR2dZ0p6, CR2dZ0p7, CR2dZ0p8, CR2dZ0p9, CR2dZ1p0, CR2dZ1p1, CR2dZ1p2, CR2dZinf, CR2dX, CR2dY
]

regionMapping = { # CR:nSRs
    0:4, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 
    10:4, 11:4, 12:4, 13:4, 14:4, 15:4, 16:4, 17:4, 18:4, 19:4, 
    20:4, 21:4, 22:4, 23:4, 24:4, 25:4, 26:4, 27:4, 28:3, 29:3, 
    30:4, 31:4, 32:4, 33:4, 34:4, 35:4, 36:4, 37:4, 38:3, 39:3, 
    
    40:4, 41:4, 42:4, 43:4, 44:4, 45:4, 46:4, 47:4, 48:4, 49:4, 
    50:4, 51:4, 52:4, 53:4, 54:4, 55:4, 56:4, 57:4, 58:4, 59:4, 
    60:4, 61:4, 62:4, 63:4, 64:4, 65:4, 66:4, 67:4, 68:3, 69:3, 
    70:4, 71:4, 72:4, 73:4, 74:4, 75:4, 76:4, 77:4, 78:3, 79:3 
}

regionNames = [
    "CR1aZ0p6", "CR1aZ0p7", "CR1aZ0p8", "CR1aZ0p9", "CR1aZ1p0", "CR1aZ1p1", "CR1aZ1p2", "CR1aZinf", "CR1aX", "CR1aY", 
    "CR1bZ0p6", "CR1bZ0p7", "CR1bZ0p8", "CR1bZ0p9", "CR1bZ1p0", "CR1bZ1p1", "CR1bZ1p2", "CR1bZinf", "CR1bX", "CR1bY", 
    "CR1cZ0p6", "CR1cZ0p7", "CR1cZ0p8", "CR1cZ0p9", "CR1cZ1p0", "CR1cZ1p1", "CR1cZ1p2", "CR1cZinf", "CR1cX", "CR1cY",
    "CR1dZ0p6", "CR1dZ0p7", "CR1dZ0p8", "CR1dZ0p9", "CR1dZ1p0", "CR1dZ1p1", "CR1dZ1p2", "CR1dZinf", "CR1dX", "CR1dY",
    
    "CR2aZ0p6", "CR2aZ0p7", "CR2aZ0p8", "CR2aZ0p9", "CR2aZ1p0", "CR2aZ1p1", "CR2aZ1p2", "CR2aZinf", "CR2aX", "CR2aY", 
    "CR2bZ0p6", "CR2bZ0p7", "CR2bZ0p8", "CR2bZ0p9", "CR2bZ1p0", "CR2bZ1p1", "CR2bZ1p2", "CR2bZinf", "CR2bX", "CR2bY", 
    "CR2cZ0p6", "CR2cZ0p7", "CR2cZ0p8", "CR2cZ0p9", "CR2cZ1p0", "CR2cZ1p1", "CR2cZ1p2", "CR2cZinf", "CR2cX", "CR2cY",
    "CR2dZ0p6", "CR2dZ0p7", "CR2dZ0p8", "CR2dZ0p9", "CR2dZ1p0", "CR2dZ1p1", "CR2dZ1p2", "CR2dZinf", "CR2dX", "CR2dY",
             
             "SR1laZ0p6", "SR1maZ0p6", "SR1haZ0p6", "SR1vhaZ0p6",
             "SR1laZ0p7", "SR1maZ0p7", "SR1haZ0p7", "SR1vhaZ0p7",
             "SR1laZ0p8", "SR1maZ0p8", "SR1haZ0p8", "SR1vhaZ0p8",
             "SR1laZ0p9", "SR1maZ0p9", "SR1haZ0p9", "SR1vhaZ0p9",
             "SR1laZ1p0", "SR1maZ1p0", "SR1haZ1p0", "SR1vhaZ1p0",
             "SR1laZ1p1", "SR1maZ1p1", "SR1haZ1p1", "SR1vhaZ1p1",
             "SR1laZ1p2", "SR1maZ1p2", "SR1haZ1p2", "SR1vhaZ1p2",
             "SR1laZinf", "SR1maZinf", "SR1haZinf", "SR1vhaZinf",
    "SR1vlaX", "SR1laX", "SR1maX", "SR1haX", 
    "SR1vlaY", "SR1laY", "SR1maY", "SR1haY",
 
             "SR1lbZ0p6", "SR1mbZ0p6", "SR1hbZ0p6", "SR1vhbZ0p6",
             "SR1lbZ0p7", "SR1mbZ0p7", "SR1hbZ0p7", "SR1vhbZ0p7",
             "SR1lbZ0p8", "SR1mbZ0p8", "SR1hbZ0p8", "SR1vhbZ0p8",
             "SR1lbZ0p9", "SR1mbZ0p9", "SR1hbZ0p9", "SR1vhbZ0p9",
             "SR1lbZ1p0", "SR1mbZ1p0", "SR1hbZ1p0", "SR1vhbZ1p0",
             "SR1lbZ1p1", "SR1mbZ1p1", "SR1hbZ1p1", "SR1vhbZ1p1",
             "SR1lbZ1p2", "SR1mbZ1p2", "SR1hbZ1p2", "SR1vhbZ1p2",
             "SR1lbZinf", "SR1mbZinf", "SR1hbZinf", "SR1vhbZinf",
    "SR1vlbX", "SR1lbX", "SR1mbX", "SR1hbX", 
    "SR1vlbY", "SR1lbY", "SR1mbY", "SR1hbY",
 
             "SR1lcZ0p6", "SR1mcZ0p6", "SR1hcZ0p6", "SR1vhcZ0p6",
             "SR1lcZ0p7", "SR1mcZ0p7", "SR1hcZ0p7", "SR1vhcZ0p7",
             "SR1lcZ0p8", "SR1mcZ0p8", "SR1hcZ0p8", "SR1vhcZ0p8",
             "SR1lcZ0p9", "SR1mcZ0p9", "SR1hcZ0p9", "SR1vhcZ0p9",
             "SR1lcZ1p0", "SR1mcZ1p0", "SR1hcZ1p0", "SR1vhcZ1p0",
             "SR1lcZ1p1", "SR1mcZ1p1", "SR1hcZ1p1", "SR1vhcZ1p1",
             "SR1lcZ1p2", "SR1mcZ1p2", "SR1hcZ1p2", "SR1vhcZ1p2",
             "SR1lcZinf", "SR1mcZinf", "SR1hcZinf", "SR1vhcZinf",
             "SR1lcX", "SR1mcX", "SR1hcX",
             "SR1lcY", "SR1mcY", "SR1hcY", 
             
             "SR1ldZ0p6", "SR1mdZ0p6", "SR1hdZ0p6", "SR1vhdZ0p6",
             "SR1ldZ0p7", "SR1mdZ0p7", "SR1hdZ0p7", "SR1vhdZ0p7",
             "SR1ldZ0p8", "SR1mdZ0p8", "SR1hdZ0p8", "SR1vhdZ0p8",
             "SR1ldZ0p9", "SR1mdZ0p9", "SR1hdZ0p9", "SR1vhdZ0p9",
             "SR1ldZ1p0", "SR1mdZ1p0", "SR1hdZ1p0", "SR1vhdZ1p0",
             "SR1ldZ1p1", "SR1mdZ1p1", "SR1hdZ1p1", "SR1vhdZ1p1",
             "SR1ldZ1p2", "SR1mdZ1p2", "SR1hdZ1p2", "SR1vhdZ1p2",
             "SR1ldZinf", "SR1mdZinf", "SR1hdZinf", "SR1vhdZinf",
             "SR1ldX", "SR1mdX", "SR1hdX",
             "SR1ldY", "SR1mdY", "SR1hdY", 
             

             "SR2laZ0p6", "SR2maZ0p6", "SR2haZ0p6", "SR2vhaZ0p6", 
             "SR2laZ0p7", "SR2maZ0p7", "SR2haZ0p7", "SR2vhaZ0p7", 
             "SR2laZ0p8", "SR2maZ0p8", "SR2haZ0p8", "SR2vhaZ0p8", 
             "SR2laZ0p9", "SR2maZ0p9", "SR2haZ0p9", "SR2vhaZ0p9", 
             "SR2laZ1p0", "SR2maZ1p0", "SR2haZ1p0", "SR2vhaZ1p0", 
             "SR2laZ1p1", "SR2maZ1p1", "SR2haZ1p1", "SR2vhaZ1p1", 
             "SR2laZ1p2", "SR2maZ1p2", "SR2haZ1p2", "SR2vhaZ1p2", 
             "SR2laZinf", "SR2maZinf", "SR2haZinf", "SR2vhaZinf", 
    "SR2vlaX", "SR2laX", "SR2maX", "SR2haX", 
    "SR2vlaY", "SR2laY", "SR2maY", "SR2haY",
 
             "SR2lbZ0p6", "SR2mbZ0p6", "SR2hbZ0p6", "SR2vhbZ0p6",
             "SR2lbZ0p7", "SR2mbZ0p7", "SR2hbZ0p7", "SR2vhbZ0p7",
             "SR2lbZ0p8", "SR2mbZ0p8", "SR2hbZ0p8", "SR2vhbZ0p8",
             "SR2lbZ0p9", "SR2mbZ0p9", "SR2hbZ0p9", "SR2vhbZ0p9",
             "SR2lbZ1p0", "SR2mbZ1p0", "SR2hbZ1p0", "SR2vhbZ1p0",
             "SR2lbZ1p1", "SR2mbZ1p1", "SR2hbZ1p1", "SR2vhbZ1p1",
             "SR2lbZ1p2", "SR2mbZ1p2", "SR2hbZ1p2", "SR2vhbZ1p2",
             "SR2lbZinf", "SR2mbZinf", "SR2hbZinf", "SR2vhbZinf",
    "SR2vlbX", "SR2lbX", "SR2mbX", "SR2hbX", 
    "SR2vlbY", "SR2lbY", "SR2mbY", "SR2hbY",
 
             "SR2lcZ0p6", "SR2mcZ0p6", "SR2hcZ0p6", "SR2vhcZ0p6",
             "SR2lcZ0p7", "SR2mcZ0p7", "SR2hcZ0p7", "SR2vhcZ0p7",
             "SR2lcZ0p8", "SR2mcZ0p8", "SR2hcZ0p8", "SR2vhcZ0p8",
             "SR2lcZ0p9", "SR2mcZ0p9", "SR2hcZ0p9", "SR2vhcZ0p9",
             "SR2lcZ1p0", "SR2mcZ1p0", "SR2hcZ1p0", "SR2vhcZ1p0",
             "SR2lcZ1p1", "SR2mcZ1p1", "SR2hcZ1p1", "SR2vhcZ1p1",
             "SR2lcZ1p2", "SR2mcZ1p2", "SR2hcZ1p2", "SR2vhcZ1p2",
             "SR2lcZinf", "SR2mcZinf", "SR2hcZinf", "SR2vhcZinf",
             "SR2lcX",  "SR2mcX", "SR2hcX",
             "SR2lcY",  "SR2mcY", "SR2hcY",
             
             "SR2ldZ0p6", "SR2mdZ0p6", "SR2hdZ0p6", "SR2vhdZ0p6",
             "SR2ldZ0p7", "SR2mdZ0p7", "SR2hdZ0p7", "SR2vhdZ0p7",
             "SR2ldZ0p8", "SR2mdZ0p8", "SR2hdZ0p8", "SR2vhdZ0p8",
             "SR2ldZ0p9", "SR2mdZ0p9", "SR2hdZ0p9", "SR2vhdZ0p9",
             "SR2ldZ1p0", "SR2mdZ1p0", "SR2hdZ1p0", "SR2vhdZ1p0",
             "SR2ldZ1p1", "SR2mdZ1p1", "SR2hdZ1p1", "SR2vhdZ1p1",
             "SR2ldZ1p2", "SR2mdZ1p2", "SR2hdZ1p2", "SR2vhdZ1p2",
             "SR2ldZinf", "SR2mdZinf", "SR2hdZinf", "SR2vhdZinf",
             "SR2ldX",  "SR2mdX", "SR2hdX",
             "SR2ldY",  "SR2mdY", "SR2hdY"
]
