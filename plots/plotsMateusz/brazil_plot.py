import ROOT, os, math
import pickle, shutil
import pandas

from RootTools.core.standard                import *
from array import array

from StopsCompressed.Tools.user              import plot_directory, analysis_results
#from Workspace.DegenerateStopAnalysis.tools.degTools import setup_style

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
#argParser.add_argument('--spin',           action='store',      default='scalar',            nargs='?', choices=['scalar','pseudoscalar'], help="scalar (S) or pseudoscalar (PS)?")
argParser.add_argument('--scan',               action='store',      default='TChiWZ',           help='Which scan?')
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

suffix = "_%s"%args.channel

# generic
sensitivityStudies = [ 
    "baseline_redSys", # baseline
    "baselinePlusLowMET3_redSys", 
    "baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ",
    "baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ",
]
if args.scan == "TChiWZ":
    sensitivityStudies.extend([
        #"baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusiveZ",
        "baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusiveZ",
        "baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusive",
    ])

# all scaled
if False:
    sensitivityStudies_ = []
    for sens in sensitivityStudies:
       sens += "_scaled4p3"
       sensitivityStudies_.append(sens) 
    sensitivityStudies = sensitivityStudies_

# final
if True:
    sensitivityStudies = [ 
        "baseline_redSys", # baseline
        "baseline_redSys_chargeInclusive",
        #"baseline_redSys_scaled4p3",
        "baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusiveZ_scaled4p3",
        "baseline_redSys_chargeInclusive_scaled4p3",
        #"baselinePlusLowMET3_redSys_scaled4p3", 
        #"baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_scaled4p3",
        "baselinePlusLowMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusive_scaled4p3",
        #"baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_scaled4p3",
        #"baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_scaled4p3",
        #"baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusiveZ_scaled4p3",
        #"baselinePlusLowPlusHighMET3_redSys_4mTregionsZ_ratioCTZ_highPtBinZ60_vTightMuonsZ_chargeInclusive_scaled4p3",
    ]

#ROOT.gROOT.SetBatch(True)
ROOT.gROOT.LoadMacro('../../../RootTools/plot/scripts/tdrstyle.C')
ROOT.setTDRStyle()

#setup_style()

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

if args.scan == 'TChiWZ':
    scanVar = 'dm'
    fixedVar = 'stop'
    fixedMass = 100
else:
    scanVar = 'dm'
    fixedVar = 'stop'
    fixedMass = 550

suffix += "_mCha" + str(fixedMass)

limits_files = {}
res = {}
df = {}
filteredResults = {}
exp_ = {}

mass        = []
obs         = []
obsUp       = []
obsDown     = []
exp         = []
exp1Up      = []
exp2Up      = []
exp1Down    = []
exp2Down    = []
xsecs       = []
zeros       = []

for i, sens in enumerate(sensitivityStudies):
    limits_files[sens] = os.path.join(results_dir, "fitAll_{sensitivityStudyName}_{channel}_v1", "limits", args.scan, args.scan, "limitResults.pkl").format(sensitivityStudyName = sens, channel = args.channel)
    if "scaled" in sens: limits_files[sens] = limits_files[sens].replace("scaled4p3_" + args.channel, args.channel + "_scaled4p3") # workaround 

    res[sens] = pickle.load(file(limits_files[sens]))

    df[sens] = pandas.DataFrame(res[sens])

    filteredResults[sens] = df[sens][(df[sens][fixedVar]==fixedMass)].sort_values(by=scanVar)
    
    exp_[sens] = []

    for s in filteredResults[sens][scanVar].tolist():
        if i == 0:
            mass.append(s)
            if args.scan == 'mChi':
                mChi = s
                mPhi = fixedMass
            else:
                mChi = fixedMass
                mPhi = s
            try:
                tmp = filteredResults[sens][filteredResults[sens][scanVar]==s]#['0.500']
                xsec = 1
    
                # x-sec line
                xsecs.append(xsec)
    
                # expected line and bands
                exp.append(xsec*float(tmp['0.500']))
                exp1Up.append(xsec*(float(tmp['0.840']) - float(tmp['0.500'])))
                exp2Up.append(xsec*(float(tmp['0.975']) - float(tmp['0.500'])))
                exp1Down.append(xsec*(float(tmp['0.500']) - float(tmp['0.160'])))
                exp2Down.append(xsec*(float(tmp['0.500']) - float(tmp['0.025'])))
    
                # observed line and theory uncertainty band
                obs.append(xsec*(float(tmp['-1.000'])))
                obsUp.append(xsec*(float(tmp['-1.000']))*0.3)
                obsDown.append(xsec*(float(tmp['-1.000']))*0.3)
    
                #obsUp.append(xsec*res[(s[0],s[1],s[2])]['-1.000']*math.sqrt(0.3**2 + (xSecDM_.getXSec(tp,s[1],s[0],sigma=1)/xSecDM_.getXSec(tp,s[1],s[0]) - 1)**2))
                #obsDown.append(xsec*res[(s[0],s[1],s[2])]['-1.000']*math.sqrt(0.3**2 + (1 - xSecDM_.getXSec(tp,s[1],s[0],sigma=-1)/xSecDM_.getXSec(tp,s[1],s[0]))**2))
    
                # technicality
                zeros.append(0)
            except KeyError:
                print "Result not found for"
        else: 
            try:
                tmp = filteredResults[sens][filteredResults[sens][scanVar]==s]#['0.500']
            
                exp_[sens].append(xsec*float(tmp['0.500']))
            except KeyError:
                print "Result not found for"

