''' Object selection for StopsCompressed Analysis
'''

# StopsCompressed
from StopsCompressed.Tools.helpers import getVarValue, getObjDict, deltaR, ptRatio

# standard imports 
from math import *
import numbers
import textwrap  # needed for CutBased Ele ID
import operator

jetVars = ['eta','pt','phi','btagDeepB', 'btagCSVV2', 'jetId', 'area', 'rawFactor', 'corr_JER']

def getJets(c, jetVars=jetVars, jetColl="Jet"):
    return [getObjDict(c, jetColl+'_', jetVars, i) for i in range(int(getVarValue(c, 'n'+jetColl)))]

def jetId(j, ptCut=30, absEtaCut=2.4, ptVar='pt', idVar='jetId', corrFactor=None):
  j_pt = j[ptVar] if not corrFactor else j[ptVar]*j[corrFactor]
  return j_pt>ptCut and abs(j['eta'])<absEtaCut and ( j[idVar] > 0 if idVar is not None else True )

def getGoodJets(c, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetColl="Jet", ptVar='pt'):
    return filter(lambda j:jetId(j, ptCut=ptCut, absEtaCut=absEtaCut, ptVar='pt'), getJets(c, jetVars, jetColl=jetColl))

def getAllJets(c, leptons, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetCollections=[ "Jet"], idVar='jetId'):

    jets = sum( [ filter(lambda j:jetId(j, ptCut=ptCut, absEtaCut=absEtaCut, idVar=idVar), getJets(c, jetVars, jetColl=coll)) for coll in jetCollections], [] )
    res  = []

    for jet in jets:
        clean = True
        for lepton in leptons:
		if deltaR(jet, lepton) < 0.4:
			if ptRatio(jet, lepton) < 2:
				clean = False
				break
        if clean:
            res.append(jet)
    res.sort( key = lambda j:-j['pt'] )

    return res

def isBJet(j, tagger = 'DeepCSV', year = 2016):
    if tagger == 'CSVv2':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagCSVV2'] > 0.8484 
        elif year == 2017 or year == 2018:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagCSVV2'] > 0.8838 
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)
    elif tagger == 'DeepCSV':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagDeepB'] > 0.6321
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagDeepB'] > 0.4941
        elif year == 2018:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
            return j['btagDeepB'] > 0.4184
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def getGenLeps(c):
    return [getObjDict(c, 'genLep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId'], i) for i in range(int(getVarValue(c, 'ngenLep')))]

def getGenParts(c):
    return [getObjDict(c, 'GenPart_', ['eta','pt','phi','charge', 'pdgId', 'motherId', 'grandmotherId'], i) for i in range(int(getVarValue(c, 'nGenPart')))]

genVars = ['eta','pt','phi','mass','charge', 'status', 'pdgId', 'genPartIdxMother', 'statusFlags','index'] 
def getGenPartsAll(c, genVars=genVars):
    return [getObjDict(c, 'GenPart_', genVars, i) for i in range(int(getVarValue(c, 'nGenPart')))]

def matchLep (recoLep):
	''' check reco leptons Flav,  0 unmatched, 1 prompt (gamma*) , 15 tau, 22 prompt photon (conv), 5 b, 4 c, 3 light/unknown,
	remember: if type is /b use ord()
	'''
	if (ord(recoLep['genPartFlav']) == 1) or (ord(recoLep['genPartFlav']) == 15):
		return True
	else: return False

def categorizeLep(recoPart, genParts, cone=0.1):
	''' get matched reco lepton with gen lepton
	'''
	#recoPart = reco particle to categorize
	#genParts = gen leptons coming from W, W from top, tau coming from W
	dR = -999
	dRcoll =[]
	for g in genParts:
		dR = deltaR(recoPart,g)	
		print "deltaR: ", dR, "gen index: ", g['index'], "reco genPartIdx: ", recoPart['genPartIdx']
		if g['index'] == recoPart['genPartIdx'] : return True, dR
		if deltaR(recoPart,g) < cone: 
			print "?"*15
			print "deltaR: ", dR
			dRcoll.append(dR)
	if dRcoll:
		return True, min(dRcoll)
	else:	
		return False, dR
		
def genLepFromZ( genParts ):
    ''' get all gen leptons (e,m,tau) from Z
    '''
    try:
        leptons = list( filter( lambda l: abs(l['pdgId']) in [11,13,15] and abs(genParts[l['genPartIdxMother']]['pdgId']) == 23, genParts ) )
    except:
        print "Found no generated leptons"
        leptons = []
    return leptons

