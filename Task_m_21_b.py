# Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
# a) c использованием строк, b) без использования строк.
# def get_max_digit(number): # returns int
# 		     pass

import random
number = random.randint(10 ** 11, 10 ** 12 - 1)
print(number)

def get_max_digit_1(number):
    digit_list_1 = [number]
    lst = slice(digit_list_1)
    max_digit_1 = max(lst)
    return max_digit_1

print(get_max_digit_1(number))
