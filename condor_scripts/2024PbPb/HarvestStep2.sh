#!/bin/sh

source Setup_FileLocation.sh

hadd -k -f $Step2Output/output_ak3pfchs.root $Step2Output/Result_ak3_*root

jet_synchfit_x \
   -inputDir  $Step2Output/ \
   -outputDir `pwd`/Files/ \
   -algo1 ak3pfchs \
   -algo2 ak3pfchs \
   -highPU false \
   -useNPU false \
   -functionType ak4 \
   -era ParallelMCPreDeriveL1




# was standard
