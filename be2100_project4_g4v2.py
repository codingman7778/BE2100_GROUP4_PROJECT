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
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


#initialization and importation of ai4i2020.csv from repo as pandas dataframe 
g = Github()
repo_path = "codingman7778/BE2100_GROUP4_PROJECT" 
repo = g.get_repo(repo_path)

#prints repo name
print(f"repository name: {repo.name}\n")
print("⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚")

faultDB_url = "https://raw.githubusercontent.com/codingman7778/BE2100_GROUP4_PROJECT/refs/heads/main/EngineFaultDB_Final.csv"
df = pd.read_csv(faultDB_url)
print("CSV EngineFaultDB loaded from GitHub.\n")
print("⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚")
# display all column names
print("column names:")
print(df.columns.tolist())
print("⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚⤙⤚")






# build fault count summary dataframe
fault_counts = df['Fault'].value_counts().sort_index()
faults_df = pd.DataFrame([{
    'No Fault': int(fault_counts.get(0, 0)),
    'Fault 1':  int(fault_counts.get(1, 0)),
    'Fault 2':  int(fault_counts.get(2, 0)),
    'Fault 3':  int(fault_counts.get(3, 0)),
}])

print("\nfaults_df head:")
print(faults_df.head())
print(f"rows: {faults_df.shape[0]}, columns: {faults_df.shape[1]}")

# build fault index dataframe with original row numbers
fault_idx = {col: df[df['Fault'] == i].index.tolist()
             for i, col in enumerate(faults_df.columns)}
max_len = max(len(v) for v in fault_idx.values())
for k in fault_idx:
    fault_idx[k] = fault_idx[k] + [np.nan] * (max_len - len(fault_idx[k]))

df_faults_index = pd.DataFrame(fault_idx)

print("\ndf_faults_index head:")
print(df_faults_index.head())
print(f"rows: {df_faults_index.shape[0]}, columns: {df_faults_index.shape[1]}")

# shared plot settings
labels  = faults_df.columns.tolist()
values  = faults_df.iloc[0].values.astype(int)
palette = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2']

# all three charts in one figure
fig = plt.figure(figsize=(18, 10))
gs  = fig.add_gridspec(2, 4, hspace=0.38, wspace=0.35)
ax1 = fig.add_subplot(gs[0, 0:2])
ax2 = fig.add_subplot(gs[0, 2:4])
ax3 = fig.add_subplot(gs[1, 1:3])

# histogram (touching bars)
for i, (lbl, val, col) in enumerate(zip(labels, values, palette)):
    ax1.bar(i, val, width=1.0, color=col, edgecolor='white', linewidth=1.2)
ax1.set_title('Fault Analysis — Histogram', fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel('fault type', fontsize=11)
ax1.set_ylabel('count', fontsize=11)
ax1.set_xticks(range(len(labels)))
ax1.set_xticklabels(labels, fontsize=10)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.spines[['top', 'right']].set_visible(False)

# bar chart (spaced bars with labels)
bars = ax2.bar(labels, values, color=palette, edgecolor='white', linewidth=1.2, width=0.6)
for bar, val in zip(bars, values):
    ax2.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + max(values) * 0.012,
             f'{val:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax2.set_title('Fault Analysis — Bar Chart', fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel('fault type', fontsize=11)
ax2.set_ylabel('count', fontsize=11)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax2.set_ylim(0, max(values) * 1.12)
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.spines[['top', 'right']].set_visible(False)

# pie chart
wedges, texts, autotexts = ax3.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    colors=palette,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2},
    startangle=90,
    pctdistance=0.78,
)
for t in texts:
    t.set_fontsize(10)
for at in autotexts:
    at.set_fontsize(9)
    at.set_fontweight('bold')
ax3.set_title('Fault Analysis — Pie Chart', fontsize=13, fontweight='bold', pad=14)

plt.show()
