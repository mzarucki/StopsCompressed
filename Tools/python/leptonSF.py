'''
Evaluate lepton SF specific to the soft single lepton analysis.
'''

import ROOT
from StopsCompressed.Tools.helpers import getObjFromFile
from Analysis.Tools.u_float import u_float
import os
from math import sqrt

class leptonSF:
    def __init__(self, year):

        # default assumptions
        self.mu_x_is_pt  = True
        self.mu_abs_eta  = True
        self.mu_max_pt   = 120
        self.ele_x_is_pt = True
        self.ele_abs_eta = True
        self.ele_max_pt  = 200

        if   '2016' in year :
            keys_mu  = [ ("mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-10.root",  "mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-10_merged"),
                         ("2016_mu_sf.root",   "muon_SF_IpIsoSpec_2D_merged")
			 ]
            self.ele_x_is_pt = False 
            self.ele_abs_eta = False 
            self.ele_max_pt  = 500
            keys_ele = [ ("el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2016.root",       "el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2016"),
                         ("2016_el_sf.root",       "ele_SF_IpIso_2D") 
			 ]
        elif '2017' in year:
            keys_mu  = [("mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-20.root",         "mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-20"),
                        ("2017_mu_sf.root",  "muon_SF_IpIsoSpec_2D")]
            self.ele_x_is_pt = False 
            self.ele_abs_eta = False 
            self.ele_max_pt  = 500
            keys_ele = [("el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2017.root", "el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2017"),
                        ("2017_el_sf.root", "ele_SF_IpIso_2D")]
        elif '2018' in year:
            keys_mu  = [("mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-20_2018.root",           "mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-20_2018"),
                        ("2018_mu_sf.root",  "muon_SF_IpIsoSpec_2D")] # 2017 Iso SF are recommended
            self.ele_x_is_pt = False 
            self.ele_abs_eta = False 
            self.ele_max_pt  = 500
            keys_ele = [("el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2018.root", "el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2018"),
                        ("2018_el_sf.root", "ele_SF_IpIso_2D")]
        
        self.dataDir = "$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/"

        self.mu  = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in keys_mu]
        self.ele = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in keys_ele]
        for effMap in self.mu + self.ele: assert effMap

    def getPartialSF(self, effMap, pt, eta):

        bin_x, bin_y = effMap.GetXaxis().FindBin(pt), effMap.GetYaxis().FindBin(eta)
        sf  = effMap.GetBinContent(bin_x, bin_y)
        err = effMap.GetBinError  (bin_x, bin_y)
        return u_float(sf, err)

    def mult(self, list):
        res = list[0]
        for i in list[1:]: res = res*i
        return res

    def getSF(self, pdgId, pt, eta):
        # protection for the abs(eta)=2.4 case
        if eta >= 2.4:  eta = 2.39
        if eta <= -2.4: eta = -2.39

        if abs(pdgId)==13:   
          if pt >= self.mu_max_pt: pt = self.mu_max_pt-1 # last bin is valid to infinity
          eta_ = abs(eta) if self.mu_abs_eta else eta
          sf   = self.mult([ self.getPartialSF(effMap, pt, eta_) if self.mu_x_is_pt else self.getPartialSF(effMap, eta_, pt) for effMap in self.mu])
          #sf.sigma = 0.03 # Recommendation for Moriond17
        elif abs(pdgId)==11:
          if pt >= self.ele_max_pt: pt = self.ele_max_pt-1 # last bin is valid to infinity
          eta_ = abs(eta) if self.ele_abs_eta else eta
          sf   = self.mult([self.getPartialSF(effMap, pt, eta_) if self.ele_x_is_pt else self.getPartialSF(effMap, eta_, pt) for effMap in self.ele])
        else: 
          raise Exception("Lepton SF for PdgId %i not known"%pdgId)

        return sf.val, (1-sf.sigma)*sf.val, (1+sf.sigma)*sf.val 

if __name__ == "__main__":
    sf_2016 = leptonSF( year = 'UL2016' )
    sf_2017 = leptonSF( year = 'UL2017' )
    sf_2018 = leptonSF( year = 'UL2018' )
