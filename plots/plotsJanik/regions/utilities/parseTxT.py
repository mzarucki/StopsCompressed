import json
import numpy as np
import argparse


argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--mstop", default=500,  type=int,              action="store",                            help="stop mass")
argParser.add_argument("--dm",    default=10,   type=int,              action="store",                            help="mass split between mstop and mneutralino")
args = argParser.parse_args()

mstop=args.mstop
dm=args.dm


keyword = "rate"


DCards = {
    "CC" : {
        "textFile"  : open("/scratch/janik.andrejkovic/StopsCompressed/results/2016/fitAllregion_2016_v0p1/cardFiles/T2tt/expected/T2tt_{}_{}.txt".format(mstop,mstop-dm),"r"),
        "processes" : ["signal", "WJets", "DY", "Top", "ZInv", "singleTop", "VV", "TTX", "QCD"],
        "shift"     : 0
    },
    "SUS17005" : {
        "textFile" : open("/mnt/hephy/cms/priya.hussain/StopsCompressed/results/2016/SUS17005/CC/DataCards/T2tt/T2tt_{}_{}.txt".format(mstop,mstop-dm),"r"),
        "processes" : ["signal", "Top", "WJets", "Others", "Fakes"],
        "shift" : 12
    }

}

for name in DCards.keys() :
    
    out = {}
    out["Data"] = {}
    out["signal_unc"] = {}

    stat_unc = []
    for p in DCards[name]["processes"] :
        out[p] = {}

    for x in DCards[name]["textFile"]:
        if x.startswith("observation") :
            data = (x.split())[1:]

        if x.startswith(keyword) :
            vals = (x.split())[1:]
            stat_unc = np.zeros(len(vals))
            SUS_counter = 0

        if x.startswith("Stat_Bin") :
            w = x.split()[0] 
            if "signal" in w :
                index = int(w.split("_")[1][3:])
                value = [v for v in x.split()[2:] if v != "-"][0]
                stat_unc[index] = value

        if x.startswith("signal") :
            w = x.split()[0] 
            if "Sta" in w :
                if x.split()[1] == "gmN" :
                    # print float(x.split()[2])
                    value = 1. + 1./ np.sqrt(float(x.split()[2])) #[float(v)*np.sqrt(float(x.split()[2])) for v in x.split()[3:] if v != "-"][0]
                else :
                    value = [v for v in x.split()[2:] if v != "-"][0]

                stat_unc[SUS_counter] = value  
                SUS_counter += 1 


    for i_bin in range(len(data)) :
        out["Data"]["Bin{}".format((i_bin+DCards[name]["shift"])%56)] = data[i_bin]
        out["signal_unc"]["Bin{}".format((i_bin+DCards[name]["shift"])%56)] = stat_unc[i_bin]
        
        for i_p, p in enumerate(DCards[name]["processes"]) :
            out[p]["Bin{}".format((i_bin+DCards[name]["shift"])%56)] = vals[i_p + i_bin * len(DCards[name]["processes"])]




    with open('jsonFilesDCcomparison/{}_mstop{}_dm{}.json'.format(name,mstop,dm), 'w') as fp:
        json.dump(out, fp)

