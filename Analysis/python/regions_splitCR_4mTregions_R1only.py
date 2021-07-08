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
# c- mT region 
SR1lcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region ("CT1", (300,400))   
SR1mcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1hcX  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

SR1lcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999)) 
SR1mcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999)) 
SR1hcY  = SR1 + Region("mt", (95,130)) + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999)) 


CR1mcX   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,50)) + Region ("CT1", (300,400))   
CR1mcY   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (30,50)) + Region ("CT1", (400, -999)) 

CR1hcX   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (50,-999)) + Region ("CT1", (300,400))   
CR1hcY   = SR1 + Region("mt", (95,130)) + Region("l1_pt", (50,-999)) + Region ("CT1", (400, -999)) 

SR1ldX  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region ("CT1", (300,400))   
SR1mdX  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region ("CT1", (300,400)) 
SR1hdX  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region ("CT1", (300,400)) 

SR1ldY  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (5,12))  + Region ("CT1", (400,-999)) 
SR1mdY  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (12,20)) + Region ("CT1", (400,-999)) 
SR1hdY  = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (20,30)) + Region ("CT1", (400,-999)) 


CR1mdX   = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,50)) + Region ("CT1", (300,400))   
CR1mdY   = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (30,50)) + Region ("CT1", (400, -999)) 

CR1hdX   = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (50,-999)) + Region ("CT1", (300,400))   
CR1hdY   = SR1 + Region("mt", (130,-999)) + Region("l1_pt", (50,-999)) + Region ("CT1", (400, -999)) 





signalRegions = [SR1vlaX,SR1laX, SR1maX, SR1haX, CR1maX, SR1vlaY,SR1laY, SR1maY, SR1haY, CR1maY,
                 SR1vlbX,SR1lbX, SR1mbX, SR1hbX, CR1mbX, SR1vlbY,SR1lbY, SR1mbY, SR1hbY, CR1mbY, 
                 SR1lcX, SR1mcX, SR1hcX, CR1mcX, SR1lcY, SR1mcY, SR1hcY, CR1mcY, 
                 SR1ldX, SR1mdX, SR1hdX, CR1mdX, SR1ldY, SR1mdY, SR1hdY, CR1mdY, 
                 ]
controlRegions= [ CR1haX, CR1haY, CR1hbX, CR1hbY, CR1hcX, CR1hcY, CR1hdX, CR1hdY]
regionMapping = { 0 : 5, 
                1 : 5, 
                2 : 5, 
                3 : 5, 
                4 : 4, 
                5 : 4, 
                6 : 4, 
                7 : 4, 
                }
