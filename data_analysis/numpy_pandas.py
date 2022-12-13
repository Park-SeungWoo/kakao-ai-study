import numpy as np
import pandas as pd


arr = np.array([1, 2, 3, 4])
# print(arr.dtype)  # int64
arr = np.array([1, 2, 3.3, 4])
# print(arr.dtype)  # float64

# print(arr.shape)  # (4,) -> 1 dim array

sample_matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(sample_matrix)
# print(sample_matrix.shape)

# print(sample_matrix[0, 1])
# print(sample_matrix[0:2, 1:2])  # [ [2] [5] ]
# print(sample_matrix[:, 1])  # [ 2 5]

ar = np.arange(5)
# print(ar)
ar = np.arange(0, 10, 2)
ar = np.arange(0, 10, 2) ** 2
# print(ar)

ar = np.arange(12)
# print(ar)
ar = ar.reshape(3, 4)
ar = ar.reshape(3, -1)  # same as above
# print(ar)
ar = np.arange(12).reshape(2, 6)  # method chaining
# print(ar)
ar = ar.reshape(3, -1, order='F')
# print(ar)

ar = np.arange(1, 5).reshape(2, -1)
# print(np.max(ar, axis=1))  # max column
# print(np.max(ar, axis=0))  # max row
# print(np.max(ar))  # max element

arr = np.arange(5, 9).reshape(2, -1)
# print(arr)

# print(np.add(ar, arr))
# print(np.subtract(ar, arr))
# print(np.multiply(ar, arr))
# print(np.dot(ar, arr))

# pandas

pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
a = pd.Series([1, 2, 3, 4])
# print(a)
# print(a.values)
# print(a.index)
# print(a.keys())

a = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(a)

df = pd.read_csv('./data_analysis/data/cosmetics_.csv')
# print(df)

df.insert(8, 'total_payment', df['count'] * df['amount'])
# df['total_payment'] = df['count'] * df['amount']  # same as above
# print(df)

del df['total_payment']
# print(df)

df_men = df[df['gender'] == 1]
df_women = df[df['gender'] == 2]
# print(df_men.describe())
# print(df_women.describe())

df_count = df[(df['count'] >= 1) & (df['count'] < 10)]
# print(df_count)

edu_count = df['edu'].value_counts(sort=False)
# print(edu_count)

# same as above
from collections import Counter
counted = Counter(df['edu'].values)
edu_count_counter = pd.Series(counted.values(), counted.keys())
# print(edu_count_counter)


def num_to_character(num):
    if num == 1:
        return 'male'
    else:
        return 'female'


# df.insert(1, 'gender_2', df['gender'].apply(num_to_character))
df.insert(1, 'gender_2', df['gender'].apply(lambda num: 'male' if num == 1 else 'female'))
print(df)