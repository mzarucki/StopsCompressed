from StopsCompressed.Analysis.MCBasedEstimate             import MCBasedEstimate
from StopsCompressed.Analysis.Region                      import *

class estimatorList:
    def __init__(self, setup, samples=['DY','WJets','TTLep','TTSingleLep','singleTop','VV','TTX']):
        for s in samples:
            setattr(self, s, MCBasedEstimate(name=s, sample=setup.processes[s]))
                
        
    def constructEstimatorList(self, samples):
        self.estimatorList = [ getattr(self, s) for s in samples ]
        return self.estimatorList

    def constructSampleDict(self, processDict):
        self.sampleDict = { sName:self.constructEstimatorList( samples=sList["sample"] ) for sName, sList in sampleDict.items() }
        return self.sampleDict


