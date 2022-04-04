# StopsCompressed
```
cmsrel CMSSW_10_6_25
cd CMSSW_10_6_25
cmsenv
git cms-init
git clone https://github.com/HephyAnalysisSW/StopsCompressed.git
git clone https://github.com/HephyAnalysisSW/Samples.git
git clone https://github.com/HephyAnalysisSW/RootTools.git
git clone https://github.com/HephyAnalysisSW/Analysis.git
cd StopsCompressed
git checkout -b UltraLegacy 
cd ../Samples 
git checkout -b StopsCompressedUL

git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

#compile
scram b -j9

# Get combine
# Latest recommendations at https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#setting-up-the-environment-and-installation
cd $CMSSW_BASE/src
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git fetch origin
#git checkout v8.0.1
##for UL recommendations changed, will get new version :
git checkout v8.2.0
scramv1 b clean; scramv1 b # always make a clean build


# for combineTools
cd $CMSSW_BASE/src
wget https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-https.sh; source sparse-checkout-https.sh
scram b -j 8

# for correctionlib installation
git clone --recursive git@github.com:cms-nanoAOD/correctionlib.git
cd correctionlib
make PYTHON=python2
make install  # set PREFIX=... to change from default (./correctionlib)
cp correctionlib Analysis/Tools/python/
```
