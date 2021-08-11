#!/usr/bin/env python
import os

#data_directory              = ' /scratch/priya.hussain/StopsCompressed/nanoTuples/'
#postProcessing_directory    = 'compstops_2016_nano_v11/MetSingleLep/'
#from StopsCompressed.samples.nanoTuples_FastSim_Summer16_postProcessed import signals_T2tt


#signalEstimators = [s.name for s in signals_T2tt]
#signalEstimators = []

import time

#cmd = "submit --title='limit' "
#cmd = "submit --title='limit' --walltime 12:00:00 --cmssw 10_2_18"
#cmd = "submit --title='limit' --walltime 02:55:00"
cmd = "echo"

#print len(signalEstimators)
#for i, estimator in enumerate(signalEstimators):
for i in range(280):
#     #os.system(cmd+" 'python run_limit.py --control2016 --skipFitDiagnostics --expected --only=%s'"%str(i))
#     #to run control regions 2016
#     #os.system(cmd+" 'python run_limit.py --control2016 --expected --only=%s'"%str(i))
#     #os.system(cmd+" 'python run_limit.py --control2016 --only=%s'"%str(i))
#     ### change v2 later
    #os.system(cmd+" 'python check_limit.py --fitAll --expected --skipFitDiagnostics --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --only=%s'"%str(i))
    os.system(cmd+" 'python check_limit.py --fitAll --expected --skipFitDiagnostics --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --isPrompt --only=%s'"%str(i))
    # os.system(cmd+" 'python check_limit.py --fitAll --expected --skipFitDiagnostics --usePromptSignalOnly --only=%s'"%str(i))


# os.system(cmd+" 'python check_limit.py --fitAll --expected --only=T2tt_500_440'")    
    
