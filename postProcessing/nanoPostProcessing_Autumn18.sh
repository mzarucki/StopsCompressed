### Signal ###

## Scans
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample T2tt_dM-10to80     --susySignal --fastSim #SPLIT20
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample T2bW_X05_dM-10to80 --susySignal --fastSim #SPLIT20
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TChiWZ             --susySignal --fastSim #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample N2C1-higgsino      --susySignal --fastSim #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample N2N1-higgsino      --susySignal --fastSim #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample MSSM-higgsino      --susySignal --fastSim #SPLIT10

### TTJets ###

## LO
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTbar #SPLIT5

## TTLep
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTLep_pow #SPLIT20
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTSingleLep_pow #SPLIT20

### WJets ###

## HT-binned
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT70to100    #SPLIT20
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT100to200   #SPLIT20
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT200to400   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT400to600   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT600to800   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT800to1200  #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT1200to2500 #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WJetsToLNu_HT2500toInf  #SPLIT10

### ZInv ###
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT100to200   #SPLIT15
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT200to400   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT400to600   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT600to800   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT800to1200  #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT1200to2500 #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToNuNu_HT2500toInf  #SPLIT5

### DY ###

## LO
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50        #SPLIT20
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_LO     #SPLIT20
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M10to50_LO #SPLIT20

## HT-binned

# low mass 
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --LHEHTCut 70 --sample DYJetsToLL_M10to50_LO #SPLIT20
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M4to50_HT70to100         #SPLIT10 # NOTE: sample empty
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M4to50_HT100to200        #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M4to50_HT200to400        #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M4to50_HT400to600        #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M4to50_HT600toInf        #SPLIT5

# high mass
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --LHEHTCut 70 --sample DYJetsToLL_M50_LO #SPLIT20
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT70to100        #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT100to200       #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT200to400       #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT400to600 DYJetsToLL_M50_HT400to600_ext #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT600to800       #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT800to1200      #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT1200to2500     #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample DYJetsToLL_M50_HT2500toInf      #SPLIT5

### QCD ###
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT50to100    #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT100to200   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT200to300   #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT300to500   #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT500to700   #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT700to1000  #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT1000to1500 #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT1500to2000 #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample QCD_HT2000toInf  #SPLIT5

#### Top ####

### ST ####
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample T_tch_pow    #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TBar_tch_pow #SPLIT10

python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample T_tWch       #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TBar_tWch    #SPLIT10

python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TToLeptons_sch_amcatnlo #SPLIT20

#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample tZq_ll #SPLIT10
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample tWll   #SPLIT11
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample THQ    #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample THW    #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTTT   #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample tWnunu #SPLIT5

### TTX ###

## TTW
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTW_LO   #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTWToLNu #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTWToQQ  #SPLIT14

## TTZ
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTZ_LO  #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTZToQQ #SPLIT10

python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTZToLLNuNu        #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTZToLLNuNu_m1to10 #SPLIT5

## TTG
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTGJets #SPLIT10

## TTH
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTHbbLep    #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTHnobb_pow #SPLIT10


#### Di/Multi-boson ####

### VV ###
 
## LO
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WW #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WZ #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample ZZ #SPLIT5

## NLO
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample VVTo2L2Nu #SPLIT10

# WW
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WWTo1L1Nu2Q #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WWToLNuQQ   #SPLIT10

# WZ
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WZTo3LNu_amcatnlo #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WZTo2L2Q          #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WZTo1L3Nu         #SPLIT10

# ZZ
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample ZZTo4L    #SPLIT10
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample ZZTo2Q2Nu #SPLIT5
python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample ZZTo2L2Q  #SPLIT20

### Multi-boson ###

#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WWW_4F #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WWZ    #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample WZZ    #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample ZZZ    #SPLIT5

### Rare ###

#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTWZ #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTWW #SPLIT5
#python nanoPostProcessing.py --skim Met --year 2018 --processingEra stops_2018_nano_v1 --sample TTZZ #SPLIT5
