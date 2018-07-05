import numpy as np
#Q1.

v=np.random.rand(10,1)
print(v)
print("Mean =",np.mean(v))

#Q2.

N=np.random.rand(20,1)
print(N)
print("Standard Deviation =",N.std())
print("Variance =",N.var())


#Q3.
A=np.random.rand(10,20)
B=np.random.rand(20,25)
C=np.dot(A,B)
print("Multiplication of matrix A and matrix B,i.e., matrix C =",C)
print("Shape of C matrix =",C.shape)
print("Sum of all elements of matrix C =",np.sum(C))

#Q4.

def f(i):
    return( 1 / (1 +( np.exp(-i))))
A=np.random.rand(10,1)
print("Original array =",A)
B=f(A)
print("New array =",B)