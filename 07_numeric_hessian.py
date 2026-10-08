import numpy as np
#
def rosen(v):
    x, y = v
    return (1 - x)**2 + 100*(y - x*x)**2
#
def num_hessian(f, v, h=1e-4):
    n = len(v)
    E = np.eye(n) * h
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = (f(v + E[i] + E[j]) - f(v + E[i] - E[j])
                       - f(v - E[i] + E[j]) + f(v - E[i] - E[j])) / (4*h*h)
    return H
#
print(num_hessian(rosen, np.array([-1.2, 1.0])).round(3))
