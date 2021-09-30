#Standard import
import copy
import os
import ROOT as R
import glob 
# RootTools
from RootTools.core.standard          import *

#user specific
from StopsCompressed.Analysis.SystematicEstimator import jmeVariations, metVariations
from StopsCompressed.Tools.user            import analysis_results, cache_directory
from StopsCompressed.Tools.cutInterpreter  import *
from StopsCompressed.Analysis.SetupHelpers import *

from Analysis.Tools.metFilters        import getFilterCut

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger( "INFO", logFile=None)
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger( "INFO", logFile=None )
else:
    import logging
    logger = logging.getLogger(__name__)

default_HT          = (300,-999)
default_nISRJet     = (1,-999)
default_dphiJets    = True
default_tauVeto     = True
default_hardJets    = True
default_lepVeto     = True
default_jetVeto     = True
default_MET         = (300, -999)
default_prompt      = False
default_isLooseAndNotTight = False

# default_HI_tight    = True
# default_isSignal    = False

class Setup:
    def __init__(self, year=2016):

        logger.info("Initializing Setup")
        self.analysis_results = analysis_results
        self.prefixes         = []
        self.externalCuts     = []
        self.year             = year

        #Default cuts and requirements. Those three things below are used to determine the key in the cache!
        self.parameters   = {
            "HT":           default_HT,
            "nISRJet":      default_nISRJet,
            "dphiJets":     default_dphiJets,
            "tauVeto":      default_tauVeto,
            "hardJets":     default_hardJets,
            "lepVeto":      default_lepVeto,
            "jetVeto":      default_jetVeto,
            "MET":          default_MET,
            "l1_prompt":    default_prompt,
            "l1_isLooseAndNotTight" : default_isLooseAndNotTight
            # "l1_HI"    :    default_HI_tight,
            # "isSignal" :    default_isSignal
        }


        self.puWeight = "reweightPUVUp" if self.year == 2018 else "reweightPU"
        
        for macro in glob.glob(os.path.join(os.environ['CMSSW_BASE'], 'src/StopsCompressed/Analysis/macros/*.C')) :
            if R.gROOT.LoadMacro(macro): #compile it
                raise OSError("Unable to load: {}".format(macro))
        
        self.sys = {"weight":"weight", "reweight":[ self.puWeight, "reweightnISR", "reweightwPt","reweightL1Prefire", "reweightBTag_SF", "reweightLeptonSF_new(l1_pt,l1_eta,l1_pdgId)", "reweightHEM"], "selectionModifier":None} 
        
        #if runOnLxPlus:
        #    # Set the redirector in the samples repository to the global redirector
        #    from Samples.Tools.config import redirector_global as redirector
        if year == 2016 :
            #define samples
            from StopsCompressed.samples.nanoTuples_Summer16_postProcessed 	     import DY_HT_LO_16, Top_pow_16 , singleTop_16, ZInv_16, TTX_16, WJetsToLNu_HT_16,VV_16, QCD_HT_16

            from StopsCompressed.samples.nanoTuples_Run2016_17July2018_postProcessed import Run2016
            DY           = DY_HT_LO_16
            WJets        = WJetsToLNu_HT_16
            Top          = Top_pow_16
            singleTop    = singleTop_16 
            VV           = VV_16 
            QCD		     = QCD_HT_16
            TTX          = TTX_16
            ZInv    	 = ZInv_16
            data         = Run2016

        elif year == 2017 :
            #define samples
            from StopsCompressed.samples.nanoTuples_Fall17_postProcessed  	    import DY_HT_LO_17, TTLep_pow_17 ,TTSingleLep_pow_17 , singleTop_17, singleTop_tch_17, TTX_17, WJetsToLNu_HT_17,VV_17
            from StopsCompressed.samples.nanoTuples_Run2017_nanoAODv6_postProcessed import Run2017
            DY           = DY_HT_LO_17
            WJets       = WJetsToLNu_HT_17
            TTLep        = TTLep_pow_17
            TTSingleLep  = TTSingleLep_pow_17
            singleTop    = singleTop_17 
            VV           = VV_17 
            TTX          = TTX_17
            data        = Run2017

        elif year == 2018 :
            #define samples
            from StopsCompressed.samples.nanoTuples_Autumn18_postProcessed  import DY_HT_LO_18, TTLep_pow_18 ,TTSingleLep_pow_18 , singleTop_18, singleTop_tch_18, TTX_18, WJetsToLNu_HT_18,VV_18
            #from StopsCompressed.samples.nanoTuples_Run2018_14Dec2018_postProcessed import Run2018
            DY           = DY_HT_LO_18
            WJets       = WJetsToLNu_HT_18
            TTLep        = TTLep_pow_18
            TTSingleLep  = TTSingleLep_pow_18
            singleTop    = singleTop_18 
            VV           = VV_18 
            TTX          = TTX_18
            #data        = Run2018



        if year == 2016:
            self.lumi     = 35.92*1000
            self.dataLumi = 35.92*1000
        elif year == 2017:
            self.lumi     = 41.53*1000
            self.dataLumi = 41.53*1000
        elif year == 2018:
            self.lumi     = 59.74*1000
            self.dataLumi = 59.74*1000

        mc           = [DY, WJets, Top, singleTop, VV, TTX, ZInv, QCD ]
        self.processes = {

            'DY'        : DY,
            'WJets'     : WJets,
            'Top'       : Top,
            'singleTop' : singleTop,
            'VV'        : VV,
            'TTX'       : TTX,        
	        'ZInv'      : ZInv,
	        'QCD'       : QCD
        }
        self.processes["Data"] = data

        self.lumi     = data.lumi
        self.dataLumi = data.lumi # get from data samples later
        

    def prefix(self, channel="all"):
        return "_".join(self.prefixes+[self.preselection("MC", channel=channel)["prefix"]])

    def defaultCacheDir(self,specificNameForSensitivityStudy=''):
        
        if (specificNameForSensitivityStudy) :
            cacheDir = os.path.join(cache_directory, str(self.year), "estimates_{}".format(specificNameForSensitivityStudy))
        else :
            cacheDir = os.path.join(cache_directory, str(self.year), "estimates") #switch of MCs (->v26)
        # cacheDir = os.path.join(cache_directory, str(self.year), "estimates_mt100") #switch of MCs (->v26)
        # cacheDir = os.path.join(cache_directory, str(self.year), "check_wPt_syst") #switch of MCs (->v26)
        # cacheDir = os.path.join(cache_directory, str(self.year), "estimates_AN_comb_sigv30_promptNewWpt") #switch of MCs (->v26)
        # cacheDir = os.path.join(cache_directory, str(self.year), "estimates_AN_comb_sigv30_NewWpt") #switch of MCs (->v26)
        # cacheDir = os.path.join(cache_directory, str(self.year), "estimates_AN_comb_sigv30") #switch of MCs (->v26)
        # cacheDir = os.path.join(cache_directory, str(self.year), "estimates_AN_comb")
        #cacheDir = os.path.join(cache_directory, str(self.year), "estimates_splitCR")
        #cacheDir = os.path.join(cache_directory, str(self.year), "estimates_split_erCR")
        logger.info("Default cache dir is: %s", cacheDir)

        return cacheDir

    #Clone the setup and optinally modify the systematic variation
    def sysClone(self, sys=None, parameters=None):
        """Clone setup and change systematic if provided"""

        res            = copy.copy(self)
        res.sys        = copy.deepcopy(self.sys)
        res.parameters = copy.deepcopy(self.parameters)

        if sys:
            for k in sys.keys():
                if k=="remove":
                    for i in sys[k]:
                      res.sys["reweight"].remove(i)
                elif k=="reweight":
                    res.sys[k] = list(set(res.sys[k]+sys[k])) #Add with unique elements
                    
                    for upOrDown in ["Up","Down"]:
                        if "reweightL1Prefire"+upOrDown             in res.sys[k]: res.sys[k].remove("reweightL1Prefire")
                        if "reweightPU"+upOrDown                    in res.sys[k]: res.sys[k].remove("reweightPU")
                        if 'reweightBTag_SF_b_'+upOrDown            in res.sys[k]: res.sys[k].remove('reweightBTag_SF')
                        if 'reweightBTag_SF_l_'+upOrDown            in res.sys[k]: res.sys[k].remove('reweightBTag_SF')
                        if 'reweightBTag_SF_FS_'+upOrDown         in res.sys[k]: res.sys[k].remove('reweightBTag_SF')
                        if 'reweightLeptonFastSimSF'+upOrDown     in res.sys[k]: res.sys[k].remove('reweightLeptonFastSimSF')
                        if "reweightnISR"+upOrDown                    in res.sys[k]: res.sys[k].remove("reweightnISR")
                        if "reweightwPt"+upOrDown                    in res.sys[k]: res.sys[k].remove("reweightwPt")
                        if "reweightLeptonSF_new{}(l1_pt,l1_eta,l1_pdgId)".format(upOrDown)              in res.sys[k]: res.sys[k].remove("reweightLeptonSF_new(l1_pt,l1_eta,l1_pdgId)")
                        if "reweightFakeRate{}(l1_pt,l1_eta,l1_pdgId)".format(upOrDown)              in res.sys[k]: res.sys[k].remove("reweightFakeRate(l1_pt,l1_eta,l1_pdgId)")


                else:
                    res.sys[k] = sys[k]

        if parameters:
            for k in parameters.keys():
                res.parameters[k] = parameters[k]
        return res

    def defaultParameters(self, update={} ):
        assert type(update)==type({}), "Update arguments with key arg dictionary. Got this: %r"%update
        res = copy.deepcopy(self.parameters)
        res.update(update)
        return res
    def weightString(self):
        return "*".join([self.sys['weight']] + (self.sys['reweight'] if self.sys['reweight'] else []))


    def preselection(self, dataMC , channel="all", isFastSim = False):
        """Get preselection  cutstring."""
        cut = self.selection(dataMC, channel = channel, isFastSim = False, **self.parameters)
        logger.debug("Using cut-string: %s", cut)
        return cut

    def selection(self, dataMC, HT, MET, nISRJet, dphiJets, tauVeto, hardJets, lepVeto, jetVeto,l1_prompt, l1_isLooseAndNotTight,channel='all', isFastSim =False):
        """Define full selection
           dataMC: "Data" or "MC"
           channel: "all", "e" or "mu"
           isFastSim: adjust filter cut etc. for fastsim
        """
        #if not HT:   		HT   	  	= self.parameters["ht"]
        #if not mt:   		mt   	  	= self.parameters["mt"]
        #if not CT1:   		CT1   	  	= self.parameters["CT1"]
        #if not CT2:   		CT2   	  	= self.parameters["CT2"]

        #Consistency checks
        assert dataMC in ["Data","MC","DataMC"], "dataMC = Data or MC or DataMC, got %r."%dataMC
        if self.sys['selectionModifier']:
            assert self.sys['selectionModifier'] in jmeVariations+metVariations, "Don't know about systematic variation %r, take one of %s"%(self.sys['selectionModifier'], ",".join(jmeVariations+metVariations))
        #assert channel in allChannels, "channel must be one of "+",".join(allChannels)+". Got %r."%channel
        #Postfix for variables (only for MC and if we have a jme variation)
        sysStr = ""
        if dataMC == "MC" and self.sys['selectionModifier'] in jmeVariations + metVariations:
            sysStr = "_" + self.sys['selectionModifier']

        res={"cuts":[], "prefixes":[]}
        if hardJets: 
            res['prefixes'].append('nHardJetsTo2')
            res['cuts'].append('Sum$(JetGood_pt>=60&&abs(Jet_eta)<2.4)<=2')

        if dphiJets:
            res['prefixes'].append('deltaPhiJets')
            res['cuts'].append('dphij0j1<2.5')

        if tauVeto:
            res['prefixes'].append('tauveto')
            res['cuts'].append('nGoodTaus==0')

        if lepVeto:
            res['prefixes'].append('lepSel')
            res['cuts'].append('Sum$(lep_pt>20&&abs(lep_dxy)<0.02&&abs(lep_dz)<0.1)<=1&&l1_pt>0')

        if nISRJet:
            res['prefixes'].append('nISRJets')
            res['cuts'].append('nISRJets>=1')
        
        if l1_prompt:
             res['prefixes'].append('l1_prompt')
             res['cuts'].append('l1_isPrompt>=1')
        
        if l1_isLooseAndNotTight :
            res['prefixes'].append('l1_HI_dxy_dz')
            res['cuts'].append('l1_HI>5&&abs(l1_dxy)<0.02&&abs(l1_dz)<0.1')

            
            
        # if l1_HI :
        #     res['prefixes'].append('l1_HI')
        #     res['cuts'].append('l1_HI<=5')
        # else :
        #     if (isSignal == False) : # in case of signal don't apply HI cut - the variable l1_HI is not even in the ntuple
        #         res['prefixes'].append('l1_HI')
        #         res['cuts'].append('l1_HI>5') 


       # if nISRJet and not (nISRJet[0]==0 and nISRJet[1]<0):
       #     assert nISRJet[0]>=0 and (nISRJet[1]>=nISRJet[0] or nISRJet[1]<0), "Not a good nISRJet selection: %r"%nISRJet
       #     njetsstr = "nISRJets"+sysStr+">="+str(nISRJet[0])
       #     prefix   = "nISRJet"+str(nISRJet[0])
       #     if nISRJet[1]>=0:
       #         njetsstr+= "&&"+"nISRJets"+sysStr+"<="+str(nISRJet[1])
       #         if nISRJet[1]!=nISRJet[0]: prefix+=str(nISRJet[1])
