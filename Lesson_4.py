#Work with Github

#Repeating work with strings
import math

s = 'github'
print(s[:3])
print(s[3:])
print(s[-3:])
print(s[-6:-3])


#Functions

def power(base, exp):
    return base**exp

result = power(3, 2)
print(result)

print('******************************')
#************************************

def print_delimeter_stars(symbol = '*', num_repeat=23):
    print(symbol * num_repeat)

def pretty_print(value):
    print_delimeter_stars()
    print('Value:', value)
    print_delimeter_stars('+', 33)

#************************************

def rectangle_square(width, heigth):
    result = width*heigth
    return result

result2 = rectangle_square(10, 20)
pretty_print(result2)

print('******************************')
#*************************************
my_pi = math.pi

def circle_square(radius):
    result = power(radius, 2) * my_pi
    return result

result3 = circle_square(10)
pretty_print(result3)

print('*******************************')
#**************************************

def calculate_sum_and_product(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

result4, result5 = calculate_sum_and_product(2, 3)
pretty_print(result4)
pretty_print(result5)

#Debug
