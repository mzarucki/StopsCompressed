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

DY_M4to50_HT = [
                "DYJetsToLL_M4to50_HT70to100",
                "DYJetsToLL_M4to50_HT100to200",
                "DYJetsToLL_M4to50_HT200to400",
                "DYJetsToLL_M4to50_HT400to600",
                "DYJetsToLL_M4to50_HT600toInf"
                ] 

DY_M50_HT =[
            "DYJetsToLL_M50_HT70to100",
            "DYJetsToLL_M50_HT100to200",
            "DYJetsToLL_M50_HT200to400",
            "DYJetsToLL_M50_HT400to600_comb",
            "DYJetsToLL_M50_HT600to800",
            "DYJetsToLL_M50_HT800to1200",
            "DYJetsToLL_M50_HT1200to2500",
            "DYJetsToLL_M50_HT2500toInf"
            ] 


dirs = {}
#dirs['DY']              = ["DYJetsToLL_M50" ]
#dirs['DY_LO']           = ["DYJetsToLL_M50_LO", "DYJetsToLL_M10to50_LO"]
#dirs['DY_LO_M50']       = ["DYJetsToLL_M50_LO"]
dirs['DY_HT_LO']               =  DY_M50_HT + DY_M4to50_HT
#
dirs['TTLep_pow']              = ["TTLep_pow"]
dirs['TTSingleLep_pow']      = ['TTSingleLep_pow']
dirs['Top_pow']                = dirs['TTLep_pow'] + dirs['TTSingleLep_pow'] 
#
dirs['singleTop']        = ["TBar_tWch", "T_tWch" , "T_tch_pow", "TBar_tch_pow"]#, "TToLeptons_tch_powheg", "TBarToLeptons_tch_powheg"]
dirs['singleTop_tch']    = ["T_tch_pow", "TBar_tch_pow"]
#
#
dirs['TTZToLLNuNu']     = ['TTZToLLNuNu_m1to10']
dirs['TTZToQQ']         = ['TTZToQQ']
dirs['TTZ_LO']         = ['TTZ_LO']
##
dirs['TTG']             = ["TTGJets"]
##
dirs['TTW']             = ['TTWToLNu', 'TTWToQQ']
dirs['TTX']             = dirs['TTW'] + dirs['TTG'] + dirs['TTZ_LO']
#
dirs['WJetsToLNu_HT']   = [ "WJetsToLNu_HT70To100", "WJetsToLNu_HT100To200", "WJetsToLNu_HT200To400", "WJetsToLNu_HT400To600", "WJetsToLNu_HT600To800", "WJetsToLNu_HT800To1200", "WJetsToLNu_HT1200To2500", "WJetsToLNu_HT2500ToInf"]
dirs['QCD_HT']         = ["QCD_HT100to200", "QCD_HT200to300", "QCD_HT300to500", "QCD_HT500to700", "QCD_HT700to1000", "QCD_HT1000to1500", "QCD_HT1500to2000", "QCD_HT2000toInf" ]
dirs['QCD_Ele']         = ["QCD_Ele_pt20to30", "QCD_Ele_pt30to50", "QCD_Ele_pt50to80", "QCD_Ele_pt80to120", "QCD_Ele_pt120to170", "QCD_Ele_pt170to300", "QCD_Ele_pt300toInf" ]
dirs['QCD_Mu']          = ["QCD_Mu_pt20to30", "QCD_Mu_pt30to50", "QCD_Mu_pt50to80", "QCD_Mu_pt80to120", "QCD_Mu_pt120to170", "QCD_Mu_pt170to300", "QCD_Mu_pt300to470", "QCD_Mu_pt470to600","QCD_Mu_pt600to800","QCD_Mu_pt800to1000_ext","QCD_Mu_pt1000toInf" ]

dirs['ZInv']            = ["DYJetsToNuNu_HT100to200","DYJetsToNuNu_HT200to400","DYJetsToNuNu_HT400to600","DYJetsToNuNu_HT600to800","DYJetsToNuNu_HT800to1200","DYJetsToNuNu_HT1200to2500","DYJetsToNuNu_HT2500toInf"]  


dirs['WW']              = ["WWToLNuQQ", "WWTo2L2Nu"]
dirs['WZ']              = ["WZTo1L1Nu2Q",  "WZTo1L3Nu", "WZTo2L2Q", "WZTo3LNu_ext"]
dirs['ZZ']              = ["ZZTo2L2Q", "ZZTo2Q2Nu", "ZZTo4L" , "ZZTo2L2Nu"]
dirs['VVTo2L2Nu']       = ["VVTo2L2Nu_comb"]

