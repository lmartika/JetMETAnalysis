import FWCore.ParameterSet.Config as cms

#!
#! PROCESS
#!
# Conditions source options: GT, SQLite, DB
conditionsSource = "GT"
era = "Spring16_25nsV1_MC"
doProducer = False
process = cms.Process("JRA")
multithread = False
if doProducer:
    process = cms.Process("JRAP")
    multithread = True


#!
#! CHOOSE ALGORITHMS
#!
# Note: Not all combinations of options will work
# Algorithm options: ak, kt, ic, sc, ca
# Size options: integers 1-10
# Jet type options: calo, pf, pfchs, puppi
# Correction levels: '' (blank), l1, l2, l3, l2l3, l1l2l3
algsizetype = {'ak':[2,3,4,5,6]}
jettype = ['pf']
corrs = ['']

algorithms = []
jcr = cms.VPSet()

for k, v in algsizetype.items():
    for s in v:
        for j in jettype:
            for c in corrs:
                algorithms.append(str(k+str(s)+j+c))
                if conditionsSource != "GT":
                    upperAlg = str(k.upper()+str(s)+j.upper().replace("CHS","chs")).replace("PUPPI","PFPuppi")
                    jcr.append(cms.PSet(record = cms.string("JetCorrectionsRecord"),
                        tag = cms.string("JetCorrectorParametersCollection_"+era+"_"+upperAlg),
                        label= cms.untracked.string(upperAlg)))

# If need be you can append additional jet collections using the style below
#algorithms.append('ak5calo')


#!
#! CONDITIONS (DELIVERING JEC BY DEFAULT!)
#!
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('125X_mcRun3_2022_realistic_v3')

if conditionsSource != "GT":
    if conditionsSource == "DB":
        conditionsConnect = cms.string("frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS")
    elif conditionsSource == "SQLite":
        conditionsConnect = cms.string('sqlite_file:'+era+'.db')

    from CondCore.DBCommon.CondDBSetup_cfi import *
    process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
                   connect = conditionsConnect,
                   toGet =  cms.VPSet(jcr))
    process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")


#!
#! INPUT
#!
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

##############################################
# External Input File (most likely from DAS) #
##############################################
try:
    process.load("JetMETAnalysis.JetAnalyzers.<filename without extension>")
except ImportError:
    print("Couldn't open the external list of files from DAS. If you just checkout out the JetResponseAnalyzer package you will need to make this file yourself. Currently Falling back to opening the list hard-coded in run_JRA_cfg.py. This is not a bad action as long as it is what you intended to have happen.")
#    inputFiles = cms.untracked.vstring(
#            '/store/user/katatar/run3/run3_pbpb22_privateMC_QCDDijet15_pythia8_RECO//CRAB_UserFiles//crab_run3_pbpb22_privateMC_QCDDijet15_pythia8_RECO_userInput//220820_220735/0000//step3_RECO_1.root'
#        )
#    process.source = cms.Source("PoolSource", fileNames = inputFiles )

    inputFiles = cms.untracked.vstring(
#            '/store/group/phys_heavyions/ec/lcunquei/Run3PbPbDijets_full_reco_justAOD/name/230831_161549/0000/step3_RAW2DIGI_L1Reco_RECO_352.root',
        '/store/mc/RunIIIpp5p36Winter24MiniAOD/QCD_pThat-15to1200_TuneCP5_5p36TeV_pythia8/MINIAODSIM/NoPU_FEVTDEBUGHLT_forTracking_141X_mcRun3_2024_realistic_ppRef5TeV_v7-v4/2810000/19e4be36-d724-4a20-a7b6-043e314e4a0b.root'
            )
    process.source = cms.Source("PoolSource", fileNames = inputFiles )



#!
#! SERVICES
#!
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))
if doProducer:
    process.add_(cms.Service("Tracer"))
    process.options.numberOfThreads = cms.untracked.uint32(8)
    process.options.numberOfStreams = cms.untracked.uint32(0)
else:
    process.load('CommonTools.UtilAlgos.TFileService_cfi')
    process.TFileService.fileName=cms.string('JRA.root')


#!
#! NEEDED FOR PFCHS
#!
process.load('CommonTools.ParticleFlow.pfNoPileUpJME_cff')
process.pfPileUpJME.checkClosestZVertex = False


#!
#! JET & REFERENCE KINEMATIC CUTS
#!
import JetMETAnalysis.JetAnalyzers.Defaults_cff as Defaults


#!
#! RUN JET RESPONSE ANALYZER
#!

# set to False to use jets from the input file (NOT RECOMMENDED)
doJetReco = True
outCom = cms.untracked.vstring('drop *')
from JetMETAnalysis.JetAnalyzers.addAlgorithm import addAlgorithm
for algorithm in algorithms:
    if (algorithm.find('HLT') > 0) :
        process.load("Configuration.Geometry.GeometryIdeal_cff")
        process.load("Configuration.StandardSequences.MagneticField_cff")
        addAlgorithm(process,algorithm,Defaults,False,doProducer)
    else:
        addAlgorithm(process,algorithm,Defaults,doJetReco,doProducer)
    outCom.extend(['keep *_'+algorithm+'_*_*'])


#process.ak2PFJets.src = cms.InputTag("packedPFCandidates") 
#process.kt6PFJetsRhos.src = cms.InputTag("packedPFCandidates") 
#process.ak2GenJetsNoNu.src = cms.InputTag("packedGenParticles")
#process.genParticlesForJetsNoNu.src = cms.InputTag("packedGenParticles")


#process.ak2pf.srcGenParticles = cms.InputTag("packedGenParticles")
#process.ak2pf.srcPFCandidates = cms.InputTag("packedPFCandidates")


#!
#! Check the keep and drop commands being added to the outputCommamnds
#!
printOC = False
if printOC:
    for oc in outCom:
        print(oc)


#!
#! Output
#!
if doProducer:
    process.out = cms.OutputModule("PoolOutputModule",
                   fileName = cms.untracked.string('JRAP.root'),
                   outputCommands = outCom
                   )
    process.e = cms.EndPath(process.out)


#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!

#Not sure what this does
#processDumpFile = open('runJRA.dump' , 'w')
#print >> processDumpFile, process.dumpPython()
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)
