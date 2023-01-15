# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

from task01 import combinations

m = combinations(9, 3)  # число благоприятных исходов 3 деталей из 9 окрашенных
n = combinations(15, 3)  # общее количество исходов взятия 3 деталей из ящика
result = round(m / n, 4)
print(f'Вероятность того, что все извлеченные детали окрашены = {result}')