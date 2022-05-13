#Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)³ - cos( c )
import math

a = 8
b = 12
c = 99

result = abs(a - b) / (a + b)**3 - math.cos(c)

print('Результат выражения | a - b | /( a + b)³ - cos( c ) при a = {}, b = {}, c = {} равен {:.3f}'.format(a, b, c, result))