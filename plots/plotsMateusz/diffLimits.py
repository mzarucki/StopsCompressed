import ROOT, os, math
import pickle, shutil
import pandas

from RootTools.core.standard                import *
from array import array

from StopsCompressed.Tools.niceColorPalette       import niceColorPalette
from StopsCompressed.Tools.user              import plot_directory, analysis_results
#from Workspace.DegenerateStopAnalysis.tools.degTools import setup_style

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
#argParser.add_argument('--spin',           action='store',      default='scalar',            nargs='?', choices=['scalar','pseudoscalar'], help="scalar (S) or pseudoscalar (PS)?")
argParser.add_argument('--scan',               action='store',      default='T2tt',           help='Which scan?')
argParser.add_argument("--year",               action='store',   type=int,    default=2018, help="Which year?")
argParser.add_argument('--plot_directory',     action='store',      default='limits/brazil')
argParser.add_argument('--baseline',           action='store',      default='fitAll_baseline_redSys')
argParser.add_argument("--channel",            action='store',      help = "Lepton channel", type = str, default = "mu")
#argParser.add_argument("--scaled",             action='store',   type=float,    default=1.0, help="Scaled limits?")
argParser.add_argument('--blinded',            action='store_true')
argParser.add_argument('--cardDir',            action='store',      default='TTbarDM_preAppFix_DYttZflat')
argParser.add_argument('--xsec',            action='store_true')
args = argParser.parse_args()

args.blinded = True
yearString = str(args.year)# if not options.combined else 'comb'

suffix = "_%s_%s"%(args.scan,args.channel)

