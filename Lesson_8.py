# Loops with operator while:

import random

x = 10

while x > 0:
    print('Hello world!', x)
    x -= 1

##############################################
print('***************************************')

x = 0
while x < 100:
    print('Hello World!', x)
    x += random.randint(0, 5)

##############################################
print('***************************************')


def fill_truck(max_volume, lower_bound, upper_bound):
    current_volume = 0
    while current_volume < max_volume:
        random_box = random.randint(lower_bound, upper_bound)
        free_space = max_volume - current_volume
        if random_box > free_space:
            print('Skipped random box: %d' % random_box)
        else:
            current_volume += random_box
            print('Current_volume = %d, last random box = %d' %
                  (current_volume, random_box))

fill_truck(1000, 1, 10)

##############################################
print('***************************************')

print('Привет богатырь!')
print('1: Прямо пойдешь - коня потеряешь')
print('2: Налево пойдешь - полцарства найдешь')
print('3: Направо пойдешь - <сюрприз>')

while True:
    user_choice = input("Сделай свой выбор ('q' - выход): ")

    if user_choice == 'q':
        print('Пока!')
        break

    valid_user_choice = user_choice.isnumeric() and 1 <= int(user_choice) <= 3
    if not valid_user_choice:
        print('Неверный ввод. Повторите свой выбор [1..3].')
        continue

    if user_choice == '1':
        print('Лошадку жалко')

    elif user_choice == '2':
        print('Поздравляю с полцарством!')

    elif user_choice == '3':
        print('Вторые полцарства нашел!')

#####################################################

# Lists:

lst = [1, 2, 3]
print(type(lst))
print(lst)

print(lst[0])
print(lst[1])
print(lst[2])

lst[0] = 42
print(lst)

#####################################################
print('********************************************')

lst_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
lst_2 = ['aaa', 'bbb', 'ccc']

print(type(lst_1), type(lst_2))
print(lst_1)
print(len(lst_1), len(lst_2))


print("Elem #1: ", lst_1[0])
print("Elem #2: ", lst_1[1])
print("Elem #3: ", lst_1[2])

lst_1[0] = 42
print(lst)

def multiply_lst_by_n(lst_1, n):
    for i in range(len(lst_1)):
        print('Element #%d:' % i, lst_1[i])
        lst_1[i] *= n

def pretty_print_lst(lst_1):
    print('*****List*****')
    for elem in lst_1:
        print('Elem: ', elem)

multiply_lst_by_n(lst_1, 25)
pretty_print_lst(lst_1)




