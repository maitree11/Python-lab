import numpy as np

arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)

flattened = arr.flatten()
unique_vals = np.unique(flattened)
second_max = unique_vals[-2]

print("Row sum:", row_sum)
print("Column sum:", col_sum)
print("Second max:", second_max)