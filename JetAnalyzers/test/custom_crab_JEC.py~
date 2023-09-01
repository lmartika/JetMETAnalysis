from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName = 'Run3DjJRA'
config.General.workArea = 'MyWorkArea'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'run_JRA_cfg.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.inputFiles = ['']
config.JobType.maxMemoryMB = 5000
config.section_("Data")
config.Data.userInputFiles = open('/afs/cern.ch/user/l/lcunquei/Run3/CMSSW_13_2_0_pre1/src/JetMETAnalysis/JetAnalyzers/test/inputfiles.txt').readlines();
config.Data.outputPrimaryDataset = 'Run3PbPbDijets_JRA'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = 'name'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/ec/lcunquei/'
config.Data.ignoreLocality = False

config.section_("Site")

config.Site.storageSite = 'T2_CH_CERN'
