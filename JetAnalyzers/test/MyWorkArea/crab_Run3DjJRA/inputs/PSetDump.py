import FWCore.ParameterSet.Config as cms

process = cms.Process("JRA")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/group/phys_heavyions/ec/lcunquei/Run3PbPbDijets_full_reco_justAOD/name/230831_161549/0000/step3_RAW2DIGI_L1Reco_RECO_352.root')
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.untracked.bool(True),
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.ak2CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak2GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak2PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak2caloJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak2caloGenPtEta"),
    srcRec = cms.InputTag("ak2caloPtEta")
)


process.ak2caloJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak2caloPtEtaUncor"),
    srcRec = cms.InputTag("ak2caloPtEta")
)


process.ak2pfJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak2pfGenPtEta"),
    srcRec = cms.InputTag("ak2pfPtEta")
)


process.ak2pfJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak2pfPtEtaUncor"),
    srcRec = cms.InputTag("ak2pfPtEta")
)


process.ak3CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak3GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak3PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak3caloJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak3caloGenPtEta"),
    srcRec = cms.InputTag("ak3caloPtEta")
)


process.ak3caloJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak3caloPtEtaUncor"),
    srcRec = cms.InputTag("ak3caloPtEta")
)


process.ak3pfJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak3pfGenPtEta"),
    srcRec = cms.InputTag("ak3pfPtEta")
)


process.ak3pfJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak3pfPtEtaUncor"),
    srcRec = cms.InputTag("ak3pfPtEta")
)


process.ak4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4caloJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4caloGenPtEta"),
    srcRec = cms.InputTag("ak4caloPtEta")
)


process.ak4caloJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4caloPtEtaUncor"),
    srcRec = cms.InputTag("ak4caloPtEta")
)


process.ak4pfJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfGenPtEta"),
    srcRec = cms.InputTag("ak4pfPtEta")
)


process.ak4pfJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfPtEtaUncor"),
    srcRec = cms.InputTag("ak4pfPtEta")
)


process.ak5CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak5GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak5PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak5caloJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak5caloGenPtEta"),
    srcRec = cms.InputTag("ak5caloPtEta")
)


process.ak5caloJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak5caloPtEtaUncor"),
    srcRec = cms.InputTag("ak5caloPtEta")
)


process.ak5pfJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak5pfGenPtEta"),
    srcRec = cms.InputTag("ak5pfPtEta")
)


process.ak5pfJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak5pfPtEtaUncor"),
    srcRec = cms.InputTag("ak5pfPtEta")
)


process.ak6CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak6GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak6caloJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak6caloGenPtEta"),
    srcRec = cms.InputTag("ak6caloPtEta")
)


process.ak6caloJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak6caloPtEtaUncor"),
    srcRec = cms.InputTag("ak6caloPtEta")
)


process.ak6pfJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak6pfGenPtEta"),
    srcRec = cms.InputTag("ak6pfPtEta")
)


process.ak6pfJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak6pfPtEtaUncor"),
    srcRec = cms.InputTag("ak6pfPtEta")
)


process.genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    excludeResonances = cms.bool(False),
    ignoreParticleIDs = cms.vuint32(
        1000022, 1000012, 1000014, 1000016, 2000012,
        2000014, 2000016, 1000039, 5100039, 4000012,
        4000014, 4000016, 9900012, 9900014, 9900016,
        39, 12, 14, 16
    ),
    partonicFinalState = cms.bool(False),
    src = cms.InputTag("genParticles"),
    tausAsJets = cms.bool(False)
)


process.kt6PFJetsRhos = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME")
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(2),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.primaryVertexAssociation = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.uint32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("particleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("offlinePrimaryVertices")
)


process.primaryVertexAssociationJME = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(2.4),
        NumOfPUVtxsForCharged = cms.uint32(2),
        OnlyUseFirstDz = cms.bool(True),
        PtMaxCharged = cms.double(20.0),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(10000000000.0),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.3),
        maxDzSigForPrimaryAssignment = cms.double(10000000000.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("particleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("goodOfflinePrimaryVertices")
)


process.ak2caloGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak2GenJetsNoNu")
)


