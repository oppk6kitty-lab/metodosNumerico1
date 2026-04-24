import  numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

x1 = np.linspace(-2, 0, 50) 
x2 = np.linspace(0, 3, 50)

X1, X2 = np.meshgrid(x1, x2)

f = 2 + X1 - X2 + 2*X1**2 + 2*X1*X2 + X2**2

plt.figure()
ax= plt.axes(projection='3d')
cs = ax.plot_surface(X1, X2,f, cmap='viridis')

plt.figure()
plt.contour(X1, X2, f, cmap='viridis')

plt.show()

print(X1)
print(X2)
