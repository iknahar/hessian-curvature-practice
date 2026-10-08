import sympy as sp
#
x, y = sp.symbols("x y")
g = x**2 * y + sp.exp(x * y)
H = sp.hessian(g, (x, y))
print(H)
print(sp.simplify(H[0, 1] - H[1, 0]))  # the two twists, compared
