import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns


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
