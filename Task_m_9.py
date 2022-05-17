#Написать функцию, которая будет переводить градусы в радианы (без использования math.radians).
#Используя эту функцию, вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
#def degrees2radians(degrees): # returns float
#			pass

import math

my_pi = math.pi

def print_delimeter_stars(symbol = '*', num_repeat=23):
    print(symbol * num_repeat)

def pretty_print(value):
    print_delimeter_stars()
    print('Значение косинуса угла:', value)
    print_delimeter_stars()

#**********************************************************
def degrees2radians(degrees):
    result = float((degrees * my_pi) / 180)
    return result

result1 = degrees2radians(60)
pretty_print(result1)

result2 = degrees2radians(45)
pretty_print(result2)

result3 = degrees2radians(40)
pretty_print(result3)
