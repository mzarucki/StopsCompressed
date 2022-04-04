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
    data_directory_ = default_locations.data_2017_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory_ = sys.modules['__main__'].postProcessing_directory
except:
  from StopsCompressed.samples.default_locations import default_locations
  postProcessing_directory_ = default_locations.data_2017_postProcessing_directory 


logger.info("Loading data samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))

dirs = {}
for (run, version) in [('B',''),('C',''),('D',''),('E',''),('F','')]: 
    runTag = 'Run2017' + run + '_14Dec2018' + version
    dirs["JetHT_Run2017"         	+ run + version ] = ["JetHT_"             + runTag ]
    dirs["MET_Run2017"       	 	+ run + version ] = ["MET_"	          + runTag ]
    dirs["SingleElectron_Run2017"   	+ run + version ] = ["SingleElectron_"    + runTag ]
    dirs["SingleMuon_Run2017"       	+ run + version ] = ["SingleMuon_"        + runTag ]

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['MET', 'JetHT', 'SingleElectron', 'SingleMuon']:
    merge(pd, 'Run2017BCD',    ['Run2017B', 'Run2017C', 'Run2017D'])
    merge(pd, 'Run2017', ['Run2017BCD', 'Run2017E', 'Run2017F'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

#l_tot = (5.883+2.646+4.353+4.050+3.124+7.554+8.494+0.217) # old normtag

allSamples_Data25ns = []

JetHT_Run2017                  	  = getSample('JetHT',            'Run2017',           (41.5)*1000)
MET_Run2017                	  = getSample('MET',       	  'Run2017',           (41.5)*1000)
SingleElectron_Run2017            = getSample('SingleElectron',   'Run2017',           (41.5)*1000)
SingleMuon_Run2017                = getSample('SingleMuon',       'Run2017',           (41.5)*1000)

allSamples_Data25ns += [MET_Run2017, JetHT_Run2017, SingleElectron_Run2017, SingleMuon_Run2017]

Run2017 = Sample.combine("Run2017", [MET_Run2017, JetHT_Run2017,SingleElectron_Run2017, SingleMuon_Run2017], texName = "Run2017")
Run2017.lumi = (41.5)*1000
allSamples_Data25ns.append(Run2017)


for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True


