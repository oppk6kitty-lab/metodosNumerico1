import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

# Dados de entrada
date = {
    'x' : [0,2,4,6,9,11,12,15,17,19],
    'y' : [5,6,7,8,9,10,10,11,12,12]
    }

df = pd.DataFrame(date)

# Gráfico
plt.plot(df['x'],df['y'],'or',label= 'Dados Discretos')
plt.show()

#Cálculos
n = len(df['x'])
sum_x = np.sum(df['x'])
sum_y = np.sum(df['y'])
sum_xx = np.sum(df['x']*df['x'])
sum_yx = np.sum(df['y']*df['x'])

#Construindo as matrizes A e b
A = np.array([[n, sum_x],
              [sum_x, sum_xx]])

b = np.array([sum_y, sum_yx])

# Solução do Sistema Linear
x = np.linalg.solve(A,b)
print(x)

