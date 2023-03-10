# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from task01 import combinations

m = combinations(2, 2)  # 2 билета из 2 выйграшных или 1
n = combinations(100, 2)  # общее количество исходов взятия 2 билетов из общего количества
result = round(m / n, 4)
print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {result}')