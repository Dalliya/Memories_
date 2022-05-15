import math

width = 15
height = 22

rectangle_square = width * height

print('Площадь прямоугольника при ширине = {}, высоте = {} равна: {:.3f}' .format(width, height, rectangle_square))

print('*********************************************************')

catheter1 = 8
catheter2 = 90
hypotenuse = math.sqrt(catheter1**2 + catheter2**2)

print('Значение гипотенузы трегольника при катете1 = {} и катете2 = {} равно: {:.3f}' .format(catheter1, catheter2, hypotenuse))