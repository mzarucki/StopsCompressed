import ROOT

f1_name = "/scratch/priya.hussain/StopsCompressed/nanoTuples/compstops_2016_nano_v21/MetSingleLep/T2tt/T2tt_500_420.root"
f2_name = "/scratch/priya.hussain/StopsCompressed/nanoTuples/compstops_2016_nano_v30/Met/T2tt/T2tt_500_420.root"
weight = "reweight_nISR"
# weight*reweightBTag_SF*reweightL1Prefire*reweightLeptonSF*reweight_nISR
f1 = ROOT.TFile(f1_name)
f2 = ROOT.TFile(f2_name)

# print f1, f2
# 
t1 = f1.Get("Events")
t2 = f2.Get("Events")

print t1.GetEntries()
print t2.GetEntries()
exit(0)

h1 = ROOT.TH1D("h1","h1",10,0,2)
h2 = ROOT.TH1D("h2","h2",10,0,2)
h2.SetLineColor(2)

t1.Draw("{}>>h1".format(weight))
t2.Draw("{}>>h2".format(weight))

c = ROOT.TCanvas()
h1.Draw()
h2.Draw("same")

c.SaveAs("{}.png".format(weight))