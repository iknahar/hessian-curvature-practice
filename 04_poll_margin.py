import sympy as sp
#
p = sp.symbols("p", positive=True)
n, k = 1000, 520
ell = k * sp.log(p) + (n - k) * sp.log(1 - p)
bend = sp.diff(ell, p, 2).subs(p, sp.Rational(k, n))
se = sp.sqrt(-1 / bend)
print(round(float(bend), 1), round(float(se), 4), round(float(1.96 * se), 4))
