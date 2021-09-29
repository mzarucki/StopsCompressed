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
git checkout -b StopsCompressed

git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

#compile
scram b -j9

# Get combine
# Latest recommendations at https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#setting-up-the-environment-and-installation
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

```
