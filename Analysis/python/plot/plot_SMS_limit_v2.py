'''
Create 2D limit plots.

No smoothing for T2bW for now.
T8bbllnunu need some manual cleaning

'''

#!/usr/bin/env python
import ROOT
import sys, ctypes, os, array
from StopsCompressed.Tools.helpers                import getObjFromFile
from StopsCompressed.Tools.interpolate            import interpolate, rebin
from StopsCompressed.Tools.niceColorPalette       import niceColorPalette
from StopsCompressed.Tools.user                   import plot_directory, analysis_results
from StopsCompressed.Analysis.plot.limitHelpers   import getContours, cleanContour, getPoints, extendContour, getProjection

#ROOT.gROOT.SetBatch(True)

from optparse import OptionParser
parser = OptionParser()
#parser.add_option("--file",             dest="filename",    default=None,   type="string", action="store",  help="Which file?")
parser.add_option("--sensitivityStudyName", default = "baseline",  type=str,    action="store",      help="Name of sensitivity study")
parser.add_option("--signal",           action='store',     default='T2tt',  choices=["T2tt","TTbarDM","T8bbllnunu_XCha0p5_XSlep0p05", "T8bbllnunu_XCha0p5_XSlep0p5", "T8bbllnunu_XCha0p5_XSlep0p95", "T2bt","T2bW", "T8bbllnunu_XCha0p5_XSlep0p09", "ttHinv", "TChiWZ"], help="which signal?")
parser.add_option("--year",             dest="year",   type="int",    default=2018, action="store",  help="Which year?")
parser.add_option("--version",          dest="version",  default='v9',  action="store",  help="Which version?")
parser.add_option("--subDir",           dest="subDir",  default='unblindV1',  action="store",  help="Give some extra name")
parser.add_option("--smoothAlgo",       dest="smoothAlgo",  default='k5a', choices=["k5a", "k3a", "k5b"],  action="store",  help="Which smoothing algo?")
parser.add_option("--iterations",       dest="iterations", type="int",  default=1,  action="store",  help="How many smoothing iterations?")
parser.add_option("--combined",         action="store_true",  help="Combine the years?")
parser.add_option("--expected",         action="store_true",  help="Use expected instead of observed limit for 2D hist?")
parser.add_option("--unblind",          action="store_true",  help="Use real data?")
parser.add_option("--smooth",           action="store_true",  help="Use real data?")
parser.add_option("--dmPlot",           action="store_true",  help="Use real data?")
(options, args) = parser.parse_args()

def toGraph2D(name,title,length,x,y,z):
    result = ROOT.TGraph2D(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i,x[i],y[i],z[i])
    h = result.GetHistogram()
    h.SetMinimum(min(z))
    h.SetMaximum(max(z))
    c = ROOT.TCanvas()
    result.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result

def toGraph(name,title,length,x,y):
    result = ROOT.TGraph(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i,x[i],y[i])
    c = ROOT.TCanvas()
    result.Draw()
    del c
    return result

scale = 1.0 # 4.3 # 0.6 

suffix = "mu" #"comb" # "mu" "e"

if scale != 1.0:
    suffix += "_scaled%s"%str(scale).replace(".","p")

dmplot = options.dmPlot
yearString = str(options.year) if not options.combined else 'comb'
signalString = options.signal

#analysis_results = '/scratch/janik.andrejkovic/StopsCompressed/results/2016/fitAllregion_nbins88_mt95_extramTTrue_CT400_isLNotTFalse/limits/T2tt/T2tt/'

