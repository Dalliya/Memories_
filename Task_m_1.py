# Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )

# New style format
a = 5
b = 10
c = 15

result = a + b * (c/2)

print('Результат выражения (a + b * (c/2) при a = {}, b = {}, c = {} равен {:.3f}'.format(a, b, c, result))

print("**********************************************************************")
# Old style format

a = 5
b = 10
c = 15

result = a + b * (c/2)

print("Результат выражения (a + b * (c/2) при a = %d , b = %d и c = %d равен: %.3f" % (a, b, c, result))



