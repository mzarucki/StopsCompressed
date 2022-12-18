from math import pi

from StopsCompressed.Analysis.Region import Region

# Put all sets of regions that are used in the analysis, closure, tables, etc.

# Adding lowMET region Z with 200 < CT < 300 GeV
# NOTE: MET plateau ~ 200 GeV
# NOTE: muon plateau ~ 8 GeV and cut at 6 GeV (~ 85 %)    # NOTE: abs(eta) < 1.5
# NOTE: jet plateau ~ 140 GeV and cut at 130 GeV (~ 90 %) # NOTE: all jets already have abs(eta) < 2.4

# nSR = 104
# nCR = 32
# nSR + nCR = 136 regions

### SR1
SR1 = Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) #NOTE: reduced MET and HT cuts in Setup.py 
signalRegions = []
controlRegions = []
region = {}

## SR1a
# SR1aZ
SR1laZ1 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1maZ1 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1haZ1 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

SR1laZ2 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1maZ2 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1haZ2 = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

# SR1aX
SR1vlaX = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1laX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1maX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1haX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1aY
SR1vlaY = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1laY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1maY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1haY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 

## CR1a
CR1aZ1  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1aZ2  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1aX   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) 
CR1aY   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## SR1b
# SR1bZ
SR1lbZ1 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1mbZ1 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1hbZ1 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

SR1lbZ2 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1mbZ2 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1hbZ2 = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

# SR1bX
SR1vlbX = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1lbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1mbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1hbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1bY
SR1vlbY = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1lbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1mbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1hbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 

## CR1b
CR1bZ1  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1bZ2  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1bX   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) 
CR1bY   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 

## SR1c
# SR1cZ
SR1lcZ1 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1mcZ1 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1hcZ1 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

SR1lcZ2 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1mcZ2 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1hcZ2 = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

# SR1cX
SR1lcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999)) 
SR1mcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1hcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1cY
SR1lcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1mcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1hcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## CR1c
CR1cZ1  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1cZ2  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1cX   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999))
CR1cY   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## SR1d
# SR1dZ
SR1ldZ1 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts 
SR1mdZ1 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1hdZ1 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

SR1ldZ2 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts 
SR1mdZ2 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1hdZ2 = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts

# SR1dX
SR1ldX  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999)) 
SR1mdX  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1hdX  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1dY
SR1ldY  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1mdY  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1hdY  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## CR1d
CR1dZ1  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1dZ2  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("HT", (300,400)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replaced CT1 with separate MET and HT cuts
CR1dX   = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999))
CR1dY   = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

### SR2
SR2 =  Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) # NOTE: reduced MET cut in Setup.py

## SR2a
# SR2aZ
SR2laZ1 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: reducing ISR jet pT cut due to correlation with CT2 # NOTE: replacing CT2 cut with MET cut
SR2maZ1 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2haZ1 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

SR2laZ2 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: reducing ISR jet pT cut due to correlation with CT2 # NOTE: replacing CT2 cut with MET cut
SR2maZ2 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2haZ2 = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2aX
SR2vlaX = SR2 + Region("mt", (0,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2laX  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2maX  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2haX  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2aY
SR2vlaY = SR2 + Region("mt", (0,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2laY  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2maY  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2haY  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2a
CR2aZ1   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300))+ Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
CR2aZ2   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999))+ Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
CR2aX   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
CR2aY   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 

## SR2b
# SR2bZ
SR2lbZ1 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2mbZ1 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2hbZ1 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut

SR2lbZ2 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2mbZ2 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2hbZ2 = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut

# SR2bX
SR2vlbX = SR2 + Region("mt", (60,95)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2lbX  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mbX  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hbX  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2bY
SR2vlbY = SR2 + Region("mt", (60,95)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2lbY  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mbY  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hbY  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2b
CR2bZ1  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
CR2bZ2  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
CR2bX   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2bY   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2c
# SR2cZ
SR2lcZ1 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2mcZ1 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2hcZ1 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut

SR2lcZ2 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2mcZ2 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2hcZ2 = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut

# SR2cX
SR2lcX  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcX  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcX  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2cY
SR2lcY  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcY  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcY  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2c
CR2cZ1  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut 
CR2cZ2  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999))  + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut 
CR2cX   = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2cY   = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2d
# SR2dZ
SR2ldZ1 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2mdZ1 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2hdZ1 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut

