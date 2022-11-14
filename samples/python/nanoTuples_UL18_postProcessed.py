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
#                ##"DYJetsToLL_M4to50_HT70to100",   ## not in samples list of 2016 Analysis
                "DYJetsToLL_M4to50_HT100to200",
#                "DYJetsToLL_M4to50_HT200to400",
#                "DYJetsToLL_M4to50_HT400to600",
                "DYJetsToLL_M4to50_HT600toInf"
                ] 

DY_M50_HT =[
            "DYJetsToLL_M50_HT70to100",
            "DYJetsToLL_M50_HT100to200",
            "DYJetsToLL_M50_HT200to400",
            "DYJetsToLL_M50_HT400to600",
            "DYJetsToLL_M50_HT600to800",
            "DYJetsToLL_M50_HT800to1200",
            "DYJetsToLL_M50_HT1200to2500",
            "DYJetsToLL_M50_HT2500toInf"
            ] 


dirs = {}
dirs['DY_HT_LO']         =  DY_M50_HT + DY_M4to50_HT
dirs['DY_HT_M50_LO']     =  DY_M50_HT 
#dirs['DY_HT_M5to50_LO']  =  DY_M5to50_HT 
#
dirs['TTLep_pow']        = ["TTLep_pow_CP5"]
dirs['TTSingleLep_pow']  = ["TTSingleLep_pow_CP5"]
dirs['Top_pow']          = dirs['TTLep_pow'] + dirs['TTSingleLep_pow']
#
##
dirs['singleTop']        = ["TBar_tWch_ext", "T_tWch_ext" , "TBar_tch_pow", "T_tch_pow"] #  "TToLeptons_tch_powheg", "TBarToLeptons_tch_powheg"]
dirs['singleTop_tch']    = ["TBar_tch_pow", "T_tch_pow"] 
#
#
dirs['TTZ_LO']         = ['TTZ_LO']
##
dirs['TTG']             = ["TTGJets"]
##
#dirs['TTW']             = ['TTWToLNu_CP5', 'TTWToQQ']
dirs['TTW']             = ['TTW_LO']

dirs['TTX']             = dirs['TTW'] + dirs['TTG'] + dirs['TTZ_LO']

##added WJetsHT800T01200 from legacy as place holder to check the affect : compstops_2017_nano_v8
dirs['WJetsToLNu_HT']   = [
          "WJetsToLNu_HT70to100", 
          "WJetsToLNu_HT100to200", 
          "WJetsToLNu_HT200to400", 
          "WJetsToLNu_HT400to600", 
          "WJetsToLNu_HT600to800", 
          "WJetsToLNu_HT800to1200",
          "WJetsToLNu_HT1200to2500", 
          "WJetsToLNu_HT2500toInf"  
          ] 

dirs['WW']              = ["WWTo1L1Nu2Q", "WWTo2L2Nu"] 
dirs['WZ']              = ["WZTo3LNu_amcatnlo", "WZTo1L1Nu2Q", "WZTo2Q2L"] # ,"WZTo1L3Nu"
dirs['ZZ']              = [ "ZZTo4L", "ZZTo2Nu2Q", "ZZTo2Q2L", "ZZTo2L2Nu"]

dirs['VV']              = dirs['WW'] + dirs['WZ'] + dirs['ZZ']

dirs['QCD_HT'] 		= [
    "QCD_HT50to100",
    "QCD_HT100to200",  
    "QCD_HT200to300",
    "QCD_HT300to500", 
    "QCD_HT500to700", 
    "QCD_HT700to1000" ,
    "QCD_HT1000to1500",   
    "QCD_HT1500to2000", 
    "QCD_HT2000toInf"
]
dirs['ZInv']            = [
  "DYJetsToNuNu_HT100to200", 
  "DYJetsToNuNu_HT200to400", 
  "DYJetsToNuNu_HT400to600", 
  "DYJetsToNuNu_HT600to800", 
  "DYJetsToNuNu_HT800to1200", 
  "DYJetsToNuNu_HT1200to2500", 
  "DYJetsToNuNu_HT2500toInf" 
]

dirs['others']           = dirs['DY_HT_LO'] + dirs['singleTop'] + dirs['TTX'] + dirs['VV']

