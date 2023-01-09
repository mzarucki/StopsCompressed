from StopsCompressed.Analysis.Region import Region

# Extra regions for testing 

# Reminder on preselection from Setup.py
# default_MET         = (200, -999) # NOTE: reduced from 300 to 200 for lowMET region
# default_HT          = (200,-999)
# default_nISRJet     = (1,-999)
# default_dphiJets    = True
# default_hardJets    = True
# default_tauVeto     = True
# default_lepVeto     = True
# default_jetVeto     = True # FIXME: unused. Supposed to be hardJets?
# default_l1_prompt   = False
# default_dphiMetJets = False

# MET > 200 GeV, HT > 200 GeV

SRc = Region("mt", (95,-999))

SR_lepPt = Region("l1_pt", (3.5,30))

## SRZ
SRZ                     = Region("ISRJets_pt", (130,-999)) + Region("abs(l1_pdgId)", (13,13)) + Region("l1_pt", (6,30)) # trigger plateau cuts

### SR1
SR1_base                = SR_lepPt + Region("ISRJets_pt", (100,-999)) + Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) # NOTE: base = no MET/HT/CT cuts
SR1Z_base               =                                               Region("nSoftBJets", (0,0)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-1.5, 1.5)) # NOTE: base = no MET/HT/CT/ISR/lepPt cuts

SR1                     = SR1_base + Region("CT1", (300,-999)) + Region("HT", (400,-999)) # CT1 = MET > 300, HT > 400 GeV # NOTE: 'default' definition with additional CT > 300 GeV cut
SR1_CT300               = SR1_base + Region("CT1", (300,-999))                            # CT1 = MET > 300, HT > 400 GeV # NOTE: should be redundnant with SR1 = simplified definiton
SR1_CT200               = SR1_base + Region("CT1", (200,-999))                            # CT1 = MET > 200, HT > 300 GeV = CTZ
SR1_CT200_HT300         = SR1_base + Region("CT1", (200,-999)) + Region("HT", (300,-999)) # CT1 = MET > 200, HT > 300 GeV = CTZ # NOTE: should be redundnant with SR1_CT200

SR1c                    = SR1 + SRc

# split CTZ
SR1_MET200_HT200        = SR1_base + Region("MET_pt", (200,-999)) + Region("HT", (200,-999)) # split CTZ = CTZ1 (= low HT bin)
SR1_MET200_HT300        = SR1_base + Region("MET_pt", (200,-999)) + Region("HT", (300,-999)) # split CTZ = CTZ2

## SR1Z
SR1Z                    = SR1Z_base + SRZ + Region("MET_pt", (200,300)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1Z1                   = SR1Z + Region("HT", (200,300))
SR1Z2                   = SR1Z + Region("HT", (300,400))
SR1Z3                   = SR1Z + Region("HT", (400,-999))

SR1Z1_tightIPZ          = SR1Z1 + Region("abs(l1_dxy)", (0,0.005)) + Region("abs(l1_dz)", (0,0.01))
SR1Z2_tightIPZ          = SR1Z2 + Region("abs(l1_dxy)", (0,0.005)) + Region("abs(l1_dz)", (0,0.01))
SR1Z3_tightIPZ          = SR1Z3 + Region("abs(l1_dxy)", (0,0.005)) + Region("abs(l1_dz)", (0,0.01))

## SR1Zc
SR1Zc                   = SR1Z_base + SRZ + SRc
SR1Z1c                  = SR1Zc + Region("MET_pt", (200,300)) + Region("HT", (200,300)) # NOTE: replaced CT1 with separate MET and HT cuts
SR1Z2c                  = SR1Zc + Region("MET_pt", (200,300)) + Region("HT", (300,400))
SR1Z3c                  = SR1Zc + Region("MET_pt", (200,300)) + Region("HT", (400,-999))

SR1Z1c_tightIPZ         = SR1Z1c + Region("abs(l1_dxy)", (0,0.005)) + Region("abs(l1_dz)", (0,0.01))
SR1Z2c_tightIPZ         = SR1Z2c + Region("abs(l1_dxy)", (0,0.005)) + Region("abs(l1_dz)", (0,0.01))
SR1Z3c_tightIPZ         = SR1Z3c + Region("abs(l1_dxy)", (0,0.005)) + Region("abs(l1_dz)", (0,0.01))

### SR2
SR2_base                = SR_lepPt + Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-2.4, 2.4)) # NOTE: base = no MET/HT/CT/ISR cuts
SR2Z_base               =            Region("nSoftBJets", (1,-999)) + Region("nHardBJets", (0,0)) + Region("l1_eta", (-2.4, 2.4)) # NOTE: base = no MET/HT/CT/ISR/lepPt cuts

SR2                     = SR2_base + Region("CT2", (300,-999)) + Region("HT", (300,-999)) + Region("ISRJets_pt", (325,-999)) # CT2 = MET > 300, ISR jet pT > 325 GeV # NOTE: 'default' definition with additional CT > 300 GeV cut
SR2_CT300               = SR2_base + Region("CT2", (300,-999)) + Region("HT", (300,-999))                                    # CT2 = MET > 300, ISR jet pT > 325 GeV # NOTE: should be redundant with SR2 = simplified definition
SR2_CT200               = SR2_base + Region("CT2", (200,-999)) + Region("HT", (300,-999))                                    # CT2 = MET > 200, ISR jet pT > 225 GeV
SR2_CT200_ISR225        = SR2_base + Region("CT2", (200,-999)) + Region("HT", (300,-999)) + Region("ISRJets_pt", (225,-999)) # CT2 = MET > 200, ISR jet pT > 225 GeV # NOTE: should be redundant with SR2_CT200

# split CTZ
SR2_MET200_ISR225 = SR2_base + Region("MET_pt", (200,-999)) + Region("ISRJets_pt", (225,-999)) # split CTZ = CTZ1 (= low ISR jet pT bin)
SR2_MET200_ISR325 = SR2_base + Region("MET_pt", (200,-999)) + Region("ISRJets_pt", (325,-999)) # split CTZ = CTZ2

SR2_MET200_ISR225_HT200 = SR2_base + Region("MET_pt", (200,-999)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (200,-999)) # split CTZ = CTZ1 (= low ISR jet pT bin + low HT bin) # NOTE: should be equivalent to SR2_MET200_ISR225
SR2_MET200_ISR225_HT300 = SR2_base + Region("MET_pt", (200,-999)) + Region("ISRJets_pt", (225,-999)) + Region("HT", (300,-999)) # split CTZ = CTZ2 (= low ISR jet pT bin + higher HT bin)
                                                                                                                                
SR2_MET200_ISR325_HT200 = SR2_base + Region("MET_pt", (200,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (200,-999)) # split CTZ = CTZ1 (= higher ISR jet pT bin + low HT bin) # NOTE: should be equivalent to SR2_MET200_ISR325_HT300
SR2_MET200_ISR325_HT300 = SR2_base + Region("MET_pt", (200,-999)) + Region("ISRJets_pt", (325,-999)) + Region("HT", (300,-999)) # split CTZ = CTZ2 (= higher ISR jet pT bin + higher HT bin)

## SR2Z
SR2Z  = SRZ + SR2Z_base + Region("MET_pt", (200,300))
SR2Z1 = SR2Z + Region("HT", (200,300))  # NOTE: removed ISR225 cut 
SR2Z2 = SR2Z + Region("HT", (300,-999)) # NOTE: removed ISR225 cut
