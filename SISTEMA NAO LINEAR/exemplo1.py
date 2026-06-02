import numpy as np

#Funcao F(x)
def f1(x1,x2):
    return x1**2 - x1*x2 - 10

def f2(x1,x2):
    return x2 + 3*x1*x2**2 - 57

def df1dx1(x1,x2):
    return 2*x1 - x2

def df1dx2(x1,x2):
    return -x1

def df2dx1(x1,x2):
    return 3*x2**2

def df2dx2(x1,x2):
    return 1 + 6*x1*x2

Epest = 100
n = 6
Eppara = 0.5 * 10**(2-n)
k = 0
maxit = 1000

xold = np.array([1.5,3.5])
xnew = np.array([0,0])


while Epest >= Eppara and k < maxit:

    x1 = xold[0]
    x2 = xold[1]

    xnew[0] = x1 - ((f1(x1,x2) * df2dx2(x1,x2)) - (f2(x1,x2)*df1dx2(x1,x2))) / ((df1dx1(x1,x2)*(df2dx2(x1,x2))-(df1dx2(x1,x2))*(df2dx1(x1,x2))))
    xnew[1] = x2 - ((f2(x1,x2) * df1dx1(x1,x2)) - (f1(x1,x2)*df2dx1(x1,x2))) / ((df1dx1(x1,x2)*(df2dx2(x1,x2))-(df1dx2(x1,x2))*(df2dx1(x1,x2))))

    Epest = np.max(np.abs((xold - xnew) / xnew)) * 100
    xold = xnew.copy()
    k += 1
    
print(xnew)
print(k)


    
