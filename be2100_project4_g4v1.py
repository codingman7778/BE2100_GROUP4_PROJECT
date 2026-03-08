import numpy as np
import pandas as pd
import os
import csv
import operator
import matplotlib.pyplot as plt
import seaborn as sns
from github import Github
import scipy
import sklearn
import ssl
import certifi


#initialization and importation of ai4i2020.csv from repo as pandas dataframe 
g = Github()
repo_path = "codingman7778/BE2100_GROUP4_PROJECT" 
repo = g.get_repo(repo_path)

print(f"repository name: {repo.name}")

ai4i2020_csv_url = "https://raw.githubusercontent.com/codingman7778/BE2100_GROUP4_PROJECT/refs/heads/main/ai4i2020.csv"
df = pd.read_csv(ai4i2020_csv_url)
print("csv loaded.")
print("rows, columns:", df.shape)
print(df.head())

#replace blank str w/missing vals; 
df = df.replace(r'^\s*$', pd.NA, regex=True)
#remove columns that are completely empty
df = df.dropna(axis=1, how='all')

#print first 5 rows of cleaned dataframe
print("rows, columns:", df.shape)
print(df.head())


#....operations 
