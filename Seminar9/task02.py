# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя
# градиентный спуск (без intercept)

import numpy as np

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(x)
b1 = 0.1

def mse_(b1, y=y, x=x, n=len(x)):
    return np.sum((b1 * x - y) ** 2) / n

print(f'mse = {mse_(b1, y, x, 10)}\n')

alpha = 1e-6

for i in range(10):
    b1 -= alpha * (2 / n) * np.sum((b1 * x - y) * x)
    print(f'B1={b1}')
print('___________________________')

for i in range(3000):
    b1 -= alpha * (2 / n) * np.sum((b1 * x - y) * x)
    if i % 500 == 0:
        print(f'Iteranion = {i}, B1={b1}, mse={mse_(b1, y, x)}')
