import FWCore.ParameterSet.Config as cms

process = cms.Process("testevtloop")
process.load("FWCore.MessageService.MessageLogger_cfi")

import FWCore.Framework.test.cmsExceptionsFatalOption_cff
process.options = cms.untracked.PSet(
  wantSummary = cms.untracked.bool(True),
  Rethrow = FWCore.Framework.test.cmsExceptionsFatalOption_cff.Rethrow
)
process.maxLuminosityBlocks=cms.untracked.PSet(
    input=cms.untracked.int32(-1)
)

process.source= cms.Source("PoolSource",
              processingMode=cms.untracked.string('RunsAndLumis'),
              fileNames=cms.untracked.vstring(
    'file:/afs/cern.ch/user/s/sukulkar/work/sukulkar/public/T2tt_displaced_200_180_5.root',
    ),
             )

process.efficiency = cms.EDAnalyzer("testEvtLoop", 
            genFilterInfoTag = cms.InputTag("genFilterEfficiencyProducer"))

process.p1 = cms.Path( process.efficiency )