process.ak2caloPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak2CaloJets")
)


process.ak2caloPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak2CaloJets")
)


process.ak2pfGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak2GenJetsNoNu")
)


process.ak2pfPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak2PFJets")
)


process.ak2pfPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak2PFJets")
)


process.ak3caloGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak3GenJetsNoNu")
)


process.ak3caloPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak3CaloJets")
)


process.ak3caloPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak3CaloJets")
)


process.ak3pfGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak3GenJetsNoNu")
)


process.ak3pfPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak3PFJets")
)


process.ak3pfPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak3PFJets")
)


process.ak4caloGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4GenJetsNoNu")
)


process.ak4caloPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4caloPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4pfGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4GenJetsNoNu")
)


process.ak4pfPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4PFJets")
)


process.ak4pfPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4PFJets")
)


process.ak5caloGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak5GenJetsNoNu")
)


process.ak5caloPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak5CaloJets")
)


process.ak5caloPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak5CaloJets")
)


process.ak5pfGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak5GenJetsNoNu")
)


process.ak5pfPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak5PFJets")
)


process.ak5pfPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak5PFJets")
)


process.ak6caloGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak6GenJetsNoNu")
)


process.ak6caloPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak6CaloJets")
)


process.ak6caloPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak6CaloJets")
)


process.ak6pfGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak6GenJetsNoNu")
)


process.ak6pfPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak6PFJets")
)


