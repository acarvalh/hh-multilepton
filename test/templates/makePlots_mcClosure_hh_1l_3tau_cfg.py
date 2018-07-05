import FWCore.ParameterSet.Config as cms

import os

from tthAnalysis.HiggsToTauTau.makePlots_mcClosure_cfg import process

process.makePlots.pluginType = cms.string("Plotter_mcClosure")

process.makePlots.processesBackground = cms.vstring(
    "TT",
    "TTW",
    "TTZ",
    "EWK",
    "Rares",
    "fakes_data"
)
process.makePlots.processSignal = cms.string("signal")

process.makePlots.categories = cms.VPSet(
    cms.PSet(
        name = cms.string("1l_3tau_OS_Fakeable_mcClosure_wFakeRateWeights"),
        label = cms.string("1l+3#tau_{h}")
    )
)

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/leadHadTau/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadHadTau/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadHadTau/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading #tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadHadTau/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading #tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/thirdHadTau/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('third #tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/thirdHadTau/$PROCESS/eta'),
        xAxisTitle = cms.string('third #tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/m4Vis'),
        xAxisTitle = cms.string('m_{HH}^{vis} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/m4'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    )
])