# Run through parents in genparticles, and return list of their pdgId
def getParentIds( g, genParticles ):
    parents = []
    if g['genPartIdxMother'] >= 0:
        try:
	    # This is safer than "genParticles[ g['genPartIdxMother'] ]", as the genParticles list can be sorted first, however it requires to add "index" in the dict before sorting
	    mother1  = [ genParticle for genParticle in genParticles if genParticle["index"] == g['genPartIdxMother'] ][0]
	    parents += [ mother1['pdgId'] ] + getParentIds( mother1, genParticles )
	except:
	    # when no 'status' selection is made for g, this can run in a kind of endless-loop, then python throws an Exception
	    return parents
    return parents

def get_index_str( index ):
    if isinstance(index, int):
        index_str = "["+str(index)+"]"
    elif type(index)==type(""):
        if index.startswith('[') and index.endswith(']'):
            index_str = index
        else:
            index_str = '['+index+']'
    elif index is None:
        index_str=""
    else:
        raise ValueError( "Don't know what to do with index %r" % index )
    return index_str

def alwaysTrue(*args, **kwargs):
  return True
def alwaysFalse(*args, **kwargs):
  return False

def mergeCollections( a, b ):
    allKeys = []
    for coll in [a[0], b[0]]:
        keys = coll.keys()
        for k in keys:
            if k not in allKeys: allKeys += [k]

    merged = a + b
    for m in merged:
        for key in allKeys:
            if not m.has_key(key):
                m[key] = float('nan')

    return merged

def ECALGap(e):
    if abs(e['pdgId']) == 11: absEta = abs(e["eta"] + e["deltaEtaSC"])   # eta supercluster
    else:                     absEta = abs(e["eta"])                     # eta
    return ( absEta > 1.566 or absEta < 1.4442 )

## MUONS ##
#def muonSelector( lepton_selection, year, ptCut = 10):
def muonSelector( lepton_selection, year):
    # tigher isolation applied on analysis level
    # medium Id for sensitivity studies from l["looseId"] -> l["mediumId"]
    if lepton_selection == 'hybridIso':
        def func(l):
            if l["pt"] <= 25 and l["pt"] >3.5:
                return \
                    abs(l["eta"])       < 2.4 \
                    and (l['pfRelIso03_all']*l['pt']) < 5.0 \
                    and abs(l["dxy"])       < 0.02 \
                    and abs(l["dz"])        < 0.1 \
                    and l["looseId"] 
            elif l["pt"] > 25:
                return \
                    abs(l["eta"])       < 2.4 \
                    and l['pfRelIso03_all'] < 0.2 \
                    and abs(l["dxy"])       < 0.02 \
                    and abs(l["dz"])        < 0.1 \
                    and l["looseId"] 
                    
    elif lepton_selection == 'looseHybridIso':
        def func(l):
            if l["pt"] <= 25 and l["pt"] >3.5:
                return \
                    abs(l["eta"])       < 2.4 \
                    and (l['pfRelIso03_all']*l['pt']) < 20.0 \
                    and abs(l["dxy"])       < 0.1 \
                    and abs(l["dz"])        < 0.5 \
                    and l["looseId"] 
            elif l["pt"] > 25:
                return \
                    abs(l["eta"])       < 2.4 \
                    and l['pfRelIso03_all'] < 0.8 \
                    and abs(l["dxy"])       < 0.1 \
                    and abs(l["dz"])        < 0.5 \
                    and l["looseId"] 
    return func


## ELECTRONS ##

# Electron bitmap
# or  https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
vidNestedWPBitMapNamingList = \
    ['GsfEleMissingHitsCut',
     'GsfEleConversionVetoCut',
     'GsfEleRelPFIsoScaledCut',
     'GsfEleEInverseMinusPInverseCut',
     'GsfEleHadronicOverEMEnergyScaledCut',
     'GsfEleFull5x5SigmaIEtaIEtaCut',
     'GsfEleDPhiInCut',
     'GsfEleDEtaInSeedCut',
     'GsfEleSCEtaMultiRangeCut',
     'MinPtCut']
vidNestedWPBitMap           = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # Bitwise (Electron vidNestedWPBitMap ID flags (3 bits per cut), '000'=0 is fail, '001'=1 is veto, '010'=2 is loose, '011'=3 is medium, '100'=4 is tight)


