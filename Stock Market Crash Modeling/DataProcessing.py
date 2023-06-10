# This script is using Shiller's Stock Market data 1871-present w/CAPE ratio

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# load chapt26copy.xlsx, keep original for reference materials in sheet

chapt_df = pd.read_excel("chapt26copy.xlsx")

# data processing, cleaning, formatting, etc.
chapt_df = chapt_df.dropna()
print(chapt_df.head(), "\n", chapt_df.tail())


