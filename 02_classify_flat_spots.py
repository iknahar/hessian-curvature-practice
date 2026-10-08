import sympy as sp
#
x, y = sp.symbols("x y")
f = x**3 - 3*x + y**3 - 3*y
grad = [sp.diff(f, v) for v in (x, y)]
H = sp.hessian(f, (x, y))
for pt in sp.solve(grad, (x, y), dict=True):
    Hp = H.subs(pt)
    D = Hp.det()
    if D < 0:
        kind = "saddle"
    elif D > 0 and Hp[0, 0] > 0:
        kind = "minimum"
    elif D > 0:
        kind = "maximum"
    else:
        kind = "no verdict"
    print(pt, Hp.tolist(), kind)
