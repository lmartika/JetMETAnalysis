#!/bin/sh

source Setup_FileLocation.sh

#hadd -k -f /tmp/chenyi/output_ak4pfchs.root $Step2bOutput/Result_*root
#cp /tmp/chenyi/output_ak4pfchs.root $Step2bOutput/

#mkdir -p SynchPlotStep2Closure
#mkdir -p SynchPlotStep2b

hadd -k -f $Step2OutputClosure/output_ak10pfchs.root $Step2OutputClosure/Result_*root

jet_synchplot_x \
   -inputDir $Step2OutputClosure \
   -algo1 ak10pfchs \
   -algo2 ak10pfchs \
   -outDir `pwd`/SynchPlotStep2Closure \
   -outputFormat .png \
   -fixedRange true \
   -tdr true \
   -npvRhoNpuBinWidth 2 \
   -NBinsNpvRhoNpu 5

#jet_synchplot_x \
#   -inputDir $Step2bOutput \
#   -algo1 ak4pfchs \
#   -algo2 ak4pfchs \
#   -outDir `pwd`/SynchPlotStep2b \
#   -outputFormat .png \
#   -fixedRange true \
#   -tdr true \
#   -npvRhoNpuBinWidth 10 \
#   -NBinsNpvRhoNpu 6

#tar zcvf SynchPlot.tar.gz SynchPlotStep2/ SynchPlotStep2b/
#cp SynchPlot.tar.gz ~/public/html/

