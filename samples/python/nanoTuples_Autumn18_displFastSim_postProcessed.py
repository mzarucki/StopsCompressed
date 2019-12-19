import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

from StopsCompressed.samples.color import color

from StopsCompressed.samples.default_locations import default_locations

data_directory_ = default_locations.mc_2018_data_directory
postProcessing_directory_ = default_locations.mc_2018_postProcessing_directory

logger.info("Loading MC samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))



dirs = {}
dirs['DisplacedStops_mStop_250_ctau_0p01']   = ['DisplacedStops_mStop_250_ctau_0p01']

directories = { key : [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]] for key in dirs.keys()}

#

# FullSim signals
DisplacedStops_mStop_250_ctau_0p01    = Sample.fromDirectory(name="DisplacedStops_mStop_250_ctau_0p01",     treeName="Events", isData=False, color=color.DY,     texName="mStop250ctau0p01",     directory=directories['DisplacedStops_mStop_250_ctau_0p01'])

signals_displ = [
    DisplacedStops_mStop_250_ctau_0p01,
]

for s in signals_displ:
    #t1, mStop, t2, ctau = s.name.replace('Displaced_','').split('_')
    #s.mStop = int(mStop)
    #s.mNeu = int(ctau)
    s.isFastSim = True

