#Задача 4. Рост взрослого населения города X имеет нормальное распределение, причем, средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
# посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
#1. больше 182 см?
#2. больше 190 см?
#3. от 166 см до 190 см?
#4. от 166 см до 182 см?
#5. от 158 см до 190 см?
#6. не выше 150 см или не ниже 190 см?
#7. не выше 150 см или не ниже 198 см?
#8. ниже 166 см?

#Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.), а затем проверить себя с помощью встроенных функций

from scipy import stats
result1=1-stats.norm.cdf(182, loc=174, scale=8)
result2=1-stats.norm.cdf(190, loc=174, scale=8)
result3=stats.norm.cdf(190, loc=174, scale=8)-stats.norm.cdf(166, loc=174, scale=8)
result4=stats.norm.cdf(182, loc=174, scale=8)-stats.norm.cdf(166, loc=174, scale=8)
result5=stats.norm.cdf(190, loc=174, scale=8)-stats.norm.cdf(158, loc=174, scale=8)
result6=(1-stats.norm.cdf(190, loc=174, scale=8))+stats.norm.cdf(150, loc=174, scale=8)
result7=(1-stats.norm.cdf(198, loc=174, scale=8))+stats.norm.cdf(150, loc=174, scale=8)
result8=stats.norm.cdf(166, loc=174, scale=8)
print(f'Вероятность больше 182 см = {result1}\nВероятность больше 190 см = {result2}\nВероятность от 166 см до 190 см = {result3}\n'
      f'Вероятность от 166 см до 182 см = {result4}\nВероятность от 158 см до 190 см = {result5}\n'
      f'Вероятность не выше 150 см или не ниже 190 см = {result6}\nВероятность не выше 150 см или не ниже 198 см = {result7}\n'
      f'Вероятность ниже 166 см = {result8}\n')