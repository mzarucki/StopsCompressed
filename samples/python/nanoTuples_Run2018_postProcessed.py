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
    data_directory_ = default_locations.data_2018_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory_ = sys.modules['__main__'].postProcessing_directory
except:
  from StopsCompressed.samples.default_locations import default_locations
  postProcessing_directory_ = default_locations.data_2018_postProcessing_directory 


logger.info("Loading data samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))

dirs = {}
for pd in ['MET', 'SingleMuon', 'SingleElectron','JetHT']:
    for (run, version) in [('A','25Oct2019'),('B','25Oct2019'),('C','25Oct2019'),('D','25Oct2019')]:
    #for (run, version) in [('A',''), ('B',''),('C',''),('D','')]: 
        runTag = "Run2018" + run
        versionTag = "%s_%s"%(runTag, version)
        dirs["%s_%s"%(pd, runTag) ] = ["%s_%s"%(pd, versionTag)]

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

#for pd in ['MET', 'JetHT', 'SingleElectron', 'SingleMuon']:
for pd in ['MET']:
    merge(pd, 'Run2018', ['Run2018A', 'Run2018B', 'Run2018C', 'Run2018D'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

#l_tot = (5.883+2.646+4.353+4.050+3.124+7.554+8.494+0.217) # old normtag

allSamples_Data25ns = []

#JetHT_Run2017                  	  = getSample('JetHT',            'Run2017',           (41.5)*1000)
MET_Run2018                	  = getSample('MET',       	  'Run2018',           (59.83)*1000)
#SingleElectron_Run2017            = getSample('SingleElectron',   'Run2017',           (41.5)*1000)
#SingleMuon_Run2017                = getSample('SingleMuon',       'Run2017',           (41.5)*1000)

#allSamples_Data25ns += [MET_Run2017, JetHT_Run2017, SingleElectron_Run2017, SingleMuon_Run2017]
allSamples_Data25ns += [MET_Run2018]

#Run2017 = Sample.combine("Run2017", [MET_Run2017, JetHT_Run2017,SingleElectron_Run2017, SingleMuon_Run2017], texName = "Run2017")
Run2018 = Sample.combine("Run2018", [MET_Run2018], texName = "Run2018")
Run2018.lumi = (59.83)*1000
allSamples_Data25ns.append(Run2018)


for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True


