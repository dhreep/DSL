import numpy as np

#1
a = int(input("Enter a number to find its factors: "))
print("Factors are: ")
for i in range(1,a+1):
    if a%i==0:
        print(i,end="\t")

#2
b = np.array([[0, 1, 2, 3],
              [10, 11, 12, 13],
              [40, 41, 42, 43]])
print("Array: \n",b)
scol = b.sum(axis=0)
print("Sum of columns: ",scol)
srow = b.sum(axis=1)
print("Sum of rows: ",srow)

#3
list = [1, 2, 3, 4, 5]
float_array = np.array(list, dtype=float)
print("Float Array: ",float_array)
tuple = (1, 2, 3, 4, 5)
array = np.array(tuple)
print("Tuple Array: ",array)
array = np.zeros((3, 4))
print("Zeros Array: ",array)
sequence = np.arange(0, 21, 5)
print("Sequence: ",sequence)
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reshaped_array = np.reshape(array, (2, 2, 3))
print("Reshaped array: ",reshaped_array)
print("New Array: ",array)
# Maximum and minimum element of array
print("Maximum element: ", np.max(array))
print("Minimum element: ", np.min(array))
# Row wise max and min
print("Row wise max: ", np.max(array, axis=1))
print("Row wise min: ", np.min(array, axis=1))
# Column wise max and min
print("Column wise max: ", np.max(array, axis=0))
print("Column wise min: ", np.min(array, axis=0))
# Sum of elements
print("Sum of elements: ", np.sum(array))

#4
print("Transposed matrix: ",array.T)

#5
print("Sum of matrices: ",b+array)

#6
print("Elementwise product of matrices: ",b*array)