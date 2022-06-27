# -*- coding: utf-8 -*-
"""Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IaNFxIvyyU-yVnaxNnwiEp2lBPqz_LOv

# Seaborn

on top of matplotlib
Statistics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Datasets/Marketing Raw Data.csv")

data.head()

data["Promo"].unique()

data["Year"].unique()

data.shape

#balanced
data["Year"].value_counts()

sns.countplot(data["Year"])

sns.lineplot(x="Year", y="Revenue", data=data)

sns.scatterplot(x="Year", y="Revenue", data=data)

plt.figure(figsize=(35,5))
sns.lineplot(x="Date", y="Revenue", data=data)
plt.xticks(rotation=90)

sns.lineplot(x="Week_ID", y="Revenue", data=data)

sns.lineplot(x="Week_ID", y="Revenue", data=data, hue="Promo", style="Promo")

plt.figure(figsize=(15,5))
sns.lineplot(x="Week_ID", y="Revenue", data=data, hue="Promo", style="Promo", ci=False)

plt.figure(figsize=(15,5))
sns.lineplot(x="Week_ID", y="Revenue", data=data, hue="Promo", style="Promo", ci=False, markers=True)

data.columns

plt.figure(figsize=(15,5))
sns.lineplot(x="Month_ID", y="Revenue", data=data, hue="Day_Name", ci=False, markers=True)

sns.barplot(data["Month_ID"], data["Revenue"])

plt.scatter()

sns.barplot(data["Revenue"], data["Month_ID"], orient="h")

data["Month_ID"].unique()

data[["Revenue", "Month_ID"]].groupby("Month_ID").mean()

plt.figure(figsize=(15,5))

b1 = sns.barplot(data["Month_ID"], data["Revenue"])
for bar in b1.patches:
    b1.annotate(format(bar.get_height(), "0.2f"),
                  (bar.get_x() + bar.get_width()/2, bar.get_height()),
                   ha="center", va="center", size=10, xytext=(0,6),
                  textcoords= "offset points")

sns.barplot(x="Month_ID", y="Revenue", data=data, hue="Promo", ci=False)

sns.barplot(x="Revenue", y="Month_ID", data=data, hue="Promo", ci=False, orient="h")

sns.barplot(x="Revenue", y="Month_ID", data=data, hue="Promo", ci=False, orient="h", color="#33ACFF")

sns.distplot(data["Revenue"], color="r")

nmean1 = data["Revenue"].mean()
sns.distplot(data["Revenue"], color="r")
plt.axvline(nmean1, 0, 1)

sns.boxplot(data["Revenue"])

data.columns

sns.boxplot(x="Day_Name", y="Revenue", data=data)

sns.boxplot(x ="Revenue", y="Day_Name", data=data)

sns.boxplot(x ="Revenue", y="Day_Name", data=data, hue= "Promo")

sns.boxplot(x ="Day_Name", y="Revenue", data=data, hue= "Promo")

sns.boxplot(x="Day_Name", y="Revenue", data=data, color="r")
sns.swarmplot(x="Day_Name", y="Revenue", data=data, color="b", dodge=True)

data.columns

sns.scatterplot(x="Marketing Spend", y="Revenue", data=data)

sns.scatterplot(x="Marketing Spend", y="Revenue", data=data, hue= "Promo")

sns.scatterplot(x="Marketing Spend", y="Revenue", data=data, hue= "Promo", style="Promo")

plt.figure(figsize=(10,5))
sns.scatterplot(x="Marketing Spend", y="Revenue", data=data, 
                   hue= "Promo", style="Promo", size="Revenue")

plt.figure(figsize=(10,5))
sns.scatterplot(x="Marketing Spend", y="Revenue", data=data, hue= "Promo", style="Promo", size="Revenue", sizes=(50,250))

plt.figure(figsize=(10,5))
sns.scatterplot(x="Marketing Spend", y="Revenue", data=data, hue= "Promo",  size="Revenue", sizes=(50,250))

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False)

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, hue="Promo")

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, hue="Promo", markers=["*", "^", "o"])

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, col="Promo")

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, col="Promo", line_kws={"color":"green"})

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, col="Promo", line_kws={"color":"green"}, scatter_kws={"color":"red"})

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, col="Day_Name", line_kws={"color":"green"}, scatter_kws={"color":"red"})

sns.lmplot(x="Marketing Spend", y="Revenue", data=data, ci=False, col="Day_Name", line_kws={"color":"green"}, scatter_kws={"color":"red"}, col_wrap=3)

fig, ax = plt.subplots(2,2,figsize=(8,5))
sns.distplot(data["Revenue"], ax=ax[0,0])
sns.lineplot(x="Visitors", y="Revenue", data=data, ax=ax[0,1])
sns.distplot(data["Marketing Spend"], ax=ax[1,0])
sns.boxplot(x="Day_Name", y="Revenue", data=data,ax=ax[1,1])
sns.swarmplot(x="Day_Name", y="Revenue", data=data, color="red")

"""# Multivariate plots"""

data.head()

sns.lineplot(x="Day_Name", y="Revenue", data=data)

sns.pairplot(data)

data.corr()

plt.figure(figsize=(8,8))
sns.heatmap(data.corr(), annot=True)

correlation = relationship (continous)

-1   0    +1

data.head()

data.shape

data.describe()

np.round(data.var(), 2)

"""# How to convert categorical to continous data"""

data.dtypes

data["Day_Name"].unique()

data["Day_Name"].nunique()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

day_c = le.fit_transform(data["Day_Name"])

data["Day_Name_converted"] = pd.Series(day_c)

dict(zip(data["Day_Name"], data["Day_Name_converted"]))

data.head()

data["Promo"].unique()

data1 = pd.get_dummies(data["Promo"])

data = pd.concat([data, data1], axis=1)

data.drop(["Promo", "Day_Name"], axis=1, inplace=True)

data.head()

data["Date"] = pd.to_datetime(data["Date"])

data.head()

data.info()

import datetime
data["Date"].dt.year

data.head()

data.isnull().sum()

data.describe()

d1 = data.iloc[:, 1:-3]
d1.head()

from sklearn.preprocessing import StandardScaler #normal disr= mean=0, std=1, x-mean/std
sc = StandardScaler()
v1 = sc.fit_transform(d1.values)
input1 = pd.DataFrame(v1, columns=d1.columns)
np.round(input1.describe(),2)

from sklearn.preprocessing import MinMaxScaler #x-xmean/xmax-xmin
m1 = MinMaxScaler(feature_range=(1,5))
b1 = m1.fit_transform(d1)
x2 = pd.DataFrame(b1, columns=d1.columns)
np.round(x2.describe(),2)

x2.var()

sns.jointplot(x="Marketing Spend", y="Revenue", data=data)

sns.jointplot(x="Marketing Spend", y="Revenue", data=data, color="red", kind="reg")

data = pd.read_csv("Datasets/Marketing Raw Data.csv")
sns.pairplot(data, hue="Promo")