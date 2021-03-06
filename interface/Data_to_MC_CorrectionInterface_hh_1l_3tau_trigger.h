#ifndef hhAnalysis_multilepton_Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger_h
#define hhAnalysis_multilepton_Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger_h

#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_1l_2tau_trigger.h"

#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // lutWrapperBase, vLutWrapperBase

class Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger
  : public Data_to_MC_CorrectionInterface_1l_2tau_trigger
{
public:
  Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger(const edm::ParameterSet & cfg);
  ~Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger();

  //-----------------------------------------------------------------------------
  // set HLT trigger bits
  // (to be called once per event, before calling any of the getSF.. functions)
  void
  setTriggerBits(bool isTriggered_1e,
                 bool isTriggered_1e1tau,
                 bool isTriggered_1m,
                 bool isTriggered_1m1tau);// disable
  void
  setTriggerBits(bool isTriggered_1e,
                 bool isTriggered_1e1tau,
                 bool isTriggered_1m,
                 bool isTriggered_1m1tau,
                 bool isTriggered_2tau);
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // set lepton type, pT and eta as well as hadTau pT, eta and decay mode
  // (to be called once per event, before calling any of the getSF.. functions)
  void
  setLeptons(int lepton_type,
             double lepton_pt,
             double lepton_eta);

  void
  setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
             double hadTau2_pt, double hadTau2_eta, double hadTau2_phi);// disable

  void
  setHadTaus(int hadTau1_genPdgId, double hadTau1_pt, double hadTau1_eta, int hadTau1_decayMode,
             int hadTau2_genPdgId, double hadTau2_pt, double hadTau2_eta, int hadTau2_decayMode);// disable

  void
  setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
             double hadTau2_pt, double hadTau2_eta, double hadTau2_phi,
             double hadTau3_pt, double hadTau3_eta, double hadTau3_phi);

  void
  setHadTaus(int hadTau1_genPdgId, double hadTau1_pt, double hadTau1_eta, int hadTau1_decayMode,
             int hadTau2_genPdgId, double hadTau2_pt, double hadTau2_eta, int hadTau2_decayMode,
             int hadTau3_genPdgId, double hadTau3_pt, double hadTau3_eta, int hadTau3_decayMode);
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // data/MC correction for trigger efficiency 
  double
  getSF_triggerEff() const;
  //-----------------------------------------------------------------------------

private:

  // define states of single lepton trigger and of lepton leg of lepton+tau cross trigger for each reconstructed lepton
  enum
  {
    k1lAnd1l1tau,
    k1lAndNot1l1tau,
    kNot1lAnd1l1tau,
    kNot1lAndNot1l1tau
  };
    
  // define states of tau leg of lepton+tau cross trigger and of tau leg of ditau trigger for each reconstructed tau
  enum
  {
    k1l1tauAnd2tau,
    k1l1tauAndNot2tau,
    kNot1l1tauAnd2tau,
    kNot1l1tauAndNot2tau
  };

  // define auxiliary functions
  double
  getProb_lepton(int lepton_status,
                 double eff_1l,
                 double eff_1l1tau_lepLeg) const;

  double
  getProb_tau(int tau_status,
              double eff_1l1tau_tauLeg,
              double eff_2tau_tauLeg) const;

  //-----------------------------------------------------------------------------
  // data/MC corrections for trigger efficiencies in 2017 ReReco data and Summer17 MC
  std::map<int, vLutWrapperBase> effTrigger_2tau_perLeg_data_gentau_;  // key = reconstructed tau decay mode
  std::map<int, vLutWrapperBase> effTrigger_2tau_perLeg_data_faketau_; // key = reconstructed tau decay mode
  std::map<int, vLutWrapperBase> effTrigger_2tau_perLeg_mc_gentau_;    // key = reconstructed tau decay mode
  std::map<int, vLutWrapperBase> effTrigger_2tau_perLeg_mc_faketau_;   // key = reconstructed tau decay mode

  bool isTriggered_2tau_;

  int hadTau3_genPdgId_;
  double hadTau3_pt_;
  double hadTau3_eta_;
  double hadTau3_phi_;
  int hadTau3_decayMode_;
};

#endif // tthAnalysis_HiggsToTauTau_data_to_MC_corrections_hh_1l_3tau_trigger_h
