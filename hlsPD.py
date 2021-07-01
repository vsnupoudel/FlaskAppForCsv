import pandas as pd
import  numpy as np

class HLSpd():
  def __init__(self, csvInput):
    self.df = pd.read_csv(csvInput)
      
  def print_stats_numeric(self):
      return self.df.describe(include= np.number).transpose().to_json()
      
  def print_stats_object(self):
      return self.df.describe(include= np.object).transpose().to_json()