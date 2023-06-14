# This script is using Shiller's Stock Market data 1871-present w/CAPE ratio
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# load chapt26copy.xlsx, keep original for reference materials in sheets
noninflated_df = pd.read_excel('chapt26copy.xlsx')

# Extract the year values from the first column
years = noninflated_df.iloc[:, 0]

# Convert the years column to a datetime format
noninflated_df['Year'] = pd.to_datetime(years, format='%Y')

# Set the 'Year' column as the index
noninflated_df.set_index('Year', inplace=True)

# Remove the original years column
noninflated_df.drop(columns=noninflated_df.columns[0], inplace=True)

# Check df
print(noninflated_df.head())

