#Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию, которая переставляет его элементы в случайном
#порядке (например, 99 11 43 19 … 7 91 3 1).
#Примечание: использовать метод random.shuffle не допускается.

import random

list_to_shuffle = [i for i in range(101) if i % 2 != 0]
print(list_to_shuffle)

def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
    lst = []
    for i in range(1, 101):
        rand_num = random.choice(list_to_shuffle)
        lst.append(rand_num)
    print(lst)

shuffle_list(list_to_shuffle)
