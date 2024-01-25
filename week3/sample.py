# Usage of Numpy Data Structure
import numpy as np
import random
# Array creation
A = np.array([2, 5, 10])
print("A.dtype=\n", A.dtype)
# Will show, int64 data type
B = np.array([2.4, 10.6, 5.2])
print("B.dtype=\n", B.dtype)
# Will show, float64 data type

# Creating sequence of sequence will create 2-dimensional array.
A = np.array([(3, 4, 5), (12, 6, 1)])
Z = np.zeros((2, 4))  # will create zero matrix of dimension 2x4
print("A=\n", A)
print("Z=\n", Z)
# Similarly,
# will create one's matrix of dimension 3x3
print("np.ones((3, 3))=\n", np.ones((3, 3)))

# To create a sequence of data,
S = np.arange(10, 30, 5)
print("S=\n", S)  # will give (10,15,20,25,30), with step size of 5
S = np.arange(0, 2, 0.3)  # it accepts float arguments
print("S=\n", S)
# array([ 0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

# lnstead of step-size, we can specify total number of elements in the array using
# produce 9 numbers starting 0 & ends with 2array([ 0. , 0.25, 0.5 , 0.75, 1. ,1.25, 1.5 , 1.75, 2. ])
S1 = np.linspace(0, 2, 9)
print("S1=\n",S1)
# Usage of Random Number functions

# , this will pick one number from the list randomly
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice('python'))  # , will pick one character from the string randomly
print(random.randrange(25, 50))  # , will pick one integer between 25 to 50
# , will pick one integer between 25 to 50 with step size of 2
print(random.randrange(25, 50, 2))
print(random.random())  # , will pick a random number between 0 to 1
print(random.uniform(5, 10))  # , will pick a floating point number between 5 to 10
print(random.shuffle([1, 2, 3, 4, 5]))  # , will shuffle the list elements
print(random.seed(10))  # , to get same random value during every execution

# 2- Dimensional array (Matrix)
a = np.arange(15).reshape(3, 5)
# to check the dimension
print("Shape of A: ",a.shape)
print("Size of A: ",a.size)  # will return total elements in matrix (here 15)
# to transpose a matrix
print("Transpose of A: ",a.T)  # transposed to 5x3 matrix

# 3- Dimensional array
# 1st value indicates (no of planes) (3,4) is the dimension
c = np.arange(24).reshape(2, 3, 4)
print(c)
print("Shape of c: ",c.shape)  # will return (2,3,4)
print(c[1, ...] ) # is equal to c[1,:,:] # will fetch all elements of 2nd plane
print(c[..., 2])  # is equal to c[:,:,2] [[3,7,11],[15,19,23]]

# Array operations
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print("B: ",b)
c = a-b
print("C: ",c)
print("Squares: ",b**2)
print("10*sine: ",10*np.sin(a))
print("a<35: ",a < 35)

# Matrix operations
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print("A*B: ",A*B)
print("A.B: ",A.dot(B))
# (OR)
# another matrix product
b = np.arange(12).reshape(3, 4)
print("b: ",b)
print("Col Sum: ",b.sum(axis=0))  # sum of each column
print("Row Sum: ",b.sum(axis=1))  # sum of each row

# Indexing, Slicing & Iterating Array
a = np.arange(10)**3
a
a[2:5]
a[0:6:2]
# Let 'b', is an input matrix of size 5x4
b = np.array([[0, 1, 2, 3],
              [10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])
b[2, 3]  # will fetch 23
b[0:5, 1]
b[:5, 1]
b[:, 1]  # will fetch [1,11,21,31,41]
b[-1, :]  # will fetch last row
b[:, -1]  # will fetch last col
for row in b:
    print(row,end="\t")  # will print every rowfor element in b.flat:
print()
for element in b.flat:
    print(element,end="\t")  # will show all elements of b in 1-D array
print()

# Changing the shape of a matrix
print("Flattened: ",b.ravel() ) # returns the array flattened to (1x 20)
# Later, we can convert 5x4 matrix into 4x 5 matrix using
B1 = b.reshape(4, 5)
print("Reshaped: ",B1)
# Stacking together different arrays
A1 = np.array([(3, 4, 5), (12, 6, 1)])
A2 = np.array([(1, 2, 6), (-4, 3, 8)])
D1 = np.vstack((A1, A2))
D2 = np.hstack((A1, A2))

# Stacking 1-D array into 2-D array (column wise)
a = np.array([4., 2.])
b = np.array([3., 8.])
np.column_stack((a, b))  # returns a 2D array
np.hstack((a, b))
# the result is different
# np.hstack((a[:,newaxis],b[:,newaxis])) # the result is the same

# Indexing with array of indices
a = np.arange(12)**2  # the first 12 square numbers
i = np.array([1, 1, 3, 8, 5])  # an array of indices
a[i]  # the elements of a at the positions i
j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
a[j]  # the same shape as j

# Usage of for-loop (Mapping by Value)
# Calculate sum of all the elements in a 2D Numpy Array (iterate over elements)
a = np.array([(3, 2, 9), (1, 6, 7)])
s1 = 0
for row in a:
    for col in row:
        s1 += col
print("Sum: ",s1)

# Usage of for-loop (Mapping by Index)
# Calculate sum of all the elements in a 2D Numpy Array (iterate over range)
a = np.array([(3, 2, 9), (1, 6, 7)])
s = 0
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        s += a[i, j]
print("Sum: ",s)
