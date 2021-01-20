import os
import time

cmd = "submit --title='est16' --walltime 12:00:00 "
#cmd = "echo"

#regions for split CR(m,h): 68 (44+24)
#regions for split CR(m,h,vh): 80 (44+36)
#for i in range(80):
# regions for AN splitting:56 (44+12)
for i in range(56):
	os.system(cmd+" 'python run_estimate.py --selectEstimator WJets     --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator DY        --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator Top       --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator singleTop --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator VV        --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator TTX       --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator QCD       --year 2016 --all --selectRegion %s'"%str(i))
	os.system(cmd+" 'python run_estimate.py --selectEstimator Data      --year 2016 --all --selectRegion %s'"%str(i))


#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 0  --overwrite   
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator WJets --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator DY --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator Top --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator singleTop --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator ZInv --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator VV --year 2016 --selectRegion 23  --overwrite
#
#
#
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator TTX --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator QCD --year 2016 --selectRegion 23  --overwrite
#
#
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 0  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 1  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 2  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 3  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 4  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 5  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 6  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 7  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 8  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 9  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 10  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 11  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 12  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 13  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 14  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 15  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 16  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 17  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 18  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 19  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 20  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 21  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 22  --overwrite
#python run_estimate.py --selectEstimator Data --year 2016 --selectRegion 23  --overwrite
