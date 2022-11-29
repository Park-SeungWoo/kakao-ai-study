import numpy as np

arr1 = np.array([1, 2, 3])
# print(arr1.dtype)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2)
# print(arr2.shape)  # shape
# print(arr2.ndim)  # dimension

zarr = np.zeros((2, 2))
oarr = np.ones((2, 2))
# print(zarr)
# print(oarr)

earr = np.eye(3)
# print(earr)

rarr = np.random.random((2, 2))
# print(rarr)
riarr = np.random.randint(1, 100, size=(4, 4))
# print(riarr)

a = np.random.random(10)
a.sort()
# print(a)
# print(a[::-1])

ar = np.arange(9)
# print(ar)

ar = ar.reshape(3, 3)
# print(ar)

# print(ar.sum(axis=1))
# print(ar.min())
# print(ar.max())
# print(np.median(ar, axis=1))

d = np.diag(ar)
# print(d)
d = np.diag(d)
# print(d)

a = np.random.randint(1, 10, (2, 3))
b = np.random.randint(1, 10, (2, 3))
c = np.random.randint(1, 10, (3, 2))
# print(a)
# print(b)
# print(c)

# print(np.dot(a, c))

######################matplotlib

import matplotlib as mlp
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd


rc('font', family='Nanum GaRamYeonGgoc')  # set font
plt.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# plt.plot(x, y)

# plt.grid()  # add grid
# plt.xlabel('x label')
# plt.ylabel('y label')

# plt.title('title')
# plt.show()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(axis=0),
                  columns=['A', 'B', 'C', 'D'],
                  index=np.arange(0, 100, 10))

# df.plot()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('title')
# plt.show()

s = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))

# s.plot(kind="bar")
# df.plot(kind='bar')
# plt.show()

norm = np.random.normal(1, 1, size=(100, 1))
norm2 = np.random.normal(-2, 4, size=(100, 1))

norm = pd.DataFrame(np.concatenate((norm, norm2), axis=1), columns=['x1', 'x2'])
# print(norm)

plt.scatter(norm['x1'], norm['x2'])
plt.show()

