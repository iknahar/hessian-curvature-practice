import numpy as np
import statsmodels.api as sm
#
np.set_printoptions(suppress=True)
rng = np.random.default_rng(7)
X = sm.add_constant(rng.normal(size=(500, 2)))
beta = np.array([-0.5, 1.0, -2.0])
y = (rng.random(500) < 1 / (1 + np.exp(-X @ beta))).astype(float)
fit = sm.Logit(y, X).fit(disp=0)
print(np.asarray(fit.bse).round(4))
#
X2 = np.column_stack([X, X[:, 1]])  # the same column, twice
fit2 = sm.Logit(y, X2).fit(disp=0)
print(np.asarray(fit2.bse).round(2))
p = fit.predict(X)
H2 = -(X2.T * (p * (1 - p))) @ X2
print(np.linalg.eigvalsh(-H2).round(3))
