# This script is a data pipeline. Shiller's Stock Market data 1871-present w/CAPE ratio

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


"""
Part I
Data loading, cleaning, inspection, deconstruction and reconstruction
"""

# load chapt26.xlsx

chapt_df = pd.read_excel("chapt26copy.xlsx")
chapt_df = chapt_df.dropna()
chapt_df.head()

