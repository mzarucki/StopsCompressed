import ROOT
import math
processes = [ 'signal', 'Top', 'ZInv', 'WJets', 'Others', 'QCD']
cuts = ["dphijets", "dphimetjets"]
dphijets_file 	= ROOT.TFile("/groups/hephy/cms/priya.hussain/www/StopsCompressed/fit/2016preVFP/dPhiJets/nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/T2tt_500_470/controlRegions.root")
dphimetjets_file = ROOT.TFile("/groups/hephy/cms/priya.hussain/www/StopsCompressed/fit/2016preVFP/dPhiMetJets/nbins88_mt95_extramTTrue_CT400_R1onlyFalse_R2onlyFalse/T2tt_500_470/controlRegions.root")

dphijets_canvas      = dphijets_file.Get("220fd275_d84a_44c3_9734_f725f6930c81")
dphijets_sig_hist    = (dphijets_canvas.FindObject("220fd275_d84a_44c3_9734_f725f6930c81_1")).GetPrimitive("signal")
dphimetjets_canvas   = dphimetjets_file.Get("8afede2b_404c_4452_9f84_477ad0c6f6dc")
dphimetjets_sig_hist = (dphimetjets_canvas.FindObject("8afede2b_404c_4452_9f84_477ad0c6f6dc_1")).GetPrimitive("signal")
canvas={"dphijets": dphijets_canvas, "dphimetjets": dphimetjets_canvas }
sig_hist={"dphijets": dphijets_sig_hist, "dphimetjets": dphimetjets_sig_hist}
#print "sig hist bins: ", sig_hist.GetNbinsX()
hsb 	= {}
hsb_sig = {}
for cut in cuts:
	print "for which antiQCD cut: ", cut
	bkg_hist = []
	for process in processes[1:]:
		if "met" in cut:
			print "here for dphimetjets: ", cut
			bkg_hist.append((dphimetjets_canvas.FindObject("8afede2b_404c_4452_9f84_477ad0c6f6dc_1")).GetPrimitive(process))
			sig_hist = dphimetjets_sig_hist
		else:
			print "here for dphijets: ", cut
			bkg_hist.append((dphijets_canvas.FindObject("220fd275_d84a_44c3_9734_f725f6930c81_1")).GetPrimitive(process))
			sig_hist = dphijets_sig_hist
	htot = bkg_hist[0].Clone("TotalBkg")
	for h in bkg_hist[1:]:
		htot.Add(h)
	del bkg_hist
	for b in range(htot.GetNbinsX()):
		print "total bkg bin content before sqrt", htot.GetBinContent(b+1)
		#print "signal bin content before sqrt", sig_hist.GetBinContent(b+1)
		htot.SetBinContent(b+1, math.sqrt(htot.GetBinContent(b+1)))


	hsb[cut] = sig_hist.Clone("sOB")
	hsb[cut].Divide(htot)
ROOT.gStyle.SetErrorX(0)
ROOT.gStyle.SetOptStat(0)
c = ROOT.TCanvas('c', '', 1400, 1000)
#c = ROOT.TCanvas()
leg1 = ROOT.TLegend(0.7, 0.8, 0.9, 0.9)
for i, cut in enumerate(hsb):
	leg1.AddEntry(hsb[cut], cut ,"l")
	hsb[cut].SetLineColor(i+1)
	hsb[cut].SetLineWidth(2)
	if i==0:
		hsb[cut].SetTitle("T2tt_500_470")
		hsb[cut].GetYaxis().SetTitle('#frac{S}{sqrtB}')
		#hsb[cut].GetYaxis().SetTitleSize(0.035)
		#hsb[cut].GetYaxis().SetTitleOffset(1.2)
		#hsb[cut].GetYaxis().SetLabelSize(0.03)
		hsb[cut].GetYaxis().SetRangeUser(0,1.5)
		hsb[cut].Draw('hist')
	else:
		hsb[cut].Draw('histsame')
leg1.Draw('same')

c.Update()
c.SaveAs("SOB_T2tt_500_470.png")
hsb.clear()


#zinv = (canvas.FindObject("d0bedf4a_1926_4b37_9aae_9f793556c09e_1")).GetPrimitive("ZInv")
#values      = [(zinv.GetBinContent(_bin+1)) for _bin in range(zinv.GetNbinsX())]
#print "zinv bins: ", zinv.GetNbinsX(), "   no of values: ", len(values)
#print "values of zinv hist: ", values

