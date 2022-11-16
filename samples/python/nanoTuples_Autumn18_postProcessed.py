import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

from StopsCompressed.samples.color import color

# Data directory
try:
    data_directory_ = sys.modules['__main__'].data_directory
except:
    from StopsCompressed.samples.default_locations import default_locations
    data_directory_ = default_locations.mc_2018_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory_ = sys.modules['__main__'].postProcessing_directory
except:
  from StopsCompressed.samples.default_locations import default_locations
  postProcessing_directory_ = default_locations.mc_2018_postProcessing_directory 


logger.info("Loading MC samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))

dirs = {}

### TTJets ###

## LO
dirs['TTBar']           = ["TTbar"]

## TTLep
dirs['TTLep_pow']       = ["TTLep_pow"]
dirs['TTSingleLep_pow'] = ["TTSingleLep_pow"]
dirs['TTBar_pow'] = dirs['TTLep_pow'] + dirs['TTSingleLep_pow']

#dirs['TTJets_SingleLeptonFromT']    = ["TTJets_SingleLeptonFromT"]
#dirs['TTJets_SingleLeptonFromTbar'] = ["TTJets_SingleLeptonFromTbar"]
#dirs['TTJets_SingleLepton']         = dirs['TTJets_SingleLeptonFromT'] + dirs['TTJets_SingleLeptonFromTbar']

#dirs['TTJets'] = dirs['TTBar']
dirs['TTJets'] = dirs['TTBar_pow'] # NOTE: alternative


### WJets ###
dirs['WJetsToLNu_HT'] = ["WJetsToLNu_HT70to100", 
                         "WJetsToLNu_HT100to200", 
                         "WJetsToLNu_HT200to400", 
                         "WJetsToLNu_HT400to600",
                         "WJetsToLNu_HT600to800", 
                         "WJetsToLNu_HT800to1200", 
                         "WJetsToLNu_HT1200to2500", 
                         "WJetsToLNu_HT2500toInf"]

dirs['WJets'] = dirs['WJetsToLNu_HT']


### ZInv ###

dirs['ZInv'] = ["DYJetsToNuNu_HT100to200",
                "DYJetsToNuNu_HT200to400",
                "DYJetsToNuNu_HT400to600",
                "DYJetsToNuNu_HT600to800",
                "DYJetsToNuNu_HT1200to2500",
                "DYJetsToNuNu_HT2500toInf"]  


### DY ###

## HT-binned

# low mass
DY_M4to50_HT = [#"DYJetsToLL_M4to50_HT70to100", # NOTE: sample empty
                "DYJetsToLL_M4to50_HT100to200",
                "DYJetsToLL_M4to50_HT200to400",
                "DYJetsToLL_M4to50_HT400to600",
                "DYJetsToLL_M4to50_HT600toInf"] 

# high mass
DY_M50_HT =["DYJetsToLL_M50_HT70to100",
            "DYJetsToLL_M50_HT100to200",
            "DYJetsToLL_M50_HT200to400",
            "DYJetsToLL_M50_HT400to600_comb",
            "DYJetsToLL_M50_HT600to800",
            "DYJetsToLL_M50_HT800to1200",
            "DYJetsToLL_M50_HT1200to2500",
            "DYJetsToLL_M50_HT2500toInf"]

dirs['DY_HT_LO'] =  DY_M4to50_HT + DY_M50_HT

## LO
dirs['DY_M50']    = ["DYJetsToLL_M50"]
dirs['DY_M50_LO'] = ["DYJetsToLL_M50_LO"]
dirs['DY_LO']     = ["DYJetsToLL_M50_LO", "DYJetsToLL_M10to50_LO"]

dirs['DY'] = dirs['DY_HT_LO']
#dirs['DY'] = dirs['DY_M50'] # NOTE: alternative
#dirs['DY'] = dirs['DY_LO']  # NOTE: alternative


### QCD ###

## HT-binned
dirs['QCD_HT']  = ["QCD_HT100to200", 
                   "QCD_HT200to300", 
                   "QCD_HT300to500", 
                   "QCD_HT500to700", 
                   "QCD_HT700to1000", 
                   "QCD_HT1500to2000", 
                   "QCD_HT2000toInf" ]

## pT-binned

# electron-enriched
dirs['QCD_Ele'] = ["QCD_Ele_pt20to30", 
                   "QCD_Ele_pt30to50", 
                   "QCD_Ele_pt50to80", 
                   "QCD_Ele_pt80to120",
                   "QCD_Ele_pt120to170",
                   "QCD_Ele_pt170to300",
                   "QCD_Ele_pt300toInf" ]

# muon-enriched
dirs['QCD_Mu']  = ["QCD_Mu_pt20to30", 
                   "QCD_Mu_pt30to50",
                   "QCD_Mu_pt50to80",
                   "QCD_Mu_pt80to120",
                   "QCD_Mu_pt120to170",
                   "QCD_Mu_pt170to300",
                   "QCD_Mu_pt300to470",
                   "QCD_Mu_pt470to600",
                   "QCD_Mu_pt600to800",
                   "QCD_Mu_pt800to1000_ext",
                   "QCD_Mu_pt1000toInf" ]

dirs['QCD'] = dirs['QCD_HT']


#### Top ####

### ST ###

dirs['ST_tch']  = ["T_tch_pow", "TBar_tch_pow"]#, "TToLeptons_tch_powheg", "TBarToLeptons_tch_powheg"]
dirs['ST_tWch'] = ["T_tWch", "TBar_tWch"]
dirs['ST_sch']  = ["TToLeptons_sch_amcatnlo"] #, "TToHad_sch"]

dirs['ST'] = dirs['ST_tch'] + dirs['ST_tWch'] + dirs['ST_sch']


### TTX ###

## TTW
dirs['TTW_LO'] = ['TTW_LO']
#dirs['TTW_NLO'] = ['TTWToQQ', 'TTWToLNu']

dirs['TTW'] = dirs['TTW_LO']
#dirs['TTW'] = dirs['TTW_NLO'] # NOTE: alternative

## TTZ
dirs['TTZ_LO'] = ['TTZ_LO']

#dirs['TTZToQQ']     = ['TTZToQQ']
#dirs['TTZToLLNuNu'] = ['TTZToLLNuNu', 'TTZToLLNuNu_m1to10']
#dirs['TTZ_NLO']     = dirs['TTZ_TTZToLLNuNu'] + dirs['TTZToQQ'] 

dirs['TTZ'] = dirs['TTZ_LO']
#dirs['TTZ'] = dirs['TTZ_NLO'] # NOTE: alternative

## TTG
dirs['TTG'] = []#"TTGJets"] # FIXME: processing

dirs['TTX'] = dirs['TTW'] + dirs['TTZ'] + dirs['TTG']


#### Di/Multi-boson ####

### VV ###

## LO
dirs['WW_LO'] = ["WW"]
dirs['WZ_LO'] = ["WZ"]
dirs['ZZ_LO'] = ["ZZ"]

dirs['VV_LO'] = dirs['WW_LO'] + dirs['WZ_LO'] + dirs['ZZ_LO']

## NLO
#dirs['WW_NLO']    = ["WWTo2L2Nu"]
#dirs['WZ_NLO']    = ["WZTo3LNu_amcatnlo", "WZTo1L1Nu2Q"]
#dirs['ZZ_NLO']    = ["ZZTo2Q2Nu", "ZZTo4L" ]
#dirs['VVTo2L2Nu'] = ["VVTo2L2Nu_comb"]

#dirs['VV_NLO']    = dirs['WW_NLO'] + dirs['WZ_NLO'] + dirs['ZZ_NLO'] + dirs['VVTo2L2Nu']

dirs['VV'] = dirs['VV_LO']
#dirs['VV'] = dirs['VV_NLO'] # NOTE: alternative


### Others ###
dirs['others'] = dirs['DY'] + dirs['ST'] + dirs['TTX'] + dirs['VV']

directories = {key:[os.path.join(data_directory_, postProcessing_directory_, dir) for dir in dirs[key]] for key in dirs.keys()}

TTJets_18          = Sample.fromDirectory(name="TTJets",          treeName="Events", isData=False, color=color.TTJets,     texName="t#bar{t}",             directory=directories['TTJets'])
#TTBar_pow_18       = Sample.fromDirectory(name="TTBar_pow",       treeName="Events", isData=False, color=color.TTBar_pow,  texName="t#bar{t}/t",           directory=directories['TTBar_pow'])
#TTLep_pow_18       = Sample.fromDirectory(name="TTLep_pow",       treeName="Events", isData=False, color=color.TTJets,     texName="t#bar{t}",             directory=directories['TTLep_pow'])
#TTSingleLep_pow_18 = Sample.fromDirectory(name="TTSingleLep_pow", treeName="Events", isData=False, color=color.TTJets_1l,  texName="t#bar{t} (1l)",        directory=directories['TTSingleLep_pow'])
#TTBar_pow_1l_18    = Sample.fromDirectory(name="Top_1l_pow",      treeName="Events", isData=False, color=color.TTJets_1l,  texName="t#bar{t} (1l)",        directory=directories['TTSingleLep_pow'])
WJets_18           = Sample.fromDirectory(name="WJetsToLNu_HT",   treeName="Events", isData=False, color=color.WJetsToLNu, texName="W(l,#nu) + Jets (HT)", directory=directories['WJets'])
ZInv_18            = Sample.fromDirectory(name="ZInv",            treeName="Events", isData=False, color=color.ZInv,       texName="Z(#nu,#nu + Jets)",    directory=directories['ZInv'])
DY_18              = Sample.fromDirectory(name="DY",              treeName="Events", isData=False, color=color.DY,         texName="Drell-Yan",            directory=directories['DY'])
ST_18              = Sample.fromDirectory(name="ST",              treeName="Events", isData=False, color=color.ST,         texName="Single top",           directory=directories['ST'])
#ST_tch_18          = Sample.fromDirectory(name="ST_tch",          treeName="Events", isData=False, color=color.ST,         texName="Single top (tch)",     directory=directories['ST_tch'])
TTX_18             = Sample.fromDirectory(name="TTX",             treeName="Events", isData=False, color=color.TTX,        texName="t#bar{t}G/W/Z",        directory=directories['TTX'])
#TTW_18             = Sample.fromDirectory(name="TTW",             treeName="Events", isData=False, color=color.TTW,        texName="t#bar{t}W",            directory=directories['TTW'])
#TTZ_18             = Sample.fromDirectory(name="TTZ",             treeName="Events", isData=False, color=color.TTZ,        texName="t#bar{t}Z",            directory=directories['TTZ'])
#TTG_18             = Sample.fromDirectory(name="TTG",             treeName="Events", isData=False, color=color.TTG,        texName="t#bar{t}#gamma",       directory=directories['TTG'])
VV_18              = Sample.fromDirectory(name="VV",              treeName="Events", isData=False, color=color.VV,         texName="VV ",                  directory=directories['VV'])
QCD_18             = Sample.fromDirectory(name="QCD",             treeName="Events", isData=False, color=color.QCD_HT,     texName="QCD",                  directory=directories['QCD'])
#QCD_Ele_18         = Sample.fromDirectory(name="QCD_Ele",         treeName="Events", isData=False, color=color.QCD_Ele,    texName="QCD (Ele)",            directory=directories['QCD_Ele'])
#QCD_Mu_18          = Sample.fromDirectory(name="QCD_Mu",          treeName="Events", isData=False, color=color.QCD_Mu,     texName="QCD (Mu)",             directory=directories['QCD_Mu'])
Others_18          = Sample.fromDirectory(name="Others",          treeName="Events", isData=False, color=color.others,     texName="Others",               directory=directories['others'])
