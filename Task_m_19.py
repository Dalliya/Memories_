# Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit случайно сгенерированных чисел в
# указанном числовом диапазоне.
# def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
# pass

import random

lower_bound = int(input('Input lower bound: '))
upper_bound = int(input('Input upper bound: '))
num_limit = 101

def diff_min_max(num_limit, lower_bound, upper_bound):
    lst = []
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        lst.append(rand_num)
    print(lst)
    diff = max(lst) - min(lst)
    return diff

print(diff_min_max(num_limit, lower_bound, upper_bound))





