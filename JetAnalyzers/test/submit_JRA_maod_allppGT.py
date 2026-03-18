from CRABClient.UserUtilities import config

jobTag = "JRA-MC-ppref-pbpbreco-allppGT-2023-maod"
config = config()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = jobTag

config.section_('JobType')
config.JobType.psetName =  '/afs/cern.ch/user/l/lamartik/work/HIJEC/MCTruth2023PbPbfromMAOD/CMSSW_13_2_6/src/JetMETAnalysis/JetAnalyzers/test/run_JRA_cfg.py'
config.JobType.pluginName = 'Analysis'
#config.JobType.outputFiles = [config.General.requestName + '.root']
#config.JobType.maxMemoryMB = 4000
#config.JobType.maxMemoryMB = 4500


config.section_('Data')
# input from simulation where GT is from pp for all the steps
config.Data.inputDataset = '/Pythia_5362GeV_2023_ppref_pbpbreco_13_0_23_HeavyIon/lamartik-crab_MC-ppref-pbpbreco-allppGT-2023-step3-mAODSIM-4dba33a3747e9d42ddff2165091dbd9d/USER'
config.Data.inputDBS = 'phys03'
config.Data.publication = True
config.Data.splitting = 'Automatic'

#config.Data.unitsPerJob = 1
config.Data.outLFNDirBase ='/store/group/phys_heavyions/lamartik/' + config.General.requestName

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

print(config)
