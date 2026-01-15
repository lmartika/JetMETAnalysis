# JetMETAnalysis
This is an updated version of the code to run on CMSSW_13 or newer, using miniAOD inputs
Usage:
cmsrel CMSSW_13_2_0_pre1
cd src
cmsenv
git clone git@github.com:lamartik/JetMETAnalysis.git

Inside JetAnalyzers/test there is a macro run_JRA_cfg.py to create the JRA files from the mAOD input. Calo jets do not work properly at the moment.
