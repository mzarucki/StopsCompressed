#!/bin/sh
for era in "Run2016" "Run2016preVFP" "Run2016postVFP" "Run2017" "Run2018"
do
    sbatch --job-name="plot_$era" \
	   --output="$SCRATCHDIR/batch_output/analyis_plot_$era-%A.out" \
	   --error="$SCRATCHDIR/batch_output/analyis_plot_$era-%A.err" \
	   --time="03:00:00" \
	   --wrap="python analysisPlots.py --era $era --reweightPU Central --targetDir UL_v03"
done

