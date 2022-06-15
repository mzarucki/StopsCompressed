# UL FULL SIM point: T2tt_mStop_500_mLSP_420
python fitResults.py --plotRegionPlot --cardfile T2tt_mStop_500_mLSP_420 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch/priya.hussain/StopsCompressed/results/2016preVFP/others_dphiMetJets_fitAllregion_nbins88_mt95_extramTTrue_CT400_isPromptFalse/cardFiles/T2tt/expected


python fitResults.py --plotRegionPlot --cardfile T2tt_mStop_500_mLSP_420 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch/priya.hussain/StopsCompressed/results/2016preVFP/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/cardFiles/T2tt/expected
## year = "2016postVFP":

python fitResults.py --plotRegionPlot --cardfile T2tt_mStop_500_mLSP_420 --year '2016postVFP' --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch/priya.hussain/StopsCompressed/results/2016postVFP/fitAllregion_dphiJets_nbins88_mt95_extramTTrue_CT400_isPromptFalse/cardFiles/T2tt/expected/ 

python fitResults.py --plotRegionPlot --cardfile T2tt_500_420 --year '2017' --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch-cbe/users/priya.hussain/StopsCompressed/results/2017/fitAllregion_dphiJets_nbins88_mt95_extramTTrue_CT400_isPromptFalse_v2/cardFiles/T2tt/expected/ 

python fitResults.py --plotRegionPlot --cardfile T2tt_500_420 --year '2018' --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch-cbe/users/priya.hussain/StopsCompressed/results/2018/fitAllregion_dphiJets_nbins88_mt95_extramTTrue_CT400_isPromptFalse_v2/cardFiles/T2tt/expected/ 

#comparison between QCD dphijets vs dphimetjet cuts:
python fitResults.py --plotRegionPlot --cardfile T2tt_mStop_500_mLSP_420 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /groups/hephy/cms/priya.hussain/StopsCompressed/results/2016preVFP/2016preVFP/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/cardFiles/T2tt/expected/

python fitResults.py --plotRegionPlot --cardfile T2tt_mStop_500_mLSP_420 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /groups/hephy/cms/priya.hussain/StopsCompressed/results/2016preVFP/2016preVFP/others_dphiMetJets_fitAllregion_nbins88_mt95_extramTTrue_CT400_isPromptFalse/cardFiles/T2tt/expected/
#comparison between QCD dphijets vs dphimetjet cuts for dm 30:

python fitResults.py --plotRegionPlot --cardfile T2tt_500_470 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch-cbe/users/priya.hussain/StopsCompressed/results/2016preVFP/fitAllregion_dphiJets_nbins88_mt95_extramTTrue_CT400_isPromptFalse_v2/cardFiles/T2tt/expected/

python fitResults.py --plotRegionPlot --cardfile T2tt_500_470 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir scratch-cbe/users/priya.hussain/StopsCompressed/results/2016preVFP/fitAllregion_dphiMetJets_nbins88_mt95_extramTTrue_CT400_isPromptFalse_v2/cardFiles/T2tt/expected/

#dphicut b/w jets (AN anti QCD cut) for dm = 50 
python fitResults.py --plotRegionPlot --cardfile T2tt_500_450 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir /scratch-cbe/users/priya.hussain/StopsCompressed/results/2016preVFP/fitAllregion_dphiJets_nbins88_mt95_extramTTrue_CT400_isPromptFalse_v2/cardFiles/T2tt/expected/
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyTrue_R2onlyFalse/cardFiles/T2tt/expected --cores 10 --R1only
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyTrue_R2onlyFalse/cardFiles/T2tt/expected --cores 10 --R1only --postFit
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyTrue_R2onlyFalse/cardFiles/T2tt/expected --cores 10 --R1only --postFit --plotImpacts
#
#
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyTrue/cardFiles/T2tt/expected --cores 10 --R2only
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyTrue/cardFiles/T2tt/expected --cores 10 --R2only --postFit
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyTrue/cardFiles/T2tt/expected --cores 10 --R2only --postFit --plotImpacts
#
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/cardFiles/T2tt/expected --cores 10 
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/cardFiles/T2tt/expected --cores 10  --postFit
#python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_08_07_21/noDY/fitAllregion_nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/cardFiles/T2tt/expected --cores 10  --postFit --plotImpacts


