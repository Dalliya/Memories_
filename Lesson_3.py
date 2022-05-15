import math

#Calculate square of rectangle

radius = 22

circle_square = radius**2 * math.pi

print('Площадь круга при радиусе = {} равна: {:.3f} кв.см'.format(radius, circle_square))

print('***************************************************************')

#Тип данных - строки

s1 = "abcd"
s2 = 'abcd'
print(type(s1))
print(type(s2))

print('**************************************')

current_time = '18:29:01'
hours = int(current_time[:2])
minutes = int(current_time[3:5])
seconds = int(current_time[6:])

total_seconds = hours*3600 + minutes*60 + seconds
print('Total seconds: {}'.format(total_seconds))



