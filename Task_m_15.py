# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.
# def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
#			pass

import math

x1 = int(input("Input x1 of the centre = "))
x2 = int(input("Input x2 of the centre = "))
y1 = int(input("Input y1 of the centre = "))
y2 = int(input("Input y2 of the centre = "))
r1 = int(input("Input value of the 1-st radius = "))
r2 = int(input("Input value of the 2-nd radius = "))

def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.fabs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

    if d == math.fabs(r1 - r2):
        return True #Окружности соприкасаются в одной точке

    if d == math.fabs(r1 + r2):
        return True #Окружности соприкасаются в одной точке

    if math.fabs(r1 - r2) < d < (r1 + r2):
        return True #Окружности соприкасаются в двух точках

    else:
        return False

print(circles_intersect(x1, y1, r1, x2, y2, r2))






