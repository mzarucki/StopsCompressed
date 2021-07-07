import ROOT

syst = "wPt"
proc = "WJets"

path = "/scratch/janik.andrejkovic/StopsCompressed/results/2016/fitAllregion_2016_v30SigNonPromptNewSystNewWpt/cardFiles/T2tt/expected/T2tt_500_490_shape.root"

_file = ROOT.TFile(path)

for bin_i in range(12) :
    up      = _file.Get("Bin{}_{}_{}_2016Up".format(bin_i,proc,syst))
    nominal = _file.Get("Bin{}_{}".format(bin_i,proc))

    print "Bin {:2} ".format(bin_i)

    for bb in range(up.GetNbinsX()) :
        print "up/nominal: {}".format(up.GetBinContent(bb+1)/nominal.GetBinContent(bb+1))
    print "-"*90
_file.Close()