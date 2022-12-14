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
# print(df["name"].str.contains("ar"))
# print(sum(df["name"].str.contains("ar")))
# print(df[df["name"].str.contains("ar")])  # dataframe filtering

############ advanced ways to handle dataframe

new_df = df[['name', 'hair', 'feathers', 'eggs', 'milk', 'type']]
# print(new_df.head(3))
# new_df['new_hair'] = new_df['hair'].apply(lambda x: x + 1)
# print(new_df.head(3))
#
# def my_sum(x):
#     res = 0
#     for item in x:
#         res = res + 1 if item else res
#     return res
#
#
# pivot_df = pd.pivot_table(new_df, index="type", aggfunc=my_sum)
pivot_df = pd.pivot_table(new_df, index="type", aggfunc=np.sum)
# print(pivot_df)

######drop column
# del pivot_df['new_hair']

######drop row
# pivot_df = pivot_df.drop([3, 5])  # not mean index, it means label
# pivot_df = pivot_df.drop(['eggs'], axis=1)  # axis 0 = row, 1 = column
# pivot_df.drop(['eggs'], axis=1, inplace=True)  # axis 0 = row, 1 = column
# print(pivot_df)
# print(pivot_df)
# print(list(pivot_df.columns))
# print(list(pivot_df.index))

# pivot_df.rename(columns={'eggs': '에그그그', 'feathers': '기기기깃털'}, inplace=True)
# print(pivot_df)

pivot_df.sort_values(by='eggs', inplace=True, ascending=False)
print(pivot_df)
