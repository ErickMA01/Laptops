import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from scipy.stats import yeojohnson

df = pd.read_csv('laptops.csv')

print(df.head(10))

print(df.shape)
print(df.describe())
df.columns

print(f"Null values: {df.isna().sum().sum()}")

a = []
for i in df.columns:
    a.append(len(df[f"{i}"].unique()))

print(df.columns.values)
print(f"Unique values per column: {a}")

# EDA

# CompanyName

df.iloc[:,0].unique()

plt.figure(figsize=(20, 5))
sns.boxplot(x=df.iloc[:,0], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# TypeOfLaptop

df.iloc[:,1].unique()

plt.figure(figsize=(20, 6))
sns.boxplot(x=df.iloc[:,1], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Inches

plt.figure(figsize=(10, 3))
sns.histplot(df.iloc[:,2], kde=True, color='magenta')
plt.xlabel('Inches')
plt.ylabel('Freq')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df.iloc[:,2], df.iloc[:,10], edgecolors='red')
plt.xlabel('Inches')
plt.ylabel('Price')
plt.show()

# ScreenResolution
df.iloc[:,3].unique()

plt.figure(figsize=(20, 6))
sns.boxplot(x=df.iloc[:,3], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Cpu
df.iloc[:,4].unique()

plt.figure(figsize=(25, 6))
sns.boxplot(x=df.iloc[:,4], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Ram
df.iloc[:,5].unique()

plt.figure(figsize=(10, 3))
sns.boxplot(x=df.iloc[:,5], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Memory
df.iloc[:,6].unique()

plt.figure(figsize=(35, 6))
sns.boxplot(x=df.iloc[:,6], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Gpu
df.iloc[:,7].unique()

plt.figure(figsize=(10, 3))
sns.boxplot(x=df.iloc[:,7], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# OpSys
df.iloc[:,8].unique()

plt.figure(figsize=(10, 3))
sns.boxplot(x=df.iloc[:,8], y=df.iloc[:,10], data=df)
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Weight
plt.figure(figsize=(10, 3))
sns.histplot(df.iloc[:,9], kde=True, color='pink')
plt.xlabel('Weight')
plt.ylabel('Freq')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df.iloc[:,9], df.iloc[:,10], edgecolors='pink')
plt.xlabel('Weight')
plt.ylabel('Price')
plt.show()


