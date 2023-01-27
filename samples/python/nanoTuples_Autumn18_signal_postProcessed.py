#Standard import 
import copy, os, sys
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

#RootTools
from RootTools.core.standard import *

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
  #postProcessing_directory_ = default_locations.mc_2018_postProcessing_directory 
  postProcessing_directory_ = default_locations.signal_2018_postProcessing_directory 

logger.info("Loading Signal samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))

signals_T2tt=[]

try:
    for f in os.listdir(os.path.join(data_directory_, postProcessing_directory_, 'T2tt')):
        if f.endswith('.root') and f.startswith('T2tt_'):
            name = f.replace('.root','')
            mStop, mNeu = name.replace('T2tt_','').split('_')
    
            tmp = Sample.fromFiles(\
                name = name,
                files = [os.path.join(os.path.join(data_directory_, postProcessing_directory_,'T2tt',f))],
                treeName = "Events",
                isData = False,
                color = 2,
                texName = "#tilde{t} #rightarrow t#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}} ("+mStop+","+mNeu+")"
            )
    
            tmp.mStop = int(mStop)
            tmp.mNeu = int(mNeu)
            tmp.isFastSim = True
    
            exec("%s=tmp"%name)
            exec("signals_T2tt.append(%s)"%name)
    
    logger.info("Loaded %i T2tt signals", len(signals_T2tt))
    logger.debug("Loaded T2tt signals: %s", ",".join([s.name for s in signals_T2tt]))
except:
    logger.info("No T2tt signals found.")

signals_T2bW=[]

try:
    for f in os.listdir(os.path.join(data_directory_, postProcessing_directory_, 'T2bW')):
        if f.endswith('.root') and f.startswith('T2bW_'):
            name = f.replace('.root','')
            mStop, mNeu = name.replace('T2bW_','').split('_')
    
            tmp = Sample.fromFiles(\
                name = name,
                files = [os.path.join(os.path.join(data_directory_, postProcessing_directory_,'T2bW',f))],
                treeName = "Events",
                isData = False,
                color = 6 ,
                texName = "#tilde{t} #rightarrow t#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}} ("+mStop+","+mNeu+")"
            )
    
            tmp.mStop = int(mStop)
            tmp.mNeu = int(mNeu)
            tmp.isFastSim = True
    
            exec("%s=tmp"%name)
            exec("signals_T2bW.append(%s)"%name)
    
    logger.info("Loaded %i T2bW signals", len(signals_T2bW))
    logger.debug("Loaded T2bW signals: %s", ",".join([s.name for s in signals_T2bW]))
except:
    logger.info("No T2bW signals found.")

signals_TChiWZ=[]

try:
    for f in os.listdir(os.path.join(data_directory_, postProcessing_directory_, 'TChiWZ')):
        if f.endswith('.root') and f.startswith('TChiWZ_'):
            name = f.replace('.root','')
            mCha, mNeu = name.replace('TChiWZ_','').split('_')
    
            tmp = Sample.fromFiles(\
                name = name,
                files = [os.path.join(os.path.join(data_directory_, postProcessing_directory_,'TChiWZ',f))],
                treeName = "Events",
                isData = False,
                color = 7 ,
                texName = "#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}#tilde{#chi}_{#lower[-0.3]{2}}^{#lower[0.4]{0}} #rightarrow WZ#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}}#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}} ("+mCha+","+mNeu+")"
            )
    
            tmp.mCha = int(mCha)
            tmp.mNeu = int(mNeu)
            tmp.isFastSim = True
    
            exec("%s=tmp"%name)
            exec("signals_TChiWZ.append(%s)"%name)
    
    logger.info("Loaded %i TChiWZ signals", len(signals_TChiWZ))
    logger.debug("Loaded TChiWZ signals: %s", ",".join([s.name for s in signals_TChiWZ]))
except:
    logger.info("No TChiWZ signals found.")
