class triggerSelector:
    def __init__(self, year, era=None):
        if year in ["UL2016", "UL2016_preVFP"]:
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_Mu3_PFJet40", "HLT_Mu8", "HLT_Mu17", "HLT_Mu27"]
            self.jet     = ["HLT_PFJet40"]
            self.e       = ["HLT_Ele8_CaloIdM_TrackIdM_PFJet30", "HLT_Ele17_CaloIdM_TrackIdM_PFJet30", "HLT_Ele23_CaloIdM_TrackIdM_PFJet30"] 

        elif year == "UL2017":
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_Mu3_PFJet40", "HLT_Mu8", "HLT_Mu17", "HLT_Mu27"]
            self.jet     = ["HLT_PFJet40"]
            self.e       = ["HLT_Ele8_CaloIdM_TrackIdM_PFJet30", "HLT_Ele17_CaloIdM_TrackIdM_PFJet30", "HLT_Ele23_CaloIdM_TrackIdM_PFJet30"] 

        elif year == "UL2018":
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_Mu3_PFJet40", "HLT_Mu8", "HLT_Mu17", "HLT_Mu27"]
            self.jet     = ["HLT_PFJet40"]
            self.e       = ["HLT_Ele8_CaloIdM_TrackIdM_PFJet30", "HLT_Ele17_CaloIdM_TrackIdM_PFJet30", "HLT_Ele23_CaloIdM_TrackIdM_PFJet30"] 

        else:
            raise NotImplementedError("Trigger selection %r not implemented"%year)

        # define which triggers should be used for which dataset. could join several lists of triggers
        self.MET            = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.met ] ) if self.met else None
        self.JetHT          = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.jet ] )if self.jet else None
        self.SingleMuon     = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.m ] ) if self.m else None
        self.DoubleMuon     = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.m ] ) if self.m else None
        self.DoubleEG 	    = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None
        self.SingleElectron = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None

        # define an arbitrary hierarchy
        if year == "UL2016" or year == "UL2016_preVFP" or year == "UL2017":
            #self.PDHierarchy = ["MET"]
            self.PDHierarchy = [ "MET" , "DoubleEG"]
        else:
            # DoubleEG and SingleElectron PDs are merged into EGamma. No change necessary for MC though.
            self.PDHierarchy = ["MET" ]
            #self.PDHierarchy = [ "MET", "EGamma", "JetHT", "SingleMuon" ]

    def __getVeto(self, cutString):
        return "!%s"%cutString

    def getSelection(self, PD):
        found = False
        cutString = ""
        if PD == "MC":
            #return "(%s)"%"||".join([self.MET, self.JetHT, self.SingleMuon, self.SingleElectron])
            return "(%s)"%"||".join([self.MET])
        else:
            #for x in reversed(self.PDHierarchy):
	    #    if not getattr( self, x ): continue 
            #    if found:
            #        cutString += "&&%s"%self.__getVeto(getattr(self,x))
            #    if x in PD:# == getattr(self, PD):
            #        found = True
            #        cutString = getattr(self, x)

	    print "PD will be: ", PD.split("_")[0]
	    cutString = getattr( self, PD.split("_")[0] )
	    if cutString == "":
	            raise NotImplementedError( "Trigger selection for %s not implemented" %PD )
            return "(%s)"%cutString

class triggerSelectorMetLepEnergy:
    def __init__(self, year, era=None):
        if year in ["UL2016", "UL2016_preVFP"]:
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_IsoMu24", "HLT_IsoTkMu24"]
            self.jet     = ["HLT_PFJet40"]
            self.e       = ["HLT_Ele27_WPTight_Gsf"] 

        elif year == "UL2017":
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_IsoMu27"]
            self.jet     = ["HLT_PFJet40"]
            self.e       = ["HLT_Ele35_WPTight_Gsf"] 

        elif year == "UL2018":
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_IsoMu24"]
            self.jet     = ["HLT_PFJet40"]
            self.e       = ["HLT_Ele32_WPTight_Gsf"] 

        else:
            raise NotImplementedError("Trigger selection %r not implemented"%year)

        # define which triggers should be used for which dataset. could join several lists of triggers
        self.MET            = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.met ] ) if self.met else None
        self.JetHT          = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.jet ] )if self.jet else None
        self.SingleMuon     = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.m ] ) if self.m else None
        self.DoubleMuon     = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.m ] ) if self.m else None
        self.DoubleEG 	    = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None
        self.SingleElectron = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None

        # define an arbitrary hierarchy
        if year == "UL2016" or year == "UL2016_preVFP" or year == "UL2017":
            #self.PDHierarchy = ["MET"]
            self.PDHierarchy = [ "MET" , "DoubleEG"]
        else:
            # DoubleEG and SingleElectron PDs are merged into EGamma. No change necessary for MC though.
            self.PDHierarchy = ["MET" ]
            #self.PDHierarchy = [ "MET", "EGamma", "JetHT", "SingleMuon" ]

    def __getVeto(self, cutString):
        return "!%s"%cutString

    def getSelection(self, PD):
        found = False
        cutString = ""
        if PD == "MC":
            #return "(%s)"%"||".join([self.MET, self.JetHT, self.SingleMuon, self.SingleElectron])
            return "(%s)"%"||".join([self.MET])
        else:
            #for x in reversed(self.PDHierarchy):
	    #    if not getattr( self, x ): continue 
            #    if found:
            #        cutString += "&&%s"%self.__getVeto(getattr(self,x))
            #    if x in PD:# == getattr(self, PD):
            #        found = True
            #        cutString = getattr(self, x)

	    print "PD will be: ", PD.split("_")[0]
	    cutString = getattr( self, PD.split("_")[0] )
	    if cutString == "":
	            raise NotImplementedError( "Trigger selection for %s not implemented" %PD )
            return "(%s)"%cutString