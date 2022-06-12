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
        break

    if user_choice == '1':
        print('Лошадку жалко')

    if user_choice == '2':
        print('Поздравляю с полцарством!')

    if user_choice == '3':
        print('Вторые полцарства нашел!')




