import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']])
print(arr)

for x in arr:
  print(x)

print(type(arr))
print(type(arr2))

print(arr.ndim)
print(arr2.ndim)

print(arr[1:5])
print(arr[2:7:2])

x = arr.copy()
arr[0] = 42
print(arr)
print(x)

x = arr.view()
x[0] = 31
print(arr)
print(x)

x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr3.shape)

arr4 = np.array([1, 2, 3, 4], ndmin=3)
print(arr4)
print('shape of array :', arr4.shape)

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr5.reshape(4, 3)
print(newarr)

arr6 = np.array([1, 2, 3])
arr7 = np.array([4, 5, 6])
arr8 = np.concatenate((arr6, arr7))
print(arr8)
