import os
import time

cmd = "submit --title='est16' --walltime 07:00:00 --cmssw 10_2_18 "
#cmd = "echo"

# print cmd
# print "Is the walltime ok?"
# exit

#regions for split CR(m,h): 68 (44+24)
#regions for split CR(m,h,vh): 80 (44+36)
#for i in range(80):
# regions for AN splitting:56 (44+12)

for i in range(88): #needed for split l1_pt region and split in further mT region 
#	os.system(cmd+" 'python run_estimate.py --selectEstimator WJets     --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))
#	os.system(cmd+" 'python run_estimate.py --selectEstimator Others    --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))
#	os.system(cmd+" 'python run_estimate.py --selectEstimator Top       --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))
#	os.system(cmd+" 'python run_estimate.py --selectEstimator QCD       --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))
#	os.system(cmd+" 'python run_estimate.py --selectEstimator Data      --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))

##	os.system(cmd+" 'python run_estimate.py --selectEstimator singleTop --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))
##	os.system(cmd+" 'python run_estimate.py --selectEstimator VV        --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))
##	os.system(cmd+" 'python run_estimate.py --selectEstimator TTX       --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion %s'"%str(i))

#for running prompt estimates:
#for i in range(88): #needed for split l1_pt region and split in further mT region 
	os.system(cmd+" 'python run_estimate.py --selectEstimator WJets     --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --isPrompt --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator Top       --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --isPrompt --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator Others    --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --isPrompt --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator QCD       --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --isPrompt --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator Data      --year 2016 --all  --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --isPrompt --selectRegion %s'"%str(i))

