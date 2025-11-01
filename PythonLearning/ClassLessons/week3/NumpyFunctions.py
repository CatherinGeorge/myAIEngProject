#indexing & shaping
#access the first, last & 3rd element of array
#print the shape of the array

import numpy as np

id=np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("1st element of array", id[0])
print("last element of array", id[-1])
print("3rd element to end of array", id[2])
print("shape of the array:", id.shape)
print("execution times of first 3 tests", id[:3])
print("print every alternate test time", id[::2])
print("2D array\n", id.reshape(2, 4))
print("3D array\n", id.reshape(2, 2, 2))

secondid = np.array([50, 55, 60, 65])
allid = np.concatenate((id, secondid))
print("All test time:\n", allid)
print(np.split(allid,3))
