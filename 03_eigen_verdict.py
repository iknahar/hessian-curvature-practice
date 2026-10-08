import numpy as np
#
def verdict(H, tol=1e-9):
    lam = np.linalg.eigvalsh(H)  # H is symmetric, so this is safe
    if np.all(lam > tol):
        return lam, "minimum"
    if np.all(lam < -tol):
        return lam, "maximum"
    if lam.min() < -tol and lam.max() > tol:
        return lam, "saddle"
    return lam, "no verdict"
#
for H in ([[2, 3], [3, 2]], [[3, 1], [1, 2]], [[-2, 0], [0, -1]]):
    print(verdict(np.array(H, dtype=float)))