#ROOT.gROOT.SetBatch(True)
ROOT.gROOT.LoadMacro('../../../RootTools/plot/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetPaintTextFormat("4.2f")

#setup_style()

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

categories = []
mChi_list = []
mPhi_list = []

#for s in DMsamples:
#    if not s[0] in mChi_list: mChi_list.append(s[0])
#    if not s[1] in mPhi_list: mPhi_list.append(s[1])
#    if not s[2] in categories: categories.append(s[2])

results_dir = "/eos/user/m/mzarucki/StopsCompressed/sensitivity/" + yearString

#if args.scaled != 1.0:
#    limits_file_baseline = limits_file_baseline.replace("_v1", "_%s_v1"%scaledStr)
#    limits_file_compare  = limits_file_compare.replace("_v1", "_%s_v1"%scaledStr)

if "T2" in args.scan:
    sensitivityStudies = [ 
        "baseline_redSys", # baseline
        "baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ", 
    ]
elif args.scan in ["TChiWZ", "MSSM"]:
    suffix += "_CI"
    sensitivityStudies = [ 
        "baseline_redSys_chargeInclusive", # baseline (CI)
        "baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusive",
    ]

assert sensitivityStudies[0] in ["baseline_redSys", "baseline_redSys_chargeInclusive"]
assert len(sensitivityStudies) == 2

if args.scan == 'TChiWZ':
    yVar = 'dm'
    xVar = 'stop'
    xLabel = 'm_{#tilde{#chi}^{#pm}_{1}} = m_{#tilde{#chi}^{0}_{2}} [GeV]'
    yLabel = '#Deltam(#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}, #tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}}) [GeV]'
    #fixedMass = 100
    #suffix += "_mCha" + str(fixedMass)

    xmin = 100
    xmax = 500
    ymin = 10 # TODO: add 3, 5, 7 variable bins 
    ymax = 50
    
    nbinsx = (xmax-xmin)/25# * 2
    nbinsy = (ymax-ymin)/10# * 5
    #nbinsx = 50
    #nbinsy = 35
elif args.scan == 'MSSM':
    yVar = 'lsp'
    xVar = 'stop'
    xLabel = '#mu'
    yLabel = 'M_{1}'
    #fixedMass = 100
    #suffix += "_mu" + str(fixedMass)
    
    #mus = [100, 120, 140, 160, 180, 200, 220, 240]
    #M1s = [300, 400, 500, 600, 800, 1000, 1200]
    #nbinsx = 8
    #nbinsy = 10
    xmin = 100
    xmax = 240
    ymin = 300
    ymax = 1200
    
    nbinsx = (xmax-xmin)/10# * 2 # max: 240
    nbinsy = (ymax-ymin)/100# * 5
else:
    yVar = 'dm'
    xVar = 'stop'
    xLabel = 'm_{#tilde{t}} [GeV]'
    yLabel = "#Deltam(#tilde{t},#tilde{#chi}^{0}_{1}) [GeV]"
    #fixedMass = 500
    #suffix += "_mStop" + str(fixedMass)
    
    xmin = 250
    xmax = 800
    ymin = 10
    ymax = 80
    
    nbinsx = (xmax-xmin)/25# * 2
    nbinsy = (ymax-ymin)/10# * 5
    
    #nbins = 105 # bin size 10 GeV
    #nbins = 55 # bin size 10 GeV for dm plots
    #nbinsx = 55
    #nbinsy = 55

graphs  = {}
hists   = {"exp_dm":{}}

limits_files = {}
res = {}
df = {}
filteredResults = {}
exp_ = {}
exp_dm_graph = {}

a_mass = {}
a_dm   = {}
a_exp  = {}

from StopsCompressed.samples.default_locations import default_locations
samples_tag = default_locations.mc_2018_postProcessing_directory.split("/")[0]

plot_dir = os.path.join(plot_directory, samples_tag, 'limits', yearString, args.scan, 'difference')
#plot_dir = os.path.join(plot_directory,args.plot_directory)

filetypes = [".pdf",".png",".root"]

if not os.path.isdir(plot_dir):
    os.makedirs(plot_dir)

for i, sens in enumerate(sensitivityStudies):
    limits_files[sens] = os.path.join(results_dir, "fitAll_{sensitivityStudyName}_{channel}_v1", "limits", args.scan, args.scan, "limitResults.pkl").format(sensitivityStudyName = sens, channel = args.channel)
    if "scaled" in sens: limits_files[sens] = limits_files[sens].replace("scaled4p3_" + args.channel, args.channel + "_scaled4p3") # workaround 

    res[sens] = pickle.load(file(limits_files[sens]))

    df[sens] = pandas.DataFrame(res[sens])

    #filteredResults[sens] = df[sens][(df[sens][xVar]==fixedMass)].sort_values(by=yVar)
   
    try:
        a_mass[sens] = df[sens][xVar].to_numpy()
        a_dm[sens]   = df[sens][yVar].to_numpy()
        a_exp[sens]  = df[sens]['0.500'].to_numpy()
    except KeyError:
        print "Result not found for ", sens

    if args.scan == "MSSM": # workaround to not use dm results for MSSM
        exp_graph       = toGraph2D('exp',      'exp',      len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['lsp'].tolist(),df[sens]['0.500'].tolist())
        #exp_up_graph    = toGraph2D('exp_dm_up',   'exp_dm_up',   len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['lsp'].tolist(),df[sens]['0.840'].tolist())
        #exp_down_graph  = toGraph2D('exp_dm_down', 'exp_dm_down', len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['lsp'].tolist(),df[sens]['0.160'].tolist())
        #obs_graph       = toGraph2D('obs_dm',      'obs_dm',      len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['lsp'].tolist(),df[sens]['-1.000'].tolist())
        exp_dm_graph       = exp_graph
        #exp_dm_up_graph    = exp_up_graph
        #exp_dm_down_graph  = exp_down_graph
        #obs_dm_graph       = obs_graph
    else:
        #exp_graph       = toGraph2D('exp',      'exp',      len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['lsp'].tolist(),df[sens]['0.500'].tolist())
        exp_dm_graph       = toGraph2D('exp_dm',      'exp_dm',      len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['dm'].tolist(),df[sens]['0.500'].tolist())
        #exp_dm_up_graph    = toGraph2D('exp_dm_up',   'exp_dm_up',   len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['dm'].tolist(),df[sens]['0.840'].tolist())
        #exp_dm_down_graph  = toGraph2D('exp_dm_down', 'exp_dm_down', len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['dm'].tolist(),df[sens]['0.160'].tolist())
        #obs_dm_graph       = toGraph2D('obs_dm',      'obs_dm',      len(df[sens]['stop'].tolist()),df[sens]['stop'].tolist(),df[sens]['dm'].tolist(),df[sens]['-1.000'].tolist())
    
    #graphs["exp"]       = exp_graph
    graphs["exp_dm"]       = exp_dm_graph
    #graphs["exp_dm_up"]    = exp_dm_up_graph
    #graphs["exp_dm_down"]  = exp_dm_down_graph
    #graphs["obs_dm"]       = obs_dm_graph
    
    for i in ["exp_dm"]:#,"exp_dm_up","exp_dm_down", "obs_dm"]:
    
        graphs[i].SetNpx(nbinsx)
        graphs[i].SetNpy(nbinsy)
    
        # hists[i] = ROOT.TH2F(i,i,23,250,800,15,10,80)
        # x = 0
        # y = 0 
        # z = 0
        # graphs[i].GetPoint(0,x,y,z)
    
        # for i_i in range(graphs[i].GetN()) :
        #     print i_i
        #     graphs[i].GetPoint(i_i,x,y,z)
        #     print x,y,z
    
        hists[i][sens] = graphs[i].GetHistogram().Clone()

    can = ROOT.TCanvas("can","",700,700)
    can.SetRightMargin(0.15)
    #can.SetLogy()
    niceColorPalette(255)
    hists["exp_dm"][sens].GetZaxis().SetRangeUser(0.002, 2999)
    hists["exp_dm"][sens].GetXaxis().SetTitle(xLabel)
    hists["exp_dm"][sens].GetYaxis().SetTitle(yLabel)
    hists["exp_dm"][sens].Draw("COLZ TEXT89")
    can.SetLogz()
    
    for f in filetypes:
        can.Print(os.path.join(plot_dir, 'limit_%s%s'%(sens,f)))

can2 = ROOT.TCanvas("can","",700,700)
can2.SetRightMargin(0.15)

comp = "relDiff" # "ratio"
den = hists["exp_dm"][sensitivityStudies[0]].Clone()
num = hists["exp_dm"][sensitivityStudies[1]].Clone()

diffPlot = num
if comp == "ratio": # ratio
    if 'TChiWZ' in args.scan:
        diffPlot.GetZaxis().SetRangeUser(0.5,1.2)
    else:
        diffPlot.GetZaxis().SetRangeUser(0.8,1.2)
    suffix += "_ratio" 
elif comp == "relDiff": # relative difference
    diffPlot.Add(den,-1.) # difference
    diffPlot.Scale(-1.) # invert 
    diffPlot.GetZaxis().SetRangeUser(0,0.5)
    suffix += "_relDiff" 

diffPlot.Divide(den)
diffPlot.Draw('COLZ TEXT89')
##y_max = 500
##y_min = 0.05
##mg.SetMaximum(y_max)
##mg.SetMinimum(y_min)

diffPlot.GetXaxis().SetTitle(xLabel)
diffPlot.GetYaxis().SetTitle(yLabel)
#diffPlot.GetZaxis().SetTitle("Difference")
diffPlot.GetXaxis().SetRangeUser(xmin,xmax)
diffPlot.GetYaxis().SetRangeUser(ymin,ymax)
extraText = "Private Work"

#latex2 = ROOT.TLatex()
#latex2.SetNDC()
#latex2.SetTextSize(0.03)
#latex2.SetTextAlign(11) # align right
#if args.scan == 'mChi' and args.spin == 'scalar':
#    latex2.DrawLatex(0.20,0.89,'#bf{'+tp_+', Dirac DM, m_{#phi} = '+str(fixedMass)+' GeV}')
#elif args.scan == 'mChi' and args.spin == 'pseudoscalar':
#    latex2.DrawLatex(0.20,0.89,'#bf{'+tp_+', Dirac DM, m_{a} = '+str(fixedMass)+' GeV}')
#elif args.scan == 'TChiWZ':
#    latex2.DrawLatex(0.20,0.89,'#bf{#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}#tilde{#chi}_{#lower[-0.3]{2}}^{#lower[0.4]{0}} #rightarrow WZ#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}}#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}}}')
#elif args.scan == 'MSSM':
#    latex2.DrawLatex(0.20,0.89,'#bf{Higgsino pMSSM}')
#else:
#    latex2.DrawLatex(0.20,0.89,'#bf{'+tp_+', Dirac DM, m_{#chi} = '+str(fixedMass)+' GeV}')
#
#if args.scan == 'TChiWZ':
#    latex2.DrawLatex(0.20,0.85,'#bf{m_{#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}} = m_{#tilde{#chi}_{#lower[-0.3]{2}}^{#lower[0.4]{0}}} = %s GeV}'%fixedMass)
#elif args.scan == 'MSSM':
#    latex2.DrawLatex(0.20,0.85,'#bf{#mu = %s GeV}'%fixedMass)
#else: 
#    latex2.DrawLatex(0.20,0.85,'#bf{g_{q} = 1, g_{DM} = 1}')
#
#latex2.DrawLatex(0.20,0.80,'#bf{95% CL upper limits}')
#latex2.DrawLatex(0.22,0.84,'#bf{m_{#chi} = '+str(mChi)+' GeV, g_{q} = 1, g_{#chi} = 1}')

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11) # align right
latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
#latex1.DrawLatex(0.85,0.96,"#bf{13 TeV}")
latex1.DrawLatex(0.57,0.96,"#bf{59.7 fb^{-1} (13 TeV)}")

can2.RedrawAxis()

for f in filetypes:
    can2.Print(os.path.join(plot_dir, 'diffLimits%s%s'%(suffix,f)))
