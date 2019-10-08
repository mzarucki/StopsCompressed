# StopsCompressed
cmsrel CMSSW_10_2_12_patch1
cd CMSSW_10_2_12_patch1/src
cmsenv
git cms-init
git clone https://github.com/HephyAnalysisSW/StopsCompressed
cd $CMSSW_BASE/src
git clone https://github.com/HephyAnalysisSW/Samples.git
cd $CMSSW_BASE/src
git clone https://github.com/HephyAnalysisSW/Analysis.git
cd $CMSSW_BASE/src
#compile
scram b -j9