#dirs['others']           = dirs['DY_HT_LO'] + dirs['singleTop'] + dirs['TTX'] + dirs['VV']
#dirs['fakes'] 		= dirs['DY_HT_LO'] + dirs['Top_pow'] + dirs['singleTop'] + dirs['TTX'] + dirs['WJetsToLNu_HT'] + dirs['VV'] + dirs['QCD_HT'] +dirs['ZInv']

directories = { key : [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]] for key in dirs.keys()}


DY_HT_LO_18             = Sample.fromDirectory(name="DY_HT_LO",             treeName="Events", isData=False, color=color.DY,              texName="Drell-Yan",                      directory=directories['DY_HT_LO'])
#DY_HT_M50_LO_18         = Sample.fromDirectory(name="DY_HT_M50_LO",         treeName="Events", isData=False, color=color.DY,              texName="Drell-Yan_M50",                    directory=directories['DY_HT_M50_LO'])
Top_pow_18              = Sample.fromDirectory(name="Top_pow",              treeName="Events", isData=False, color=color.Top_pow,         texName="t#bar{t}",                     directory=directories['Top_pow'])
TTLep_pow_18            = Sample.fromDirectory(name="TTLep_pow",            treeName="Events", isData=False, color=color.TTJets,          texName="t#bar{t}",                       directory=directories['TTLep_pow'])
#TTJets_1l_18      = Sample.fromDirectory(name="TTJets_SingleLepton",      treeName="Events", isData=False, color=color.TTJets_1l,       texName="t#bar{t} (1l)",                  directory=directories['TTJets_SingleLepton'])
#TTJets_2l_18         	= Sample.fromDirectory(name="TTJets_DiLept",       treeName="Events", isData=False, color=color.TTJets,          texName="t#bar{t}",                 directory=directories['TTJets_DiLept'])
#Top_pow_1l_18      	= Sample.fromDirectory(name="Top_1l_pow",           treeName="Events", isData=False, color=color.TTJets_1l,       texName="t#bar{t} (1l)",                 directory=directories['TTSingleLep_pow'])
singleTop_18      	= Sample.fromDirectory(name="singleTop",            treeName="Events", isData=False, color=color.singleTop,         texName="single top",                        directory=directories['singleTop'])
singleTop_tch_18  	= Sample.fromDirectory(name="singleTop_tch",        treeName="Events", isData=False, color=color.singleTop,         texName="single top tch",                    directory=directories['singleTop_tch'])
TTX_18            	= Sample.fromDirectory(name="TTX",                  treeName="Events", isData=False, color=color.TTX,               texName="t#bar{t}G/W/Z",                     directory=directories['TTX'])
TTW_LO_18            	= Sample.fromDirectory(name="TTW_LO",                  treeName="Events", isData=False, color=color.TTW,              texName="t#bar{t}W",                         directory=directories['TTW'])
#TTZ_LO_18            	= Sample.fromDirectory(name="TTZ_LO",               treeName="Events", isData=False, color=color.TTZ,              texName="t#bar{t}Z",                         directory=directories['TTZ_LO'])
TTG_18            	= Sample.fromDirectory(name="TTG",                  treeName="Events", isData=False, color=color.TTG,              texName="t#bar{t}#gamma",                    directory=directories['TTG'])
WJetsToLNu_HT_18  	= Sample.fromDirectory(name="WJetsToLNu_HT",       treeName="Events", isData=False, color=color.WJetsToLNu,       texName="W(l,#nu) + Jets (HT)",              directory=directories['WJetsToLNu_HT'])
VV_18           	= Sample.fromDirectory(name="VV",                   treeName="Events", isData=False, color=color.VV,              texName="VV ",                               directory=directories['VV'])
QCD_HT_18  		= Sample.fromDirectory(name="QCD_HT",    	    treeName="Events", isData=False, color=color.QCD_HT,          texName="QCD (HT)",                 directory=directories['QCD_HT'])
ZInv_18  		= Sample.fromDirectory(name="ZInv",    	    	    treeName="Events", isData=False, color=color.ZInv,           texName="Z(#nu,#nu + Jets)",                 directory=directories['ZInv'])
Others_18                = Sample.fromDirectory(name="others",              treeName="Events", isData=False, color=color.others,           texName="Others",                 directory=directories['others'])    
#Fakes_18  		= Sample.fromDirectory(name="fakes",    	    treeName="Events", isData=False, color=color.fakes,           texName="Fakes(MC-nonPrompt)",                 directory=directories['fakes'])