process.ak6pfPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak6PFJets")
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.ak2calo = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak2caloJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak2caloGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak2caloJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak2pf = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak2pfJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcRef = cms.InputTag("ak2pfGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak2pfJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak3calo = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak3caloJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak3caloGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak3caloJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak3pf = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak3pfJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcRef = cms.InputTag("ak3pfGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak3pfJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak4calo = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak4caloJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak4caloGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak4caloJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak4pf = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak4pfJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcRef = cms.InputTag("ak4pfGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak4pfJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak5calo = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak5caloJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak5caloGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak5caloJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak5pf = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak5pfJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcRef = cms.InputTag("ak5pfGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak5pfJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak6calo = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak6caloJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak6caloGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak6caloJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.ak6pf = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.2),
    deltaRPartonMax = cms.double(0.4),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("genParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak6pfJetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcRef = cms.InputTag("ak6pfGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak6pfJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlinePrimaryVertices")
)


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(100)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(False),
    fileName = cms.string('JRA.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'CASTOR',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerHardcodeGeometryEP = cms.ESProducer("CaloTowerHardcodeGeometryEP")


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorHardcodeGeometryEP = cms.ESProducer("CastorHardcodeGeometryEP")


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(True),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryEP = cms.ESProducer("EcalBarrelGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryEP = cms.ESProducer("EcalEndcapGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryEP = cms.ESProducer("EcalPreshowerGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalHardcodeGeometryEP = cms.ESProducer("HcalHardcodeGeometryEP",
    UseOldLoader = cms.bool(False)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcHardcodeGeometryEP = cms.ESProducer("ZdcHardcodeGeometryEP")


process.caloSimulationParameters = cms.ESProducer("CaloSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.ecalSimulationParametersEB = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEB')
)


process.ecalSimulationParametersEE = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEE')
)


process.ecalSimulationParametersES = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsES')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalParameters = cms.ESProducer("HcalParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.hcalSimulationConstants = cms.ESProducer("HcalSimulationConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalSimulationParameters = cms.ESProducer("HcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(True),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(True)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityLabel = cms.string(''),
    siPixelQualityLabel_RawToDigi = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(True)
)


process.trackerNumberingGeometry = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(True)
)


process.trackerParameters = cms.ESProducer("TrackerParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('125X_mcRun3_2022_realistic_v3'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring( (
        'Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/normal/cmsextent.xml',
        'Geometry/CMSCommonData/data/cms.xml',
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/cmsTracker.xml',
        'Geometry/CMSCommonData/data/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/CMSCommonData/data/muonBase.xml',
        'Geometry/CMSCommonData/data/cmsMuon.xml',
        'Geometry/CMSCommonData/data/mgnt.xml',
        'Geometry/CMSCommonData/data/beampipe.xml',
        'Geometry/CMSCommonData/data/cmsBeam.xml',
        'Geometry/CMSCommonData/data/muonMB.xml',
        'Geometry/CMSCommonData/data/muonMagnet.xml',
        'Geometry/TrackerCommonData/data/trackerParameters.xml',
        'Geometry/TrackerCommonData/data/pixfwdMaterials.xml',
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
        'Geometry/TrackerCommonData/data/pixfwdPlaq.xml',
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x2.xml',
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x5.xml',
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x3.xml',
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x4.xml',
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x5.xml',
        'Geometry/TrackerCommonData/data/pixfwdPanelBase.xml',
        'Geometry/TrackerCommonData/data/pixfwdPanel.xml',
        'Geometry/TrackerCommonData/data/pixfwdBlade.xml',
        'Geometry/TrackerCommonData/data/pixfwdNipple.xml',
        'Geometry/TrackerCommonData/data/pixfwdDisk.xml',
        'Geometry/TrackerCommonData/data/pixfwdCylinder.xml',
        'Geometry/TrackerCommonData/data/pixfwd.xml',
        'Geometry/TrackerCommonData/data/pixbarmaterial.xml',
        'Geometry/TrackerCommonData/data/pixbarladder.xml',
        'Geometry/TrackerCommonData/data/pixbarladderfull.xml',
        'Geometry/TrackerCommonData/data/pixbarladderhalf.xml',
        'Geometry/TrackerCommonData/data/pixbarlayer.xml',
        'Geometry/TrackerCommonData/data/pixbarlayer0.xml',
        'Geometry/TrackerCommonData/data/pixbarlayer1.xml',
        'Geometry/TrackerCommonData/data/pixbarlayer2.xml',
        'Geometry/TrackerCommonData/data/pixbar.xml',
        'Geometry/TrackerCommonData/data/tibtidcommonmaterial.xml',
        'Geometry/TrackerCommonData/data/tibmaterial.xml',
        'Geometry/TrackerCommonData/data/tibmodpar.xml',
        'Geometry/TrackerCommonData/data/tibmodule0.xml',
        'Geometry/TrackerCommonData/data/tibmodule0a.xml',
        'Geometry/TrackerCommonData/data/tibmodule0b.xml',
        'Geometry/TrackerCommonData/data/tibmodule2.xml',
        'Geometry/TrackerCommonData/data/tibstringpar.xml',
        'Geometry/TrackerCommonData/data/tibstring0ll.xml',
        'Geometry/TrackerCommonData/data/tibstring0lr.xml',
        'Geometry/TrackerCommonData/data/tibstring0ul.xml',
        'Geometry/TrackerCommonData/data/tibstring0ur.xml',
        'Geometry/TrackerCommonData/data/tibstring0.xml',
        'Geometry/TrackerCommonData/data/tibstring1ll.xml',
        'Geometry/TrackerCommonData/data/tibstring1lr.xml',
        'Geometry/TrackerCommonData/data/tibstring1ul.xml',
        'Geometry/TrackerCommonData/data/tibstring1ur.xml',
        'Geometry/TrackerCommonData/data/tibstring1.xml',
        'Geometry/TrackerCommonData/data/tibstring2ll.xml',
        'Geometry/TrackerCommonData/data/tibstring2lr.xml',
        'Geometry/TrackerCommonData/data/tibstring2ul.xml',
        'Geometry/TrackerCommonData/data/tibstring2ur.xml',
        'Geometry/TrackerCommonData/data/tibstring2.xml',
        'Geometry/TrackerCommonData/data/tibstring3ll.xml',
        'Geometry/TrackerCommonData/data/tibstring3lr.xml',
        'Geometry/TrackerCommonData/data/tibstring3ul.xml',
        'Geometry/TrackerCommonData/data/tibstring3ur.xml',
        'Geometry/TrackerCommonData/data/tibstring3.xml',
        'Geometry/TrackerCommonData/data/tiblayerpar.xml',
        'Geometry/TrackerCommonData/data/tiblayer0.xml',
        'Geometry/TrackerCommonData/data/tiblayer1.xml',
        'Geometry/TrackerCommonData/data/tiblayer2.xml',
        'Geometry/TrackerCommonData/data/tiblayer3.xml',
        'Geometry/TrackerCommonData/data/tib.xml',
        'Geometry/TrackerCommonData/data/tidmaterial.xml',
        'Geometry/TrackerCommonData/data/tidmodpar.xml',
        'Geometry/TrackerCommonData/data/tidmodule0.xml',
        'Geometry/TrackerCommonData/data/tidmodule0r.xml',
        'Geometry/TrackerCommonData/data/tidmodule0l.xml',
        'Geometry/TrackerCommonData/data/tidmodule1.xml',
        'Geometry/TrackerCommonData/data/tidmodule1r.xml',
        'Geometry/TrackerCommonData/data/tidmodule1l.xml',
        'Geometry/TrackerCommonData/data/tidmodule2.xml',
        'Geometry/TrackerCommonData/data/tidringpar.xml',
        'Geometry/TrackerCommonData/data/tidring0.xml',
        'Geometry/TrackerCommonData/data/tidring0f.xml',
        'Geometry/TrackerCommonData/data/tidring0b.xml',
        'Geometry/TrackerCommonData/data/tidring1.xml',
        'Geometry/TrackerCommonData/data/tidring1f.xml',
        'Geometry/TrackerCommonData/data/tidring1b.xml',
        'Geometry/TrackerCommonData/data/tidring2.xml',
        'Geometry/TrackerCommonData/data/tid.xml',
        'Geometry/TrackerCommonData/data/tidf.xml',
        'Geometry/TrackerCommonData/data/tidb.xml',
        'Geometry/TrackerCommonData/data/tibtidservices.xml',
        'Geometry/TrackerCommonData/data/tibtidservicesf.xml',
        'Geometry/TrackerCommonData/data/tibtidservicesb.xml',
        'Geometry/TrackerCommonData/data/tobmaterial.xml',
        'Geometry/TrackerCommonData/data/tobmodpar.xml',
        'Geometry/TrackerCommonData/data/tobmodule0.xml',
        'Geometry/TrackerCommonData/data/tobmodule2.xml',
        'Geometry/TrackerCommonData/data/tobmodule4.xml',
        'Geometry/TrackerCommonData/data/tobrodpar.xml',
        'Geometry/TrackerCommonData/data/tobrod0c.xml',
        'Geometry/TrackerCommonData/data/tobrod0l.xml',
        'Geometry/TrackerCommonData/data/tobrod0h.xml',
        'Geometry/TrackerCommonData/data/tobrod0.xml',
        'Geometry/TrackerCommonData/data/tobrod1l.xml',
        'Geometry/TrackerCommonData/data/tobrod1h.xml',
        'Geometry/TrackerCommonData/data/tobrod1.xml',
        'Geometry/TrackerCommonData/data/tobrod2c.xml',
        'Geometry/TrackerCommonData/data/tobrod2l.xml',
        'Geometry/TrackerCommonData/data/tobrod2h.xml',
        'Geometry/TrackerCommonData/data/tobrod2.xml',
        'Geometry/TrackerCommonData/data/tobrod3l.xml',
        'Geometry/TrackerCommonData/data/tobrod3h.xml',
        'Geometry/TrackerCommonData/data/tobrod3.xml',
        'Geometry/TrackerCommonData/data/tobrod4c.xml',
        'Geometry/TrackerCommonData/data/tobrod4l.xml',
        'Geometry/TrackerCommonData/data/tobrod4h.xml',
        'Geometry/TrackerCommonData/data/tobrod4.xml',
        'Geometry/TrackerCommonData/data/tobrod5l.xml',
        'Geometry/TrackerCommonData/data/tobrod5h.xml',
        'Geometry/TrackerCommonData/data/tobrod5.xml',
        'Geometry/TrackerCommonData/data/tob.xml',
        'Geometry/TrackerCommonData/data/tecmaterial.xml',
        'Geometry/TrackerCommonData/data/tecmodpar.xml',
        'Geometry/TrackerCommonData/data/tecmodule0.xml',
        'Geometry/TrackerCommonData/data/tecmodule0r.xml',
        'Geometry/TrackerCommonData/data/tecmodule0s.xml',
        'Geometry/TrackerCommonData/data/tecmodule1.xml',
        'Geometry/TrackerCommonData/data/tecmodule1r.xml',
        'Geometry/TrackerCommonData/data/tecmodule1s.xml',
        'Geometry/TrackerCommonData/data/tecmodule2.xml',
        'Geometry/TrackerCommonData/data/tecmodule3.xml',
        'Geometry/TrackerCommonData/data/tecmodule4.xml',
        'Geometry/TrackerCommonData/data/tecmodule4r.xml',
        'Geometry/TrackerCommonData/data/tecmodule4s.xml',
        'Geometry/TrackerCommonData/data/tecmodule5.xml',
        'Geometry/TrackerCommonData/data/tecmodule6.xml',
        'Geometry/TrackerCommonData/data/tecpetpar.xml',
        'Geometry/TrackerCommonData/data/tecring0.xml',
        'Geometry/TrackerCommonData/data/tecring1.xml',
        'Geometry/TrackerCommonData/data/tecring2.xml',
        'Geometry/TrackerCommonData/data/tecring3.xml',
        'Geometry/TrackerCommonData/data/tecring4.xml',
        'Geometry/TrackerCommonData/data/tecring5.xml',
        'Geometry/TrackerCommonData/data/tecring6.xml',
        'Geometry/TrackerCommonData/data/tecring0f.xml',
        'Geometry/TrackerCommonData/data/tecring1f.xml',
        'Geometry/TrackerCommonData/data/tecring2f.xml',
        'Geometry/TrackerCommonData/data/tecring3f.xml',
        'Geometry/TrackerCommonData/data/tecring4f.xml',
        'Geometry/TrackerCommonData/data/tecring5f.xml',
        'Geometry/TrackerCommonData/data/tecring6f.xml',
        'Geometry/TrackerCommonData/data/tecring0b.xml',
        'Geometry/TrackerCommonData/data/tecring1b.xml',
        'Geometry/TrackerCommonData/data/tecring2b.xml',
        'Geometry/TrackerCommonData/data/tecring3b.xml',
        'Geometry/TrackerCommonData/data/tecring4b.xml',
        'Geometry/TrackerCommonData/data/tecring5b.xml',
        'Geometry/TrackerCommonData/data/tecring6b.xml',
        'Geometry/TrackerCommonData/data/tecpetalf.xml',
        'Geometry/TrackerCommonData/data/tecpetalb.xml',
        'Geometry/TrackerCommonData/data/tecpetal0.xml',
        'Geometry/TrackerCommonData/data/tecpetal0f.xml',
        'Geometry/TrackerCommonData/data/tecpetal0b.xml',
        'Geometry/TrackerCommonData/data/tecpetal3.xml',
        'Geometry/TrackerCommonData/data/tecpetal3f.xml',
        'Geometry/TrackerCommonData/data/tecpetal3b.xml',
        'Geometry/TrackerCommonData/data/tecpetal6f.xml',
        'Geometry/TrackerCommonData/data/tecpetal6b.xml',
        'Geometry/TrackerCommonData/data/tecpetal8f.xml',
        'Geometry/TrackerCommonData/data/tecpetal8b.xml',
        'Geometry/TrackerCommonData/data/tecwheel.xml',
        'Geometry/TrackerCommonData/data/tecwheela.xml',
        'Geometry/TrackerCommonData/data/tecwheelb.xml',
        'Geometry/TrackerCommonData/data/tecwheelc.xml',
        'Geometry/TrackerCommonData/data/tecwheeld.xml',
        'Geometry/TrackerCommonData/data/tecwheel6.xml',
        'Geometry/TrackerCommonData/data/tecservices.xml',
        'Geometry/TrackerCommonData/data/tecbackplate.xml',
        'Geometry/TrackerCommonData/data/tec.xml',
        'Geometry/TrackerCommonData/data/trackermaterial.xml',
        'Geometry/TrackerCommonData/data/tracker.xml',
        'Geometry/TrackerCommonData/data/trackerpixbar.xml',
        'Geometry/TrackerCommonData/data/trackerpixfwd.xml',
        'Geometry/TrackerCommonData/data/trackertibtidservices.xml',
        'Geometry/TrackerCommonData/data/trackertib.xml',
        'Geometry/TrackerCommonData/data/trackertid.xml',
        'Geometry/TrackerCommonData/data/trackertob.xml',
        'Geometry/TrackerCommonData/data/trackertec.xml',
        'Geometry/TrackerCommonData/data/trackerbulkhead.xml',
        'Geometry/TrackerCommonData/data/trackerother.xml',
        'Geometry/EcalCommonData/data/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebcon.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/eefixed.xml',
        'Geometry/EcalCommonData/data/eehier.xml',
        'Geometry/EcalCommonData/data/eealgo.xml',
        'Geometry/EcalCommonData/data/escon.xml',
        'Geometry/EcalCommonData/data/esalgo.xml',
        'Geometry/EcalCommonData/data/eeF.xml',
        'Geometry/EcalCommonData/data/eeB.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/hcalalgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/hcalendcapalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/HcalCommonData/data/hcalSimNumbering.xml',
        'Geometry/HcalCommonData/data/hcalRecNumbering.xml',
        'Geometry/MuonCommonData/data/mbCommon.xml',
        'Geometry/MuonCommonData/data/mb1.xml',
        'Geometry/MuonCommonData/data/mb2.xml',
        'Geometry/MuonCommonData/data/mb3.xml',
        'Geometry/MuonCommonData/data/mb4.xml',
        'Geometry/MuonCommonData/data/muonYoke.xml',
        'Geometry/MuonCommonData/data/mf.xml',
        'Geometry/ForwardCommonData/data/forward.xml',
        'Geometry/ForwardCommonData/data/bundle/forwardshield.xml',
        'Geometry/ForwardCommonData/data/brmrotations.xml',
        'Geometry/ForwardCommonData/data/brm.xml',
        'Geometry/ForwardCommonData/data/totemMaterials.xml',
        'Geometry/ForwardCommonData/data/totemRotations.xml',
        'Geometry/ForwardCommonData/data/totemt1.xml',
        'Geometry/ForwardCommonData/data/totemt2.xml',
        'Geometry/ForwardCommonData/data/ionpump.xml',
        'Geometry/MuonCommonData/data/muonNumbering.xml',
        'Geometry/TrackerCommonData/data/trackerStructureTopology.xml',
        'Geometry/TrackerSimData/data/trackersens.xml',
        'Geometry/TrackerRecoData/data/trackerRecoMaterial.xml',
        'Geometry/EcalSimData/data/ecalsens.xml',
        'Geometry/HcalCommonData/data/hcalsenspmf.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HcalSimData/data/CaloUtil.xml',
        'Geometry/MuonSimData/data/muonSens.xml',
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
        'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml',
        'Geometry/ForwardCommonData/data/brmsens.xml',
        'Geometry/HcalSimData/data/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/EcalSimData/data/ESProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        'Geometry/MuonSimData/data/muonProdCuts.xml',
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml'
     ) ),
    rootNodeName = cms.string('cms:OCMS')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.ak2pfSequence = cms.Sequence(process.kt6PFJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak2PFJets+process.ak2GenJetsNoNu+process.ak2pfGenPtEta+process.ak2pfPtEta+process.ak2pfPtEtaUncor))+process.ak2pfJetToRef)+process.ak2pfJetToUncorJet)+process.ak2pf)


