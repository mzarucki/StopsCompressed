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
    
from StopsCompressed.PlotsSMS.inputFile import inputFile
from StopsCompressed.PlotsSMS.smsPlotXSEC import smsPlotXSEC
from StopsCompressed.PlotsSMS.smsPlotCONT import smsPlotCONT
from StopsCompressed.PlotsSMS.smsPlotBrazil import smsPlotBrazil

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

options.expected = True

if scale != 1.0:
    suffix += "_scaled%s"%str(scale).replace(".","p")

dmplot = options.dmPlot
yearString = str(options.year) if not options.combined else 'comb'
signalString = options.signal

from StopsCompressed.samples.default_locations import default_locations
samples_tag = default_locations.mc_2018_postProcessing_directory.split("/")[0]

saveDir = os.path.join(plot_directory, samples_tag, 'limits', yearString, signalString, "simultaneous", 'FR_limitAll_%s_%s'%(yearString, suffix))
 
if options.smooth:
    saveDir += "_smooth_it%s_%s"%(options.iterations, options.smoothAlgo)
if options.expected:
    saveDir += '_expected'
    
import RootTools.plot.helpers as plot_helpers
plot_helpers.copyIndexPHP( saveDir )

if not os.path.exists(saveDir):
    os.makedirs(saveDir)

if signalString == "TChiWZ":
    modelname = 'TChiWZ_dm'
else:
    modelname = 'T2deg_dm'
    
rootFileDirs = {'xsec':{}, 'cont':{}, 'objects':{}}
rootFiles    = {'xsec':{}, 'cont':{}, 'objects':{}}
canvs        = {'xsec':{}, 'cont':{}}
plots        = {'xsec':{}, 'cont':{}}

sensitivityStudies = [
    "baseline_redSys", 
    "baselinePlusLowMET3_redSys", 
    ##"baselinePlusLowMET3_redSys_4mTregions", 
    ##"baselinePlusLowMET3_redSys_4mTregions_splitCTZ", 
    ##"baselinePlusLowMET3_redSys_4mTregions_splitCTZ_lowHTbin", 
    "baselinePlusLowMET3_redSys_low5mTregions", 
    "baselinePlusLowMET3_redSys_high5mTregions", 
    #"baselinePlusLowMET3_redSys_high5mTregions_splitCTZ_lowHTbin", 
    #"baselinePlusLowMET3_redSys_high5mTregions_splitCTZ3_lowHTbin", 
    #"baselinePlusLowMET3_redSys_high5mTregions_splitCTZ3_lowHTbin_tightIPZ", 
    "baselinePlusLowMET3_redSys_6mTregions_splitCTZ_lowHTbin",
]

for i, sens in enumerate(sensitivityStudies):
    if sens in ["baseline", "baseline_redSys"]:
        fullSensitivityStudyName = sens + "_nbins56_mt95_3mTregions_CT400_isPromptFalse_lowMETregionFalse"
    elif sens in ["baselinePlusLowMET", "baselinePlusLowMET_redSys", "baselinePlusLowMET2_redSys", "baselinePlusLowMET3_redSys"]:
        fullSensitivityStudyName = sens + "_nbins80_mt95_3mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_4mTregions", "baselinePlusLowMET3_redSys_4mTregions_splitCTZ"]:
        fullSensitivityStudyName = sens + "_nbins104_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_4mTregions_splitCTZ_lowHTbin"]:
        fullSensitivityStudyName = sens + "_nbins136_mt95_4mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_low5mTregions"]:
        fullSensitivityStudyName = sens + "_nbins132_mt95_low5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_high5mTregions"]:
        fullSensitivityStudyName = sens + "_nbins128_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_high5mTregions_splitCTZ_lowHTbin"]:
        fullSensitivityStudyName = sens + "_nbins168_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_high5mTregions_splitCTZ3_lowHTbin", "baselinePlusLowMET3_redSys_high5mTregions_splitCTZ3_lowHTbin_tightIPZ"]:
        fullSensitivityStudyName = sens + "_nbins208_mt95_high5mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_6mTregions"]:
        fullSensitivityStudyName = sens + "_nbins156_mt95_6mTregions_CT400_isPromptFalse_lowMETregionTrue"
    elif sens in ["baselinePlusLowMET3_redSys_6mTregions_splitCTZ_lowHTbin"]:
        fullSensitivityStudyName = sens + "_nbins204_mt95_6mTregions_CT400_isPromptFalse_lowMETregionTrue"
    else:
        raise NotImplementedError

    plotDir = os.path.join(plot_directory, samples_tag, 'limits', yearString, signalString, fullSensitivityStudyName, 'FR_limitAll_%s_%s'%(yearString, suffix))

    #analysis_results = '/eos/user/m/mzarucki/StopsCompressed/sensitivity/2018/fitAll_{sensitivityStudyName}_{suffix}_v1/limits/{signal}/{signal}/'.format(sensitivityStudyName = sens, signal = signalString, suffix = suffix)

    rootFileDirs['xsec'][sens]    = os.path.join(plotDir, "limitXSEC.root")
    rootFileDirs['cont'][sens]    = os.path.join(plotDir, "limitCONT.root")
    rootFileDirs['objects'][sens] = os.path.join(plotDir, "limitObjects.root")

    rootFiles['xsec'][sens]    = ROOT.TFile.Open(rootFileDirs['xsec'][sens])
    rootFiles['cont'][sens]    = ROOT.TFile.Open(rootFileDirs['cont'][sens])
    rootFiles['objects'][sens] = ROOT.TFile.Open(rootFileDirs['objects'][sens])
    
    canvs['xsec'][sens] = rootFiles['xsec'][sens].Get("cCONT_")
    #canvs['cont'][sens] = rootFiles['cont'][sens].Get("cCONT_")
    #plots['xsec'][sens] = rootFiles['objects'][sens].Get("temperature")
    plots['cont'][sens] = rootFiles['objects'][sens].Get("contour_exp_dm")
    #plots['xsec'][sens] = canvs['xsec'][sens].GetPrimitive("emptyHisto")
    
    # read input arguments
    outputname = os.path.join(saveDir, 'limit')
    
    if i == 0 and sens in ["baseline", "baseline_redSys"]: # always baseline as default
        cMain = canvs['xsec'][sens].Clone()
        cMain.Draw()
    else:
        cMain.cd()
        plots['cont'][sens].SetLineColor(i+2) # ignoring black and red and starting from green
        plots['cont'][sens].SetLineStyle(1)
        plots['cont'][sens].SetLineWidth(2)
        plots['cont'][sens].Draw('same')
        
for ext in [".root", ".png", ".pdf"]:
    cMain.SaveAs("%sXSEC%s"%(outputname, ext))
