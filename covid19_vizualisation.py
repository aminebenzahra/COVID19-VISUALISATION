# -*- coding: utf-8 -*-
"""covid19 vizualisation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zwAmHXUrUPKykbXmRu9URIqAKMBLwPzS
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

corona_dataset_csv=pd.read_csv("covid19_dataset.csv")
corona_dataset_csv.head()

corona_dataset_csv.shape

df=corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)

corona_dataset_csv.head()

corona_dataset_aggregated=corona_dataset_csv.groupby("Country/Region").sum()

corona_dataset_aggregated.head()

corona_dataset_aggregated.loc["Morocco"].plot()
corona_dataset_aggregated.loc["Algeria"].plot()
corona_dataset_aggregated.loc["Tunisia"].plot()
plt.legend()

corona_dataset_aggregated.loc["Morocco"].plot()

corona_dataset_aggregated.loc["Italy"].plot()