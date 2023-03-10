# Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
#
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей.

import math
import numpy as np
import scipy.stats as stats

array1 = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
array2 = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
n = len(array1)
a = 0.05
m1 = np.mean(array1)
m2 = np.mean(array2)
delta = abs(m1 - m2)
print(f'Разность средних = {delta}')
t = stats.t.ppf(1 - (a / 2), 2 * (n - 1))
print(f'Табличное значение t-критерия = {t}')
d = (np.var(array1, ddof=1) + np.var(array2, ddof=1)) / 2
print(f'Дисперсия двух групп = {d}')
s = math.sqrt((d / n) + (d / n))
print(f'Sdelta = {s}')
result1 = delta - t * s
result2 = delta + t * s
print(
    f'Доверительный интервал для разности среднего роста родителей и детей с доверительной вероятностью 0,95 = ({result1},{result2})')
