''' Gen Samples for compressed stops 4 body decay'''

import os,sys
import ROOT
# RootTools
from RootTools.core.standard import *

results_directory = '/afs/hephy.at/data/cms07/StopsCompressed/fwlite_signals_fastSim/'

# sqlite3 sample cache file
dbFile = os.path.join( results_directory, 'sample_cache', 'fwlite_benchmarks.db')
overwrite = False

# Logging
if __name__ == "__main__":
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger('DEBUG')


fwlite_signals_fastSim_Stops2l_200k = FWLiteSample.fromDAS("fwlite_signals_fastSim_Stops2l_200k", "/Stops2l/schoef-Stops2l-393b4278a04aeb4c6106d6aae1db462e/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')

fwlite_signals_DisplacedStops_500_200 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_500_200", "/DisplacedStops-mstop-500-ctau-200/schoef-Stops2l-2514d262db8aee2ee8f9b68a132535de/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')

fwlite_signals_DisplacedStops_500_0p2 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_500_0p2", "/DisplacedStops-mstop-500-ctau-0p2/schoef-Stops2l-696607c465bf9d1efb6998a42053c58f/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_500_0p1 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_500_0p1", "/DisplacedStops-mstop-500-ctau-0p1/schoef-Stops2l-b3305f94ae3c4426e3b8a42cc54b1e32/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_500_0p01 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_500_0p01", "/DisplacedStops-mstop-500-ctau-0p01/schoef-Stops2l-f16749d4bb27f8b758497fd8fa01f5f4/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_500_0p001 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_500_0p001", "/DisplacedStops-mstop-500-ctau-0p001/schoef-Stops2l-e6ae6bf58c2190ad6428e8d970e9029d/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')

fwlite_signals_DisplacedStops_250_200 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_250_200", "/DisplacedStops-mstop-250-ctau-200/schoef-Stops2l-2160d9a73c43039b0c883d8f50793a06/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_250_0p2 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_250_0p2", "/DisplacedStops-mstop-250-ctau-0p2/schoef-Stops2l-018519dd1326b5580094371464eea427/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_250_0p1 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_250_0p1", "/DisplacedStops-mstop-250-ctau-0p1/schoef-Stops2l-a19b5846e9911d7daa1e4ef4f70e9350/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_250_0p01 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_250_0p01", "/DisplacedStops-mstop-250-ctau-0p01/schoef-Stops2l-00b89d02933778e18fabfa9e3d5e723a/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
fwlite_signals_DisplacedStops_250_0p001 = FWLiteSample.fromDAS("fwlite_signals_DisplacedStops_250_0p001", "/DisplacedStops-mstop-250-ctau-0p001/schoef-Stops2l-b7cb2997c733ed6634f766239526f924/USER", "phys03", dbFile = dbFile, overwrite=overwrite, prefix='root://hephyse.oeaw.ac.at/')
