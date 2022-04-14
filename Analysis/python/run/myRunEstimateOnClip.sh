#!/bin/bash -x
#
#SBATCH --job-name=run_estimate
#SBATCH --chdir=/users/dietrich.liko/working/MyStopsCompressed/CMSSW_10_6_25/src/StopsCompressed/Analysis/python/run
#SBATCH --output=/scratch-cbe/users/dietrich.liko/batch_output/run_estimate-%A-%a.out
#SBATCH --error=/scratch-cbe/users/dietrich.liko/batch_output/run_estimate-%A-%a.err
#SBATCH --time=00:30:00
#SBATCH --array=0-440 # all samples
##SBATCH --array=0-5 # 2016preVFP

(for era in "2016preVFP" "2016postVFP" "2017" "2018"; do [[ $1 == $era ]] && exit 0; done) || exit 1

SAMPLES=("Top" "QCD" "WJets" "Others" "Data")
MAXREGION=88

REGION=$((SLURM_ARRAY_TASK_ID % MAXREGION))
SAMPLE=${SAMPLES[$((SLURM_ARRAY_TASK_ID / MAXREGION))]}

python run_estimate.py --selectEstimator $SAMPLE --year $1 --all --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --selectRegion $REGION
