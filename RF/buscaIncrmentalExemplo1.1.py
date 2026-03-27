import numpy as np
import math

def f(x):
    return np.sin(10*x) + np.cos(3*x)

# Vetor
n = 100
x = np.linspace(3, 6, n)

# Alocação de memória
xb = []
nb=0

# Busca Incremental
for i in range(n-1) :
    xl = x[i]
    xu = x[i+1]

    if(f(xl)*f(xu) < 0):
        nb += 1
        xb.append([xl,xu])
    else:
        print("Nenhum subintervalo foi encontrado!")


print("xb = ", xb)
print("y = ", f(x))
print("Número de subintervalos = ", nb)




A = np.array([
    [1,2],
    [3,4]
])
print("A = ", A)