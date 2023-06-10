# This script is using Shiller's Stock Market data 1871-present w/CAPE ratio

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# load chapt26copy.xlsx, keep original for reference materials in sheet

# need to split excel data sheet in two
    # theres 2 time columns to seperate the inflation adjusted variables from the non-inflation adjusted variables
chapt_df = pd.read_excel("chapt26copy.xlsx", header=2, skiprows=7, names=None)


# data processing, cleaning, formatting, etc.
print(chapt_df.head())



