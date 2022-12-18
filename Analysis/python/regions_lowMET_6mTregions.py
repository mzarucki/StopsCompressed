from math import pi

from StopsCompressed.Analysis.Region import Region

# Put all sets of regions that are used in the analysis, closure, tables, etc.

# Adding lowMET region Z with 200 < CT < 300 GeV
# NOTE: MET plateau ~ 200 GeV
# NOTE: muon plateau ~ 8 GeV and cut at 6 GeV (~ 85 %)    # NOTE: abs(eta) < 1.5
# NOTE: jet plateau ~ 140 GeV and cut at 130 GeV (~ 90 %) # NOTE: all jets already have abs(eta) < 2.4

# nSR = 120
# nCR = 36
# nSR + nCR = 156 regions

### SR1
SR1 = Region("HT", (300,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) # NOTE: reducing HT cut due to correlation with CT1 
#SR1 = Region("MET_pt", (200,-999)) + Region("HT", (300,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) # NOTE: adding reduced MET cut and reducing HT cut as well due to correlation with CT1
signalRegions = []
controlRegions = []
region = {}

## SR1a1
# SR1a1Z
SR1la1Z  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
SR1ma1Z  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
SR1ha1Z  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))

# SR1aX
SR1vla1X = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1la1X  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1ma1X  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1ha1X  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1a1Y
SR1vla1Y = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1la1Y  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1ma1Y  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1ha1Y  = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 

## CR1a1
CR1a1Z   = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
CR1a1X   = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) 
CR1a1Y   = SR1 + Region("mt", (0,40)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))


## SR1a2
# SR1a2Z
SR1la2Z  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
SR1ma2Z  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
SR1ha2Z  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))

# SR1a2X
SR1vla2X = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1la2X  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1ma2X  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1ha2X  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1a2Y
SR1vla2Y = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (3.5,5)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1la2Y  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1ma2Y  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1ha2Y  = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 

## CR1a2
CR1a2Z   = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
CR1a2X   = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) 
CR1a2Y   = SR1 + Region("mt", (40,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## SR1b
# SR1bZ
SR1lbZ  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1mbZ  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1hbZ  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 

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
CR1bZ   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
CR1bX   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) 
CR1bY   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 

## SR1c
# SR1cZ
SR1lcZ  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1mcZ  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1hcZ  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 

# SR1cX
SR1lcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999)) 
SR1mcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1hcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1cY
SR1lcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1mcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1hcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## CR1c
CR1cZ   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
CR1cX   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999))
CR1cY   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## SR1d
# SR1dZ
SR1ldZ  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1mdZ  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1hdZ  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 

# SR1dX
SR1ldX  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999)) 
SR1mdX  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1hdX  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1dY
SR1ldY  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1mdY  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1hdY  = SR1 + Region("mt", (130,160)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## CR1d
CR1dZ   = SR1 + Region("mt", (130,160)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
CR1dX   = SR1 + Region("mt", (130,160)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999))
CR1dY   = SR1 + Region("mt", (130,160)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## SR1e
# SR1eZ
SR1leZ  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1meZ  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1heZ  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 

# SR1eX
SR1leX  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999)) 
SR1meX  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1heX  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1eY
SR1leY  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1meY  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1heY  = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## CR1e
CR1eZ   = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
CR1eX   = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999))
CR1eY   = SR1 + Region("mt", (160,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

### SR2
SR2 = Region("HT", (300,-999)) + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0))
#SR2 = Region("MET_pt", (200,-999)) + Region("HT", (300,-999)) + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) # NOTE: adding reduced MET cut

