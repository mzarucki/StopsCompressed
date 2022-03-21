import copy, os, sys
from RootTools.core.Sample import Sample 
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
try:
    data_directory_ = sys.modules['__main__'].data_directory
except:
    from StopsCompressed.samples.default_locations import default_locations
    data_directory_ = default_locations.data_2016_36fb_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory_ = sys.modules['__main__'].postProcessing_directory
except:
  from StopsCompressed.samples.default_locations import default_locations
  postProcessing_directory_ = default_locations.data_2016_36fb_postProcessing_directory 


logger.info("Loading data samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))

dirs = {}
for (run, version) in [('B','_ver2'),('C',''),('D',''),('E',''),('F','')]: 
    runTag = 'Run2016' + run  + version + '_HIPM_UL_preVFP'
    dirs["MET_Run2016"       	 	+ run + version + '_preVFP'] = ["MET_"	          + runTag ]
for (run, version) in [('F',''),('G',''),('H','')]:
    runTag = 'Run2016' + run + '_UL' + version
    dirs["MET_Run2016"                  + run + version ] = ["MET_"               + runTag ]

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['MET']:
    merge(pd, 'Run2016BCD_preVFP',   ['Run2016B_ver2_preVFP', 'Run2016C_preVFP', 'Run2016D_preVFP'])
    merge(pd, 'Run2016preVFP', 	     ['Run2016BCD_preVFP', 'Run2016E_preVFP', 'Run2016F_preVFP'])
    merge(pd, 'Run2016FGH', 	     [ 'Run2016F', 'Run2016G', 'Run2016H'])
    merge(pd, 'Run2016',   	     ['Run2016FGH', 'Run2016preVFP'])
    

for key in dirs:
    dirs[key] = [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

#l_tot = (5.883+2.646+4.353+4.050+3.124+7.554+8.494+0.217) # old normtag

allSamples_Data25ns = []

MET_Run2016                	  = getSample('MET',       	  'Run2016',           (36)*1000)

allSamples_Data25ns += [MET_Run2016]

Run2016 	= Sample.combine("Run2016", [MET_Run2016], texName = "Run2016")
Run2016.lumi 	= (36)*1000
allSamples_Data25ns.append(Run2016)


for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True


