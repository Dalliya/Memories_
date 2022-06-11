#Loops - циклы

#for i in range(5):
#    if i % 2 == 0:
#        print("Hello world!", i)
#    else:
#        print("Happy New Year!", i)

#for i in range(100, 20, -2):
#    print("Iteration#: ", i)
import random

for _ in range(10):
    print('print smth!')

##############################################

print('******************************')
for char in 'abc':
    print(char)

##############################################

print('******************************')
for week_day in ['Mo', 'Tu', 'Wd', 'Th', 'Fr', 'St', 'Sn']:
    print(week_day)

##############################################

print('******************************')
for i in range(1, 101):
    print(i)

##############################################

print('******************************')
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

##############################################

print('******************************')

sum_total = 0
for i in range(1, 101):
    sum_total = sum_total + i
print(sum_total)

##############################################

print('******************************')

def sum_of_n(n):
    sum_total_1 = 0
    for i in range(1, n + 1):
        sum_total_1 += i  #sum_total_1 = sum_total_1 + i
    return sum_total_1

print(sum_of_n(100))
print(sum_of_n(10))
print(sum_of_n(3))
print(sum_of_n(42))

################################################"
print('*******************************')

s = 'Вы перешли в режим инкогнито'
print(len(s.split(' ')) - 1)
print(s.count(' '))

################################################"
print('*******************************')

text = 'Вы перешли в режим инкогнито. Вы перешли в режим инкогнито. Вы перешли в режим инкогнито.'

def find_number_of_uppers(text):
    upper_total = 0
    for char in text:
        #print(char)
        if char.isupper():
           upper_total += 1
    return upper_total

print(find_number_of_uppers(text))

################################################"
print('*******************************')

def camelize_me(var_name):
    var_name_lst = var_name.split('_')
    result = ''
    #print(var_name_lst)
    for part_name in var_name_lst:
        #print(part_name, part_name.capitalize())
        result += part_name.capitalize()
    return result

print(camelize_me('this_is_a_long_snake_style_var_name'))
print(camelize_me('style_var_name'))
print(camelize_me('a_b_c_d'))

################################################"
print('*******************************')

def avr_whatever_of_n(n, lower_bound, upper_bound):
    rand_total = 0
    for _ in range(n):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        rand_total += rand_num
    avr_rand = rand_total / n
    return avr_rand

print('%.2f' % avr_whatever_of_n(11, 100, 200))




