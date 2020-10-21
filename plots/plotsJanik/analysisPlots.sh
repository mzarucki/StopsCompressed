
#analysis plot with QCD rejection, i.e. deltaphi && 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data --selection nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3Veto-met200-ht300 --small |& tee debug_small.out
#analysis plot with inverted QCD rejection, invert deltaPhi keep 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_deltaPhiInv --selection nISRJets1p-ntau0-lepSel-deltaPhiJetsInverted-jet3Veto-met200-ht300 --small |& tee debug_deltaPhiInv_small.out
#analysis plot with inverted QCD rejection, invert deltaPhi remove 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_deltaPhiInvNo3jetVeto --selection nISRJets1p-ntau0-lepSel-deltaPhiJetsInverted-met200-ht300 --small |& tee debug_deltaPhiInvNo3jetVeto_small.out
#analysis plot with inverted QCD rejection, invert deltaPhi invert 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_deltaPhiInvInv3jetVeto --selection nISRJets1p-ntau0-lepSel-deltaPhiJetsInverted-jet3VetoInverted-met200-ht300 --small |& tee debug_deltaPhiInvInv3jetVeto_small.out
#analysis plot with inverted QCD rejection, remove deltaPhi keep 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_NodeltaPhi --selection nISRJets1p-ntau0-lepSel-jet3Veto-met200-ht300 --small |& tee debug_NodeltaPhi_small.out
#analysis plot with inverted QCD rejection, remove deltaPhi remove 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_NodeltaPhiNo3jetVeto --selection nISRJets1p-ntau0-lepSel-met200-ht300 --small |& tee debug_NodeltaPhiNo3jetVeto_small.out
#analysis plot with inverted QCD rejection, remove deltaPhi invert 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_NodeltaPhiInv3jetVeto --selection nISRJets1p-ntau0-lepSel-jet3VetoInverted-met200-ht300 --small |& tee debug_NodeltaPhiInv3jetVeto_small.out
#analysis plot with inverted QCD rejection, keep deltaPhi remove 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_No3jetVeto --selection nISRJets1p-ntau0-lepSel-deltaPhiJets-met200-ht300 --small |& tee debug_No3jetVeto_small.out
#analysis plot with inverted QCD rejection, keep deltaPhi invert 3jetVeto
python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data_Inv3jetVeto --selection nISRJets1p-ntau0-lepSel-deltaPhiJets-jet3VetoInverted-met200-ht300 --small |& tee debug_Inv3jetVeto_small.out






# no phi
# python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data --logLevel DEBUG --selection nISRJets1p-ntau0-lepSel-jet3Veto-met200-ht300 --small |& tee debugNoPhi_small.out

#inverted phi
# python analysisPlots.py --era Run2016 --reweightPU Central --targetDir v19MC_v20Data --logLevel DEBUG --selection nISRJets1p-ntau0-lepSel-deltaPhiJetsInverted-jet3Veto-met200-ht300 --small |& tee debugInvPhi_small.out

# python analysisPlots.py --era Run2016 --reweightPU Central --small --targetDir v17MC_v18Data --logLevel DEBUG |& tee debug_small.out
# python analysisPlots.py --era Run2016 --reweightPU Central --small --targetDir v15MC_v18Data --logLevel DEBUG