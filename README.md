# StopsCompressed
```
cmsrel CMSSW_10_6_25
cd CMSSW_10_6_25/src
cmsenv


# Download patched version of install_correctionslib.sh
curl -sLO https://gist.githubusercontent.com/dietrichliko/96865aa4c47d7fabc7d746d163fc7cf5/raw/3cc1cb04dd0991b5dc920b3c45266a5b82baea0e/install_correctionslib.sh
. ./install_correctionslib.sh
rm install_correctionslib.sh

# clone repositories
git clone git@github.com:HephyAnalysisSW/StopsCompressed -b UltraLegacy
git clone git@github.com:HephyAnalysisSW/Samples.git -b StopsCompressedUL
git clone git@github.com:HephyAnalysisSW/RootTools.git -b StopCompressed
git clone git@github.com:HephyAnalysisSW/Analysis.git -b StopsCompressed
git clone git@github.com:priyasajid/nanoAOD-tools.git PhysicsTools/NanoAODTools

#compile
scram b -j9

# to be verified ...

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