# python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_r_hat --postFit 
# python fitResults.py --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir debugging_r_hat --postFit --plotImpacts


# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/observed_signalInjected 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/observed_signalInjected --postFit 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 400 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/observed_signalInjected --postFit --plotImpacts



# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 450 --carddir fitAllregion_CT_splitCR_140fb/cardFiles/T2tt/expected 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 95 --CT_cut_value 450 --carddir fitAllregion_CT_splitCR_140fb/cardFiles/T2tt/expected 


# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/expected 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/expected 

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/expected --postFit 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/expected --postFit 

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/expected --postFit --plotImpacts 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --carddir fitAllregion_nbins88_mt95_extramTTrue_CT400/cardFiles/T2tt/expected --postFit --plotImpacts 


# exercise with signal injection
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_nbins68_mt100/cardFiles/T2tt/expected 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_nbins68_mt100/cardFiles/T2tt/expected --postFit
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_nbins68_mt100/cardFiles/T2tt/expected --postFit --plotImpacts

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_nbins68_mt100/cardFiles/T2tt/observed_signalInjected 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_nbins68_mt100/cardFiles/T2tt/observed_signalInjected --postFit
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_nbins68_mt100/cardFiles/T2tt/observed_signalInjected --postFit --plotImpacts


# # # split CR 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_mt100_splitCR/cardFiles/T2tt/expected/ 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_490 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_mt100_splitCR/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_mt100_splitCR/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_540 --l1pT_CR_split --mT_cut_value 100 --carddir fitAllregion_mt100_splitCR/cardFiles/T2tt/expected/

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 105 --carddir fitAllregion_mt105_splitCR/cardFiles/T2tt/expected/ 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_490 --l1pT_CR_split --mT_cut_value 105 --carddir fitAllregion_mt105_splitCR/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 105 --carddir fitAllregion_mt105_splitCR/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_540 --l1pT_CR_split --mT_cut_value 105 --carddir fitAllregion_mt105_splitCR/cardFiles/T2tt/expected/

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --carddir fitAllregion_2016_newsplitCR/cardFiles/T2tt/expected/ 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_490 --l1pT_CR_split --mT_cut_value 95 --carddir fitAllregion_2016_newsplitCR/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --l1pT_CR_split --mT_cut_value 95 --carddir fitAllregion_2016_newsplitCR/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_540 --l1pT_CR_split --mT_cut_value 95 --carddir fitAllregion_2016_newsplitCR/cardFiles/T2tt/expected/

# # # no split CR 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --mT_cut_value 100 --carddir fitAllregion_mt100/cardFiles/T2tt/expected/ 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_490 --mT_cut_value 100 --carddir fitAllregion_mt100/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --mT_cut_value 100 --carddir fitAllregion_mt100/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_540 --mT_cut_value 100 --carddir fitAllregion_mt100/cardFiles/T2tt/expected/

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --mT_cut_value 105 --carddir fitAllregion_mt105/cardFiles/T2tt/expected/ 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_490 --mT_cut_value 105 --carddir fitAllregion_mt105/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --mT_cut_value 105 --carddir fitAllregion_mt105/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_540 --mT_cut_value 105 --carddir fitAllregion_mt105/cardFiles/T2tt/expected/

# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_510 --mT_cut_value 95 --carddir fitAllregion_2016_v30SigNonPromptNewSystNewWpt/cardFiles/T2tt/expected/ 
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_490 --mT_cut_value 95 --carddir fitAllregion_2016_v30SigNonPromptNewSystNewWpt/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_470 --mT_cut_value 95 --carddir fitAllregion_2016_v30SigNonPromptNewSystNewWpt/cardFiles/T2tt/expected/
# python fitResults.py  --plotRegionPlot --cardfile T2tt_550_540 --mT_cut_value 95 --carddir fitAllregion_2016_v30SigNonPromptNewSystNewWpt/cardFiles/T2tt/expected/

