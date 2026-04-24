from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return x**2 / 10-2 * np.sin(x)

x0 = 0
x1 = 4
min = optimize.fminbound(f, x0, x1)
print(min)

x= np.linspace(x0, x1, 1000)
plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.grid()
plt.axvline(min, linestyle="--")     
plt.show()