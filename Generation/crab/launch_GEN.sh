#!/bin/sh
python launch_GEN.py $@ --config  cmssw_10_2_12_patch1_fastSim --production_label first_attempt --unitsPerJob 5000 --totalUnits 1000000  --publish
