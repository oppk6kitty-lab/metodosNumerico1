import numpy as np
import math   
import matplotlib.pyplot as plt 

def f(x): 
    return (x ** 2) - 2

def f_derivada(x): 
    return 2 * x

x1= x old
xi+1= x new

Eppara = 
Epest = 100

while Epest > Eppara:
    x new = x old - f(x)/f_derivada(x)

    Epest = abs((x new - x old) / x new) * 100

end while



