import numpy as np
#
def grad(v):
    x, y = v
    return np.array([-2*(1 - x) - 400*x*(y - x*x), 200*(y - x*x)])
#
def hess(v):
    x, y = v
    return np.array([[2 - 400*(y - x*x) + 800*x*x, -400*x],
                     [-400*x, 200.0]])
#
def newton(v, steps=50, tol=1e-6):
    for k in range(steps):
        g = grad(v)
        if np.linalg.norm(g) < tol:
            return v, k
        v = v - np.linalg.solve(hess(v), g)
    return v, steps
#
print(newton(np.array([-1.2, 1.0])))
