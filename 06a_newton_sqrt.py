def newton_sqrt(S, x=1.0, steps=5):
    for k in range(steps):
        x = (x + S / x) / 2   # one Newton step
        print(k + 1, x)
    return x
#
newton_sqrt(2)
