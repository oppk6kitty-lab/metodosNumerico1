import numpy as np
import matplotlib.pyplot as plt 


def f(m):
    return np.sqrt(9.81 * m / 0.25) * np.tanh(np.sqrt(9.81 * 0.25 / m) * 4 ) - 36

    # algarismos significativosw, critérios de parada e erro percentual estimado
alg = 6
Eppara = 0.5 * 10 **(2-alg)
Ept = 100
Epest = 100

# valor real
u = 142.7376

#variáveis gerais
k = 0
xl = 140
xu = 150
# xr_old = 0

while Ept > Eppara:

    xr = (xl + xu) / 2

    if f(xl) * f(xr) < 0:
        xu = xr
    else:
        xl = xr

    # Epest = abs((xr - xr_old) / xr) * 100
    Ept = abs((u - xr) / u) * 100
    # xr_old = xr
    k += 1

print(xr)


