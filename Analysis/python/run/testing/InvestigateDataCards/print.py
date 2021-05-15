import ROOT as R
import os

# _file = R.TFile("T2tt_500_490_shape.root")

# for region in range(12) :
#     name = "Bin{}_data_obs".format(region)
#     nominal = _file.Get(name)
#     # up = _file.Get("{}_wPt_2016Up".format(name))
#     # down = _file.Get("{}_wPt_2016Down".format(name))
#     val = 0
#     for ibin in range(nominal.GetNbinsX()) :
#         print nominal.GetBinContent(ibin+1)
#         # print "Region {} Bin {} sigma(up)   : {:.3f} ".format(region,ibin,up.GetBinContent(ibin+1)/nominal.GetBinContent(ibin+1) )
#         # print "Region {} Bin {} sigma(down) : {:.3f} ".format(region,ibin,nominal.GetBinContent(ibin+1)/down.GetBinContent(ibin+1) )
    
#     print "-"*90


for i in xrange(0,151,10):
    os.system("mkdir autoMCstats3_{}".format(i))
    os.system("sed -i 's/autoMCStats.*/autoMCStats {0}/g' T2tt_500_420_shapeCard.txt ".format(i))
    os.system("combine -M AsymptoticLimits T2tt_500_420_shapeCard.txt")
    os.system("mv higgsCombineTest.AsymptoticLimits.mH120.root autoMCstats3_{}/".format(i))
    
for i in xrange(0,151,10):
    openFile = R.TFile("autoMCstats3_{}/higgsCombineTest.AsymptoticLimits.mH120.root".format(i))

    limit = openFile.Get("limit")
    limit.GetEntry(2)
    print "autoMC stats {:3} ->  {:.3}".format(i,limit.limit)
    openFile.Close()

exit(0)

Systs = {
    "Lumi_2016" : True,
    "SFb_2016" : True,
    "SFl_2016" : True,
    "nISR_2016" : True,
    "wPt_2016" : True,
    "JEC_2016" : True,
    "JER_2016" : True,
    "leptonSF_2016" : True,
    "leptonSFsignal_2016" : True,
    "PU_2016" : True,
    "Stat" : True,
    # "Bin" : False,
    

}

# sed -i 's/old-text/new-text/g' input.txt

for s in Systs.keys() :
    os.system("sed -i 's/shape/lnN  /g' T2tt_400_390.txt")

    if Systs[s] :
        os.system("sed -i 's/#{0}/{0}/g' T2tt_400_390.txt".format(s))
    else :
        os.system("sed -i 's/{0}/#{0}/g' T2tt_400_390.txt".format(s))
