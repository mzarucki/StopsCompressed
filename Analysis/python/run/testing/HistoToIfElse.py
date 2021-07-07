import ROOT 



# path = "$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/2016_mu_sf_merged.root"
# name = "muon_SF_IpIsoSpec_2D_merged"

# path = "$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-10_merged.root"
# name = "mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-10_merged"

# path = "$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/2016_el_sf_merged.root"
# name = "ele_SF_IpIso_2D_merged"

# path = "$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2016_merged.root"
# name = "el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2016_merged"

for shift in ["", "Up", "Down"] :

    code =  "#include \"TFile.h\"\n"
    code += "#include \"TH2F.h\"\n"
    code += "#include \"TTree.h\"\n"
    code += "#include \"TMath.h\"\n\n"


    code += "double reweightLeptonSF_new{}(double pt, double eta, int pdg_id){{ \n".format(shift)
        
    code += "\tdouble lepton_SF = 0.0;\n"
    code += "\tdouble lepton_SF_err = 0.0;\n"
    code += "\tdouble sf_muon_SF_IpIsoSpec_2D_merged = 0.0;\n"
    code += "\tdouble sf_err_muon_SF_IpIsoSpec_2D_merged = 0.0;\n"
    code += "\tdouble sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.0;\n"
    code += "\tdouble sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.0;\n"
    code += "\tdouble sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0;\n"
    code += "\tdouble sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0;\n"
    code += "\tdouble sf_ele_SF_IpIso_2D_merged = 0.0;\n"
    code += "\tdouble sf_err_ele_SF_IpIso_2D_merged = 0.0;\n"



    for i, [path,name] in enumerate([
        ["$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/2016_mu_sf_merged.root", "muon_SF_IpIsoSpec_2D_merged"],
        ["$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-10_merged.root", "mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5-10_merged"],
        ["$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/2016_el_sf_merged.root", "ele_SF_IpIso_2D_merged"],
        ["$CMSSW_BASE/src/StopsCompressed/Tools/data/leptonSFData/el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2016_merged.root", "el_SF_2D_VetoWP_cent_VetoWP_priv_5-10_2016_merged"]
    ]) :

        _file = ROOT.TFile(path)
        histo = _file.Get(name)

        if (i == 0) : # adding muons
            code += "\tif (abs(pdg_id) == 13 ) {\n"  
        if (i==2) : #adding electrons
            # code += "\t}}\n" # don't forget to close muon bracket
            code += "\tif (abs(pdg_id) == 11 ) {\n" 
        
        for x in range(1,histo.GetNbinsX()+1) :
            low_x = histo.ProjectionX().GetBinLowEdge(x)
            high_x = histo.ProjectionX().GetBinLowEdge(x+1)
            if (x==1) :
                if "mu" in name :
                    code += "\tif (pt >= {low} && pt < {up}) {{\n".format(low=low_x,up=high_x)
                else :
                    code += "\tif (eta >= {low} && eta < {up}) {{\n".format(low=low_x,up=high_x)
            else :
                if "mu" in name :
                    code += "\telse if (pt >= {low} && pt < {up}) {{\n".format(low=low_x,up=high_x)
                else :
                    code += "\telse if (eta >= {low} && eta < {up}) {{\n".format(low=low_x,up=high_x)
            
            for y in range(1,histo.GetNbinsY()+1) :
                low_y  = histo.ProjectionY().GetBinLowEdge(y)
                high_y = histo.ProjectionY().GetBinLowEdge(y+1)

                if (y==1) :
                    if "mu" in name :
                        code += "\t\t if (abs(eta) >= {low} && abs(eta) < {up}) {{\n".format(low=low_y,up=high_y)
                    else :
                        code += "\t\t if (pt >= {low} && pt < {up}) {{\n".format(low=low_y,up=high_y)
                else :
                    if "mu" in name :
                        code += "\t\t else if (abs(eta) >= {low} && abs(eta) < {up}) {{\n".format(low=low_y,up=high_y)
                    else :
                        code += "\t\t else if (pt >= {low} && pt < {up}) {{\n".format(low=low_y,up=high_y)
            
                val = histo.GetBinContent(x,y)
                val_err = histo.GetBinError(x,y)
                code += "\t \t \t sf_{} = {}; \n ".format(name.replace("-","_"),val)
                code += "\t \t \t sf_err_{} = {}; \n }}\n".format(name.replace("-","_"),val_err)

            code += "\t \t }\n"

        if (i==1) : #end of muon case
            code += "\t\tlepton_SF = sf_muon_SF_IpIsoSpec_2D_merged * sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged;\n"
            code += "\t\tlepton_SF_err = lepton_SF * sqrt(pow(sf_err_muon_SF_IpIsoSpec_2D_merged/sf_muon_SF_IpIsoSpec_2D_merged,2) + pow(sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged/sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged,2) );\n"
            if shift :
                if (shift == "Up") :
                    code += "lepton_SF += lepton_SF_err;\n"
                elif (shift == "Down") :
                    code += "lepton_SF -= lepton_SF_err;\n"
            code += "\t }\n" 
        
        if (i==3) : #end of electron case
            code += "\t\tlepton_SF = sf_ele_SF_IpIso_2D_merged*sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged;\n"
            code += "\t\tlepton_SF_err = lepton_SF * sqrt(pow(sf_err_ele_SF_IpIso_2D_merged/sf_ele_SF_IpIso_2D_merged,2) + pow(sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged/sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged,2) );\n"
            if shift :
                if (shift == "Up") :
                    code += "\t\tlepton_SF += lepton_SF_err;\n"
                elif (shift == "Down") :
                    code += "\t\tlepton_SF -= lepton_SF_err;\n"
            code += "\t }\n" 
        

        _file.Close()
        
    code += "\treturn lepton_SF;\n"
    code+= "}"

    text_file = open("reweightLeptonSF_new{}.C".format(shift), "w")

    text_file.write(code)

    text_file.close()