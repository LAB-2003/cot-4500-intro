#Lorelai Barnes
#Intro to Python

import numpy as np

#Number 1
print("Number 1: \n")
m, n = 3, 3
A = np.empty(shape=(m,n), dtype=int)

for i in range(m):
    for j in range(n):
        if(i==j):
            A[i,j] = 1
        else:
            A[i,j] = 0
print(A)
print("\n")

#Number 2
print("Number 2: \n")
print(A)
print("\n")
i, j = np.ogrid[:3, :3]
B = np.where(i==j,A,3)
print(B)           
print("\n")
#Number 3
print("Number 3: \n")
print(np.delete(B,2,1))
