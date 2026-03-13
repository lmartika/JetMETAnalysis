#!/bin/sh --login

#BSUB -q 1nh

WorkDir=$1
NoPUFile=$2
PUFile=$3
Output=$4
ID=$5

source $WorkDir/Setup_CMSSW.sh

if [[ $NoPUFile != *":"* ]]; then
   cp $NoPUFile NoPUFile.root
else
   hadd -f -k NoPUFile.root `echo $NoPUFile | tr ':' ' '`
fi

if [[ $PUFile != *":"* ]]; then
   cp $PUFile PUFile.root
else
   hadd -f -k PUFile.root `echo $PUFile | tr ':' ' '`
fi

# cp $WorkDir/Files/*PileupHistogram.root .

echo Current directory content
ls
echo

jet_synchtest_x \
   -basepath '//' \
   -samplePU `pwd`/PUFile.root \
   -sampleNoPU `pwd`/NoPUFile.root \
   -algo1 ak3pf \
   -algo2 ak3pf \
   -iftest false \
   -maxEvts 20000000 \
   -ApplyJEC false \
   -outputPath `pwd`/ \
   -npvRhoNpuBinWidth 2 \
   -NBinsNpvRhoNpu 5 \
   -useweight true \
   -nrefmax 3 \
   -doNotSave false #\
#   -reduceHistograms false

#mv output_ak2pfchs.root ${Output}/Result_ak2_${ID}.root
mv output_ak3pf.root ${Output}/Result_ak3pf_${ID}.root

rm *.root
