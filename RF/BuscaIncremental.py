import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return np.sin(10*x) + np.cos(3*x)

plt.figure()
plt.plot(np.linspace(3,6,100), f(np.linspace(3,6,100)))

# Gráfico
plt.figure()
plt.plot(x,f(x))
plt.ylabel("f(x)")
plt.grid()
plt.show()




