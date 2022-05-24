# Написать функцию, которая вычислит площадь и объем конуса по его радиусу и высоте.
# Результат работы функции должен вернуть два значения.
# def cone_square_and_volume(radius, height): # returns 2 floats
#			pass

import math

radius = int(input("Введите радиус конуса radius = "))
height = int(input("Введите высоту конуса height = "))

def cone_square_and_volume(radius, height):
    cone_square = math.pi * radius * (radius + height)
    cone_volume = height / 3 * math.pi * (radius**2)
    return(cone_square, cone_volume)

cone_squre, cone_volume = cone_square_and_volume(radius, height)
print("Square of cone = ", cone_squre, "Volume of cone = ", cone_volume)