SR2ldZ2 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (6,12))  + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2mdZ2 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
SR2hdZ2 = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("MET_pt", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut

# SR2dX
SR2ldX  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mdX  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hdX  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2dY
SR2ldY  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mdY  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hdY  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2d
CR2dZ1  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,300)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
CR2dZ2  = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("MET_pt", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: replacing CT2 cut with MET cut
CR2dX   = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2dY   = SR2 + Region("mt", (130,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) + Region("l1_eta", (-2.4, 2.4))

signalRegions = [ # nSR = 104 
             SR1laZ1, SR1maZ1, SR1haZ1, 
             SR1laZ2, SR1maZ2, SR1haZ2, 
    SR1vlaX, SR1laX, SR1maX, SR1haX, 
    SR1vlaY, SR1laY, SR1maY, SR1haY,
 
             SR1lbZ1, SR1mbZ1, SR1hbZ1, 
             SR1lbZ2, SR1mbZ2, SR1hbZ2, 
    SR1vlbX, SR1lbX, SR1mbX, SR1hbX, 
    SR1vlbY, SR1lbY, SR1mbY, SR1hbY,
 
             SR1lcZ1,  SR1mcZ1, SR1hcZ1,
             SR1lcZ2,  SR1mcZ2, SR1hcZ2,
             SR1lcX,  SR1mcX, SR1hcX,
             SR1lcY,  SR1mcY, SR1hcY, 
             
             SR1ldZ1,  SR1mdZ1, SR1hdZ1,
             SR1ldZ2,  SR1mdZ2, SR1hdZ2,
             SR1ldX,  SR1mdX, SR1hdX,
             SR1ldY,  SR1mdY, SR1hdY, 


             SR2laZ1, SR2maZ1, SR2haZ1, 
             SR2laZ2, SR2maZ2, SR2haZ2, 
    SR2vlaX, SR2laX, SR2maX, SR2haX, 
    SR2vlaY, SR2laY, SR2maY, SR2haY,
 
             SR2lbZ1, SR2mbZ1, SR2hbZ1, 
             SR2lbZ2, SR2mbZ2, SR2hbZ2, 
    SR2vlbX, SR2lbX, SR2mbX, SR2hbX, 
    SR2vlbY, SR2lbY, SR2mbY, SR2hbY,
 
             SR2lcZ1,  SR2mcZ1, SR2hcZ1,
             SR2lcZ2,  SR2mcZ2, SR2hcZ2,
             SR2lcX,  SR2mcX, SR2hcX,
             SR2lcY,  SR2mcY, SR2hcY,
             
             SR2ldZ1,  SR2mdZ1, SR2hdZ1,
             SR2ldZ2,  SR2mdZ2, SR2hdZ2,
             SR2ldX,  SR2mdX, SR2hdX,
             SR2ldY,  SR2mdY, SR2hdY
]

controlRegions= [ # nCR = 32
    CR1aZ1, CR1aZ2, CR1aX, CR1aY, 
    CR1bZ1, CR1bZ2, CR1bX, CR1bY, 
    CR1cZ1, CR1cZ2, CR1cX, CR1cY,
    CR1dZ1, CR1dZ2, CR1dX, CR1dY,

    CR2aZ1, CR2aZ2, CR2aX, CR2aY, 
    CR2bZ1, CR2bZ2, CR2bX, CR2bY, 
    CR2cZ1, CR2cZ2, CR2cX, CR2cY,
    CR2dZ1, CR2dZ2, CR2dX, CR2dY
]

regionMapping = { # CR:nSRs
    0:3, 1:3, 2:4, 3:4, 
    4:3, 5:3, 6:4, 7:4,
    8:3, 9:3, 10:3, 11:3,
    12:3, 13:3, 14:3, 15:3,
 
    16:3, 17:3, 18:4, 19:4,
    20:3, 21:3, 22:4, 23:4,
    24:3, 25:3, 26:3, 27:3,
    28:3, 29:3, 30:3, 31:3
}

regionNames = [
    "CR1aZ1", "CR1aZ2", "CR1aX", "CR1aY", 
    "CR1bZ1", "CR1bZ2", "CR1bX", "CR1bY", 
    "CR1cZ1", "CR1cZ2", "CR1cX", "CR1cY",
    "CR1dZ1", "CR1dZ2", "CR1dX", "CR1dY",

    "CR2aZ1", "CR2aZ2", "CR2aX", "CR2aY", 
    "CR2bZ1", "CR2bZ2", "CR2bX", "CR2bY", 
    "CR2cZ1", "CR2cZ2", "CR2cX", "CR2cY",
    "CR2dZ1", "CR2dZ2", "CR2dX", "CR2dY",

               "SR1laZ1", "SR1maZ1", "SR1haZ1", 
               "SR1laZ2", "SR1maZ2", "SR1haZ2", 
    "SR1vlaX", "SR1laX", "SR1maX", "SR1haX", 
    "SR1vlaY", "SR1laY", "SR1maY", "SR1haY",
 
               "SR1lbZ1", "SR1mbZ1", "SR1hbZ1", 
               "SR1lbZ2", "SR1mbZ2", "SR1hbZ2", 
    "SR1vlbX", "SR1lbX", "SR1mbX", "SR1hbX", 
    "SR1vlbY", "SR1lbY", "SR1mbY", "SR1hbY",
 
               "SR1lcZ1", "SR1mcZ1", "SR1hcZ1",
               "SR1lcZ2", "SR1mcZ2", "SR1hcZ2",
               "SR1lcX", "SR1mcX", "SR1hcX",
               "SR1lcY", "SR1mcY", "SR1hcY", 
               
               "SR1ldZ1", "SR1mdZ1", "SR1hdZ1",
               "SR1ldZ2", "SR1mdZ2", "SR1hdZ2",
               "SR1ldX", "SR1mdX", "SR1hdX",
               "SR1ldY", "SR1mdY", "SR1hdY", 


               "SR2laZ1", "SR2maZ1", "SR2haZ1", 
               "SR2laZ2", "SR2maZ2", "SR2haZ2", 
    "SR2vlaX", "SR2laX", "SR2maX", "SR2haX", 
    "SR2vlaY", "SR2laY", "SR2maY", "SR2haY",
 
               "SR2lbZ1", "SR2mbZ1", "SR2hbZ1", 
               "SR2lbZ2", "SR2mbZ2", "SR2hbZ2", 
    "SR2vlbX", "SR2lbX", "SR2mbX", "SR2hbX", 
    "SR2vlbY", "SR2lbY", "SR2mbY", "SR2hbY",
 
               "SR2lcZ1", "SR2mcZ1", "SR2hcZ1",
               "SR2lcZ2", "SR2mcZ2", "SR2hcZ2",
               "SR2lcX", "SR2mcX", "SR2hcX",
               "SR2lcY", "SR2mcY", "SR2hcY",
               
               "SR2ldZ1", "SR2mdZ1", "SR2hdZ1",
               "SR2ldZ2", "SR2mdZ2", "SR2hdZ2",
               "SR2ldX", "SR2mdX", "SR2hdX",
               "SR2ldY", "SR2mdY", "SR2hdY"
]
