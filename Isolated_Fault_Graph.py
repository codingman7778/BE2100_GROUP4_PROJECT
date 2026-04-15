import numpy as np
import pandas as pd
import os
import csv
import operator
import seaborn as sns
from github import Github
import scipy
import sklearn
import ssl
import certifi
import matplotlib

#⬇For macOS only⬇
matplotlib.use("Qt5Agg")
#⬆Delete otherwise⬆

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

#interactive mode for pyplot (usability)
plt.ion()

#Fetch CSV from repo 
try: 
    faultDB_url = "https://raw.githubusercontent.com/codingman7778/BE2100_GROUP4_PROJECT/refs/heads/main/EngineFaultDB_Final.csv"
    df = pd.read_csv(faultDB_url)
    dfN = "EngineFaultDB_Final.csv"
    print("\n")
    print("⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚")
    print(dfN)
    print("⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚\n")
    print(dfN, "has...")
    print(df.shape[0], "rows.")
    print(df.shape[1], "columns.")
    sumEnts = df.shape[0]*df.shape[1]
    print(sumEnts,"total entries.\n")
except Exception as e:
    print(f"Error fetching CSV: {e}")
    print("Closing program")
    exit()
    
columnList = df.columns.tolist()
print(dfN,"Columns Reference:") 
i=0
j=df.shape[1]
for i in range(i,j):
    print("Column",i,"=",columnList[i])
print("\n")

#form DFs of isolated fault type w/ all other variables
df_nofault = df[df['Fault'] == 0].copy()
df_type1 = df[df['Fault'] == 1].copy()
df_type2 = df[df['Fault'] == 2].copy()
df_type3 = df[df['Fault'] == 3].copy()

nf_sum = len(df_nofault)
t1_sum = len(df_type1)
t2_sum = len(df_type2)
t3_sum = len(df_type3)

print("-----------")
print("no fault amt:",nf_sum) 
print("type1 amt:",t1_sum)
print("type2 amt:",t2_sum)
print("type3 amt:",t3_sum)
print("-----------\n")

labels = ['No Fault', 'Type 1', 'Type 2', 'Type 3']
counts = [len(df_nofault), len(df_type1), len(df_type2), len(df_type3)]
colors = ['#3AB09E', '#55557F', '#93c47d', '#BD9BC1']

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(labels, counts, color=colors)
ax.set_title('Fault Type Counts')
ax.set_xlabel('Fault Type')
ax.set_ylabel('Count')
plt.tight_layout()
plt.show()


