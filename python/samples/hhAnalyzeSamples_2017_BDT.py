from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017 import samples_2017

for sample_name, sample_info in samples_2017.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["process_name_specific"] in [
        "ttHToNonbb_M125_powheg",
        "TTZJets_LO",
        "TTWJets_LO",
        "TTTo2L2Nu",
        "TTTo2L2Nu_PSweights",
        "TTToSemiLeptonic",
        "TTToSemiLeptonic_PSweights",
        "TTToHadronic",
        "TTToHadronic_PSweights",
      ]:
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"].startswith("DY") and \
    sample_info["process_name_specific"] not in [
      "DYJetsToLL_M-50", "DYJetsToLL_M-50_ext1" # disable NLO samples
    ]:
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"].startswith("signal") and \
      'hh' in sample_info["process_name_specific"]:
    sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False
