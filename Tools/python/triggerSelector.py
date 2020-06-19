class triggerSelector:
    def __init__(self, year, era=None):
        if year == 2016:
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_IsoMu24", "HLT_Mu50"]
            self.jet     = ["HLT_PFJet450", "HLT_AK8PFJet450", "HLT_PFHT800"]
            self.e       = ["HLT_Ele27_WPTight_Gsf"] 

        elif year == 2017:
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_IsoMu24", "HLT_Mu50"]
            self.jet     = ["HLT_PFJet450", "HLT_AK8PFJet450", "HLT_PFHT800"]
            self.e       = ["HLT_Ele35_WPTight_Gsf"] 

        elif year == 2018:
            self.met     = ["HLT_PFMET90_PFMHT90_IDTight", "HLT_PFMET100_PFMHT100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMET120_PFMHT120_IDTight"]
            self.m       = ["HLT_IsoMu24", "HLT_Mu50"]
            self.jet     = ["HLT_PFJet450", "HLT_AK8PFJet450", "HLT_PFHT800"]
            self.e       = ["HLT_Ele32_WPTight_Gsf" , "HLT_Ele115_CaloIdVT_GsfTrkIdT"] 

        else:
            raise NotImplementedError("Trigger selection %r not implemented"%year)

        # define which triggers should be used for which dataset. could join several lists of triggers
        self.MET            = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.met ] )
        #self.SingleElectron = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None
        #self.JetHT          = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.jet ] )if self.jet else None
        #self.SingleMuon     = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.m ] ) if self.m else None
        #self.SingleElectron = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None
        #self.EGamma 	    = "(%s)"%"||".join( [ "Alt$(%s,0)"%trigger for trigger in self.e ] ) if self.e else None

        # define an arbitrary hierarchy
        if year == 2016 or year == 2017:
            self.PDHierarchy = [ "MET" ]
        else:
            # DoubleEG and SingleElectron PDs are merged into EGamma. No change necessary for MC though.
            self.PDHierarchy = [ "MET" ]
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
            for x in reversed(self.PDHierarchy):
		if not getattr( self, x ): continue 
                if found:
                    cutString += "&&%s"%self.__getVeto(getattr(self,x))
                if x in PD:# == getattr(self, PD):
                    found = True
                    cutString = getattr(self, x)

	    if cutString == "":
		    raise NotImplementedError( "Trigger selection for %s not implemented" %PD )
            return "(%s)"%cutString

