#Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )⁴+ | a |
import math

a = 33
b = 1
c = 12

result = (math.log(1 + c) / - b)**4 + abs(a)

print('Результат выражения ( ln( 1 + c ) / -b )⁴+ | a |) при a = {}, b = {}, c = {} равен {:.3f}'.format(a, b, c, result))