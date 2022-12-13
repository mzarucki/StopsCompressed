from math import pi

from StopsCompressed.Analysis.Region import Region

# Put all sets of regions that are used in the analysis, closure, tables, etc.

# nSR = 44
# nCR = 12
# nSR + nCR = 56 regions

### SR1
SR1 = Region("HT", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5))
signalRegions  = []
controlRegions = []
region = {}

## SR1a
# SR1aX
SR1vlaX = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (300,400))    
SR1laX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (300,400)) 
SR1maX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1haX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

# SR1aY
SR1vlaY = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (400,-999))    
SR1laY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999))   
SR1maY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999))  
SR1haY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999))  

## CR1a
CR1aX   = SR1 + Region("mt", (0,60))  + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,-999)) + Region ("CT1", (300,400))   
CR1aY   = SR1 + Region("mt", (0,60))  + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,-999)) + Region ("CT1", (400, -999)) 

## SR1b
# SR1bX
SR1vlbX = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (300,400))   
SR1lbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (300,400)) 
SR1mbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1hbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

# SR1bY
SR1vlbY = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (400,-999)) 
SR1lbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999)) 
SR1mbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999)) 
SR1hbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999)) 

## CR1b
CR1bX   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,-999)) + Region ("CT1", (300,400))   
CR1bY   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,-999)) + Region ("CT1", (400, -999)) 

## SR1c
# SR1cX
SR1lcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region ("CT1", (300,400))   
SR1mcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1hcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

# SR1cY
SR1lcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999)) 
SR1mcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999)) 
SR1hcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999)) 

## CR1c
CR1cX   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region ("CT1", (300,400))   
CR1cY   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,-999)) + Region ("CT1", (400, -999)) 

### SR2
SR2 = Region("HT", (300,-999)) + Region("ISRJets_pt", (325,-999)) + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-2.4, 2.4))

## SR2a
# SR2aX
SR2vlaX = SR2 + Region("mt", (0,60))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (300,400))   
SR2laX  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2maX  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2haX  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

# SR2aY
SR2vlaY = SR2 + Region("mt", (0,60))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (400,-999)) 
SR2laY  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2maY  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2haY  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

## CR2a
CR2aX   = SR2 + Region("mt", (0,60))   + Region("l1_pt", (30,-999))+ Region ("CT2", (300,400))   
CR2aY   = SR2 + Region("mt", (0,60))   + Region("l1_pt", (30,-999))+ Region ("CT2", (400, -999))  

## SR2b
# SR2bX
SR2vlbX = SR2 + Region("mt", (60,95))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (300,400))   
SR2lbX  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2mbX  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2hbX  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

# SR2bY
SR2vlbY = SR2 + Region("mt", (60,95))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (400,-999))  
SR2lbY  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2mbY  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2hbY  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

## CR2b
CR2bX    = SR2 + Region("mt", (60,95))   + Region("l1_pt", (30,-999)) + Region ("CT2", (300,400)) 
CR2bY    = SR2 + Region("mt", (60,95))   + Region("l1_pt", (30,-999)) + Region ("CT2", (400, -999)) 

## SR2c
# SR2cX
SR2lcX  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2mcX  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2hcX  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

# SR2cY
SR2lcY  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2mcY  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2hcY  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

# CR2c
CR2cX    = SR2 + Region("mt", (95,-999))   + Region("l1_pt", (30,-999)) + Region ("CT2", (300,400)) 
CR2cY    = SR2 + Region("mt", (95,-999))   + Region("l1_pt", (30,-999)) + Region ("CT2", (400, -999)) 

signalRegions = [ # nSR = 44
    SR1vlaX, SR1laX, SR1maX, SR1haX, 
    SR1vlaY, SR1laY, SR1maY, SR1haY,
 
    SR1vlbX, SR1lbX, SR1mbX, SR1hbX, 
    SR1vlbY, SR1lbY, SR1mbY, SR1hbY,
 
             SR1lcX, SR1mcX, SR1hcX, 
             SR1lcY, SR1mcY, SR1hcY, 

    
    SR2vlaX, SR2laX, SR2maX, SR2haX, 
    SR2vlaY, SR2laY, SR2maY, SR2haY,
 
    SR2vlbX, SR2lbX, SR2mbX, SR2hbX, 
    SR2vlbY, SR2lbY, SR2mbY, SR2hbY,
 
             SR2lcX, SR2mcX, SR2hcX,
             SR2lcY, SR2mcY, SR2hcY
]

controlRegions= [ # nCR = 12
    CR1aX, CR1aY, CR1bX, CR1bY, CR1cX, CR1cY, 
    CR2aX, CR2aY, CR2bX, CR2bY, CR2cX, CR2cY
]

regionMapping = { # CR:nSRs
    0:4, 1:4, 2:4, 3:4, 4:3, 5:3,
    6:4, 7:4, 8:4, 9:4, 10:3, 11:3
}

regionNames = [
    "CR1aX", "CR1aY", "CR1bX", "CR1bY", "CR1cX", "CR1cY", 
    "CR2aX", "CR2aY", "CR2bX", "CR2bY", "CR2cX", "CR2cY",

    "SR1vlaX", "SR1laX", "SR1maX", "SR1haX", 
    "SR1vlaY", "SR1laY", "SR1maY", "SR1haY",
 
    "SR1vlbX", "SR1lbX", "SR1mbX", "SR1hbX", 
    "SR1vlbY", "SR1lbY", "SR1mbY", "SR1hbY",
 
               "SR1lcX", "SR1mcX", "SR1hcX", 
               "SR1lcY", "SR1mcY", "SR1hcY", 

    "SR2vlaX", "SR2laX", "SR2maX", "SR2haX", 
    "SR2vlaY", "SR2laY", "SR2maY", "SR2haY",
 
    "SR2vlbX", "SR2lbX", "SR2mbX", "SR2hbX", 
    "SR2vlbY", "SR2lbY", "SR2mbY", "SR2hbY",
 
               "SR2lcX", "SR2mcX", "SR2hcX",
               "SR2lcY", "SR2mcY", "SR2hcY"
]
