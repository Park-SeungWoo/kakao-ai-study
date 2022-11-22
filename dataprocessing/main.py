import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("./lecture_datas/animals.xlsx", engine="openpyxl")
print(type(df))
print(df.set_index('name'))
print(df.head(3))
print(df.tail(3))
print(df.describe())
print(df.info())
