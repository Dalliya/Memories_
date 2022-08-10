#List_Comprehensions
import string
import random
import Lesson_9_Nested_lists_matrix

lst = [i for i in range(10)]
print(lst)

print("*****************************************************************")

lst = [i ** 2 for i in range(10)]
print(lst)

print("*****************************************************************")

lst = [i ** 2 for i in range(100) if (i ** 2) % 5 == 0]
print(lst)

print("*****************************************************************")

lst = []
for i in range(100):
    if (i ** 2) % 5 == 0:
        lst.append(i ** 2)
print(lst)

print("*****************************************************************")

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
digits = [str(i) for i in range(10)]


print(alphabet)
print(digits)
print(type(digits))
print(''.join(alphabet))
print(''.join(digits))

print(string.ascii_lowercase)
print(string.digits)

print("*****************************************************************")

random_lst = [random.randint(-5, 5) for i in range(10)]
print(random_lst)

columns = 5
rows = 3
matrix = [[0]*columns for i in range(rows)]
Lesson_9_Nested_lists_matrix.pretty_print_matrix(matrix)

random_matrix = [[random.randint(-5, 5) for _ in range(columns)] for _ in range(rows)]
Lesson_9_Nested_lists_matrix.pretty_print_matrix(random_matrix)

print("*****************************************************************")

print(sum([1, 2, 3]))

print("*****************************************************************")

print(sum(i for i in range(1, 101)))
print(min(i for i in range(1, 101)))
print(max(i for i in range(1, 101)))

print(max(random.randint(-50, 50) for _ in range(100)))

print("*****************************************************************")

#Рекурсия

#Написать рекурсию, которая содержит i-тое число Фибоначчи

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

print("*****************************************************************")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

