import tensorflow_data_validation as tfdv

class HLStf():
  def __init__( self, csvInput):
    self.csvInput = csvInput
    self.gen_stats = None

  def generate_HLstats_json(self):
    self.gen_stats=  tfdv.generate_statistics_from_csv(data_location= self.csvInput)
    return self.gen_stats

  def visualize_HLstats(self):
    return tfdv.visualize_statistics(self.gen_stats)