#      #          if nJet[1]!=nJet[0]: prefix+="To"+str(nJet[1])
       #     else:
       #         prefix+="p"
       #     res["cuts"].append(njetsstr)
       #     res["prefixes"].append(prefix)


        #MET cut
        if MET and not (MET[0]==0 and MET[1]<0):
            assert MET[0]>=0 and (MET[1]>=MET[0] or MET[1]<0), "Not a good MET selection: %r"%MET
            metsstr = "MET_pt"+sysStr+">="+str(MET[0])
            prefix   = "met"+str(MET[0])
            if MET[1]>=0:
                metsstr+= "&&"+"MET_pt"+sysStr+"<"+str(MET[1])
                if MET[1]!=MET[0]: prefix+=str(MET[1])
            else:
                prefix+="p"
            res["cuts"].append(metsstr)
            res["prefixes"].append(prefix)


        #HT cut
        if HT and not (HT[0]==0 and HT[1]<0):
            assert HT[0]>=0 and (HT[1]>=HT[0] or HT[1]<0), "Not a good HT selection: %r"%HT
            metsstr = "HT>="+str(HT[0])
            prefix   = "ht"+str(HT[0])
            if HT[1]>=0:
                metsstr+= "&&"+"HT<"+str(HT[1])
                if HT[1]!=HT[0]: prefix+=str(HT[1])
            else:
                prefix+="p"
            res["cuts"].append(metsstr)
            res["prefixes"].append(prefix)



        if   channel=="e"  :  chStr = "abs(l1_pdgId)==11"
        elif channel=="mu" :  chStr = "abs(l1_pdgId)==13"
        elif channel=="all":  chStr = "(abs(l1_pdgId)==11||abs(l1_pdgId)==13)"
        res["cuts"].append(chStr)

        #badEEVeto