if options.sensitivityStudyName in ["baseline", "baseline_redSys"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins56_mt95_extramTFalse_CT400_isPromptFalse_lowMETregionFalse"
elif options.sensitivityStudyName in ["baselinePlusLowMET", "baselinePlusLowMET_redSys", "baselinePlusLowMET2_redSys", "baselinePlusLowMET3_redSys"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins80_mt95_3mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_4mTregions", "baselinePlusLowMET3_redSys_4mTregions_splitCTZ"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins104_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_4mTregions_splitCTZ_lowHTbin"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins136_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_low5mTregions"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins132_mt95_low5mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_high5mTregions"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins128_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_5mTregions_splitCTZ_lowHTbin"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins168_mt95_5mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_6mTregions"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins156_mt95_6mTregions_CT400_isPromptFalse_lowMETregionTrue"
elif options.sensitivityStudyName in ["baselinePlusLowMET3_redSys_6mTregions_splitCTZ_lowHTbin"]:
    fullSensitivityStudyName = options.sensitivityStudyName + "_nbins204_mt95_6mTregions_CT400_isPromptFalse_lowMETregionTrue"
else:
    raise NotImplementedError

analysis_results = '/eos/user/m/mzarucki/StopsCompressed/sensitivity/2018/fitAll_{sensitivityStudyName}_{suffix}_v1/limits/{signal}/{signal}/'.format(sensitivityStudyName = options.sensitivityStudyName, signal = signalString, suffix = suffix)

#if lowMETregion:
#    analysis_results = '/eos/user/m/mzarucki/StopsCompressed/sensitivity/2018/fitAll_baselinePlusLowMET2_redSys_{suffix}_v1/limits/{signal}/{signal}/'.format(signal = signalString, suffix = suffix)
#    sensitivityStudyName = "baselinePlusLowMET2_nbins80_mt95_extramTFalse_CT400_isPromptFalse_lowMETregionTrue"
#else:
#    analysis_results = '/eos/user/m/mzarucki/StopsCompressed/sensitivity/2018/fitAll_baseline_redSys_{suffix}_v1/limits/{signal}/{signal}/'.format(signal = signalString, suffix = suffix)
#    sensitivityStudyName = "baseline_nbins56_mt95_extramTFalse_CT400_isPromptFalse_lowMETregionFalse"

defFile =  os.path.join(analysis_results,"limitResults.root")

#plotDir = os.path.join(plot_directory,'limits', signalString, options.version, yearString, options.subDir)
#sppit CR
plotDir = os.path.join(plot_directory,'limits', yearString, signalString, fullSensitivityStudyName, 'FR_limitAll_%s_%s'%(yearString, suffix))
#plotDir = os.path.join(plot_directory,'limits',signalString,yearString,'fitAllregion_nbins88_mt95_extramTTrue_CT400_isLNotTFalse','FR_limitAll_'+yearString)

#AN based binning
#plotDir = os.path.join(plot_directory,'AN_sv2','FR_limitAll_2016')

if options.smooth:
    plotDir += "_smooth_it%s_%s"%(options.iterations, options.smoothAlgo)
if options.expected:
    plotDir += '_expected'

import RootTools.plot.helpers as plot_helpers
plot_helpers.copyIndexPHP( plotDir )

if not os.path.exists(plotDir):
    os.makedirs(plotDir)

graphs  = {}
hists   = {}

if options.signal in ['T2tt', 'T2bW']: # NOTE: number of points between T2tt and T2bW is the same
    nbinsx = (800-250)/25 * 2
    nbinsy = (110-10)/10 * 5 
    #nbins = 105 # bin size 10 GeV
    #nbins = 55 # bin size 10 GeV for dm plots
    #nbinsx = 55
    #nbinsy = 55
elif options.signal == 'TChiWZ':
    nbinsx = (500-100)/25 * 2
    nbinsy = (70-0)/10 * 5 
    #nbinsx = 50
    #nbinsy = 35
elif options.signal.startswith('T8'):
    nbins = 64 # bin size 25 GeV
#if options.signal == 'T2bW':
#    nbins = 1300/25 * 2 
    

import pickle
import pandas as pd
import numpy as np
results = pickle.load(file(defFile.replace('root','pkl'), 'r'))

results_df = pd.DataFrame(results)

#if options.signal == 'T2tt':
#    limit_top = float(results_df[results_df['stop']==175][results_df['lsp']==0]['-1.000'])

# filter out the failed fits
results_df = results_df[results_df['-1.000']<4*results_df['0.840']]

if options.signal == 'T2bW':
    # be a bit tighter here
    results_df = results_df[results_df['-1.000']<2.5*results_df['0.840']]
    #results_df = results_df.drop(index=331)
    #results_df = results_df.drop(index=319) #319, 334
    #results_df = results_df.drop(index=335) #this is another fluctuation point


#results_df = results_df[(results_df['stop']-results_df['lsp'])>174]

## filter out the additional points
#results_df = results_df[results_df['stop']%5==0][results_df['lsp']%5==0]
#if options.signal == 'T2tt':
#    results_df = results_df.drop(index=439)
#    results_df = results_df[results_df['stop']%5==0]


if options.signal == 'T8bbllnunu_XCha0p5_XSlep0p5':
    pass
    #results_df = results_df.drop(index=439)
    #results_df = results_df[(results_df['stop']%25==0)]
    #results_df = results_df[(results_df['lsp']%25==0)]

#print "lenghth:", len(results_df['stop'].tolist())
#print "x: ", results_df['stop'].tolist()
#print "y: ", results_df['dm'].tolist()
#print "z: ", results_df['0.500'].tolist()
#exp_graph       = toGraph2D('exp',      'exp',      len(results_df['stop'].tolist()),results_df['stop'].tolist(),results_df['lsp'].tolist(),results_df['0.500'].tolist())
exp_dm_graph       = toGraph2D('exp_dm',      'exp_dm',      len(results_df['stop'].tolist()),results_df['stop'].tolist(),results_df['dm'].tolist(),results_df['0.500'].tolist())
exp_dm_up_graph    = toGraph2D('exp_dm_up',   'exp_dm_up',   len(results_df['stop'].tolist()),results_df['stop'].tolist(),results_df['dm'].tolist(),results_df['0.840'].tolist())
exp_dm_down_graph  = toGraph2D('exp_dm_down', 'exp_dm_down', len(results_df['stop'].tolist()),results_df['stop'].tolist(),results_df['dm'].tolist(),results_df['0.160'].tolist())
obs_dm_graph       = toGraph2D('obs_dm',      'obs_dm',      len(results_df['stop'].tolist()),results_df['stop'].tolist(),results_df['dm'].tolist(),results_df['-1.000'].tolist())
#signif_graph    = toGraph2D('signif',   'signif',   len(results_df['stop'].tolist()),results_df['stop'].tolist(),results_df['lsp'].tolist(),results_df['significance'].tolist())

#graphs["exp"]       = exp_graph
graphs["exp_dm"]       = exp_dm_graph
graphs["exp_dm_up"]    = exp_dm_up_graph
graphs["exp_dm_down"]  = exp_dm_down_graph
graphs["obs_dm"]       = obs_dm_graph



#for i in ["exp","exp_up","exp_down","obs", "obs_bulk", "obs_comp"]:
for i in ["exp_dm","exp_dm_up","exp_dm_down", "obs_dm"]:
    #graphs[i] = getObjFromFile(defFile, i)
    
    graphs[i].SetNpx(nbinsx)
    graphs[i].SetNpy(nbinsy)

    print graphs[i]
    print graphs[i].GetXmin()
    print graphs[i].GetYmin()
    

    # hists[i] = ROOT.TH2F(i,i,23,250,800,15,10,80)
    # x = 0
    # y = 0 
    # z = 0
    # graphs[i].GetPoint(0,x,y,z)
    
    # print x,y,z

    
    # for i_i in range(graphs[i].GetN()) :
    #     print i_i
    #     graphs[i].GetPoint(i_i,x,y,z)
    #     print x,y,z

    hists[i] = graphs[i].GetHistogram().Clone()


    # print hists[i]
    # print "nxbins: {}".format(nbinsx)
    # print hists[i].GetNbinsX()
    # print hists[i].GetXaxis().GetBinCenter(1) - hists[i].GetXaxis().GetBinCenter(0)
    # print hists[i].GetYaxis().GetBinCenter(1) - hists[i].GetYaxis().GetBinCenter(0)




#  fix the corridor
#if options.signal == 'T2tt':
#    limit = limit_top
#    #for mStop in range(175,1000,5):
#    for mStop in range(175,650,5):
#        if len(results_df[results_df['stop']==mStop][results_df['lsp']==(mStop-175)])>0:
#            #print mStop, float(results_df[results_df['stop']==mStop][results_df['lsp']==(mStop-175)]['-1.000'])
#            limit = float(results_df[results_df['stop']==mStop][results_df['lsp']==(mStop-175)]['-1.000'])
#        else:
#            pass
#            #print "need to interpolate"
#        hists['obs'].SetBinContent(hists['obs'].GetXaxis().FindBin(mStop), hists['obs'].GetYaxis().FindBin(mStop-175), limit)

# also fix the diagonal?

for i in ["obs_dm_UL","obs_dm_up","obs_dm_down", "exp_dm_UL"]:
  hists[i] = hists["obs_dm"].Clone(i)

for i in ["obs_dm_up","obs_dm_down"]:
  hists[i].Reset()

scatter = getObjFromFile(defFile, 'scatter')
c1 = ROOT.TCanvas()
scatter.SetLineWidth(0)
scatter.SetMarkerSize(1)
scatter.SetMarkerColor(ROOT.kGreen+3)
scatter.Draw()
#scatter.GetXaxis().SetLimits(0,1000)
#scatter.GetYaxis().SetRangeUser(0,700)
scatter.Draw("p")
c1.Update()
c1.Print(os.path.join(plotDir, 'scatter.png'))


#scatter = getObjFromFile(defFile, 'scatter_excl_exp')
#nscatter = getObjFromFile(defFile, 'scatter_nexcl_exp')
#c1 = ROOT.TCanvas()
#scatter.SetLineWidth(0)
#scatter.SetMarkerSize(1)
#scatter.SetMarkerColor(ROOT.kGreen+3)
#nscatter.SetLineWidth(0)
#nscatter.SetMarkerSize(1)
#nscatter.SetMarkerColor(ROOT.kRed+2)
#scatter.Draw()
#nscatter.Draw()
#scatter.GetXaxis().SetLimits(0,1000)
#scatter.GetYaxis().SetRangeUser(0,700)
#scatter.Draw("p")
#nscatter.Draw("p same")
#c1.Update()
#c1.Print(os.path.join(plotDir, 'scatter_excl_exp.png'))
#
#scatter = getObjFromFile(defFile, 'scatter_excl_obs')
#nscatter = getObjFromFile(defFile, 'scatter_nexcl_obs')
#c1 = ROOT.TCanvas()
#scatter.SetLineWidth(0)
#scatter.SetMarkerSize(1)
#scatter.SetMarkerColor(ROOT.kGreen+3)
#nscatter.SetLineWidth(0)
#nscatter.SetMarkerSize(1)
#nscatter.SetMarkerColor(ROOT.kRed+2)
#scatter.Draw()
#nscatter.Draw()
#scatter.GetXaxis().SetLimits(0,1000)
#scatter.GetYaxis().SetRangeUser(0,700)
#scatter.Draw("p")
#nscatter.Draw("p same")
#c1.Update()
#c1.Print(os.path.join(plotDir, 'scatter_excl_obs.png'))


for i in ["exp_dm","exp_dm_up","exp_dm_down","obs_dm"]:
    c1 = ROOT.TCanvas()
    graphs[i].Draw()
    c1.SetLogz()
    c1.Print(os.path.join(plotDir, 'scatter_%s.png'%i))
    del c1

#adding TH2F for dm
hdm = ROOT.TH2F("dm","dm",111,250,800,75,10,100)
xhdm = hdm.GetXaxis()
yhdm = hdm.GetYaxis()
#print xhdm, yhdm

xsecLimits_df = [] # this will become a data frame

from StopsCompressed.Tools.xSecSusy import xSecSusy
xSecSusy_ = xSecSusy()
xSecKey = "obs_dm"


if options.signal == 'TChiWZ':
    for ix in range(hists[xSecKey].GetNbinsX()):
        for iy in range(hists[xSecKey].GetNbinsY()):
            mCha   = (hists[xSecKey].GetXaxis().GetBinUpEdge(ix)+hists[xSecKey].GetXaxis().GetBinLowEdge(ix)) / 2.
            #mNeu    = (hists[xSecKey].GetYaxis().GetBinUpEdge(iy)+hists[xSecKey].GetYaxis().GetBinLowEdge(iy)) / 2.
            dm      = (hists[xSecKey].GetYaxis().GetBinUpEdge(iy)+hists[xSecKey].GetYaxis().GetBinLowEdge(iy)) / 2.
            v       = hists[xSecKey].GetBinContent(hists[xSecKey].FindBin(mCha, dm))
            v_exp   = hists['exp_dm'].GetBinContent(hists[xSecKey].FindBin(mCha, dm)) # get expected limit
            
            #if mCha>=100 and v>0:
            print "!!! mCha", mCha
            if mCha>=100:
                scaleup   = xSecSusy_.getXSec(channel='TChiWZ_13TeV',mass=mCha,sigma=1) /xSecSusy_.getXSec(channel='TChiWZ_13TeV',mass=mCha,sigma=0)
                scaledown = xSecSusy_.getXSec(channel='TChiWZ_13TeV',mass=mCha,sigma=-1)/xSecSusy_.getXSec(channel='TChiWZ_13TeV',mass=mCha,sigma=0)
                xSec = xSecSusy_.getXSec(channel='TChiWZ_13TeV',mass=mCha,sigma=0)
                hists["obs_dm_UL"].SetBinContent(hists[xSecKey].FindBin(mCha, dm), v * xSec)
                hists["exp_dm_UL"].SetBinContent(hists[xSecKey].FindBin(mCha, dm), v_exp * xSec)
                hists["obs_dm_up"].SetBinContent(hists[xSecKey].FindBin(mCha, dm), v*scaleup)
                hists["obs_dm_down"].SetBinContent(hists[xSecKey].FindBin(mCha, dm), v*scaledown)
            
                if v>0 and xSec>0:
                    xsecLimits_df.append({'mCha':mCha, 'dm':dm, 'exp':v_exp * xSec, 'obs': v * xSec})
                    print "mCha: ", mCha, "dm: ", dm, "v_exp: ", v_exp,"xSec: ", xSec
else:
    for ix in range(hists[xSecKey].GetNbinsX()):
        for iy in range(hists[xSecKey].GetNbinsY()):
            mStop   = (hists[xSecKey].GetXaxis().GetBinUpEdge(ix)+hists[xSecKey].GetXaxis().GetBinLowEdge(ix)) / 2.
            #mNeu    = (hists[xSecKey].GetYaxis().GetBinUpEdge(iy)+hists[xSecKey].GetYaxis().GetBinLowEdge(iy)) / 2.
            dm      = (hists[xSecKey].GetYaxis().GetBinUpEdge(iy)+hists[xSecKey].GetYaxis().GetBinLowEdge(iy)) / 2.
            v       = hists[xSecKey].GetBinContent(hists[xSecKey].FindBin(mStop, dm))
            v_exp   = hists['exp_dm'].GetBinContent(hists[xSecKey].FindBin(mStop, dm)) # get expected limit
            
            if mStop>200 and v>0:
                scaleup   = xSecSusy_.getXSec(channel='stop13TeV',mass=mStop,sigma=1) /xSecSusy_.getXSec(channel='stop13TeV',mass=mStop,sigma=0)
                scaledown = xSecSusy_.getXSec(channel='stop13TeV',mass=mStop,sigma=-1)/xSecSusy_.getXSec(channel='stop13TeV',mass=mStop,sigma=0)
                xSec = xSecSusy_.getXSec(channel='stop13TeV',mass=mStop,sigma=0)
                hists["obs_dm_UL"].SetBinContent(hists[xSecKey].FindBin(mStop, dm), v * xSec)
                hists["exp_dm_UL"].SetBinContent(hists[xSecKey].FindBin(mStop, dm), v_exp * xSec)
                hists["obs_dm_up"].SetBinContent(hists[xSecKey].FindBin(mStop, dm), v*scaleup)
                hists["obs_dm_down"].SetBinContent(hists[xSecKey].FindBin(mStop, dm), v*scaledown)
                if v>0 and xSec>0:
                    xsecLimits_df.append({'mStop':mStop, 'dm':dm, 'exp':v_exp * xSec, 'obs': v * xSec})
    		if mStop>500 and mStop<700:
    	    		print "mStop: ", mStop,"dm: " , dm,"v_exp: ", v_exp,"xSec: ", xSec
                #if mStop>640 and mNeu>540 and v>0 and v_exp>0:
                #    print mStop, mNeu, v, v_exp, xSec, scaleup, scaledown
                #if mStop>650 and mStop<660 and mNeu>500 and mNeu<600 and v_exp >0 and v >0:
                #    print "acc: " ,v, v_exp, mStop, mNeu, xSec, scaleup, scaledown

xsecLimits_df = pd.DataFrame(xsecLimits_df)

if options.signal == 'T8bbllnunu_XCha0p5_XSlep0p95':
    hists["obs_UL"].SetBinContent(hists[xSecKey].FindBin(201, 1), 1)

# set bins for y=0
for ix in range(hists[xSecKey].GetNbinsX()):
    hists["obs_dm_UL"].SetBinContent(ix, 0, hists["obs_dm_UL"].GetBinContent(ix,1))
    hists["exp_dm_UL"].SetBinContent(ix, 0, hists["exp_dm_UL"].GetBinContent(ix,1))
    hists["obs_dm_up"].SetBinContent(ix, 0, hists["obs_dm_up"].GetBinContent(ix,1))
    hists["obs_dm_down"].SetBinContent(ix, 0, hists["obs_dm_down"].GetBinContent(ix,1))

# to get a properly closed contour
for ix in range(hists[xSecKey].GetNbinsX()):
    for iy in range(hists[xSecKey].GetNbinsY()):
        if iy>ix:
            for i in ["exp_dm", "exp_dm_up", "exp_dm_down", "obs_dm", "obs_dm_up", "obs_dm_down"]:
                if hists[i].GetBinContent(ix,iy) == 0:
                    hists[i].SetBinContent(ix,iy,1e6)

for i in ["exp_dm", "exp_dm_up", "exp_dm_down", "obs_dm", "obs_dm_up", "obs_dm_down", "obs_dm"]:
    hists[i + "_smooth"] = hists[i].Clone(i + "_smooth")
    if options.smooth:
        for x in range(int(options.iterations)):
            hists[i + "_smooth"].Smooth(1,options.smoothAlgo)

        if options.signal == 'T2bW':
            for ix in range(hists[i].GetNbinsX()):
                for iy in range(hists[i].GetNbinsY()):
                    if iy>(ix):#  or iy==ix-1 or iy==ix-2:
                        hists[i + "_smooth"].SetBinContent(ix, iy, hists[i].GetBinContent(ix,iy))

        



ROOT.gStyle.SetPadRightMargin(0.05)
c1 = ROOT.TCanvas()
niceColorPalette(255)

hists["obs_dm"].GetZaxis().SetRangeUser(0.002, 2999)
hists["obs_dm"].Draw('COLZ')
c1.SetLogz()

c1.Print(os.path.join(plotDir, 'limit.png'))

#modelname = signalString
#T2degenerate dm plots

if signalString == "TChiWZ":
    modelname = 'TChiWZ_dm'
else:
    modelname = 'T2deg_dm'

temp = ROOT.TFile("tmp.root","recreate")

## we currently use non-smoothed color maps!
tempHist = "obs_dm_UL" if not options.expected else "exp_dm_UL"
hists[tempHist].Clone("temperature").Write()

contourPoints = {}

for i in ["exp_dm", "exp_dm_down", "exp_dm_up", "obs_dm_up", "obs_dm_down", "obs_dm"]:
    c1 = ROOT.TCanvas()
    # get ALL the contours
    contours = getContours(hists[i + "_smooth"], plotDir)
    # cleaning
    contourPoints[i] = {}
    for j,g in enumerate(contours):
        contourPoints[i][j] = [{'x': p[0], 'y':p[1]} for p in getPoints(g)]
        #contourPoints[i][j] = getPoints(g)
        cleanContour(g, model=modelname)
        g = extendContour(g)
    contours = max(contours , key=lambda x:x.GetN()).Clone("contour_" + i)
    contours.Draw()
    c1.Print(os.path.join(plotDir, 'contour_%s.png'%i))
    contours.Write()

# take care of top corridor

def unit_vector(vector):
    return vector / np.linalg.norm(vector) if np.linalg.norm(vector) > 0 else vector

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

if options.signal == 'T2tt':
    corridor = {}
    ## this should also be automatized
    #corridor['obs']        = contourPoints['obs'][1] + contourPoints['obs'][2] + contourPoints['obs'][3] + contourPoints['obs'][4] + contourPoints['obs'][5]
    #corridor['obs_up']     = contourPoints['obs_up'][1] + contourPoints['obs_up'][2] + contourPoints['obs_up'][3] + contourPoints['obs_up'][4] + contourPoints['obs_up'][5]
    #corridor['obs_down']   = contourPoints['obs_down'][1] + contourPoints['obs_down'][2] + contourPoints['obs_down'][3]
    # this should also be automatized
    #print len(contourPoints['obs'])
    #print len(contourPoints['obs_up'])
    #print len(contourPoints['obs_down'])
    #corridor['obs']        = contourPoints['obs'][1] + contourPoints['obs'][2] + contourPoints['obs'][3]
    #corridor['obs_up']     = contourPoints['obs_up'][1] + contourPoints['obs_up'][2] + contourPoints['obs_up'][3]
    #corridor['obs_down']   = contourPoints['obs_down'][1] + contourPoints['obs_down'][2]
    #corridor['obs']        = []
    #for i in range(0, len(contourPoints['obs'])):
    #    print contourPoints['obs'][i]
    #    corridor['obs'] += contourPoints['obs'][i]
    #corridor['obs_up']     = contourPoints['obs_up'][1] + contourPoints['obs_up'][2] + contourPoints['obs_up'][3]
    #corridor['obs_down']   = contourPoints['obs_down'][1] + contourPoints['obs_down'][2]

    corridor['obs'] = [\
        #{'x':175, 'y':25}, {'x':310, 'y':185}, {'x':350, 'y':200}, {'x':425, 'y':250}, {'x':350, 'y':150}, {'x':310, 'y':170}, {'x':190, 'y':0}\
        {'x':150, 'y':0}, {'x':262.5, 'y':112.5}, {'x':370, 'y':200}, {'x':395, 'y':260}, {'x':405, 'y':260},  {'x':385, 'y':252}, {'x':325, 'y':200}, {'x':150, 'y':37}\
    ]
    corridor['obs_up']     = [\
        {'x':150, 'y':0}, {'x':262.5, 'y':112.5}, {'x':370, 'y':200}, {'x':395, 'y':260}, {'x':405, 'y':260},  {'x':385, 'y':252}, {'x':325, 'y':200}, {'x':150, 'y':37}\
        #{'x':150, 'y':0}, {'x':262.5, 'y':112.5}, {'x':370, 'y':200}, {'x':425, 'y':270}, {'x':410, 'y':275}, {'x':325, 'y':200}, {'x':150, 'y':37}\
        #{'x':175, 'y':25}, {'x':310, 'y':185}, {'x':350, 'y':200}, {'x':425, 'y':250}, {'x':350, 'y':150}, {'x':310, 'y':170}, {'x':190, 'y':0}\
    ]
    corridor['obs_down']     = [\
        {'x':150, 'y':0}, {'x':262.5, 'y':112.5}, {'x':370, 'y':200}, {'x':395, 'y':260}, {'x':405, 'y':260},  {'x':385, 'y':252}, {'x':325, 'y':200}, {'x':150, 'y':37}\
        #{'x':150, 'y':0}, {'x':262.5, 'y':112.5}, {'x':370, 'y':200}, {'x':425, 'y':270}, {'x':410, 'y':275}, {'x':325, 'y':200}, {'x':150, 'y':37}\
        #{'x':175, 'y':25}, {'x':310, 'y':185}, {'x':350, 'y':200}, {'x':425, 'y':250}, {'x':350, 'y':150}, {'x':310, 'y':170}, {'x':190, 'y':0}\
    ]
    
    for o in ['obs', 'obs_up', 'obs_down']:
        for p in corridor[o]:
            p.update(getProjection(p['x'], p['y'], 310, 175))
            corridor[o+'_df'] = pd.DataFrame(corridor[o])

        # bla
        corridor[o+'_x_list'] = corridor[o+'_df'][corridor[o+'_df']['x']<600].sort_values('phi')['x'].tolist()
        corridor[o+'_y_list'] = corridor[o+'_df'][corridor[o+'_df']['x']<600].sort_values('phi')['y'].tolist()
        
        #pos = 0
        #for j in range(len(corridor[o+'_x_list'])):
        #    if pos+2 >= len(corridor[o+'_x_list']): break
        #    i = pos
        #    phi = angle_between((corridor[o+'_x_list'][i]-corridor[o+'_x_list'][i+1], corridor[o+'_y_list'][i]-corridor[o+'_y_list'][i+1]), (corridor[o+'_x_list'][i+2]-corridor[o+'_x_list'][i+1], corridor[o+'_y_list'][i+2]-corridor[o+'_y_list'][i+1]) )
        #    if phi > 1.5 and phi is not float('nan'):
        #        pos += 1
        #    else:
        #        # remove the outlier from the list
        #        corridor[o+'_x_list'].pop(i+2)
        #        corridor[o+'_y_list'].pop(i+2)

        corridor[o+'_x_list'] += corridor[o+'_x_list'][:1]
        corridor[o+'_y_list'] += corridor[o+'_y_list'][:1]

        corridor["contour_corr_"+o] = toGraph("contour_corr_"+o, "contour_corr_"+o, len(corridor[o+'_y_list']), corridor[o+'_x_list'], corridor[o+'_y_list'])

        corridor["contour_corr_"+o].Write()
        
        #can = ROOT.TCanvas()
        #my_cont.Draw()
        #can.Print("~/www/%s_test3.png"%o)

temp.Close()

from StopsCompressed.PlotsSMS.inputFile import inputFile
from StopsCompressed.PlotsSMS.smsPlotXSEC import smsPlotXSEC
from StopsCompressed.PlotsSMS.smsPlotCONT import smsPlotCONT
from StopsCompressed.PlotsSMS.smsPlotBrazil import smsPlotBrazil


# read input arguments
analysisLabel = "SUS-17-005"
outputname = os.path.join(plotDir, 'limit')

# read the config file
# options.signal == "T2tt":
#    fileIN = inputFile('SMS_limit_T2tt.cfg')
#else:
#    fileIN = inputFile('SMS_limit.cfg')
# changes by me
#fileIN = inputFile('SMS_limit.cfg')
#T2degdm
fileIN = inputFile('SMS_limit_T2degdm.cfg')

if options.year == 2016:
    lumi    = 35.9
elif options.year == 2017:
    lumi    = 41.5
elif options.year == 2018:
    lumi    = 59.7 
else:
    lumi = 137

if True:
    lumi_ = lumi
else:
    lumi_ = fileIN.LUMI

# classic temperature histogra
xsecPlot = smsPlotXSEC(modelname, fileIN.HISTOGRAM, fileIN.OBSERVED, fileIN.EXPECTED, fileIN.ENERGY, lumi_, fileIN.PRELIMINARY, "")
#xsecPlot.Draw( lumi = lumi, zAxis_range = (10**-3,10**2) )
xsecPlot.Draw()
#if options.signal.startswith("T8"):
#    xsecPlot.Draw( lumi = lumi, zAxis_range = (10**-4,5*10**2) )
#else:
#    xsecPlot.Draw( lumi = lumi, zAxis_range = (10**-3,10**2) )
xsecPlot.Save("%sXSEC" %outputname)

temp = ROOT.TFile("tmp.root","update")
xsecPlot.c.Write("cCONT_XSEC")
temp.Close()

# only lines
contPlot = smsPlotCONT(modelname, fileIN.HISTOGRAM, fileIN.OBSERVED, fileIN.EXPECTED, fileIN.ENERGY, lumi_, fileIN.PRELIMINARY, "")
contPlot.Draw()
contPlot.Save("%sCONT" %outputname)

# brazilian flag (show only 1 sigma)
brazilPlot = smsPlotBrazil(modelname, fileIN.HISTOGRAM, fileIN.OBSERVED, fileIN.EXPECTED, fileIN.ENERGY, lumi_, fileIN.PRELIMINARY, "")
brazilPlot.Draw()
brazilPlot.Save("%sBAND" %outputname)

