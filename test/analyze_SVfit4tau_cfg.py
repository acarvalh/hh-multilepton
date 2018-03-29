import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(''),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('analyze_SVfit4tau.root')
)

process.analyze_SVfit4tau = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string('HH'),

    histogramDir = cms.string('SVfit4tau'),

    era = cms.string('2016'),

    leptonSelection = cms.string('Tight'),

    hadTauSelection = cms.string('Tight|dR03mvaMedium'),

    SVfit4tau_logM_wMassConstraint = cms.double(0.),
    SVfit4tau_logM_woMassConstraint = cms.double(0.),

    use_HIP_mitigation_mediumMuonId = cms.bool(False),

    isMC = cms.bool(True),
    central_or_shift = cms.string('central'),
    lumiScale = cms.double(1.),
    apply_genWeight = cms.bool(True),

    fillGenEvtHistograms = cms.bool(False),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_memOutput = cms.string(''),

    branchName_genLeptons1 = cms.string('GenLep'),
    branchName_genLeptons2 = cms.string(''),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genJets = cms.string('GenJet'),
    redoGenMatching = cms.bool(True),

    branchName_genTaus = cms.string('GenTau'),
    branchName_genHiggsBosons = cms.string('GenHiggsBosons'), # CV: use 'GenHiggsBoson' in CMSSW_8_0_x, 'GenHiggs' in  CMSSW_9_4_x

    selEventsFileName_input = cms.string(''),
)
