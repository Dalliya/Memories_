#Nested lists(Вложенные списки):

import random

table = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(type(table))
print(type(table[0][0]))

matrix = table

def pretty_print_matrix(matrix):
    print()
    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()

def multiply_matrix_by_n(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= n

#           print('%d' % matrix[i][j], end='\t')


def fill_matrix_by_randoms(matrix, lower_bound, upper_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(lower_bound, upper_bound)


pretty_print_matrix(matrix)
multiply_matrix_by_n(matrix, 10)
pretty_print_matrix(matrix)
fill_matrix_by_randoms(matrix, 100, 333)
pretty_print_matrix(matrix)

