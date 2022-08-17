import pprint
import string
import random
import math
import Lesson_8

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

#Сортировка списков. Сортировка списков по ключу

lst = [2, 1, 3]
lst.sort()
print(lst)

lst = ['aba', 'b', 'aaa', 'cc']
lst.sort()
print(lst)

lst.sort(reverse=True, key=len)
print(lst)

lst.sort(key=len)
print(lst)

print("*****************************************************************")

def get_distance_from_poi(elem):
    return abs(10 - elem)

pois = [9, 6, 8, 11, 123, 0]

pois.sort(key=lambda elem: abs(10 - elem))
print(pois)

#pois.sort(key=get_distance_from_poi)
#print(pois)
#pois.sort()
#print(pois)

print("*****************************************************************")

full_names = [
    'Михайловский Владимир',
    'Шишкин Сергей',
    'Мазур Андрей',
    'Шияев Павел',
    'Трусов Дмитрий',
    'Дулгеров Олег',
    'Жданова Дария',
    'Каминская Екатерина',
    'Железняк Игорь',
    'Полоз Евгений',
    'Захидова Сабина',
    'Лигута Иван',
    'Величко Алексей'
]

#def get_first_name(elem):
#    return elem.split(' ')[1]

#full_names.sort(reverse=True, key=get_first_name)
#Lesson_8.pretty_print_lst(full_names)
#pprint.pprint(full_names)

#full_names.sort(reverse=True)
#pprint.pprint(full_names)

#Анонимные функции(Называются "Лямбды" - это функции в которых есть только тело и логика.

full_names.sort(reverse=True, key=lambda  elem: elem.split(' ')[1])
Lesson_8.pretty_print_lst(full_names)
pprint.pprint(full_names)

print("*****************************************************************")

group = [
    ['Михайловский Владимир', '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Шишкин Сергей', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Мазур Андрей', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Шияев Павел', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Трусов Дмитрий', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Дулгеров Олег', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Жданова Дария', '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1'],
    ['Каминская Екатерина', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'],
    ['Железняк Игорь', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Полоз Евгений', '1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Захидова Сабина', '1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Лигута Иван', '1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0'],
    ['Величко Алексей', '1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0']
]

def print_full_names(group):
    print('\n\n---Students---')
    for i in range(len(group)):
        print(group[i][0])


def print_full_names_sorted(group):
    group.sort()
    print_full_names(group)

def print_ranks(group):
    print('\n\n--- Students Ranks ---')
    for i in range(len(group)):
        lst = group[i][1].split(',')

#        print(sum(int(lst[i]) for i in range(len(lst))))
#        print(sum(int(elem) for elem in lst))

#        print('BEFORE:', lst)
        for j in range(len(lst)):
            lst[j] = int(lst[j])
#        print('AFTER:', lst)
#        print(sum(lst))
        group[i][1] = sum(lst)
        print(group[i][0], group[i][1])

def print_top_unique_n(group, n=3):
    print('\n\n--- Top Students Ranks ---')
    group.sort(key=lambda elem: elem[1], reverse=True)
    num_unique_elems = 0
    prev_elem = -1
    for elem in group[:n]:
        if prev_elem != elem[1]:
            num_unique_elems += 1
        prev_elem = elem[1]
        print(elem[0], elem[1])
        if num_unique_elems == n:
            break

#    print(group)



print_full_names(group)
print_full_names_sorted(group)
print_ranks(group)
students = group
print_top_unique_n(group=students)
