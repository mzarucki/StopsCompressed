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


SR2lcX  = SR2 + Region("mt", (95,130))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2mcX  = SR2 + Region("mt", (95,130))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2hcX  = SR2 + Region("mt", (95,130))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

SR2lcY  = SR2 + Region("mt", (95,130))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2mcY  = SR2 + Region("mt", (95,130))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2hcY  = SR2 + Region("mt", (95,130))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

CR2mcX    = SR2 + Region("mt", (95,130))   + Region("l1_pt", (30,50)) + Region ("CT2", (300,400)) 
CR2mcY    = SR2 + Region("mt", (95,130))   + Region("l1_pt", (30,50)) + Region ("CT2", (400, -999)) 

CR2hcX    = SR2 + Region("mt", (95,130))   + Region("l1_pt", (50,-999)) + Region ("CT2", (300,400)) 
CR2hcY    = SR2 + Region("mt", (95,130))   + Region("l1_pt", (50,-999)) + Region ("CT2", (400, -999)) 

SR2ldX  = SR2 + Region("mt", (130,-999))  + Region("l1_pt", (5,12))  + Region ("CT2", (300,400)) 
SR2mdX  = SR2 + Region("mt", (130,-999))  + Region("l1_pt", (12,20)) + Region ("CT2", (300,400)) 
SR2hdX  = SR2 + Region("mt", (130,-999))  + Region("l1_pt", (20,30)) + Region ("CT2", (300,400)) 

SR2ldY  = SR2 + Region("mt", (130,-999))  + Region("l1_pt", (5,12))  + Region ("CT2", (400,-999)) 
SR2mdY  = SR2 + Region("mt", (130,-999))  + Region("l1_pt", (12,20)) + Region ("CT2", (400,-999)) 
SR2hdY  = SR2 + Region("mt", (130,-999))  + Region("l1_pt", (20,30)) + Region ("CT2", (400,-999)) 

CR2mdX    = SR2 + Region("mt", (130,-999))   + Region("l1_pt", (30,50)) + Region ("CT2", (300,400)) 
CR2mdY    = SR2 + Region("mt", (130,-999))   + Region("l1_pt", (30,50)) + Region ("CT2", (400, -999)) 

CR2hdX    = SR2 + Region("mt", (130,-999))   + Region("l1_pt", (50,-999)) + Region ("CT2", (300,400)) 
CR2hdY    = SR2 + Region("mt", (130,-999))   + Region("l1_pt", (50,-999)) + Region ("CT2", (400, -999)) 


signalRegions = [SR2vlaX, SR2laX, SR2maX, SR2haX, CR2maX, SR2vlaY,SR2laY, SR2maY, SR2haY, CR2maY, 
                 SR2vlbX, SR2lbX, SR2mbX, SR2hbX, CR2mbX, SR2vlbY,SR2lbY, SR2mbY, SR2hbY, CR2mbY, 
                 SR2lcX, SR2mcX, SR2hcX, CR2mcX, SR2lcY, SR2mcY, SR2hcY, CR2mcY,
                 SR2ldX, SR2mdX, SR2hdX, CR2mdX, SR2ldY, SR2mdY, SR2hdY, CR2mdY
                 ]
controlRegions= [ CR2haX, CR2haY ,CR2hbX ,CR2hbY, CR2hcX, CR2hcY, CR2hdX, CR2hdY]
regionMapping = { 0 : 5, 
                1 : 5, 
                2 : 5, 
                3 : 5, 
                4 : 4, 
                5 : 4, 
                6 : 4, 
                7 : 4, 
                }