a_mass      = array('d',mass)
a_obs       = array('d',obs)
a_obsUp     = array('d',obsUp)
a_obsDown   = array('d',obsDown)
a_exp       = array('d',exp) 
a_exp1Up    = array('d',exp1Up) 
a_exp2Up    = array('d',exp2Up) 
a_exp1Down  = array('d',exp1Down) 
a_exp2Down  = array('d',exp2Down) 
a_zeros     = array('d',zeros)
a_xsecs     = array('d',xsecs)

a_exp_ = {}
expM_ = {}

for i, sens in enumerate(sensitivityStudies):
    if i > 0:
        a_exp_[sens]      = array('d',exp_[sens]) 
        expM_[sens]        = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_exp_[sens], a_zeros, a_zeros, a_zeros, a_zeros)
        expM_[sens].SetLineWidth(2)
        expM_[sens].SetLineStyle(2)
        if i == 3: # avoid yellow
            expM_[sens].SetLineColor(7)
        else:
            expM_[sens].SetLineColor(i+2)

exp2Sigma   = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_exp, a_zeros, a_zeros, a_exp2Down, a_exp2Up)
exp1Sigma   = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_exp, a_zeros, a_zeros, a_exp1Down, a_exp1Up)
expM        = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_exp, a_zeros, a_zeros, a_zeros, a_zeros)
obs         = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_obs, a_zeros, a_zeros, a_zeros, a_zeros)
obs1Sigma   = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_obs, a_zeros, a_zeros, a_obsDown, a_obsUp)
xsecs       = ROOT.TGraphAsymmErrors(len(zeros), a_mass, a_xsecs, a_zeros, a_zeros, a_zeros, a_zeros)

exp2Sigma.SetFillColor(ROOT.kOrange)
exp1Sigma.SetFillColor(ROOT.kGreen+1)
obs1Sigma.SetFillStyle(3345)
obs1Sigma.SetFillColor(ROOT.kGray+2)
obs1Sigma.SetLineWidth(2)
obs1Sigma.SetMarkerSize(0)
obs1Sigma.SetFillColorAlpha(ROOT.kGray, 0.5)

expM.SetLineWidth(2)
expM.SetLineStyle(2)
obs.SetLineWidth(2)
xsecs.SetLineWidth(2)
#xsecs.SetLineColor(ROOT.kRed+1)
xsecs.SetLineStyle(3)

can = ROOT.TCanvas("can","",700,700)
can.SetLogy()
if args.scan == 'mPhi' and False:
    can.SetLogx()

mg = ROOT.TMultiGraph()
mg.SetTitle("Exclusion graphs")
mg.Add(exp2Sigma)
mg.Add(exp1Sigma)
mg.Add(obs1Sigma)
y_max = 500
y_min = 0.05
if mChi == 10:
    y_max = 5000
    y_min = 0.2
elif mChi == 50:
    y_max = 50000
    y_min = 0.2
mg.SetMaximum(y_max)
mg.SetMinimum(y_min)
mg.Draw("a3 same")
if args.scan == 'mPhi':
    if tp == 'scalar': tp_ = 'm_{#phi}'
    elif tp == 'pseudoscalar': tp_ = 'm_{a}'
elif args.scan == 'TChiWZ':
    tp_ = '#Deltam(#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}, #tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}})'
else:
    tp_ = 'm_{#chi}'
mg.GetXaxis().SetTitle(tp_+" [GeV]")
mg.GetYaxis().SetTitle("95% CL upper limit #sigma/#sigma_{theory}")
min_x = min(filteredResults[sensitivityStudies[0]][scanVar].tolist()) if not args.scan == 'mPhi' else 35
mg.GetXaxis().SetRangeUser(min_x,max(filteredResults[sensitivityStudies[0]][scanVar].tolist()))

