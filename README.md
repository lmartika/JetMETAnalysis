# JetMETAnalysis
This is an updated version of the code to run on CMSSW_13
Usage:
cmsrel CMSSW_13_2_0_pre1
cd src
cmsenv
git clone git@github.com:lcunquei/JetMETAnalysis.git

Inside JetAnalyzers/test there is a macro run_JRA_cfg.py to create the JRA files from the AOD input. Currently the framework only works with input AODs. I am working on a version valid for miniAODS.  
