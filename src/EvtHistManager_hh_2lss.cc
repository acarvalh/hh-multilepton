#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_2lss::EvtHistManager_hh_2lss(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

const TH1 *
EvtHistManager_hh_2lss::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_2lss::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",          5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0.,  1500.);
  histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0.,  1500.);
  histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0.,  1500.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",  5, -2.5, +2.5);
  histogram_HT_               = book1D(dir, "HT",               "HT",              150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",           150,  0., 1500.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",      1, -0.5,  +0.5);
}

void
EvtHistManager_hh_2lss::fillHistograms(int numElectrons,
					  int numMuons,
					  int numJets,
					  int numJetsPtGt40,
					  double dihiggsVisMass,
					  double dihiggsMass_wMet,
					  double jetMass,
					  double leptonPairCharge,
					  double HT,
					  double STMET,
					  double evtWeight)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsMass_wMet_, dihiggsMass_wMet, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jetMass_,          jetMass,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_leptonPairCharge_, leptonPairCharge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
}