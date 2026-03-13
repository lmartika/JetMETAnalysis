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

cp $WorkDir/Files/ParallelMCPreDeriveL1_L1FastJet_AK10PFchs.txt L1FJ.txt

echo Current directory content
ls
echo

jet_synchtest_x \
   -basepath '//' \
   -samplePU `pwd`/PUFile.root \
   -sampleNoPU `pwd`/NoPUFile.root \
   -algo1 ak10pfchs \
   -algo2 ak10pfchs \
   -iftest false \
   -maxEvts 20000000 \
   -ApplyJEC true \
   -JECpar `pwd`/L1FJ.txt\
   -outputPath `pwd`/ \
   -npvRhoNpuBinWidth 2 \
   -NBinsNpvRhoNpu 5 \
   -useweight true \
   -nrefmax 3 \
   -doNotSave false #\
#   -reduceHistograms false

mv output_ak10pfchs.root ${Output}/Result_${ID}.root

rm *.root
