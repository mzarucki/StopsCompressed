from RootTools.core.standard import *
import ROOT


lumi_year         = {201619: (19.5)*1000 , 201616: (16.5)*1000}
import StopsCompressed.samples.nanoTuples_UL16APV_FullSimSignal_postProcessed as T2tt_preVFP
import StopsCompressed.samples.nanoTuples_UL16_FullSimSignal_postProcessed    as T2tt_postVFP

T2tt_500_420 = Sample.combine( "T2tt_500_420", [T2tt_preVFP.T2tt_500_420, T2tt_postVFP.T2tt_500_420])
T2tt_500_450 = Sample.combine( "T2tt_500_450", [T2tt_preVFP.T2tt_500_450, T2tt_postVFP.T2tt_500_450])
T2tt_500_470 = Sample.combine( "T2tt_500_470", [T2tt_preVFP.T2tt_500_470, T2tt_postVFP.T2tt_500_470])

