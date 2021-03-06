from hhAnalysis.multilepton.samples.tthAnalyzeSamples_2017_preselected import samples_2017 as samples_2017_general
from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017_hh_private_preselected import samples_2017 as samples_2017_hh_private

import collections
import itertools

del samples_2017_hh_private['sum_events']
samples_2017 = collections.OrderedDict(itertools.chain(
  samples_2017_general.items(), samples_2017_hh_private.items()
))

from collections import OrderedDict as OD

for sample_name, sample_info in samples_2017.items():

  if not isinstance(sample_info, OD):
    continue

  if sample_info["process_name_specific"].startswith('signal') and 'hh' in sample_info["process_name_specific"]:
    sample_info["use_it"] = True

  if sample_name.startswith('/ZZ'):
    sample_info["sample_category"] = "ZZ"
  elif sample_name.startswith('/WZ'):
    sample_info["sample_category"] = "WZ"
  elif sample_name.startswith('/WW'):
    sample_info["sample_category"] = "WW"
  elif sample_name.startswith('/DY') and sample_name.find('JetsToLL') < 10:
    sample_info["sample_category"] = "DY"
  elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') < 10:
    sample_info["sample_category"] = "W"
  elif sample_name.startswith('/ttH'):
    sample_info["sample_category"] = "TTH"

  if sample_info["sample_category"] == "Rares":
    sample_info["sample_category"] = "Other"
  if sample_info["sample_category"] in [ "tHq", "tHW" ]:
    sample_info["sample_category"] = "TH"