process.ak2caloSequence = cms.Sequence(((((process.genParticlesForJetsNoNu+(process.ak2CaloJets+process.ak2GenJetsNoNu+process.ak2caloGenPtEta+process.ak2caloPtEta+process.ak2caloPtEtaUncor))+process.ak2caloJetToRef)+process.ak2caloJetToUncorJet)+process.ak2calo))


process.ak3pfSequence = cms.Sequence(process.kt6PFJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak3PFJets+process.ak3GenJetsNoNu+process.ak3pfGenPtEta+process.ak3pfPtEta+process.ak3pfPtEtaUncor))+process.ak3pfJetToRef)+process.ak3pfJetToUncorJet)+process.ak3pf)


process.ak3caloSequence = cms.Sequence(((((process.genParticlesForJetsNoNu+(process.ak3CaloJets+process.ak3GenJetsNoNu+process.ak3caloGenPtEta+process.ak3caloPtEta+process.ak3caloPtEtaUncor))+process.ak3caloJetToRef)+process.ak3caloJetToUncorJet)+process.ak3calo))


process.ak4pfSequence = cms.Sequence(process.kt6PFJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak4PFJets+process.ak4GenJetsNoNu+process.ak4pfGenPtEta+process.ak4pfPtEta+process.ak4pfPtEtaUncor))+process.ak4pfJetToRef)+process.ak4pfJetToUncorJet)+process.ak4pf)


