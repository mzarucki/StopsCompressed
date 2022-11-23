#!/bin/bash

#
# Example of usage:
# submitCondor.py --execFile submit_on_lxplus.sh --queue nextweek nanoPostProcessing_Summer16_private.sh
# submitCondor.py --execFile THISFILE (setup for condor environment) --queue NAMEofCONDORQUEUE fileWithCommands.sh
#

export USER=$(whoami)
initial="$(echo $USER | head -c 1)"
export SCRAM_ARCH=slc7_amd64_gcc700

echo "---------------------"
echo "Grid certificate 1"
voms-proxy-info --all
echo "---------------------"
echo "Current dir: `pwd`"
ls -l
echo "---------------------"
export HOME=`pwd`
echo "Current home dir: ${HOME}"
echo "---------------------"

# change to afs work directory 
cd /afs/cern.ch/work/$initial/$USER
cd Sensitivity/CMSSW_10_2_22 # hard-coded for the time being
echo "---------------------"
echo "Current dir: `pwd`"
ls -l

#scram project CMSSW CMSSW_10_2_22
#eval `scramv1 runtime -sh`
## github repos
#git cms-init

#echo "---------------------"
#echo "Using hephy token: /afs/cern.ch/user/${initial}/${USER}/private/kerberos/krb5_token_hephy.at"
#export KRB5CCNAME=/afs/cern.ch/user/${initial}/${USER}/private/kerberos/krb5_token_hephy.at
#aklog -d hephy.at
#echo "---------------------"

echo "---------------------"
echo "Changing to script dir: $1"
#cd ..
cd $1
cmsenv
ls -l
echo "---------------------"

export XRD_NETWORKSTACK=IPv4 # needed for issue with xrootd redirector on lxplus to force use of IPv4 instead of IPv6

echo "Executing:"
echo ${@:2} #--runOnLxPlus
echo "---------------------"

${@:2} #--runOnLxPlus
