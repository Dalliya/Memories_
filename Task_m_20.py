# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit случайно сгенерированных чисел
# в указанном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
# 		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
# 		     pass

import random

lower_bound = int(input('Input lower bound: '))
upper_bound = int(input('Input upper bound: '))
num_limit = 101

def diff_even_odd(num_limit, lower_bound, upper_bound):
    rand_even_total = 0
    rand_odd_total = 0
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        if rand_num % 2 == 0:
            rand_even_total += rand_num
        elif rand_num % 2 != 0:
            rand_odd_total += rand_num
    diff = rand_even_total - rand_odd_total
    return diff

print(diff_even_odd(num_limit, lower_bound, upper_bound))



