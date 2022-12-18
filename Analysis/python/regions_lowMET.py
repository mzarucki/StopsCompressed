from math import pi

from StopsCompressed.Analysis.Region import Region

# Put all sets of regions that are used in the analysis, closure, tables, etc.

# Adding lowMET region Z with 200 < CT < 300 GeV
# NOTE: MET plateau ~ 200 GeV
# NOTE: muon plateau ~ 8 GeV and cut at 6 GeV (~ 85 %)    # NOTE: abs(eta) < 1.5
# NOTE: jet plateau ~ 140 GeV and cut at 130 GeV (~ 90 %) # NOTE: all jets already have abs(eta) < 2.4

# nSR = 62
# nCR = 18
# nSR + nCR = 80 regions

### SR1
SR1 = Region("HT", (300,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) # NOTE: reducing HT cut due to correlation with CT1 
#SR1 = Region("MET_pt", (200,-999)) + Region("HT", (300,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) # NOTE: adding reduced MET cut and reducing HT cut as well due to correlation with CT1 
signalRegions = []
controlRegions = []
region = {}

## SR1a
# SR1aZ
SR1laZ  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
SR1maZ  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
SR1haZ  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))

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
CR1aZ   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
CR1aX   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999)) 
CR1aY   = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

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
SR1lcZ  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (6,12))  + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1mcZ  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 
SR1hcZ  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (200,300)) + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) 

# SR1cX
SR1lcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999)) 
SR1mcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))
SR1hcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (300,400)) + Region("ISRJets_pt", (100,-999))

# SR1cY
SR1lcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999)) 
SR1mcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))
SR1hcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

## CR1c
CR1cZ   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (200,300))  + Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13))
CR1cX   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (300,400))  + Region("ISRJets_pt", (100,-999))
CR1cY   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region("CT1", (400,-999)) + Region("ISRJets_pt", (100,-999))

### SR2
SR2 = Region("HT", (300,-999))  + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0))
#SR2 = Region("MET_pt", (200,-999)) + Region("HT", (300,-999)) + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) # NOTE: adding reduced MET cut

## SR2a
# SR2aZ
SR2laZ  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) # NOTE: reducing ISR jet pT cut due to correlation with CT2
SR2maZ  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13))
SR2haZ  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13))

# SR2aX
SR2vlaX = SR2 + Region("mt", (0,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2laX  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2maX  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2haX  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2aY
SR2vlaY = SR2 + Region("mt", (0,60)) + Region("l1_pt", (3.5,5)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2laY  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2maY  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2haY  = SR2 + Region("mt", (0,60)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2a
CR2aZ   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999))+ Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2aX   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999))+ Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
CR2aY   = SR2 + Region("mt", (0,60)) + Region("l1_pt", (30,-999))+ Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 

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
SR2lcZ  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (6,12))  + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2mcZ  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
SR2hcZ  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (200,300)) + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 

# SR2cX
SR2lcX  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcX  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcX  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (300,400)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

# SR2cY
SR2lcY  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2mcY  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))
SR2hcY  = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

## CR2c
CR2cZ   = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (200,300))  + Region("ISRJets_pt", (225,-999)) + Region("l1_eta", (-1.5, 1.5)) + Region("abs(l1_pdgId)", (13,13)) 
CR2cX   = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (300,400))  + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4)) 
CR2cY   = SR2 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region("CT2", (400,-999)) + Region("ISRJets_pt", (325,-999)) + Region("l1_eta", (-2.4, 2.4))

signalRegions = [ # nSR = 62 
             SR1laZ, SR1maZ, SR1haZ, 
    SR1vlaX, SR1laX, SR1maX, SR1haX, 
    SR1vlaY, SR1laY, SR1maY, SR1haY,
 
             SR1lbZ, SR1mbZ, SR1hbZ, 
    SR1vlbX, SR1lbX, SR1mbX, SR1hbX, 
    SR1vlbY, SR1lbY, SR1mbY, SR1hbY,
 
             SR1lcZ,  SR1mcZ, SR1hcZ,
             SR1lcX,  SR1mcX, SR1hcX,
             SR1lcY,  SR1mcY, SR1hcY, 


             SR2laZ, SR2maZ, SR2haZ, 
    SR2vlaX, SR2laX, SR2maX, SR2haX, 
    SR2vlaY, SR2laY, SR2maY, SR2haY,
 
             SR2lbZ, SR2mbZ, SR2hbZ, 
    SR2vlbX, SR2lbX, SR2mbX, SR2hbX, 
    SR2vlbY, SR2lbY, SR2mbY, SR2hbY,
 
             SR2lcZ,  SR2mcZ, SR2hcZ,
             SR2lcX,  SR2mcX, SR2hcX,
             SR2lcY,  SR2mcY, SR2hcY
]

controlRegions= [ # nCR = 18
    CR1aZ, CR1aX, CR1aY, 
    CR1bZ, CR1bX, CR1bY, 
    CR1cZ, CR1cX, CR1cY,
 
    CR2aZ, CR2aX, CR2aY, 
    CR2bZ, CR2bX, CR2bY, 
    CR2cZ, CR2cX, CR2cY
]

regionMapping = { # CR:nSRs
    0:3, 1:4, 2:4, 
    3:3, 4:4, 5:4,
    6:3, 7:3, 8:3,
 
    9:3, 10:4, 11:4,
    12:3, 13:4, 14:4,
    15:3, 16:3, 17:3
}

regionNames = [
    "CR1aZ", "CR1aX", "CR1aY", 
    "CR1bZ", "CR1bX", "CR1bY", 
    "CR1cZ", "CR1cX", "CR1cY",
 
    "CR2aZ", "CR2aX", "CR2aY", 
    "CR2bZ", "CR2bX", "CR2bY", 
    "CR2cZ", "CR2cX", "CR2cY",

               "SR1laZ", "SR1maZ", "SR1haZ", 
    "SR1vlaX", "SR1laX", "SR1maX", "SR1haX", 
    "SR1vlaY", "SR1laY", "SR1maY", "SR1haY",
 
               "SR1lbZ", "SR1mbZ", "SR1hbZ", 
    "SR1vlbX", "SR1lbX", "SR1mbX", "SR1hbX", 
    "SR1vlbY", "SR1lbY", "SR1mbY", "SR1hbY",
 
             "SR1lcZ", "SR1mcZ", "SR1hcZ",
             "SR1lcX", "SR1mcX", "SR1hcX",
             "SR1lcY", "SR1mcY", "SR1hcY", 


               "SR2laZ", "SR2maZ", "SR2haZ", 
    "SR2vlaX", "SR2laX", "SR2maX", "SR2haX", 
    "SR2vlaY", "SR2laY", "SR2maY", "SR2haY",
 
               "SR2lbZ", "SR2mbZ", "SR2hbZ", 
    "SR2vlbX", "SR2lbX", "SR2mbX", "SR2hbX", 
    "SR2vlbY", "SR2lbY", "SR2mbY", "SR2hbY",
 
             "SR2lcZ", "SR2mcZ", "SR2hcZ",
             "SR2lcX", "SR2mcX", "SR2hcX",
             "SR2lcY", "SR2mcY", "SR2hcY"
]