## SR2a1
# SR2a1Z
SR2la1Z  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: reducing ISR jet pT cut due to correlation with CT2
SR2ma1Z  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2ha1Z  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2a1X
SR2vla1X = SR2 + Region("mt", (0,40)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2la1X  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ma1X  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ha1X  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2a1Y
SR2vla1Y = SR2 + Region("mt", (0,40)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2la1Y  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ma1Y  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ha1Y  = SR2 + Region("mt", (0,40)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2a1
CR2a1Z   = SR2 + Region("mt", (0,40)) + Region("l1_pt", (30,-999))+ Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2a1X   = SR2 + Region("mt", (0,40)) + Region("l1_pt", (30,-999))+ Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
CR2a1Y   = SR2 + Region("mt", (0,40)) + Region("l1_pt", (30,-999))+ Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 

## SR2a2
# SR2a2Z
SR2la2Z  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: reducing ISR jet pT cut due to correlation with CT2
SR2ma2Z  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2ha2Z  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2a2X
SR2vla2X = SR2 + Region("mt", (40,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2la2X  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ma2X  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ha2X  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2a2Y
SR2vla2Y = SR2 + Region("mt", (40,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2la2Y  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ma2Y  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2ha2Y  = SR2 + Region("mt", (40,60)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2a2
CR2a2Z   = SR2 + Region("mt", (40,60)) + Region("l1_pt", (30,-999))+ Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2a2X   = SR2 + Region("mt", (40,60)) + Region("l1_pt", (30,-999))+ Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
CR2a2Y   = SR2 + Region("mt", (40,60)) + Region("l1_pt", (30,-999))+ Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 

## SR2b
# SR2bZ
SR2lbZ  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2mbZ  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2hbZ  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2bX
SR2vlbX = SR2 + Region("mt", (60,95)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2lbX  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mbX  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hbX  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2bY
SR2vlbY = SR2 + Region("mt", (60,95)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2lbY  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mbY  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hbY  = SR2 + Region("mt", (60,95)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2b
CR2bZ   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13))
CR2bX   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2bY   = SR2 + Region("mt", (60,95)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2c
# SR2cZ
SR2lcZ  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2mcZ  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2hcZ  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2cX
SR2lcX  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcX  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcX  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2cY
SR2lcY  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999))  + Region("l1_eta", (-2.4, 2.4))
SR2mcY  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999))  + Region("l1_eta", (-2.4, 2.4))
SR2hcY  = SR2 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999))  + Region("l1_eta", (-2.4, 2.4))

## CR2c
CR2cZ   = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2cX   = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2cY   = SR2 + Region("mt", (95,130)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2d
# SR2dZ
SR2ldZ  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2mdZ  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2hdZ  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2dX
SR2ldX  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mdX  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hdX  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2dY
SR2ldY  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mdY  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hdY  = SR2 + Region("mt", (130,160)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2d
CR2dZ   = SR2 + Region("mt", (130,160)) + Region("l1_pt", (30,-999)) + Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2dX   = SR2 + Region("mt", (130,160)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2dY   = SR2 + Region("mt", (130,160)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## SR2e
# SR2eZ
SR2leZ  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2meZ  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2heZ  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2dX
SR2leX  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2meX  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2heX  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2eY
SR2leY  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2meY  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2heY  = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2e
CR2eZ   = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2eX   = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2eY   = SR2 + Region("mt", (160,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

signalRegions = [ # nSR = 120
              SR1la1Z, SR1ma1Z, SR1ha1Z, 
    SR1vla1X, SR1la1X, SR1ma1X, SR1ha1X, 
    SR1vla1Y, SR1la1Y, SR1ma1Y, SR1ha1Y,
             
              SR1la2Z, SR1ma2Z, SR1ha2Z, 
    SR1vla2X, SR1la2X, SR1ma2X, SR1ha2X, 
    SR1vla2Y, SR1la2Y, SR1ma2Y, SR1ha2Y,
 
             SR1lbZ, SR1mbZ, SR1hbZ, 
    SR1vlbX, SR1lbX, SR1mbX, SR1hbX, 
    SR1vlbY, SR1lbY, SR1mbY, SR1hbY,
 
             SR1lcZ,  SR1mcZ, SR1hcZ,
             SR1lcX,  SR1mcX, SR1hcX,
             SR1lcY,  SR1mcY, SR1hcY, 
             
             SR1ldZ,  SR1mdZ, SR1hdZ,
             SR1ldX,  SR1mdX, SR1hdX,
             SR1ldY,  SR1mdY, SR1hdY, 
             
             SR1leZ,  SR1meZ, SR1heZ,
             SR1leX,  SR1meX, SR1heX,
             SR1leY,  SR1meY, SR1heY, 


              SR2la1Z, SR2ma1Z, SR2ha1Z, 
    SR2vla1X, SR2la1X, SR2ma1X, SR2ha1X, 
    SR2vla1Y, SR2la1Y, SR2ma1Y, SR2ha1Y,
             
              SR2la2Z, SR2ma2Z, SR2ha2Z, 
    SR2vla2X, SR2la2X, SR2ma2X, SR2ha2X, 
    SR2vla2Y, SR2la2Y, SR2ma2Y, SR2ha2Y,
 
             SR2lbZ, SR2mbZ, SR2hbZ, 
    SR2vlbX, SR2lbX, SR2mbX, SR2hbX, 
    SR2vlbY, SR2lbY, SR2mbY, SR2hbY,
 
             SR2lcZ,  SR2mcZ, SR2hcZ,
             SR2lcX,  SR2mcX, SR2hcX,
             SR2lcY,  SR2mcY, SR2hcY,
             
             SR2ldZ,  SR2mdZ, SR2hdZ,
             SR2ldX,  SR2mdX, SR2hdX,
             SR2ldY,  SR2mdY, SR2hdY,
             
             SR2leZ,  SR2meZ, SR2heZ,
             SR2leX,  SR2meX, SR2heX,
             SR2leY,  SR2meY, SR2heY
]

controlRegions= [ # nCR = 36
    CR1a1Z, CR1a1X, CR1a1Y, 
    CR1a2Z, CR1a2X, CR1a2Y, 
    CR1bZ, CR1bX, CR1bY, 
    CR1cZ, CR1cX, CR1cY,
    CR1dZ, CR1dX, CR1dY,
    CR1eZ, CR1eX, CR1eY,
 
    CR2a1Z, CR2a1X, CR2a1Y, 
    CR2a2Z, CR2a2X, CR2a2Y, 
    CR2bZ, CR2bX, CR2bY, 
    CR2cZ, CR2cX, CR2cY,
    CR2dZ, CR2dX, CR2dY,
    CR2eZ, CR2eX, CR2eY
]

regionMapping = { # CR:nSRs
    0:3, 1:4, 2:4, 
    3:3, 4:4, 5:4, 
    6:3, 7:4, 8:4,
    9:3, 10:3, 11:3,
    12:3, 13:3, 14:3,
    15:3, 16:3, 17:3,
 
    18:3, 19:4, 20:4,
    21:3, 22:4, 23:4,
    24:3, 25:4, 26:4,
    27:3, 28:3, 29:3,
    30:3, 31:3, 32:3,
    33:3, 34:3, 35:3
}

regionNames = [
    "CR1a1Z", "CR1a1X", "CR1a1Y", 
    "CR1a2Z", "CR1a2X", "CR1a2Y", 
    "CR1bZ", "CR1bX", "CR1bY", 
    "CR1cZ", "CR1cX", "CR1cY",
    "CR1dZ", "CR1dX", "CR1dY",
    "CR1eZ", "CR1eX", "CR1eY",
 
    "CR2a1Z", "CR2a1X", "CR2a1Y", 
    "CR2a2Z", "CR2a2X", "CR2a2Y", 
    "CR2bZ", "CR2bX", "CR2bY", 
    "CR2cZ", "CR2cX", "CR2cY",
    "CR2dZ", "CR2dX", "CR2dY",
    "CR2eZ", "CR2eX", "CR2eY",

                "SR1la1Z", "SR1ma1Z", "SR1ha1Z", 
    "SR1vla1X", "SR1la1X", "SR1ma1X", "SR1ha1X", 
    "SR1vla1Y", "SR1la1Y", "SR1ma1Y", "SR1ha1Y",
               
                "SR1la2Z", "SR1ma2Z", "SR1ha2Z", 
    "SR1vla2X", "SR1la2X", "SR1ma2X", "SR1ha2X", 
    "SR1vla2Y", "SR1la2Y", "SR1ma2Y", "SR1ha2Y",
 
               "SR1lbZ", "SR1mbZ", "SR1hbZ", 
    "SR1vlbX", "SR1lbX", "SR1mbX", "SR1hbX", 
    "SR1vlbY", "SR1lbY", "SR1mbY", "SR1hbY",
 
               "SR1lcZ", "SR1mcZ", "SR1hcZ",
               "SR1lcX", "SR1mcX", "SR1hcX",
               "SR1lcY", "SR1mcY", "SR1hcY", 
               
               "SR1ldZ", "SR1mdZ", "SR1hdZ",
               "SR1ldX", "SR1mdX", "SR1hdX",
               "SR1ldY", "SR1mdY", "SR1hdY", 
               
               "SR1leZ", "SR1meZ", "SR1heZ",
               "SR1leX", "SR1meX", "SR1heX",
               "SR1leY", "SR1meY", "SR1heY", 


                "SR2la1Z", "SR2ma1Z", "SR2ha1Z", 
    "SR2vla1X", "SR2la1X", "SR2ma1X", "SR2ha1X", 
    "SR2vla1Y", "SR2la1Y", "SR2ma1Y", "SR2ha1Y",
               
                "SR2la2Z", "SR2ma2Z", "SR2ha2Z", 
    "SR2vla2X", "SR2la2X", "SR2ma2X", "SR2ha2X", 
    "SR2vla2Y", "SR2la2Y", "SR2ma2Y", "SR2ha2Y",
 
               "SR2lbZ", "SR2mbZ", "SR2hbZ", 
    "SR2vlbX", "SR2lbX", "SR2mbX", "SR2hbX", 
    "SR2vlbY", "SR2lbY", "SR2mbY", "SR2hbY",
 
               "SR2lcZ", "SR2mcZ", "SR2hcZ",
               "SR2lcX", "SR2mcX", "SR2hcX",
               "SR2lcY", "SR2mcY", "SR2hcY",
               
               "SR2ldZ", "SR2mdZ", "SR2hdZ",
               "SR2ldX", "SR2mdX", "SR2hdX",
               "SR2ldY", "SR2mdY", "SR2hdY",
               
               "SR2leZ", "SR2meZ", "SR2heZ",
               "SR2leX", "SR2meX", "SR2heX",
               "SR2leY", "SR2meY", "SR2heY"
]
