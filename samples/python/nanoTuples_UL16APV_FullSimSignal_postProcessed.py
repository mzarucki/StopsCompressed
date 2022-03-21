import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

from StopsCompressed.samples.color import color

data_directory_ = '/scratch/priya.hussain/StopsCompressed/nanoTuples/'
postProcessing_directory_ = 'compstops_UL16APVv9_nano_v5/MetSingleLep/'

logger.info("Loading MC samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))



dirs = {}
dirs['T2tt_mStop_500_mLSP_420']  = ['SMS_T2tt_mStop_500_mLSP_420']
dirs['T2tt_mStop_500_mLSP_450']  = ['SMS_T2tt_mStop_500_mLSP_450']
dirs['T2tt_mStop_500_mLSP_470']  = ['SMS_T2tt_mStop_500_mLSP_470']

directories = { key : [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]] for key in dirs.keys()}

#

# FullSim signals
T2tt_mStop_500_mLSP_420   = Sample.fromDirectory(name="T2tt_mStop_500_mLSP_420",    treeName="Events", isData=False, color=color.DY,     texName="T2tt(500,420)",     directory=directories['T2tt_mStop_500_mLSP_420'])
T2tt_mStop_500_mLSP_450   = Sample.fromDirectory(name="T2tt_mStop_500_mLSP_450",    treeName="Events", isData=False, color=color.DY,     texName="T2tt(500,450)",     directory=directories['T2tt_mStop_500_mLSP_450'])
T2tt_mStop_500_mLSP_470   = Sample.fromDirectory(name="T2tt_mStop_500_mLSP_470",    treeName="Events", isData=False, color=color.DY,     texName="T2tt(500,470)",     directory=directories['T2tt_mStop_500_mLSP_470'])

signals_T2tt = [
    T2tt_mStop_500_mLSP_420,
    T2tt_mStop_500_mLSP_450,
    T2tt_mStop_500_mLSP_470,
]

for s in signals_T2tt:
    t1, mStop, t2, mNeu = s.name.replace('T2tt_','').split('_')
    s.mStop = int(mStop)
    s.mNeu = int(mNeu)
    s.isFastSim = False

