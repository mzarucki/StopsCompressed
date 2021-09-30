# StopsCompressed
```
cmsrel CMSSW_10_2_12_patch1
cd CMSSW_10_2_12_patch1/src
cmsenv
git cms-init
git clone https://github.com/HephyAnalysisSW/StopsCompressed
git clone https://github.com/HephyAnalysisSW/Samples.git
git clone https://github.com/HephyAnalysisSW/RootTools.git
git clone https://github.com/HephyAnalysisSW/Analysis.git
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

#compile
scram b -j9
```

# Get combine
Latest recommendations at https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#setting-up-the-environment-and-installation
cd $CMSSW_BASE/src
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v8.0.1
scramv1 b clean; scramv1 b # always make a clean build


# for combineTools
cd $CMSSW_BASE/src
wget https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-https.sh; source sparse-checkout-https.sh
scram b -j 8


# Running limits

* Produce or copy/use the cached estimates for the yields

* Creating a datacard and running the combine command on a single mass point (mostly for testing reasons) go to `StopsCompressed/Analysis/python/run/testing/` and execute the command inside `check_limit.sh`, e.g.
```
python check_limit.py --fitAll --expected --skipFitDiagnostics --l1pT_CR_split --extra_mT_cut --CT_cut_value 400 --only=T2tt_550_510
```

* If you want to scale processes you can use the flags `--scaleWjets` or `--scaleTTbar` available inside `check_limit.py`. Print statements are output while running `sh check_limit.sh` (see above). However, these scale the processes globally. For more specific scaling, implement your changes here:
https://github.com/jandrejk/StopsCompressed/blob/MC_based/Analysis/python/run/testing/check_limit.py#L302-L312

* After you tested with one mass point you can submit the whole mass point grid using 
```
python runLimitOnClipBatch.py
```
Inside the script you can adjust the walltime etc.

* After your jobs are finished you run without the `--only`-option
```
python check_limit.py --fitAll --expected --skipFitDiagnostics --l1pT_CR_split --extra_mT_cut --CT_cut_value 400
```
This produces a .pkl and .root file which are inputs to the plotting script

* Run the plotting (`cd StopsCompressed/Analysis/python/plot/` first) by
```
sh plot_SMS_limit_v2.py
```
but don't forget to set the path correctly inside `plot_SMS_limit_v2.py`:
https://github.com/jandrejk/StopsCompressed/blob/MC_based/Analysis/python/plot/plot_SMS_limit_v2.py#L67

and

https://github.com/jandrejk/StopsCompressed/blob/MC_based/Analysis/python/plot/plot_SMS_limit_v2.py#L82
