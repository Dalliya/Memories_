# Lists

for i in range(1, 1000):
    v = i + 1
    v2 = i + 1
    if id(v) != id(v2): 
        print('found diff: %d' % v)
        break
    else:
        print('same(%d): %d, %d' % (v, id(v), id(v2)))

print('**************************************************************')
#######################################################################
print('**************************************************************')

import random
def fill_list_by_randoms(lst, lower_bound, upper_bound):
    for i in range(len(lst)):
        lst[i] = random.randint(lower_bound, upper_bound)

lst2 = [0] * 9
fill_list_by_randoms(lst2, 10, 20)

print("*****************************************************************")
##########################################################################
print("*****************************************************************")

#Nested Loops(Вложенные списки)

for i in range(10):
    for j in range(10):
        print("{}, {}".format(i, j), end='\t|\t')
#       print("%d, %d" % (i, j), end='\t|\t')
    print()

print("*****************************************************************")
##########################################################################
print("*****************************************************************")

def print_cinema_seats(rows, num_of_seats):
    for i in range(1, rows+1):
        print("Ряд {}:".format(i), end='\t')
#       print('Ряд %d: ' % i, end=' ')
        for j in range(1, num_of_seats+1):
            vip_seat = (5 <= i <= 10) and (5 <= j <= 10)
            if vip_seat:
                print("{}*".format(j), end='\t')
#               print('%d*' % j, end='\t')
            else:
                print("{}".format(j), end='\t')
#               print('%d' % j, end='\t')

        print()

print_cinema_seats(15, 20)

print("*****************************************************************")
##########################################################################
print("*****************************************************************")




