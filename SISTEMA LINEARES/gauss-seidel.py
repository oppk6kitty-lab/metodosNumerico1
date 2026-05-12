import numpy as np

A = np.array([2,4,-6], [4,2,2], [2,8,-4]])
b = np.array ([[10], [16], [24]])

n= len(b)
x_old = np.zeros(n)
x_new = np.zeros(n)

Eppara = 0.5 *10**(2-6)

Epest = 100
k = 0
soma_A = 0
soma_B = 0

while Epest >= Eppara:

    for i in range(n-1):
        x_new[i] = 1 / A[i][i] * (b[i]- soma_A - soma_B)
        for j in range(i-1,n)