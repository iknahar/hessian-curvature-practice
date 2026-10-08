# Hessian, Curvature and Second Order Conditions: practice code

Small, runnable Python scripts for learning the Hessian matrix: how to build it,
how to classify flat spots (minimum, maximum, saddle), where standard errors come
from, Newton's method, numerical Hessians and conditioning.

## Setup

```bash
python -m pip install -r requirements.txt
```

## Scripts

| File | What it shows |
|---|---|
| `01_hessian_by_hand.py` | Build a Hessian with SymPy and confirm the two mixed partials match |
| `02_classify_flat_spots.py` | Find every critical point of x³ − 3x + y³ − 3y and classify it with the determinant test |
| `03_eigen_verdict.py` | Classify any Hessian from the signs of its eigenvalues |
| `04_coin_standard_error.py` | Curvature of a coin-flip log-likelihood gives the textbook standard error |
| `05_logistic_standard_errors.py` | Logistic regression standard errors by hand, and what a duplicated column does |
| `06_newton.py` | Newton's method on the Rosenbrock valley (6 steps) |
| `07_numeric_hessian.py` | A finite-difference Hessian checked against the exact one |
| `08_conditioning.py` | Condition number of the Longley regression Hessian, raw vs standardised |

Run any of them with `python 01_hessian_by_hand.py` and so on.

## Exercises

**1.** Classify the origin for f(x, y) = x² + 3xy + y². Then for x² + xy + y².

<details><summary>Answer</summary>

Hessians are [[2, 3], [3, 2]] and [[2, 1], [1, 2]]. Determinants are 4 − 9 = −5 (saddle)
and 4 − 1 = 3 with f_xx = 2 > 0 (minimum). Check with `03_eigen_verdict.py`:
eigenvalues (−1, 5) and (1, 3).
</details>

**2.** In `04_coin_standard_error.py`, change the data to 60 heads in 100 flips. What happens
to the standard error, and why?

<details><summary>Answer</summary>

It becomes about 0.049, roughly 3.16 times bigger than 0.0155. The curvature is ten times
smaller, and the standard error is one over its square root, so it grows by √10.
</details>

**3.** In `05_logistic_standard_errors.py`, replace the duplicated column with
`X[:, 1] + 0.01 * rng.normal(size=500)`. Are the standard errors still huge?

<details><summary>Answer</summary>

They drop from about 12 million to about 12.3, still roughly a hundred times the honest
0.15. The smallest eigenvalue of the negative Hessian is no longer zero, only tiny, so the
ridge has a little curvature.
Near-duplicates are the quiet version of the same problem.
</details>

**4.** Start `06_newton.py` from (0.8, 0.3) on f(x, y) = x² − y² + y⁴/4 instead. Where does it end?

<details><summary>Answer</summary>

Gradient: (2x, −2y + y³). Hessian: [[2, 0], [0, −2 + 3y²]]. Newton lands on (0, 0),
which is a saddle, in about 3 steps. Gradient descent from the same start reaches the
minimum at (0, √2).
</details>

**5.** In `07_numeric_hessian.py`, try h = 1e-2 and h = 1e-7. Which is closer to the exact
[[1330, 480], [480, 200]]?

<details><summary>Answer</summary>

h = 1e-2 gives 1330.08 for the top-left entry, slightly off because the step is coarse.
h = 1e-7 gives 1329.692 and 199.485, worse, because rounding error dominates when you
subtract nearly equal numbers. Around 1e-4 is the sweet spot for second differences.
</details>

## License

MIT
