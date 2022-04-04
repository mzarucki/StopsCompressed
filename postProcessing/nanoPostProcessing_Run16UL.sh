#python nanoPostProcessing.py  --skim MetSingleLep --year UL2016  --processingEra compstops_UL16v9_nano_v5 --triggerSelection  --sample MET_Run2016F_UL #SPLIT10
#python nanoPostProcessing.py  --skim MetSingleLep --year UL2016  --processingEra compstops_UL16v9_nano_v5 --triggerSelection  --sample MET_Run2016G_UL #SPLIT20
#python nanoPostProcessing.py  --skim MetSingleLep --year UL2016  --processingEra compstops_UL16v9_nano_v5 --triggerSelection  --sample MET_Run2016H_UL #SPLIT19 
##Test for DoubleEG Fake 
python nanoPostProcessing.py  --skim Fake --year UL2016  --processingEra compstops_UL16v9_nano_v5 --triggerSelection  --sample DoubleEG_Run2016F_UL #SPLIT10
python nanoPostProcessing.py  --skim Fake --year UL2016  --processingEra compstops_UL16v9_nano_v5 --triggerSelection  --sample DoubleEG_Run2016G_UL #SPLIT10
python nanoPostProcessing.py  --skim Fake --year UL2016  --processingEra compstops_UL16v9_nano_v5 --triggerSelection  --sample DoubleEG_Run2016H_UL #SPLIT10

