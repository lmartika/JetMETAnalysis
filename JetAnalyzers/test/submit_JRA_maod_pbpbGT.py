from CRABClient.UserUtilities import config

jobTag = "JRA-MC-ppref-pbpbreco-pbpbGT-2023-maod"
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
config.Data.inputDataset = '/Pythia_5362GeV_2023_ppref_pbpbreco_pbpbGT_13_0_23_HeavyIon/lamartik-crab_MC-ppref-pbpbreco-pbpGT-2023-maod-c9079d19bfc91d3fb75f47b5aea0b469/USER'
config.Data.inputDBS = 'phys03'
config.Data.publication = False
config.Data.splitting = 'Automatic'


config.Data.outLFNDirBase ='/store/group/phys_heavyions/lamartik/' + config.General.requestName

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

print(config)
