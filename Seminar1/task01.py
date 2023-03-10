# Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз

import numpy as np
from math import factorial


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


m = combinations(13, 4)  # число благоприятных исходов 13 карт одной масти и исход 4 из 13
n = combinations(52, 4)  # общее количество исходов взятия 4 карт из всей колоды
result1 = round(m / n, 4)
print(f'Вероятность того, что все карты – крести = {result1}')

m = combinations(48, 4)  # число исходов, когда 4 карты туз и 48 точно не туз
n = combinations(52, 4)  # общее количество исходов взятия 4 карт из всей колоды
result2 = 1 - round(m / n, 4)  # вычитаем из 1 вероятность того, что точно не туз
print(f'Вероятность того, что среди 4-х карт окажется хотя бы один туз = {result2}')