process.ak4caloSequence = cms.Sequence(((((process.genParticlesForJetsNoNu+(process.ak4CaloJets+process.ak4GenJetsNoNu+process.ak4caloGenPtEta+process.ak4caloPtEta+process.ak4caloPtEtaUncor))+process.ak4caloJetToRef)+process.ak4caloJetToUncorJet)+process.ak4calo))


process.ak5pfSequence = cms.Sequence(process.kt6PFJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak5PFJets+process.ak5GenJetsNoNu+process.ak5pfGenPtEta+process.ak5pfPtEta+process.ak5pfPtEtaUncor))+process.ak5pfJetToRef)+process.ak5pfJetToUncorJet)+process.ak5pf)


process.ak5caloSequence = cms.Sequence(((((process.genParticlesForJetsNoNu+(process.ak5CaloJets+process.ak5GenJetsNoNu+process.ak5caloGenPtEta+process.ak5caloPtEta+process.ak5caloPtEtaUncor))+process.ak5caloJetToRef)+process.ak5caloJetToUncorJet)+process.ak5calo))


process.ak6pfSequence = cms.Sequence(((process.kt6PFJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak6PFJets+process.ak6GenJetsNoNu+process.ak6pfGenPtEta+process.ak6pfPtEta+process.ak6pfPtEtaUncor))+process.ak6pfJetToRef)+process.ak6pfJetToUncorJet))+process.ak6pf))


process.ak6caloSequence = cms.Sequence(((((process.genParticlesForJetsNoNu+(process.ak6CaloJets+process.ak6GenJetsNoNu+process.ak6caloGenPtEta+process.ak6caloPtEta+process.ak6caloPtEtaUncor))+process.ak6caloJetToRef)+process.ak6caloJetToUncorJet)+process.ak6calo))


process.ak2pfPath = cms.Path(process.ak2pfSequence)


process.ak2caloPath = cms.Path(process.ak2caloSequence)


process.ak3pfPath = cms.Path(process.ak3pfSequence)


process.ak3caloPath = cms.Path(process.ak3caloSequence)


process.ak4pfPath = cms.Path(process.ak4pfSequence)


process.ak4caloPath = cms.Path(process.ak4caloSequence)


process.ak5pfPath = cms.Path(process.ak5pfSequence)


process.ak5caloPath = cms.Path(process.ak5caloSequence)


process.ak6pfPath = cms.Path(process.ak6pfSequence)


process.ak6caloPath = cms.Path(process.ak6caloSequence)


