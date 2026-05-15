import numpy as np

A = np.array([[2,4,-6], 
             [4,2,2],
             [2,8,-4]])
b = np.array ([10, 16, 24])

ordem = np.argmax(np.abs(A), axis=0)
A = A[ordem, :]
b = b[ordem]

n= len(b)
na = 6
Eppara = 0.5*10**(2 - na)

#Chute Inicial
x_old = np.zeros(n)
print(x_old)

#Alocacao de Memoria
x_new = np.zeros(n)
Epest = 100
print(Epest)
maxit = 1000
k = 0

while Epest > Eppara:

    for i in range (n):
        soma1 = 0
        soma2 = 0
        for j in range(n):
            if j < i:
                soma1 += A[i,j]*x_new[j]
            elif j > i:
                soma2 += A[i,j]*x_old[j]

        x_new[i] = (b[i] - soma1 - soma2) / (A[i,i])

    Epest = np.max(np.abs((x_new - x_old)/x_new))*100
    x_old = x_new
    k+=1

print(x_new)
