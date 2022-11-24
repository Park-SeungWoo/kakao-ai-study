import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("./lecture_datas/animals.xlsx", engine="openpyxl")
# print(type(df))
# print(df.set_index('name'))
# print(df.head(3))
# print(df.tail(3))
# print(df.describe())
# print(df.info())
# print(df.loc[3])  # get series by row
# series_var = df.loc[3]
# print(series_var.keys())
# print(series_var.values)
# print(series_var["name"])
# print(df.loc[3]["name"])
# print(df.loc[[3]])  # dataframe
# print(df.loc[[3, 4, 5]])  # dataframe
# print(df.loc[3:6])
# print(df.iloc[3:6])
# print(df['name'])  # get series by column
# print(df["name"][0])  # get series by column
# print(df.loc[0]["name"])  # same as above
# print(df[["name", "hair", "feathers"]])
print(df["name"].str.contains("ar"))
print(sum(df["name"].str.contains("ar")))
print(df[df["name"].str.contains("ar")])  # dataframe filtering