xsecs.Draw("l same")
expM.Draw("l same")
for i,sens in enumerate(sensitivityStudies):
    if i > 0:
        expM_[sens].Draw("l same")
if not args.blinded: obs.Draw("l same")
leg_size = 0.04 * 4


leg = ROOT.TLegend(0.185,0.79-leg_size,0.5,0.79)
leg.SetBorderSize(1)
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.SetTextSize(0.03)

if args.year == 2016:
    lumi    = 35.9
elif args.year == 2017:
    lumi    = 41.5
elif args.year == 2018:
    lumi    = 59.7
else:
    lumi = 137

lumiStr = "#bf{(%s fb^{-1})}"

#leg.AddEntry(obs,"#bf{Observed}",'l')
#leg.AddEntry(obs1Sigma,"#bf{Observed #pm theory uncertainty}")
leg.AddEntry(expM,"#bf{Median expected} " + lumiStr%lumi,'l')
leg.AddEntry(exp1Sigma,"#bf{68% expected} " + lumiStr%lumi,'f')
leg.AddEntry(exp2Sigma,"#bf{95% expected} " + lumiStr%lumi,'f')
for i, sens in enumerate(sensitivityStudies):
    if i > 0:
        if args.year == 2018 and "scaled4p3" in sens: lumi = 260 # 2018 + Run 3
        leg.AddEntry(expM_[sens],"#bf{Median expected %i} "%i + lumiStr%lumi,'l')
leg.Draw()

none = ROOT.TH1F()

#if tp == 'scalar': tp_ = 'Scalar mediator'
#elif tp == 'pseudoscalar': tp_ = 'Pseudoscalar mediator'

tp = "TChiWZ"
tp_ = tp

#extraText = ""
extraText = "Private Work"

latex2 = ROOT.TLatex()
latex2.SetNDC()
latex2.SetTextSize(0.03)
latex2.SetTextAlign(11) # align right
if args.scan == 'mChi' and args.spin == 'scalar':
    latex2.DrawLatex(0.20,0.89,'#bf{'+tp_+', Dirac DM, m_{#phi} = '+str(fixedMass)+' GeV}')
elif args.scan == 'mChi' and args.spin == 'pseudoscalar':
    latex2.DrawLatex(0.20,0.89,'#bf{'+tp_+', Dirac DM, m_{a} = '+str(fixedMass)+' GeV}')
elif args.scan == 'TChiWZ':
    latex2.DrawLatex(0.20,0.89,'#bf{#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}#tilde{#chi}_{#lower[-0.3]{2}}^{#lower[0.4]{0}} #rightarrow WZ#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}}#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{0}}}')
else:
    latex2.DrawLatex(0.20,0.89,'#bf{'+tp_+', Dirac DM, m_{#chi} = '+str(fixedMass)+' GeV}')

if args.scan == 'TChiWZ':
    latex2.DrawLatex(0.20,0.85,'#bf{m_{#tilde{#chi}_{#lower[-0.3]{1}}^{#lower[0.4]{#pm}}} = m_{#tilde{#chi}_{#lower[-0.3]{2}}^{#lower[0.4]{0}}} = %s GeV}'%fixedMass)
else: 
    latex2.DrawLatex(0.20,0.85,'#bf{g_{q} = 1, g_{DM} = 1}')
    

latex2.DrawLatex(0.20,0.80,'#bf{95% CL upper limits}')
#latex2.DrawLatex(0.22,0.84,'#bf{m_{#chi} = '+str(mChi)+' GeV, g_{q} = 1, g_{#chi} = 1}')

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11) # align right
latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
latex1.DrawLatex(0.8,0.96,"#bf{13 TeV}")
#latex1.DrawLatex(0.71,0.96,"#bf{137 fb^{-1} (13 TeV)}")

can.RedrawAxis()

from StopsCompressed.samples.default_locations import default_locations
samples_tag = default_locations.mc_2018_postProcessing_directory.split("/")[0]

plot_dir = os.path.join(plot_directory, samples_tag, 'limits', yearString, args.scan, 'brazil')
#plot_dir = os.path.join(plot_directory,args.plot_directory)

if not os.path.isdir(plot_dir):
    os.makedirs(plot_dir)

if not args.blinded:
    plot_dir += '/brazil_%s_scan_%s%s'%(tp, args.scan, suffix)
else:
    plot_dir += '/brazil_%s_scan_%s%s_blinded'%(tp, scanVar, suffix)

filetypes = [".pdf",".png",".root"]

for f in filetypes:
    can.Print(plot_dir+f)
