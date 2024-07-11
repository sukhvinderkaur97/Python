import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']])
print(arr)

print(type(arr))
print(type(arr2))

print(arr.ndim)
print(arr2.ndim)

print(arr[1:5])
print(arr[2:7:2])

