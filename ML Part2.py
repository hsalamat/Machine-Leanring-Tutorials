# Go to Kaggle.com and download Video Game sales.\
# This has a dataset for 16500 video games
# Check out courses in https://www.kaggle.com/learn/overview
# pip install pandas
# Segment2: working with pandas data frame

import pandas as pd

df = pd.read_csv('vgsales.csv')

print(df)

# Get the number of rows and columns
print(df.shape)

# Get count, min, max, standard deviation
print(df.describe())

# Get the nested array of data
print(df.values)

