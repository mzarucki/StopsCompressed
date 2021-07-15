import ROOT
import pickle
from StopsCompressed.Tools.niceColorPalette       import niceColorPalette
import numpy as np

val = pickle.load(file("/scratch/priya.hussain/StopsCompressed/results/2016/fitAllregion_CT_splitCR_140fb/limits/T2tt/T2tt/limitResults.pkl"))
stop = val['stop']
stop = np.arange(250,801,25)
print stop
#dm = val['dm']
#print dm
#print val['0.500']
dm = [10,20,30,40,50,60,70,80]
#denom = 'fitAllregion_CT_splitCR_140fb'
denom = 'tmp_nbins88'
num = 'fitAllregion_mt100_splitCR_140fb'
prefix = 'mt100tomtadd'
plots={
		"NUM": "/scratch/janik.andrejkovic/forPriya/tmp_fitAllregion_mt100_splitCR_140fb.root".format(num) ,
		"DEN": "/scratch/janik.andrejkovic/forPriya/tmp_nbins88.root".format(denom) 
		}

nanoval = []
navidval= []
stop2 = []
nstop=[]
dm2=[]
for p in plots:
	print plots[p]
	print "#"*15
	if "NUM" in p:
		
		rootFile = ROOT.TFile("{}".format(plots[p]))
		temp = rootFile.Get("temperature")
		#print "no of bins x axis {}".format(temp.GetNbinsX())
		#print "no of bins y axis {}".format(temp.GetNbinsY())
		#print "value for stop500,dm10 {}".format(temp.GetBinContent(temp.GetXaxis().FindBin(500),temp.GetYaxis().FindBin(10)))
		#print "value{} for stop{},dm{}".format(temp.GetBinContent(temp.GetXaxis().FindBin(576),temp.GetYaxis().FindBin(10)),'576','10')
		for s in stop:
			for d in dm:
				val=temp.GetBinContent(temp.GetXaxis().FindBin(s),temp.GetYaxis().FindBin(d))
				if (val == 0) :
					val=temp.GetBinContent(temp.GetXaxis().FindBin(s),temp.GetYaxis().FindBin(d-1))
					print "stop: {}".format(s)
					print "dm: {}".format(d)
					print temp.GetXaxis().FindBin(s), temp.GetYaxis().FindBin(d)
					print val
					print "*"*90


				nanoval.append(val)
				stop2.append(s)
				dm2.append(d)
		rootFile.Close()
	elif "sens":
#		print plots[p]
		rootFile = ROOT.TFile("{}".format(plots[p]))
		temp = rootFile.Get("temperature")
		#print "no of bins x axis {}".format(temp.GetNbinsX())
		#print "no of bins y axis {}".format(temp.GetNbinsY())
		##print "value for stop500,dm10 {}".format(temp.GetBinContent(temp.GetXaxis().FindBin(500),temp.GetYaxis().FindBin(10)))
		#print "value{} for stop{},dm{}".format(temp.GetBinContent(temp.GetXaxis().FindBin(576),temp.GetYaxis().FindBin(10)),'576','10')
		print "here for sensitivity study"
		for s in stop:
			for d in dm:
				#print "value{} for stop{},dm{}".format(temp.GetBinContent(temp.GetXaxis().FindBin(s),temp.GetYaxis().FindBin(d)),s,d)
				val=temp.GetBinContent(temp.GetXaxis().FindBin(s),temp.GetYaxis().FindBin(d))
				navidval.append(val)
				nstop.append(s)
		rootFile.Close()
	else:
#		print plots[p]
		rootFile = ROOT.TFile("{}".format(plots[p]))
		temp = rootFile.Get("xsecUL_Exp")
		print "hopefully not here"
		#print "no of bins x axis {}".format(temp.GetNbinsX())
		#print "no of bins y axis {}".format(temp.GetNbinsY())
		##print "value for stop500,dm10 {}".format(temp.GetBinContent(temp.GetXaxis().FindBin(500),temp.GetYaxis().FindBin(10)))
		#print "value{} for stop{},dm{}".format(temp.GetBinContent(temp.GetXaxis().FindBin(576),temp.GetYaxis().FindBin(10)),'576','10')
		for s in stop:
			for d in dm:
				#print "value{} for stop{},dm{}".format(temp.GetBinContent(temp.GetXaxis().FindBin(s),temp.GetYaxis().FindBin(d)),s,d)
				val=temp.GetBinContent(temp.GetXaxis().FindBin(s),temp.GetYaxis().FindBin(d))
				navidval.append(val)
				nstop.append(s)
		rootFile.Close()



#print stop
#print nstop
#print nanoval
#print navidval
#print len(stop)
#print len(nstop)
#print len(nanoval)
#print len(navidval)
hist =ROOT.TH2F("ratio: mt100/mtAddBin","ratio: mt100/mtAddBin",55,250,800,17,5,90)
for i in range(len(stop2)):
	#print stop2[i]
	#print nstop[i]
	#print dm2[i]
	#print nanoval[i]
	#print navidval[i]
	if stop2[i]>=250 and stop2[i]<=800:
		s=stop2[i]
		d=dm2[i]
		r = nanoval[i]/navidval[i]
		#print "ratio: {}".format(r)
		if r < 0.5 :
			print r
		hist.SetBinContent(hist.GetXaxis().FindBin(s),hist.GetYaxis().FindBin(d),r)
		if navidval[i]>0:
			r = nanoval[i]/navidval[i]
			#hist.SetBinContent(hist.GetXaxis().FindBin(s),hist.GetYaxis().FindBin(d),r)
		elif r <= 0:
			print "#"*20
			print r,"num:", nanoval[i], "denom", navidval[i]
			print "#"*20
#		#	hist.SetBinContent(hist.GetXaxis().FindBin(s),hist.GetYaxis().FindBin(d),r)
	


c1 = ROOT.TCanvas()
niceColorPalette(255)
#hist.GetZaxis().SetRangeUser(0.0001, 2)
hist.GetZaxis().SetRangeUser(0.5, 1.5)
#hist.GetZaxis().SetRangeUser(0.7, 1.3)
hist.SetStats(0)
hist.Draw('COLZ')
#c1.SetLogz()
#c1.SetLogy()
c1.Print('/mnt/hephy/cms/priya.hussain/www/StopsCompressed/sensitivityStudies/{}.png'.format(prefix))
#c1.Print('/mnt/hephy/cms/priya.hussain/www/StopsCompressed/sensitivityStudies/finerZ/{}.png'.format(prefix))
temp = ROOT.TFile("tmp_{}.root".format(prefix),"recreate")
hist.Write()
temp.Close()

