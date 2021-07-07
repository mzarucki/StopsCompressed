#include "TFile.h"
#include "TH2F.h"
#include "TTree.h"
#include "TMath.h"

double reweightLeptonSF_newUp(double pt, double eta, int pdg_id){ 
	double lepton_SF = 0.0;
	double lepton_SF_err = 0.0;
	double sf_muon_SF_IpIsoSpec_2D_merged = 0.0;
	double sf_err_muon_SF_IpIsoSpec_2D_merged = 0.0;
	double sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.0;
	double sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.0;
	double sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0;
	double sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0;
	double sf_ele_SF_IpIso_2D_merged = 0.0;
	double sf_err_ele_SF_IpIso_2D_merged = 0.0;
	if (abs(pdg_id) == 13 ) {
	if (pt >= 3.5 && pt < 5.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00454390049; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00491818491949; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00454390049; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00491818491949; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.991229772568; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00197017116346; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.991229772568; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00197017116346; 
 }
	 	 }
	else if (pt >= 5.0 && pt < 10.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00454390049; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00491818491949; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00454390049; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00491818491949; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.991229772568; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00197017116346; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.991229772568; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00197017116346; 
 }
	 	 }
	else if (pt >= 10.0 && pt < 20.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998832821846; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00142301818472; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.997996270657; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00169266866368; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.99559867382; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000684631505312; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00175392628; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00179728072722; 
 }
	 	 }
	else if (pt >= 20.0 && pt < 25.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999935090542; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00109086105983; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.996872901917; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00140632715617; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998551189899; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000706909668533; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.991229534149; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00196038377286; 
 }
	 	 }
	else if (pt >= 25.0 && pt < 30.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.981860041618; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000827207710715; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998833239079; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00103489347863; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999271869659; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000497017741208; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999069929123; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00151454622759; 
 }
	 	 }
	else if (pt >= 30.0 && pt < 40.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998699009418; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000201184988455; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00022912025; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000416459837359; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999308645725; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000235129816636; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999312877655; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.0007278835845; 
 }
	 	 }
	else if (pt >= 40.0 && pt < 50.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998964250088; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000122658336755; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999258100986; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000211548690078; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999219238758; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000144333902188; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998639941216; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000578794188595; 
 }
	 	 }
	else if (pt >= 50.0 && pt < 60.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998904883862; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000211198934984; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999163746834; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000385105263538; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999070584774; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000222190135524; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999991476536; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.00112531763653; 
 }
	 	 }
	else if (pt >= 60.0 && pt < 120.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998910784721; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000314845760039; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.998245537281; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000551345198242; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 0.999231398106; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000353433884153; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_muon_SF_IpIsoSpec_2D_merged = 1.00293517113; 
 	 	 	 sf_err_muon_SF_IpIsoSpec_2D_merged = 0.000967884428676; 
 }
	 	 }
	if (pt >= 3.5 && pt < 5.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999999940395; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00163099405042; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999999940395; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00163099405042; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.998719036579; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000517455486232; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.998719036579; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000517455486232; 
 }
	 	 }
	else if (pt >= 5.0 && pt < 10.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999999940395; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00163099405042; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999999940395; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00163099405042; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.998719036579; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000517455486232; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.998719036579; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000517455486232; 
 }
	 	 }
	else if (pt >= 10.0 && pt < 20.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.979354560375; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00355051983324; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.979354560375; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00355051983324; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999999880791; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000112095893404; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999999344349; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00176419734078; 
 }
	 	 }
	else if (pt >= 20.0 && pt < 25.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.979468882084; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00143938258468; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.991578042507; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00190239212592; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.995900332928; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000989396078193; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.996329128742; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00155691687021; 
 }
	 	 }
	else if (pt >= 25.0 && pt < 30.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.99260610342; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000627252093038; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.992465019226; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000939843552065; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.998243629932; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000518675389953; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.995540142059; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00085690915805; 
 }
	 	 }
	else if (pt >= 30.0 && pt < 40.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.998069405556; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000175014339306; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.996697902679; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000290524386028; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.999733150005; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000193726904473; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.9941650033; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000366124086273; 
 }
	 	 }
	else if (pt >= 40.0 && pt < 50.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.996044635773; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000104011016889; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.995965898037; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00509281713293; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.9986551404; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 2.2903820837e-05; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.993408203125; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 9.41319598012e-05; 
 }
	 	 }
	else if (pt >= 50.0 && pt < 60.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.97753739357; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000425242882384; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.989255785942; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000621977983309; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.992526531219; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.000470275774538; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.984524071217; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00109338330811; 
 }
	 	 }
	else if (pt >= 60.0 && pt < 120.0) {
		 if (abs(eta) >= 0.0 && abs(eta) < 0.9) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.990822255611; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.0013015977162; 
 }
		 else if (abs(eta) >= 0.9 && abs(eta) < 1.2) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.993523716927; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.0018909148208; 
 }
		 else if (abs(eta) >= 1.2 && abs(eta) < 2.1) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 1.00050103664; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00153116338194; 
 }
		 else if (abs(eta) >= 2.1 && abs(eta) < 2.4) {
	 	 	 sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.989527225494; 
 	 	 	 sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged = 0.00375064979041; 
 }
	 	 }
		lepton_SF = sf_muon_SF_IpIsoSpec_2D_merged * sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged;
		lepton_SF_err = lepton_SF * sqrt(pow(sf_err_muon_SF_IpIsoSpec_2D_merged/sf_muon_SF_IpIsoSpec_2D_merged,2) + pow(sf_err_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged/sf_mu_SF_2D_LooseWP_cent_LooseWP_priv_3p5_10_merged,2) );
