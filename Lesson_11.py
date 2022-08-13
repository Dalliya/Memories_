import string
import random
import math

def calc_pi():
    dots = [[random.random(), random.random()] for i in range(1000)]

    num_of_dots_inside_circle = sum(1 for dot in dots
                if math.sqrt((0.5-dot[0])**2 + (0.5-dot[1])**2) <= 0.5)

    num_of_dots_inside_square = len(dots)

    my_pi = num_of_dots_inside_circle/(num_of_dots_inside_square*(0.5**2))
    return my_pi

avr_pi = sum(calc_pi() for _ in range(1000)) / 1000
print(avr_pi)

print("*****************************************************************")

#Сортировка списков

lst = [2, 1, 3]
lst.sort()
print(lst)

lst = ['aba', 'b', 'aaa', 'cc']
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)