#        if self.year == 2017 and photonSel:
#            res["prefixes"].append("BadEEJetVeto")
#            badEEStr = cutInterpreter.cutString( "BadEEJetVeto" )
#            res["cuts"].append( badEEStr )


#        if dataMC=="Data" and self.year == 2018:
#            res["cuts"].append("reweightHEM>0")

        if dataMC != "DataMC":
            res["cuts"].append( getFilterCut(isData=(dataMC=="Data"), year=self.year , skipVertexFilter = True) )
            res["cuts"].extend(self.externalCuts)

        return {'cut':"&&".join(res['cuts']), 'prefix':'-'.join(res['prefixes']), 'weightStr': self.weightString()}

if __name__ == "__main__":
    print "executing now for 2016 - if you want a different year, this needs to be implemented"
    setup = Setup( year=2016 )
#    for name, dict in allRegions.items():
#        if not "Iso" in name: continue
#        print
#        print name
#        print
#        for channel in dict["channels"]:
#            print
#            print channel
#            print
#            res = setup.selection("MC", channel=channel, **setup.defaultParameters( update={"MET":(0,30)} ))
#            print res["cut"]
#            print res["prefix"]
#            print res["weightStr"]
#
#            print
#            res = setup.selection("Data", channel=channel, **setup.defaultParameters( update=dict["parameters"] ))
#            print res["cut"]
#            print res["prefix"]
#            print res["weightStr"]
#
##
