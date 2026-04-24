from scipy import optimize

def f(x):
    # x = [x1, x2]
    return 2 +x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2

def fx1x2(x):
    x1 = x[0]
    x2 = x[1]
    return 2 + x1 - x2 + 2*x1**2 + 2*x1*x2 + x2**2

x0 = [0, 0]
resultado = optimize.minimize(f,x0)

print(resultado)

