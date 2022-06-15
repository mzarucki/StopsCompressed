import copy, os, sys
#from RootTools.core.Sample import Sample
from RootTools.core.standard import *
import ROOT

from StopsCompressed.samples.nanoTuples_RunUL16APV_postProcessed import Run2016preVFP
from StopsCompressed.samples.nanoTuples_RunUL16_postProcessed 	 import Run2016postVFP

RunUL16_36fb	  = Sample.combine("RunUL16", [Run2016preVFP, Run2016postVFP])
RunUL16_36fb.lumi = Run2016preVFP.lumi + Run2016postVFP.lumi

lumi_year 	  = {201619: Run2016preVFP.lumi, 201616: Run2016postVFP.lumi}



import StopsCompressed.samples.nanoTuples_UL16APV_postProcessed  as UL16preVFP
import StopsCompressed.samples.nanoTuples_UL16_postProcessed 	 as UL16postVFP
#import StopsCompressed.samples.nanoTuples_Summer16_postProcessed as legacy16

#DY_HT_M50_LO_16        	= Sample.combine( "DY_HT_M50_LO", [UL16preVFP.DY_HT_M50_LO_16APV, UL16postVFP.DY_HT_M50_LO_16])
DY_HT_LO_16        	= Sample.combine( "DY_HT_LO", 	  [UL16preVFP.DY_HT_LO_16APV, UL16postVFP.DY_HT_LO_16])
Top_pow_16              = Sample.combine( "Top_pow", 	  [UL16preVFP.Top_pow_16APV ,   UL16postVFP.Top_pow_16])
singleTop_16            = Sample.combine( "singleTop",    [UL16preVFP.singleTop_16APV , UL16postVFP.singleTop_16])
TTX_16              	= Sample.combine( "TTX",	  [UL16preVFP.TTX_16APV , 	UL16postVFP.TTX_16])
WJetsToLNu_HT_16        = Sample.combine( "WJetsToLNu_HT",[UL16preVFP.WJetsToLNu_HT_16APV , 	UL16postVFP.WJetsToLNu_HT_16])
VV_16        		= Sample.combine( "VV",		  [UL16preVFP.VV_16APV , 	UL16postVFP.VV_16])
#VV_16        		= Sample.combine( "VV",		  [legacy16.VV_16])
#WWToLNuQQ_16		= Sample.combine( "WWToLNuQQ",	  [legacy16.WWToLNuQQ_16])
QCD_HT_16        	= Sample.combine( "QCD_HT",	  [UL16preVFP.QCD_HT_16APV , 	UL16postVFP.QCD_HT_16])
ZInv_16        		= Sample.combine( "ZInv",	  [UL16preVFP.ZInv_16APV , 	UL16postVFP.ZInv_16])
Others_16		= Sample.combine( "Others",	  [UL16preVFP.Others_16APV,	UL16postVFP.Others_16])

