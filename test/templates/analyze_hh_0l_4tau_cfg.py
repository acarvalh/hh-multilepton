import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.analyze_hh_0l_4tau = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    triggers_2tau = cms.vstring(),
    use_triggers_2tau = cms.bool(False),

    lep_mva_cut = cms.double(1.),

    hadTauSelection = cms.string(''),
    hadTauChargeSelection = cms.string(''),
    apply_hadTauGenMatching = cms.bool(False),

    applyFakeRateWeights = cms.string(""),
    hadTauFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        lead = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        ),
        sublead = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        ),
        third = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        ),
        fourth = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        )
    ),
    triggerSF_2tau = cms.PSet(),

    isMC = cms.bool(False),
    central_or_shift = cms.string(''),
    lumiScale = cms.double(1.),
    apply_genWeight = cms.bool(True),
    apply_hlt_filter = cms.bool(False),
    apply_met_filters = cms.bool(True),
    cfgMEtFilter = cms.PSet(),

    fillGenEvtHistograms = cms.bool(False),
    cfgEvtYieldHistManager = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_trigObjs = cms.string('TrigObj'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genJets = cms.string('GenJet'),
    redoGenMatching = cms.bool(True),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),

    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),

    evtWeight = cms.PSet(
        apply = cms.bool(False),
        histogramFile = cms.string(''),
        histogramName = cms.string(''),
        branchNameXaxis = cms.string(''),
        branchNameYaxis = cms.string(''),
        branchTypeXaxis = cms.string(''),
        branchTypeYaxis = cms.string(''),
    ),
)
