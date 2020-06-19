import ROOT

from StopsCompressed.samples.helpers import singleton as singleton

@singleton
class color():
  pass

color.data           = ROOT.kBlack
color.ZInv           = ROOT.kOrange-3
color.DY             = ROOT.kMagenta-6
color.DY_HT_LO       = color.DY
color.TTJets         = ROOT.kAzure+1
color.TTJets_1l      = ROOT.kAzure+2
color.Top_pow        = color.TTJets
color.singleTop      = 7
color.TTX            = ROOT.kAzure-7
color.TTXNoZ         = ROOT.kRed
color.TTH            = ROOT.kRed
color.TTW            = ROOT.kRed+3
color.TTZ            = ROOT.kPink+9
color.TTZtoLLNuNu    = 6
color.TTZtoQQ        = ROOT.kBlue
color.TTG            = ROOT.kRed
color.TZQ            = 9
color.TWZ            = ROOT.kBlue-4
color.WJetsToLNu     = 8
color.diBoson        = ROOT.kOrange
color.multiBoson     = ROOT.kOrange
color.ZZ             = ROOT.kOrange+1
color.ZZ4l           = color.ZZ
color.WZ             = ROOT.kOrange+7
color.WW             = ROOT.kOrange-7
color.VV             = ROOT.kGreen-1
color.WG             = ROOT.kOrange-5
color.ZG             = ROOT.kOrange-10
color.triBoson       = ROOT.kYellow
color.WZZ            = ROOT.kYellow
color.WWG            = ROOT.kYellow-5
color.QCD            = ROOT.kMagenta+3
color.QCD_HT         = color.QCD
color.QCD_Ele        = ROOT.kRed+1
color.QCD_Mu         = ROOT.kRed+3
color.QCD_Mu5        = 46
color.QCD_EMbcToE    = 46
color.QCD_Mu5EMbcToE = 46
color.TTJetsF        = 7
color.TTJetsG        = 7
color.TTJetsNG       = 7

color.other          = 46

color.T2tt_450_0                       = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi200 = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi10  = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi20  = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi100 = ROOT.kBlack
color.TTbarDMJets_pseudoscalar_Mchi1_Mphi100 = ROOT.kRed
color.TTbarDMJets_scalar_Mchi10_Mphi100 = ROOT.kPink
