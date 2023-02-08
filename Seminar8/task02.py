# Измерены значения IQ выборки студентов,обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95

import math
import numpy as np
import scipy.stats as stats

array = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
n = len(array)
a = 0.05
m = np.mean(array)
print(f'Среднее выборочное = {m}')
t = stats.t.ppf(1-(a / 2), n - 1)
print(f'Табличное значение t-критерия = {t}')
str = np.std(array, ddof=1)
print(f'Среднее квадратическое отклонение = {str}')
result1 = m - t * (str / math.sqrt(n))
result2 = m + t * (str / math.sqrt(n))
print(f'Доверительный интервал для математического ожидания с надежностью 0.95 = ({result1}, {result2})')