def vidNestedWPBitMapToDict( val ):
    # convert int of vidNestedWPBitMap ( e.g. val = 611099940 ) to bitmap ( e.g. "100100011011001010010100100100")
    # split vidBitmap string (containing 3 bits per cut) in parts of 3 bits ( e.g. ["100","100","011","011","001","010","010","100","100","100"] )
    # convert 3 bits to int ( e.g. [4, 4, 3, 3, 1, 2, 2, 4, 4, 4])
    # create dictionary
    idList = [ int( x, 2 ) for x in textwrap.wrap( "{0:030b}".format( val ) , 3) ] #use 2 for nanoAOD version 80x
    return dict( zip( vidNestedWPBitMapNamingList, idList ) )

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def electronVIDSelector( l, idVal, removedCuts=[] ):

    vidDict    = vidNestedWPBitMapToDict( l['vidNestedWPBitmap'] )
    if not removedCuts:
        return all( [ cut >= idVal for cut in vidDict.values() ] )

    if ("pt"             in removedCuts):
        vidDict = removekey( vidDict, "MinPtCut" )
    if ("sieie"          in removedCuts):
        vidDict = removekey( vidDict, "GsfEleFull5x5SigmaIEtaIEtaCut" )
    if ("hoe"            in removedCuts):
        vidDict = removekey( vidDict, "GsfEleHadronicOverEMEnergyScaledCut" )
    if ("pfRelIso03_all" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleRelPFIsoScaledCut" )
    if ("SCEta" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleSCEtaMultiRangeCut" )
    if ("dEtaSeed" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleDEtaInSeedCut" )
    if ("dPhiInCut" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleDPhiInCut" )
    if ("EinvMinusPinv" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleEInverseMinusPInverseCut" )
    if ("convVeto" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleConversionVetoCut" )
    if ("lostHits" in removedCuts):
        vidDict = removekey( vidDict, "GsfEleMissingHitsCut" )

    return all( [ cut >= idVal for cut in vidDict.values() ] )


#def eleSelector( lepton_selection, year, ptCut = 10):
def eleSelector( lepton_selection, year):
    # tighter isolation applied on analysis level. cutBased corresponds to Fall17V2 ID for all 2016-2018.  # (cut-based ID Fall17 V2 (0:fail, 1:veto, 2:loose, 3:medium, 4:tight))
    # using loose Id for electrons for sensitivity studies (2:loose)
    #ECAL gap masking for 1.422 < abs(eta) < 1.566
		    #change it back, this is to verify the change in signal yields
                    ###and electronVIDSelector( l, idVal= 1, removedCuts=['pt'] ) \
                    ###and electronVIDSelector( l, idVal= 1, removedCuts=['pfRelIso03_all'] ) \
    if lepton_selection == 'hybridIso':
        def func(l):
            if l["pt"] <= 25 and l["pt"] >5:
                return \
		    abs(l["eta"]) < 2.5 \
		    and ECALGap(l) \
                    and electronVIDSelector( l, idVal= 1, removedCuts=['pfRelIso03_all'] ) \
                    and (l['pfRelIso03_all']*l['pt']) < 5.0 \
                    and abs(l["dxy"])       < 0.02 \
                    and abs(l["dz"])        < 0.1
            elif l["pt"] > 25:
                
                return \
		    abs(l["eta"]) < 2.5 \
		    and ECALGap(l) \
                    and electronVIDSelector( l, idVal= 1, removedCuts=['pfRelIso03_all'] ) \
                    and l['pfRelIso03_all'] < 0.2 \
                    and abs(l["dxy"])       < 0.02 \
                    and abs(l["dz"])        < 0.1 

    elif lepton_selection == 'looseHybridIso':
	#print "electrons for looseHybridIsolation"
        def func(l):
            if l["pt"] <= 25 and l["pt"] >5:
                return \
		    abs(l["eta"]) < 2.5 \
		    and ECALGap(l) \
                    and electronVIDSelector( l, idVal= 1 , removedCuts=['pfRelIso03_all'] ) \
                    and (l['pfRelIso03_all']*l['pt']) < 20.0 \
                    and abs(l["dxy"])       < 0.1 \
                    and abs(l["dz"])        < 0.5 
            elif l["pt"] > 25:
                return \
		    abs(l["eta"]) < 2.5 \
		    and ECALGap(l) \
                    and electronVIDSelector( l, idVal= 1 , removedCuts=['pfRelIso03_all'] ) \
                    and l['pfRelIso03_all'] < 0.8 \
                    and abs(l["dxy"])       < 0.1 \
                    and abs(l["dz"])        < 0.5 
    return func


leptonVars_data = ['pt', 'eta', 'phi', 'etaSc', 'dxy', 'dxyErr', 'dz', 'dzErr', 'looseId', 'mediumId', 'tightId', 'cutBased', 'pdgId', 'mediumMuonId', 'miniRelIso', 'relIso03', 'sip3d', 'mvaIdSpring15', 'convVeto', 'lostHits', 'jetPtRelv2', 'jetPtRatiov2', 'eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz']
leptonVars = leptonVars_data + ['mcMatchId', 'mcMatchAny', 'genPartIdx', 'genPartFlav']

electronVars_data = ['pt', 'eta', 'phi', 'pdgId', 'cutBased', 'miniPFRelIso_all', 'pfRelIso03_all', 'sip3d', 'lostHits', 'convVeto', 'dxy', 'dxyErr', 'dz', 'dzErr', 'charge', 'deltaEtaSC', 'mvaFall17V2noIso_WP80', 'vidNestedWPBitmap']
electronVars = electronVars_data + ['genPartIdx', 'genPartFlav']

muonVars_data = ['pt', 'eta', 'phi', 'pdgId', 'looseId', 'mediumId', 'tightId', 'miniPFRelIso_all', 'pfRelIso03_all', 'sip3d', 'dxy', 'dxyErr', 'dz', 'dzErr', 'charge', 'Wpt']
muonVars = muonVars_data + ['genPartIdx','genPartFlav']

def getLeptons(c, collVars=leptonVars):
    return [getObjDict(c, 'LepGood_', collVars, i) for i in range(int(getVarValue(c, 'nLepGood')))]

def getMuons(c, collVars=muonVars):
    return [getObjDict(c, 'Muon_', collVars, i) for i in range(int(getVarValue(c, 'nMuon')))]

def getElectrons(c, collVars=electronVars):
    return [getObjDict(c, 'Electron_', collVars, i) for i in range(int(getVarValue(c, 'nElectron')))]

def getGoodMuons(c, collVars=muonVars, mu_selector = alwaysFalse):
    return [l for l in getMuons(c, collVars) if mu_selector(l)]

def getGoodElectrons(c, collVars=electronVars, ele_selector = alwaysFalse):
    lep=[]
    for l in getElectrons(c, collVars):
        if ele_selector(l):
            lep.append(l)
        else:
            pass
            #print "rejeted ele: " ,l # NOTE: flooding output 
    return lep
    #return [l for l in getElectrons(c, collVars) if ele_selector(l)]

idCutBased={'loose':0 ,'medium':1, 'tight':2}
photonVars=['eta','pt','phi','mass','cutBased']
photonVarsMC = photonVars + ['mcPt']

tauVars=['eta','pt','phi','pdgId','charge', 'dxy', 'dz', 'idDecayModeNewDMs', 'idCI3hit', 'idAntiMu','idAntiE', 'idMVAnewDM2017v2','idMVAoldDM2017v2'] #idMVAnewDM2017v2 :2 =VLose
def getTaus(c, collVars=tauVars):
    return [getObjDict(c, 'Tau_', collVars, i) for i in range(int(getVarValue(c, 'nTau')))]

def looseTauID( l, ptCut=20, absEtaCut=2.3):

    #print l["idMVAnewDM2017v2"], ord(l["idMVAnewDM2017v2"])
    # use Tau_idMVAnewDM2017v2 corresponding to AN-2017 newMVA ID, VLoose
    ##and ord(l["idMVAnewDM2017v2"])>=2\
    ##and ord(l["idMVAoldDM2017v2"])>=2\
    return \
    l["pt"]>=ptCut\
    and ord(l["idMVAnewDM2017v2"])>=2\
    and abs(l["eta"])<absEtaCut\

def getGoodTaus(c, leptons, collVars=tauVars):
    #taus       = getGoodTaus(r, tau_selector = tauSelector_ )
    #return [l for l in getTaus(c,collVars=tauVars) if looseTauID(l)]
    taus =  [l for l in getTaus(c,collVars=tauVars) if looseTauID(l)]
    res  =  []
    for tau in taus:
        clean = True
        for lepton in leptons:
            if deltaR(lepton, tau) < 0.4:
                clean = False
                break
        if clean:
            res.append(tau)
    return res

#def tauSelector( tau_selection, ):
#    if tau_selection == 'loose':
#        def func(l):
#            return \
#            l["pt"]>=20\
#            and abs(l["eta"])<2.4\
#            and l["idMVAnewDM2017v2"]>=2
#    return func

#def getGoodTaus(c, collVars=tauVars, tau_selector = alwaysFalse):
#    return [l for l in getTaus(c,collVars=tauVars) if tau_selector(l)]

def getPhotons(c, collVars=None, idLevel='loose', year=2016):
    if collVars is None:
        collVars = ['eta','pt','phi','mass','cutBased'] if (not (year == 2017 or year == 2018)) else ['eta','pt','phi','mass','cutBasedBitmap']
    return [getObjDict(c, 'Photon_', collVars, i) for i in range(int(getVarValue(c, 'nPhoton')))]

def getGoodPhotons(c, ptCut=50, idLevel="loose", isData=True, collVars=None, year=2016):
    idVar = "cutBased" if (not (year == 2017 or year == 2018)) else "cutBasedBitmap"
    #if collVars is None: collVars = photonVars if isData else photonVarsMC
    collVars = ['eta','pt','phi','mass','cutBased'] if (not (year == 2017 or year == 2018)) else ['eta','pt','phi','mass','cutBasedBitmap']
    return [p for p in getPhotons(c, collVars) if p[idVar] > idCutBased[idLevel] and p['pt'] > ptCut ] # > 2 is tight for 2016, 2017 and 2018

