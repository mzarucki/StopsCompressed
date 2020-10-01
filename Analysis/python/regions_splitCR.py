from math import pi

from StopsCompressed.Analysis.Region      import Region

#def getRegionsFromThresholds(var, vals, gtLastThreshold = True):
#    return [Region(var, (vals[i], vals[i+1])) for i in range(len(vals)-1)]
#
#def getRegions2D(varOne, varOneThresholds, varTwo, varTwoThresholds):
#    regions_varOne  = getRegionsFromThresholds(varOne,  varOneThresholds)
#    regions_varTwo  = getRegionsFromThresholds(varTwo, varTwoThresholds)
#
#    regions2D = []
#    for r1 in regions_varOne:
#        for r2 in regions_varTwo:
#            regions2D.append(r1+r2)
#
#    return regions2D

#Put all sets of regions that are used in the analysis, closure, tables, etc.

SR1 = Region("HT", (400,-999)) + Region("ISRJets_pt", (100,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) 
signalRegions  = []
controlRegions = []
SR1vlaX = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (300,400))    
SR1laX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (300,400)) 
SR1maX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1haX  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

SR1vlaY = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (400,-999))    
SR1laY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999))   
SR1maY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999))  
SR1haY  = SR1 + Region("mt", (0,60)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999))  

CR1maX   = SR1 + Region("mt", (0,60))  + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,50)) + Region ("CT1", (300,400))   
CR1maY   = SR1 + Region("mt", (0,60))  + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,50)) + Region ("CT1", (400, -999)) 

CR1haX   = SR1 + Region("mt", (0,60))  + Region("l1_charge", (-1,-1))  + Region("l1_pt", (50,-999)) + Region ("CT1", (300,400))   
CR1haY   = SR1 + Region("mt", (0,60))  + Region("l1_charge", (-1,-1))  + Region("l1_pt", (50,-999)) + Region ("CT1", (400, -999)) 


SR1vlbX = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (300,400))   
SR1lbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (300,400)) 
SR1mbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1hbX  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

SR1vlbY = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (3.5,5)) + Region ("CT1", (400,-999)) 
SR1lbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999)) 
SR1mbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999)) 
SR1hbY  = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999)) 

CR1mbX   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,50)) + Region ("CT1", (300,400))   
CR1mbY   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (30,50)) + Region ("CT1", (400, -999)) 

CR1hbX   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (50,-999)) + Region ("CT1", (300,400))   
CR1hbY   = SR1 + Region("mt", (60,95)) + Region("l1_charge", (-1,-1))  + Region("l1_pt", (50,-999)) + Region ("CT1", (400, -999)) 

SR1lcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region ("CT1", (300,400))   
SR1mcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1hcX  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

SR1lcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999)) 
SR1mcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999)) 
SR1hcY  = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999)) 


CR1mcX   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,50)) + Region ("CT1", (300,400))   
CR1mcY   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (30,50)) + Region ("CT1", (400, -999)) 

CR1hcX   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (50,-999)) + Region ("CT1", (300,400))   
CR1hcY   = SR1 + Region("mt", (95,-999)) + Region("l1_pt", (50,-999)) + Region ("CT1", (400, -999)) 


SR2 = Region("HT", (300,-999)) + Region("ISRJets_pt", (325,-999)) + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-2.4, 2.4))

SR2vlaX = SR2 + Region("mt", (0,60))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (300,400))   
SR2laX  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2maX  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2haX  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

SR2vlaY = SR2 + Region("mt", (0,60))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (400,-999)) 
SR2laY  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2maY  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2haY  = SR2 + Region("mt", (0,60))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

CR2maX   = SR2 + Region("mt", (0,60))   + Region("l1_pt", (30,50))+ Region ("CT2", (300,400))   
CR2maY   = SR2 + Region("mt", (0,60))   + Region("l1_pt", (30,50))+ Region ("CT2", (400, -999))  

CR2haX   = SR2 + Region("mt", (0,60))   + Region("l1_pt", (50,-999))+ Region ("CT2", (300,400))   
CR2haY   = SR2 + Region("mt", (0,60))   + Region("l1_pt", (50,-999))+ Region ("CT2", (400, -999))  


SR2vlbX = SR2 + Region("mt", (60,95))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (300,400))   
SR2lbX  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2mbX  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2hbX  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

SR2vlbY = SR2 + Region("mt", (60,95))  + Region("l1_pt", (3.5,5)) + Region ("CT2", (400,-999))  
SR2lbY  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2mbY  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2hbY  = SR2 + Region("mt", (60,95))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

CR2mbX    = SR2 + Region("mt", (60,95))   + Region("l1_pt", (30,50)) + Region ("CT2", (300,400)) 
CR2mbY    = SR2 + Region("mt", (60,95))   + Region("l1_pt", (30,50)) + Region ("CT2", (400, -999)) 

CR2hbX    = SR2 + Region("mt", (60,95))   + Region("l1_pt", (50,-999)) + Region ("CT2", (300,400)) 
CR2hbY    = SR2 + Region("mt", (60,95))   + Region("l1_pt", (50,-999)) + Region ("CT2", (400, -999)) 


SR2lcX  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2mcX  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2hcX  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

SR2lcY  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2mcY  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2hcY  = SR2 + Region("mt", (95,-999))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

CR2mcX    = SR2 + Region("mt", (95,-999))   + Region("l1_pt", (30,50)) + Region ("CT2", (300,400)) 
CR2mcY    = SR2 + Region("mt", (95,-999))   + Region("l1_pt", (30,50)) + Region ("CT2", (400, -999)) 

CR2hcX    = SR2 + Region("mt", (95,-999))   + Region("l1_pt", (50,-999)) + Region ("CT2", (300,400)) 
CR2hcY    = SR2 + Region("mt", (95,-999))   + Region("l1_pt", (50,-999)) + Region ("CT2", (400, -999)) 

signalRegions = [SR1vlaX,SR1laX, SR1maX, SR1haX, SR1vlaY,SR1laY, SR1maY, SR1haY, SR1vlbX,SR1lbX, SR1mbX, SR1hbX, SR1vlbY,SR1lbY, SR1mbY, SR1hbY, SR1lcX, SR1mcX, SR1hcX,SR1lcY, SR1mcY, SR1hcY, SR2vlaX,SR2laX, SR2maX, SR2haX, SR2vlaY,SR2laY, SR2maY, SR2haY, SR2vlbX,SR2lbX, SR2mbX, SR2hbX, SR2vlbY,SR2lbY, SR2mbY, SR2hbY,SR2lcX, SR2mcX, SR2hcX,SR2lcY, SR2mcY, SR2hcY]
controlRegions= [ CR1maX,CR1haX, CR1maY,CR1haY, CR1mbX,CR1hbX, CR1mbY,CR1hbY, CR1mcX,CR1hcX, CR1mcY,CR1hcY, CR2maX,CR2haX, CR2maY,CR2haY, CR2mbX,CR2hbX ,CR2mbY,CR2hbY, CR2mcX,CR2hcX, CR2mcY, CR2hcY]
#controlRegions= [ CR1aX]
