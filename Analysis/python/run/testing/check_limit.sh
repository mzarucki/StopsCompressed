# python check_limit.py --fitAll --expected --only=T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --CT_cut_value 400 --skipFitDiagnostics --R2only

#python check_limit.py --fitAll --expected --only=T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --CT_cut_value 400 --skipFitDiagnostics --R1only

#python check_limit.py --fitAll --expected --only=T2tt_550_510 --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --CT_cut_value 400 --skipFitDiagnostics 

# python check_limit.py --fitAll --expected --only=T2tt_550_540 --l1pT_CR_split --extra_mT_cut --mT_cut_value 95 --CT_cut_value 400 --skipFitDiagnostics
# python check_limit.py --fitAll --expected --only=T2tt_550_470 --l1pT_CR_split --extra_mT_cut --mT_cut_value 95 --CT_cut_value 400 --skipFitDiagnostics
# --scale 3.8997
 
# python check_limit.py --fitAll --expected --only=T2tt_550_510 --mT_cut_value 95 --CT_cut_value 450 --skipFitDiagnostics 
# python check_limit.py --fitAll --signalInjection --only=T2tt_550_510 --l1pT_CR_split --mT_cut_value 100

#UL changes for Full Sim point:


#python check_limit.py --fitAll --expected --only=T2tt_mStop_500_mLSP_420 --year '2016preVFP' --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --CT_cut_value 400 --skipFitDiagnostics --fullSim 
python check_limit.py --fitAll --expected --only=T2tt_mStop_500_mLSP_420 --year '2016postVFP' --l1pT_CR_split --mT_cut_value 95 --extra_mT_cut --CT_cut_value 400 --skipFitDiagnostics --fullSim
