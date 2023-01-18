# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

from task03 import *
from task02 import *

p1 = (combinations(7, 2) * combinations(3, 0)) / combinations(10, 2)  # вероятность, когда два мяча белые в первом ящике
p2 = combinations(9, 2) * combinations(2, 0) / combinations(11, 2)  # вероятность, когда два мяча белые во втором ящике
result = p1 * p2
print(f'Вероятность того, что все мячи белые = {result}')

t1 = ((combinations(7, 2) * combinations(3, 0)) / combinations(10, 2)) * (
        (combinations(9, 0) * combinations(2, 2)) / combinations(11,
                                                                 2))  # вероятность, когда два мяча белые в первом ящике и 0 во втором
t2 = (combinations(9, 2) * combinations(2, 0) / combinations(11, 2)) * (
        (combinations(7, 0) * combinations(3, 2)) / combinations(10,
                                                                 2))  # вероятность, когда два мяча белые в втором ящике и 0 в первом
t3 = ((combinations(7, 1) * combinations(3, 1)) / combinations(10, 2)) * (
        (combinations(9, 1) * combinations(2, 1)) / combinations(11,
                                                                 2))  # вероятность, когда 1 мяч из первого ящика и 1 из второго

result2 = t1 + t2 + t3
print(f'Вероятность того, что ровно два мяча белые = {result2}')

s1 = combinations(3, 2) / combinations(10, 2)  # вероятность, когда все мячи не белые в первом ящике
s2 = combinations(2, 2) / combinations(11, 2)  # вероятность, когда все мячи не белые во втором ящике
result3 = 1 - (s1 * s2)  # обратная вероятность, вычитаем вероятность когда все белые
print(f'Вероятность того, что хотя бы один мяч белый = {result3}')
