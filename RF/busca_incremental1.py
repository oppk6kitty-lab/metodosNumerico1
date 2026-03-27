import numpy as np

# Definição da função
def f(x):
    return np.sin(10*x) + np.cos(3*x)

# Intervalo e passo
a, b = 3, 6
step = 0.01

# Lista para armazenar subintervalos com mudança de sinal
subintervalos = []

# Busca incremental
x_vals = np.arange(a, b, step)
for i in range(len(x_vals)-1):
    x1, x2 = x_vals[i], x_vals[i+1]
    y1, y2 = f(x1), f(x2)
    if y1 * y2 < 0:  # Mudança de sinal
        subintervalos.append((round(x1, 2), round(x2, 2)))

# Exibir resultados
print("Subintervalos com mudança de sinal:")
for intervalo in subintervalos:
    print(intervalo)
