#!/usr/bin/env python
import os
import time

cmd = "submit --title='limit' --walltime 01:30:00"
# cmd = "echo"

for i in range(280):
    os.system(cmd+" 'python check_limit.py --fitAll --expected --skipFitDiagnostics --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --only=%s'"%str(i))
