# Пользователь вводит длины катетов прямоугольного треугольника. Написать функцию, которая вычислит площадь треугольника и его периметр.
# Результат работы функции должен вернуть два значения.
# def triangle_square_and_perimeter(a, b): # returns 2 values
#		Pass

import math

a = int(input("Введите длину катета прямоугльного треугольника а = "))
b = int(input("Введите длину катета прямоугольного треугоьника b = "))

def triangle_square_and_perimeter(a, b):
    S = 0.5 * a * b
    P = a + b + math.sqrt(a**2 + b**2)
    return(S, P)

S, P = triangle_square_and_perimeter(a, b)
print("Square of triangle: ", S, "Perimetr of triangle: ", P)