dirs['VV']              = dirs['WW'] + dirs['WZ'] + dirs['ZZ']
dirs['diBoson']         = dirs['WW'] + dirs['WZ'] + dirs['ZZ']+ dirs['VVTo2L2Nu']


#dirs['allMC']           = dirs['DY_LO'] + dirs['Top_pow'] + dirs['TTZ'] + dirs['TTXNoZ'] + dirs['multiBoson']

directories = { key : [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]] for key in dirs.keys()}

DY_HT_LO_18             = Sample.fromDirectory(name="DY_HT_LO",             treeName="Events", isData=False, color=color.DY,              texName="Drell-Yan",                      directory=directories['DY_HT_LO'])
Top_pow_18              = Sample.fromDirectory(name="Top_pow",              treeName="Events", isData=False, color=color.Top_pow,         texName="t#bar{t}/t",                     directory=directories['Top_pow'])
TTLep_pow_18            = Sample.fromDirectory(name="TTLep_pow",            treeName="Events", isData=False, color=color.TTJets,          texName="t#bar{t}",                       directory=directories['TTLep_pow'])
TTSingleLep_pow_18      = Sample.fromDirectory(name="TTSingleLep_pow",      treeName="Events", isData=False, color=color.TTJets_1l,       texName="t#bar{t} (1l)",                  directory=directories['TTSingleLep_pow'])
Top_pow_18              = Sample.fromDirectory(name="Top_pow",              treeName="Events", isData=False, color=color.TTJets,          texName="t#bar{t}/single-t",                 directory=directories['Top_pow'])
Top_pow_1l_18           = Sample.fromDirectory(name="Top_1l_pow",           treeName="Events", isData=False, color=color.TTJets_1l,       texName="t#bar{t} (1l)",                 directory=directories['TTSingleLep_pow'])
singleTop_18            = Sample.fromDirectory(name="singleTop",            treeName="Events", isData=False, color=color.singleTop,         texName="single top",                        directory=directories['singleTop'])
singleTop_tch_18        = Sample.fromDirectory(name="singleTop_tch",        treeName="Events", isData=False, color=color.singleTop,         texName="single top tch",                    directory=directories['singleTop_tch'])
TTX_18                  = Sample.fromDirectory(name="TTX",                  treeName="Events", isData=False, color=color.TTX,               texName="t#bar{t}G/W/Z",                     directory=directories['TTX'])
TTW_18                  = Sample.fromDirectory(name="TTW",                  treeName="Events", isData=False, color=color.TTW,              texName="t#bar{t}W",                         directory=directories['TTW'])
TTZ_LO_18                  = Sample.fromDirectory(name="TTZ_LO",                  treeName="Events", isData=False, color=color.TTZ,              texName="t#bar{t}Z",                         directory=directories['TTZ_LO'])
TTG_18                  = Sample.fromDirectory(name="TTG",                  treeName="Events", isData=False, color=color.TTG,              texName="t#bar{t}#gamma",                    directory=directories['TTG'])
WJetsToLNu_HT_18        = Sample.fromDirectory(name="WJetsToLNu_HT_",       treeName="Events", isData=False, color=color.WJetsToLNu,       texName="W(l,#nu) + Jets (HT)",              directory=directories['WJetsToLNu_HT'])
VV_18                   = Sample.fromDirectory(name="VV",                   treeName="Events", isData=False, color=color.VV,              texName="VV ",                               directory=directories['VV'])
QCD_HT_18               = Sample.fromDirectory(name="QCD_HT",               treeName="Events", isData=False, color=color.QCD_HT,          texName="QCD (HT)",                 directory=directories['QCD_HT'])
QCD_Ele_18              = Sample.fromDirectory(name="QCD_Ele",              treeName="Events", isData=False, color=color.QCD_Ele,          texName="QCD (Ele)",                 directory=directories['QCD_Ele'])
QCD_Mu_18               = Sample.fromDirectory(name="QCD_Mu",               treeName="Events", isData=False, color=color.QCD_Mu,          texName="QCD (Mu)",                 directory=directories['QCD_Mu'])

ZInv_18                 = Sample.fromDirectory(name="ZInv",                 treeName="Events", isData=False, color=color.ZInv,           texName="Z(#nu,#nu + Jets)",                 directory=directories['ZInv'])

