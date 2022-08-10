#Напечатать таблицу Пифагора заданной конфигурации.

def print_mult_table(n, m): # prints multiplication table n x m
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("{}". format(i * j), end='\t')
        print()
print_mult_table(9, 9)

