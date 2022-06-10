# Написать функцию решения квадратного уравнения.
# def solve_quadratic_equation(a, b, c): # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
# pass

#Квадратное уравнение: a * (x ** 2) + b * x + c = 0

import math

a = int(input("Insert value a = "))
b = int(input("Insert value b = "))
c = int(input("Insert value c = "))

def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0 and a != 0:
        result_1 = (-b + math.sqrt(d)) / (2 * a)
        result_2 = (-b - math.sqrt(d)) / (2 * a)
        return result_1, result_2

    if d == 0:
        result = (-b) / (2 * a)
        return result

    else:
        return None, None

print(solve_quadratic_equation(a, b, c))

