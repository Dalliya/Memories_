#Вывести на экран талицу Пифагора

def mult_table(rows, colomns):
    for i in range(1, rows + 1):
        for j in range(1, colomns + 1):
            print("{}" .format(i * j), end='\t')
        print()

mult_table(9, 9)

#Вывести на экран шахматную доску

def chess_table(rows = 8):
    for i in range(1, rows + 1):
        for c in 'ABCDEFGH':
            print("{}{}".format(c, i), end='\t')
        print()
chess_table()