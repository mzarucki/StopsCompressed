import ROOT as R
import os


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

mneu = 420
name = ""
for s in Systs.keys() :
    if Systs[s] : 
        if name :
            name = "_".join([name,s])
        else :
            name = s

for s in Systs.keys() :
    os.system("sed -i 's/shape/lnN  /g' T2tt_500_{mneu}.txt".format(mneu=mneu))

    if Systs[s] :
        print s
        os.system("sed -i 's/#*{0}/{0}/g' T2tt_500_{mneu}.txt".format(s,mneu=mneu))
        os.system("sed -i 's/#*{0}/{0}/g' T2tt_500_{mneu}_shapeCard.txt".format(s,mneu=mneu))
    else :
        os.system("sed -i 's/{0}/#{0}/g' T2tt_500_{mneu}.txt".format(s,mneu=mneu))
        os.system("sed -i 's/{0}/#{0}/g' T2tt_500_{mneu}_shapeCard.txt".format(s,mneu=mneu))

# exit(0)
os.system("mkdir -p {}/shape".format(name))
os.system("mkdir -p {}/CC".format(name))

os.system("combine -M AsymptoticLimits T2tt_500_{mneu}.txt".format(mneu=mneu))
os.system("mv higgsCombineTest.AsymptoticLimits.mH120.root {}/CC".format(name))


os.system("combine -M AsymptoticLimits T2tt_500_{mneu}_shapeCard.txt".format(mneu=mneu))
os.system("mv higgsCombineTest.AsymptoticLimits.mH120.root {}/shape".format(name))


for t in ["CC","shape"]:
    openFile = R.TFile("{}/{}/higgsCombineTest.AsymptoticLimits.mH120.root".format(name,t))
    
    limit = openFile.Get("limit")
    limit.GetEntry(2)
    print "exp {:5} ->  {:.4}".format(t,limit.limit)
    openFile.Close()