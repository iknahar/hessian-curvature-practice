import sympy as sp
#
p, n, k = sp.symbols("p n k", positive=True)
ell = k * sp.log(p) + (n - k) * sp.log(1 - p)
curv = sp.simplify(sp.diff(ell, p, 2).subs(p, k / n))
print(curv)
se = sp.sqrt(-1 / curv)
print(sp.simplify(se))
print(se.subs({n: 1000, k: 600}).evalf(4))
