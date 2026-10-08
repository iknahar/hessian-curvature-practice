import numpy as np
import statsmodels.api as sm
#
d = sm.datasets.longley.load_pandas().data
X = d.drop(columns="TOTEMP").to_numpy()
Xraw = sm.add_constant(X)
Z = sm.add_constant((X - X.mean(0)) / X.std(0))
print(f"{np.linalg.cond(Xraw.T @ Xraw):.2e}")
print(f"{np.linalg.cond(Z.T @ Z):.2e}")
