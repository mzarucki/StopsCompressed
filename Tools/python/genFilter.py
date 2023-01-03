''' 
gen filter efficiecny for mStop and mNeu for soft single analysis.
'''
import pickle
import ROOT
from StopsCompressed.Tools.helpers import getObjFromFile
from Analysis.Tools.u_float import u_float
import os 
from math import sqrt

class genFilter:
    def __init__(self, year = "2016", signal = "T2tt"):
        #default assumptiond
        #self.mStopmax = 800
        #self.mNeumax = 800
        
        #if year ==2016:
        #	#keys_geneff = [("filterEffs_T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1.root", "c1")]
        #	#keys_geneff = [("filterEffs_T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1.root", "filterEffs_T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1")]
        #self.dataDir = "/users/priya.hussain/public/CMSSW_10_2_18/src/StopsCompressed/Tools/data/filterEffs"
        #self.genEff = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in keys_geneff]
        ##print self.genEff
        #for self.effMap in self.genEff: assert self.effMap
        
        self.year = year
        self.signal = signal
        
        if self.year in ["2016", "2018"]: # FIXME: using 2016 filter efficiencies for 2018
            if self.signal == "T2tt":
                pklFileName = "filterEffs_T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1"
            elif self.signal == "T2bW":
                pklFileName = "filterEffs_SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1"
            elif self.signal == "TChiWZ":
                pklFileName = "filterEffs_SMS_TChiWZ_genHT_160_genMET_80" # FIXME: need to re-compte for higher chargino masses
            elif self.signal == "MSSM_higgsino":
                pklFileName = "filterEffs_MSSM_higgsino_genHT_160_genMET_80"
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError

        self.name = pklFileName
        self.dataDir = os.path.expandvars("$CMSSW_BASE/src/StopsCompressed/Tools/data/filterEffs")
        pklFile = os.path.join(self.dataDir, self.name) + ".pkl"
        self.eff = pickle.load(file(pklFile))

    def getEffFromPkl(self, mass1, mass2):
        print "signal", self.signal
        print "mass1, mass2 ", mass1, mass2
        try:
            genEff = self.eff[mass1][mass2]
        except KeyError:
            genEff = 0 
        print "genEff ", genEff
        return genEff
 
    def getEff(self, mStop, mNeu): # FIXME: hard-coded for T2tt
        effFile = ROOT.TFile("{}/{}.root".format(self.dataDir,self.name))
        canvas = effFile.Get("c1")
        hist2D = canvas.GetPrimitive(self.name)
        shift_x = 0.#12.5
        shift_y = 0.#9.9603175/2.
        mStop = mStop - mStop%25
        mNeu = mNeu - mNeu%5
        bin_x, bin_y = hist2D.GetXaxis().FindBin(mStop-shift_x), hist2D.GetYaxis().FindBin(mNeu-shift_y)
        genEff = hist2D.GetBinContent(bin_x, bin_y)
        #print mStop, mNeu
        #print bin_x, bin_y
        
        #for ix in xrange(hist2D.GetNbinsX()) :
        #	print hist2D.GetXaxis().GetBinLowEdge(ix+1)
        
        #for iy in xrange(hist2D.GetNbinsY()) :
        #	print hist2D.GetYaxis().GetBinLowEdge(iy+1)
        
        #exit(0)
        
        #print hist2D.GetYaxis().GetBinLowEdge(1)
        #print hist2D.GetYaxis().GetBinLowEdge(2)
        #print hist2D.GetYaxis().GetBinLowEdge(3)
        #print hist2D.GetYaxis().GetBinLowEdge(4)
        #print hist2D.GetYaxis().GetBinLowEdge(5)
        #print hist2D.GetYaxis().GetBinLowEdge(6)
        #print hist2D.GetYaxis().GetBinLowEdge(7)
        #print hist2D.GetYaxis().GetBinLowEdge(8)
        #print hist2D.GetXaxis().GetBinLowEdge(14)
        #print genEff
        return genEff
    
    
#print "This is only for debug purposes" 
#g = genFilter("2016")
#for mstop,mn in [[526,505],[576,495],[576,566]] :
#	#print "using pickle file"
#	#g.getEff(mstop,mn)
#	print "using th2f eff map"
#	g.getEff(mstop,mn)
#	print "-"*90
