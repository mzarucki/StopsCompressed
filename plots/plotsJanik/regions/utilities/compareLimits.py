import ROOT

dms = ['dm10','dm20','dm40','dm60','dm80']
mstop = 500

DCards = {
    "CC_SUS17005     " : "/scratch/priya.hussain/StopsCompressed/forJanik/stop{}_navid".format(mstop),
    # "CC_nanoAOD      " : "/scratch/priya.hussain/StopsCompressed/forJanik/stop{}_CC".format(mstop),
    "CC_nanoAOD      " : "/scratch/priya.hussain/StopsCompressed/results/2016/fitAllregion_nISR/cardFiles/T2tt/expected/",
    # "BinShape_nanoAOD" : "/scratch/priya.hussain/StopsCompressed/results/2016/fitAllregion_navidrange/cardFiles/T2tt/expected/"
    "BinShape_nanoAOD" : "/scratch/janik.andrejkovic/StopsCompressed/results/2016/fitAllregion_2016_v0p1/cardFiles/T2tt/expected/"
}

DC_list = ["CC_SUS17005     ", "CC_nanoAOD      ","BinShape_nanoAOD"]

quantiles = {
    "exected" : 2,
    # "observed" : 5 
} 


for dm in dms :
    for q in quantiles.keys() :
        print "(mstop={}, {})  -  {}".format(mstop,dm,q)
        
        for f in DC_list :
            
            #open file 
            if "Shape" in f or "nanoAOD" in f :
                if "Shape" in f :
                    rootFileName = "T2tt_{}_{}_shapeCard".format(mstop,mstop-int(dm[2:]))
                else :
                    rootFileName = "T2tt_{}_{}".format(mstop,mstop-int(dm[2:]))
                openFile = ROOT.TFile("{}/{}.root".format(DCards[f],rootFileName))

            else :
                openFile = ROOT.TFile("{}/{}/higgsCombineTest.AsymptoticLimits.mH120.root".format(DCards[f],dm))

            limit = openFile.Get("limit")
            limit.GetEntry(quantiles[q])

            if "SUS17005" in f :
                reference = limit.limit
                print "{}   {:.3}".format(f,limit.limit)
            else :
                print "{}   {:.3} ({:.3}%)".format(f,limit.limit,(limit.limit/reference-1)*100)

            openFile.Close()
        print "-"*40
    print "="*40 
    print "-"*40 