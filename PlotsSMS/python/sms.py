from array import *

class sms():

    def __init__(self, modelname):
        if modelname.find("T1tttt")   != -1: self.T1tttt()
        if modelname.find("T1bbbb")   != -1: self.T1bbbb()
        if modelname.find("T1qqqq")   != -1: self.T1qqqq()
        if modelname.find("T2tt")     != -1: self.T2tt()
        if modelname.find("T2bW")     != -1: self.T2bW()
        if modelname.find("T2bt")     != -1: self.T2bt()
        if modelname.find("T2deg_dm") != -1: self.T2deg_dm()
        if modelname.find("TChiWZ_dm")   != -1: self.TChiWZ_dm()
        if modelname.find("T8bbllnunu_XCha0p5_XSlep0p05") != -1: self.T8bbllnunu_XCha0p5_XSlep0p05()
        if modelname.find("T8bbllnunu_XCha0p5_XSlep0p09") != -1: self.T8bbllnunu_XCha0p5_XSlep0p09()
        if modelname.find("T8bbllnunu_XCha0p5_XSlep0p5") != -1: self.T8bbllnunu_XCha0p5_XSlep0p5()
        if modelname.find("T8bbllnunu_XCha0p5_XSlep0p95") != -1: self.T8bbllnunu_XCha0p5_XSlep0p95()


    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 700.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1600.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b f f' #tilde{#chi}^{0}_{1}";
        # scan range to plot
        #changes wrt degStop1l
        self.Xmin = 250.
        self.Xmax = 1000.
        self.Ymin = 0.
        self.Ymax = 900.
        self.Zmin = 0.1
        self.Zmax = 100.
        #produce sparticle
        self.sParticle = "m_{#tilde{t}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{0}^{1}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False
        #mW = 80
        #self.diagX = array('d',[0,20000])
        #self.diagY = array('d',[-mW, 20000-mW])

        # T2tt stops 2l
        # decay chain
        #self.label= "pp #rightarrow #tilde{t}_{1} #bar{#tilde{t}}_{1}, #tilde{t}_{1} #rightarrow t #tilde{#chi}^{0}_{1}";
        #self.Xmin = 150.
        #self.Xmax = 1200.
        #self.Ymin = 0.
        #self.Ymax = 800.
        #self.Zmin = 0.001
        #self.Zmax = 100.
        # produce sparticle
        #self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        #self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        #self.diagOn = False
    def T2deg_dm(self):
        # model name
        self.modelname = "T2deg_dm"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b f f' #tilde{#chi}^{0}_{1}";
        # scan range to plot
        #changes wrt degStop1l dm plot
        self.Xmin = 250.
        self.Xmax = 800.
        self.Ymin = 10.
        self.Ymax = 107.
        self.Zmin = 0.1
        self.Zmax = 100.
        #produce sparticle
        self.sParticle = "m_{#tilde{t}} (GeV)"
        # LSP
        self.LSP = "#Deltam(#tilde{t},#tilde{#chi}^{0}_{1}) [GeV]" 
        # turn off diagonal lines
        self.diagOn = False
    
    def TChiWZ_dm(self):
        # model name
        self.modelname = "TChiWZ_dm"
        # decay chain
        self.label= "pp #rightarrow #tilde{#chi}^{#pm}_{1} #tilde{#chi}^{0}_{2} #rightarrow W Z #tilde{#chi}^{0}_{1} #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 250.
        self.Xmax = 800.
        self.Ymin = 0.
        self.Ymax = 107.
        self.Zmin = 0.1
        self.Zmax = 100.
        #produce sparticle
        self.sParticle = "m_{#tilde{#chi}^{#pm}_{1}} = m_{#tilde{#chi}^{0}_{2}} (GeV)"
        # LSP
        self.LSP = "#Deltam(#tilde{#chi}^{#pm}_{1}, #tilde{#chi}^{0}_{1}) [GeV]" 
        # turn off diagonal lines
        self.diagOn = False

    def T2bW(self):
        # model name
        self.modelname = "T2bW"
        # decay chain
        self.label= "pp #rightarrow #tilde{t}_{1} #bar{#tilde{t}}_{1}, #tilde{t}_{1} #rightarrow b#tilde{#chi}^{+}_{1} #rightarrow bW^{+}#tilde{#chi}^{0}_{1}";
        self.mSlep = "m_{#tilde{#chi}^{#pm}_{1}} = 0.5 (m_{#tilde{t}_{1}} + m_{#tilde{#chi}^{0}_{1}})" #use mSlep since it's drawn on top
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1000.
        self.Ymin = 1.
        self.Ymax = 700.
        self.Zmin = 0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T2bt(self):
        # model name
        self.modelname = "T2bt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t}_{1} #tilde{t}_{1}, #tilde{t}_{1} #rightarrow b#tilde{#chi}^{#pm}_{1} #rightarrow #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 150.
        self.Xmax = 1200.
        self.Ymin = 0.
        self.Ymax = 800.
        self.Zmin = 0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T8bbllnunu_XCha0p5_XSlep0p05(self):
        # model name
        self.modelname = "T8bbllnunu_XCha0p5_XSlep0p05"
        # decay chain
        #self.label = ROOT.TMathText("pp \ell")
        self.label= "pp  #rightarrow #tilde{t}_{1} #bar{#tilde{t}}_{1}, #tilde{t}_{1} #rightarrow b #nu l #tilde{#chi}^{0}_{1}";
        self.mCha = "m_{#tilde{#chi}^{#pm}_{1}} = 0.5 (m_{#tilde{t}_{1}} + m_{#tilde{#chi}^{0}_{1}})"
        self.mSlep = "m_{#tilde{l}} = 0.05 (m_{#tilde{#chi}^{#pm}_{1}} - m_{#tilde{#chi}^{0}_{1}}) + m_{#tilde{#chi}^{0}_{1}}"
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1400.
        self.Ymin = 1.
        self.Ymax = 450.
        self.Zmin = 0.0001
        self.Zmax = 500.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T8bbllnunu_XCha0p5_XSlep0p09(self):
        # model name
        self.modelname = "T8bbllnunu_XCha0p5_XSlep0p09"
        # decay chain
        #self.label = ROOT.TMathText("pp \ell")
        self.label= "pp  #rightarrow #tilde{t}_{1} #bar{#tilde{t}}_{1}, #tilde{t}_{1} #rightarrow b #nu l #tilde{#chi}^{0}_{1}";
        self.mCha = "m_{#tilde{#chi}^{#pm}_{1}} = 0.5 (m_{#tilde{t}_{1}} + m_{#tilde{#chi}^{0}_{1}})"
        self.mSlep = "m_{#tilde{l}} = 0.09 (m_{#tilde{#chi}^{#pm}_{1}} - m_{#tilde{#chi}^{0}_{1}}) + m_{#tilde{#chi}^{0}_{1}}"
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1400.
        self.Ymin = 1.
        self.Ymax = 450.
        self.Zmin = 0.0001
        self.Zmax = 500.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T8bbllnunu_XCha0p5_XSlep0p5(self):
        # model name
        self.modelname = "T8bbllnunu_XCha0p5_XSlep0p5"
        # decay chain
        #self.label = ROOT.TMathText("pp \ell")
        self.label= "pp  #rightarrow #tilde{t}_{1} #bar{#tilde{t}}_{1}, #tilde{t}_{1} #rightarrow b #nu l #tilde{#chi}^{0}_{1}";
        self.mCha = "m_{#tilde{#chi}^{#pm}_{1}} = 0.5 (m_{#tilde{t}_{1}} + m_{#tilde{#chi}^{0}_{1}})"
        self.mSlep = "m_{#tilde{l}} = 0.5 (m_{#tilde{#chi}^{#pm}_{1}} - m_{#tilde{#chi}^{0}_{1}}) + m_{#tilde{#chi}^{0}_{1}}"
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1400.
        self.Ymin = 1.
        self.Ymax = 1250.
        self.Zmin = 0.0001
        self.Zmax = 500.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False

    def T8bbllnunu_XCha0p5_XSlep0p95(self):
        # model name
        self.modelname = "T8bbllnunu_XCha0p5_XSlep0p95"
        # decay chain
        #self.label = ROOT.TMathText("pp \ell")
        self.label= "pp  #rightarrow #tilde{t}_{1} #bar{#tilde{t}}_{1}, #tilde{t}_{1} #rightarrow b #nu l #tilde{#chi}^{0}_{1}";
        self.mCha = "m_{#tilde{#chi}^{#pm}_{1}} = 0.5 (m_{#tilde{t}_{1}} + m_{#tilde{#chi}^{0}_{1}})"
        self.mSlep = "m_{#tilde{l}} = 0.95 (m_{#tilde{#chi}^{#pm}_{1}} - m_{#tilde{#chi}^{0}_{1}}) + m_{#tilde{#chi}^{0}_{1}}"
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1400.
        self.Ymin = 1.
        self.Ymax = 1350.
        self.Zmin = 0.0001
        self.Zmax = 500.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}_{1}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} (GeV)"
        # turn off diagonal lines
        self.diagOn = False