lepton_SF += lepton_SF_err;
	 }
	if (abs(pdg_id) == 11 ) {
	if (eta >= -2.5 && eta < -2.0) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.994965136051; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0216780591024; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.987610757351; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00600030059169; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.979021966457; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0026267991502; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.972899138927; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00192114108582; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.975114107132; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00247275605798; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.997439265251; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0108341986324; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.912264227867; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0328019047416; 
 }
	 	 }
	else if (eta >= -2.0 && eta < -1.566) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.0375970602; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0275712262274; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.962827146053; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00417335962092; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.98595815897; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00271600133247; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.983787953854; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00161314623513; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.986295819283; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00137168939133; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.994209647179; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00597641058999; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.980926632881; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0141334440044; 
 }
	 	 }
	else if (eta >= -1.566 && eta < -1.422) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.778478443623; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0509474583466; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.02074933052; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0118099745457; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.993650257587; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00509651811837; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.991882264614; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00385835795643; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.996668219566; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00294374441847; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.00186300278; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0134260858295; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.02120316029; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0396001174001; 
 }
	 	 }
	else if (eta >= -1.422 && eta < -0.8) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.855965912342; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0167067054486; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.00988769531; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00342544133; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.992226362228; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00102118410503; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.99299377203; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000504353357813; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.991534888744; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000614787534661; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.994534492493; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00268730542608; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.00039422512; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00637485424573; 
 }
	 	 }
	else if (eta >= -0.8 && eta < 0.0) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.992478311062; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0181905335735; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.952900230885; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00251058172655; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.993426680565; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000530902230561; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.993857383728; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000245677015475; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.99458026886; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000467456927094; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.995035648346; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00182930829417; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.992980599403; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00377239488943; 
 }
	 	 }
	else if (eta >= 0.0 && eta < 0.8) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.01301312447; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0149256879936; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.986421525478; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00263958668711; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.995164036751; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000527968465337; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.993827044964; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00017999807089; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.995045959949; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000532541586654; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.00026011467; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00171178296209; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.996601343155; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00413058735743; 
 }
	 	 }
	else if (eta >= 0.8 && eta < 1.442) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.899427890778; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0178923802655; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.00702726841; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00313687891844; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.990826785564; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0010051749247; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.992357194424; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000597606781984; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.990714013577; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.000667796084554; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.996568381786; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00337038251552; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.996551334858; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.005488182903; 
 }
	 	 }
	else if (eta >= 1.442 && eta < 1.566) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.919921696186; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0692048191724; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.01137971878; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0130285093475; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.98977792263; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00492751238926; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.982821404934; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00582264510129; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.986295938492; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0030786412815; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.98513430357; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00955752310383; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.973784983158; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0265120775924; 
 }
	 	 }
	else if (eta >= 1.566 && eta < 2.0) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.986982345581; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0241912368555; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.04099988937; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00557794582336; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.980384707451; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0022533926092; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.982511520386; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00152416334556; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.985827922821; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00138114919811; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.984084844589; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00652808322926; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.982212841511; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0165603218244; 
 }
	 	 }
	else if (eta >= 2.0 && eta < 2.5) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 1.05226290226; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0247487601909; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.976322412491; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00496452629997; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.968324482441; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0026606830489; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.972045481205; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00199092082643; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.975446224213; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.00235389363779; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.994779646397; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0100221767923; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_ele_SF_IpIso_2D_merged = 0.972499370575; 
 	 	 	 sf_err_ele_SF_IpIso_2D_merged = 0.0308468799869; 
 }
	 	 }
	if (eta >= -2.5 && eta < -2.0) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.3669346571; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0539682329665; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.04924237728; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00874023294899; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.0217654705; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00781982546847; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.01756441593; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00523432666944; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.0183275938; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00304935719543; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.02485871315; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0141918691021; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.02616608143; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0440366665577; 
 }
	 	 }
	else if (eta >= -2.0 && eta < -1.566) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.864393949509; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0280364815721; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.0; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0147567863866; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.986769556999; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00970645821714; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.995623648167; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00336669251937; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.998920083046; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00280418371436; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.0; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00775479251824; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.03243243694; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0268350778448; 
 }
	 	 }
	else if (eta >= -1.566 && eta < -1.444) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.06365156174; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.173558771578; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.992967665195; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.033316708689; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.991586565971; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00355533640811; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.00118911266; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00770133968017; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.01384079456; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0226639580333; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.02061855793; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0511940654889; 
 }
	 	 }
	else if (eta >= -1.444 && eta < -0.8) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.77884376049; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.021978627876; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.00346422195; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00945315243046; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.971459925175; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0149522909166; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.981895625591; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00212765957447; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.983210921288; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00599870185653; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.992715895176; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00448271248934; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.997933864594; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0126839510354; 
 }
	 	 }
	else if (eta >= -0.8 && eta < 0.0) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.11545777321; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0268782566184; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.99104142189; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0198619619667; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.972043037415; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0113419506348; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.976963341236; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00165477637895; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.979231595993; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00418383899756; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.988636374474; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00346856459798; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.991718411446; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0204820179916; 
 }
	 	 }
	else if (eta >= 0.0 && eta < 0.8) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.13478708267; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0222705976017; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.998888909817; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0198364966467; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.981759667397; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0113419506348; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.982217550278; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00165477637895; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.982365131378; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00418383899756; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.995859205723; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00346856459798; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.985581874847; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0204820179916; 
 }
	 	 }
	else if (eta >= 0.8 && eta < 1.444) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.804939687252; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0234345842719; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.01035678387; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00922190201729; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.97807019949; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0149522909166; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.981934130192; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00212765957447; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.983246088028; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00599870185653; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.994780778885; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00448271248934; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.989690721035; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0128170715669; 
 }
	 	 }
	else if (eta >= 1.444 && eta < 1.566) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.09000003338; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.17350045311; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.98179268837; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.033316708689; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.984375; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00355533640811; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.991636812687; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00770133968017; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.00575375557; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0226639580333; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.00114679337; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0526597364248; 
 }
	 	 }
	else if (eta >= 1.566 && eta < 2.0) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.787813901901; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0248119265415; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.01936221123; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0147567863866; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.981194674969; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00970645821714; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.99345690012; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00336669251937; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.997842490673; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00280418371436; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.997879087925; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00775479251824; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.996822059155; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0268110643475; 
 }
	 	 }
	else if (eta >= 2.0 && eta < 2.5) {
		 if (pt >= 5.0 && pt < 10.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.24063205719; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0565241229552; 
 }
		 else if (pt >= 10.0 && pt < 20.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.991484165192; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00874023294899; 
 }
		 else if (pt >= 20.0 && pt < 35.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.975438594818; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00781982546847; 
 }
		 else if (pt >= 35.0 && pt < 50.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.984018266201; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00523432666944; 
 }
		 else if (pt >= 50.0 && pt < 100.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.987681984901; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.00304935719543; 
 }
		 else if (pt >= 100.0 && pt < 200.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.01541852951; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0138984225258; 
 }
		 else if (pt >= 200.0 && pt < 500.0) {
	 	 	 sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 1.02108764648; 
 	 	 	 sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged = 0.0427852421678; 
 }
	 	 }
		lepton_SF = sf_ele_SF_IpIso_2D_merged*sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged;
		lepton_SF_err = lepton_SF * sqrt(pow(sf_err_ele_SF_IpIso_2D_merged/sf_ele_SF_IpIso_2D_merged,2) + pow(sf_err_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged/sf_el_SF_2D_VetoWP_cent_VetoWP_priv_5_10_2016_merged,2) );
		lepton_SF += lepton_SF_err;
	 }
	return lepton_SF;
}