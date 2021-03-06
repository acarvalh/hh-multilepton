import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
)

scaleSignal = 50

process.makePlots = cms.PSet(
    pluginType = cms.string("Plotter_HH"),

    applyRebinning = cms.bool(True),
    apply_fixed_rebinning = cms.int32(2),
    apply_automatic_rebinning = cms.bool(True),
    minEvents_automatic_rebinning = cms.double(0.5),
    applyAutoBlinding = cms.bool(True),
    divideByBinWidth = cms.bool(True),
    processData = cms.string("data_obs"),
    processesBackground = cms.vstring(),
    processSignal = cms.string("signal_spin0_400_hh"),
    scaleSignal = cms.double(scaleSignal),
    legendEntrySignal = cms.string("%dx GGF#rightarrow X(400;spin0)#rightarrow HH#rightarrow 4W,2W2#tau,4#tau" % scaleSignal),
    categories = cms.VPSet(),
    distributions = cms.VPSet(
        cms.PSet(
            histogramName = cms.string("sel/evt/$PROCESS/numJets"),
            xAxisTitle = cms.string("jet Multiplicity"),
            yAxisTitle = cms.string("Events")
        ),
        cms.PSet(
            histogramName = cms.string("sel/evt/$PROCESS/numElectrons"),
            xAxisTitle = cms.string("electron Multiplicity"),
            yAxisTitle = cms.string("Events")
        ),
       cms.PSet(
            histogramName = cms.string("sel/evt/$PROCESS/numMuons"),
            xAxisTitle = cms.string("muon Multiplicity"),
            yAxisTitle = cms.string("Events")
        ),
        cms.PSet(
            histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
            xAxisTitle = cms.string("Run Period"),
            yAxisTitle = cms.string("Events / 1 fb^{-1}")
        ),
        cms.PSet(
            histogramName = cms.string('sel/evt/$PROCESS/HT'),
            xAxisTitle = cms.string('H_{T} [GeV]'),
            yAxisTitle = cms.string('dN/dH_{T} [1/GeV]')
        ),
        cms.PSet(
            histogramName = cms.string('sel/evt/$PROCESS/STMET'),
            xAxisTitle = cms.string('S_{T}^{MET} [GeV]'),
            yAxisTitle = cms.string('dN/dS_{T}^{MET} [1/GeV]')
        ),
    ),

    nuisanceParameters = cms.PSet(
        normalization = cms.PSet(
            TTH = cms.string("1.0 +/- 0.20"),
            TH = cms.string("1.0 +/- 0.20"),
            TT = cms.string("1.0 +/- 0.20"),
            TTW = cms.string("1.0 +/- 0.20"),
            TTWW = cms.string("1.0 +/- 0.20"),
            TTZ = cms.string("1.0 +/- 0.20"),
            Other = cms.string("1.0 +/- 0.20"),
            VH = cms.string("1.0 +/- 0.20"),
            WW = cms.string("1.0 +/- 0.20"),
            ZZ = cms.string("1.0 +/- 0.20"),
            WZ = cms.string("1.0 +/- 0.20"),
            DY = cms.string("1.0 +/- 0.20"),
            W = cms.string("1.0 +/- 0.20"),
            fakes_data = cms.string("1.0 +/- 0.20"),
            flips_data = cms.string("1.0 +/- 0.20"),
            conversions = cms.string("1.0 +/- 0.20"),
            signal_spin0_400_hh = cms.string("1.0 +/- 0.20"),
        ),
        shape = cms.PSet(
            CMS_ttHl_btag_HF = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_HFStats1 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_HFStats2 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_LF = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_LFStats1 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_LFStats2 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_cErr1 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_cErr2 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_JES = cms.string("0.00 +/- 1.00"),
        )
    ),
    showUncertainty = cms.bool(False),

    labelOnTop = cms.string(
        ("CMS Preliminary; %dx GGF#rightarrow X(400;spin0)#rightarrow HH#rightarrow " % scaleSignal) +
        "4W,2W2#tau,4#tau; %1.1f fb^{-1} at #sqrt{s} = 13 TeV"),
    intLumiData = cms.double(0.), # in units of fb^-1

    outputFileName = cms.string("")
)
