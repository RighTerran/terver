#Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз

import math
import numpy as np


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

k = 85
n = 100
p = 0.8
c = combinations(n, k)
result = c * math.pow(p, k) * math.pow(1-p, n-k)
print(f'Вероятность того, что стрелок попадет в цель ровно 85 раз = {result}')
