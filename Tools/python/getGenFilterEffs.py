import os, sys
import ROOT
import multiprocessing
import argparse
import pickle

from DataFormats.FWLite import Events, Handle, Lumis
#import DataFormats.FWLite as FWLite


argParser = argparse.ArgumentParser(description = "Input options")
argParser.add_argument('--year',       action='store',                     type=int, default=2018,                               help="Which year?" )
argParser.add_argument('--sample',     action='store',                     type=str, default='T2tt_dM-10to80',                   help="List of samples" )
options = argParser.parse_args()

if options.year == 2018:
    from Samples.miniAOD.Autumn18_miniAOD_signals import allSamples as mcSamples
    allSamples = mcSamples
else:
    raise NotImplementedError

for s in allSamples:
    if s.name == options.sample:
        sample = s

output_dir = "./genFilterEffs/" + options.sample

if not os.path.isdir(output_dir):
    os.makedirs(output_dir)


fileList_ = sample.files

badFiles = [
]

fileList = [x for x in fileList_ if x not in badFiles]

f = fileList

# Handles to get event products
genLumiInfoHandle = Handle("<GenLumiInfoHeader>")
genFilterInfoHandle = Handle("<GenFilterInfo>")

events =  Events(f)
lumis  =  Lumis(f)

genFilterEffs_ = {}
genFilterEffs = {}

events.toBegin()

for iLumi,lumi in enumerate(lumis): # GenFilterInfo stored in LuminosityBlocks
    # model information
    lumi.getByLabel("generator", genLumiInfoHandle)
    genLumiInfo = genLumiInfoHandle.product()
    model = genLumiInfo.configDescription()

    if iLumi%100 == 0: print iLumi, model

    # generator filter information
    lumi.getByLabel("genFilterEfficiencyProducer", genFilterInfoHandle)
    genFilterInfo = genFilterInfoHandle.product()
    genFilterEff = genFilterInfo.filterEfficiency()

    if model in genFilterEffs_:
        #if genFilterEffs[model] != genFilterEff: print "GenFilterEff not same across model %s: %s vs %s"%(model, genFilterEffs[model], genFilterEff)
        #assert genFilterEffs[model] == genFilterEff # check that filter efficiency is the same across files # NOTE: minor differences
        pass
    else:
        genFilterEffs_[model] = genFilterEff # NOTE: choosing first instance # FIXME: add all numEventsPassed and numEventsTotal and divide

for model in genFilterEffs_:
    signalName = model.split("_")[0]
    mass1 = int(model.split("_")[1])
    mass2 = int(model.split("_")[2])
    
    if mass1 not in genFilterEffs: 
        genFilterEffs[mass1] = {}

    genFilterEffs[mass1][mass2] = genFilterEffs_[model]

print "Extracted generator filter efficiencies:", genFilterEffs

filename = "genFilterEffs_%s"%options.sample  
pickle.dump(genFilterEffs, open(output_dir +"/%s.pkl"%filename,"w"))

print "Exported generator filter efficiencies to:", output_dir +"/%s.pkl"%filename 
