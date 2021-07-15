import ROOT
yields = {
    "Data" : "l1_pt_data_c19e16c2_8e7c_4c5c_9b4e_bb217e226d00",
    "Wjets" : "l1_pt_WJetsToLNu_HT__771f8651_0dbc_407b_8469_06ad878bf7cc",
    "Top" : "l1_pt_Top_pow_095c3ee3_d5cd_4ce2_8456_0a419c924ffc",
    "SingleTop" : "l1_pt_singleTop_84d8acb4_cf82_483e_990d_c794e40d470c",
    "Zinv" : "l1_pt_ZInv_515b51b0_4d93_4c79_9c93_3f1f76ce6c58",
    "DY" : "l1_pt_DY_HT_LO_f5851d27_0959_426e_ace1_e7f6e131effb",
    "VV" : "l1_pt_VV_ec22729f_9809_4a3c_9db0_60e4b755ba60",
    "TTX" : "l1_pt_TTX_3e3e0376_6e22_4aa8_bcc8_ad696e04bf06",
}
yields_list = ["Data", "Wjets", "Top", "SingleTop", "Zinv", "DY", "VV", "TTX"]

_file = ROOT.TFile("/mnt/hephy/cms/priya.hussain/www/StopsCompressed/analysisPlots/v_45_AN_Central/Run2016/alllog/nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300/l1_pt.root")

output = {}

canvas = _file.Get("e41368dd_51c2_4eba_b58c_72ceabf45f30")
data = (canvas.FindObject("e41368dd_51c2_4eba_b58c_72ceabf45f30_1")).GetPrimitive(yields["Data"])

print "data:"
datavals = [(data.GetBinContent(_bin+1)) for _bin in range(data.GetNbinsX())]

output["Data"] = datavals


for i_proc, proc in enumerate(yields_list[1:]) :
    thist     = (canvas.FindObject("e41368dd_51c2_4eba_b58c_72ceabf45f30_1")).GetPrimitive(yields[proc])
    
    values      = [(thist.GetBinContent(_bin+1)) for _bin in range(thist.GetNbinsX())]
    
    if i_proc < len(yields_list)-2 :
        thist_next = (canvas.FindObject("e41368dd_51c2_4eba_b58c_72ceabf45f30_1")).GetPrimitive(yields[yields_list[i_proc+2]])
        values_next = [(thist_next.GetBinContent(_bin+1)) for _bin in range(thist_next.GetNbinsX())]

        output[proc] = [j-values_next[i] for i,j in enumerate(values)]
    else :
        output[proc] = values



print output.keys()

# my_stack = (canvas.FindObject("pad1")).GetPrimitive("mcStack2")
# bkgs = {}
# for bkg_hist in my_stack.GetHists() :
    
#     process_name = bkg_hist.GetName()
#     bkgs[process_name] = [str(bkg_hist.GetBinContent(_bin+1)) for _bin in range(bkg_hist.GetNbinsX())]

# for k in bkgs.keys() :
#     print "{}:".format(k)
#     print " ".join(bkgs[k])

# my_sig_stack = (canvas.FindObject("pad1")).GetPrimitive("sigStack")
# sigs = {}
# for sig_hist in my_sig_stack.GetHists() :
#     process_name = sig_hist.GetName()
#     sigs[process_name] = [str(sig_hist.GetBinContent(_bin+1)) for _bin in range(sig_hist.GetNbinsX())]

# for k in sigs.keys() :
#     print "{}:".format(k)
#     print " ".join(sigs[k])



_file.Close()







exit(0)
dms = ['dm20','dm60']


DCards = {
    "CC_SUS17005     " : "/mnt/hephy/cms/priya.hussain/forJanik/SU17005/",
    "CC_nanoAOD      " : "/mnt/hephy/cms/priya.hussain/forJanik/navidrange",
    "BinShape_nanoAOD" : "/scratch/priya.hussain/StopsCompressed/results/2016/fitAllregion_navidrange/cardFiles/T2tt/expected/"
}

quantiles = {
    "expected" : 2,
    "observed" : 5 
} 



for dm in dms :
    for q in quantiles.keys() :
        print "(mstop=500, {})  -  {}".format(dm,q)
        
        for f in DCards.keys() :
            #open file 
            if "Shape" in f :
                rootFileName = "T2tt_500_{}_shapeCard".format(500-int(dm[2:]))
                print rootFileName
                openFile = ROOT.TFile("{}/{}.root".format(DCards[f],rootFileName))

            else :
                openFile = ROOT.TFile("{}/{}/higgsCombineTest.AsymptoticLimits.mH120.root".format(DCards[f],dm))

            limit = openFile.Get("limit")
            limit.GetEntry(quantiles[q])

            print "{}   {:.3}".format(f,limit.limit)

            openFile.Close()
        print "-"*40
    print "="*40 
    print "-"*40 


exit(0)

_file = ROOT.TFile("/scratch/janik.andrejkovic/forPriya/CMS-SUS-17-005_Figure_002-a.root")

canvas = _file.Get("canvas")
data = (canvas.FindObject("pad1")).GetPrimitive("Data")

print "data:"
datavals = [str(data.GetBinContent(_bin+1)) for _bin in range(data.GetNbinsX())]
print " ".join(datavals)

my_stack = (canvas.FindObject("pad1")).GetPrimitive("mcStack2")
bkgs = {}
for bkg_hist in my_stack.GetHists() :
    
    process_name = bkg_hist.GetName()
    bkgs[process_name] = [str(bkg_hist.GetBinContent(_bin+1)) for _bin in range(bkg_hist.GetNbinsX())]

for k in bkgs.keys() :
    print "{}:".format(k)
    print " ".join(bkgs[k])

my_sig_stack = (canvas.FindObject("pad1")).GetPrimitive("sigStack")
sigs = {}
for sig_hist in my_sig_stack.GetHists() :
    process_name = sig_hist.GetName()
    sigs[process_name] = [str(sig_hist.GetBinContent(_bin+1)) for _bin in range(sig_hist.GetNbinsX())]

for k in sigs.keys() :
    print "{}:".format(k)
    print " ".join(sigs[k])



_file.Close()


