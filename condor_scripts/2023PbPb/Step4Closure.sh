#!/bin/sh --login

#BSUB -q 1nh

WorkDir=$1
File=$2
Output=$3
ID=$4

source $WorkDir/Setup_CMSSW.sh

cp $WorkDir/Files/*txt .
#cp $WorkDir/Files/My*PileupHistogram.root .

echo Input files are: $File

#hadd -k -f Input.root `echo $File | tr ':' ' '`
hadd -k -f Input.root `echo $File | tr ':' ' '`

jet_correction_analyzer_x \
   -inputFilename Input.root \
   -outputDir ./ \
   -path ./ \
   -era Stdplusgaus-weights-bigHF \
   -levels 2 \
   -useweight false \
   -algs ak4pf \
   -drmax 0.2 \
   -evtmax 0 \
   -nbinsrelrsp 60 \
   -relrspmin 0.0 \
   -relrspmax 3.0 \
   -nrefmax 3

cp Closure_ak4pf.root ${Output}/Closure_ak4pf${ID}.root

rm *.root
