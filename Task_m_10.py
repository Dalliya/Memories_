# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли,
# без использования операторов цикла.
# a) cо строками, б) без использования строк.
# def sum_of_digits(number): # returns int
#			pass

#a) with strings:
number = input("Введите трехзначное число: ")

def sum_of_digits_a(number):
    sum = int(number[0]) + int(number[1]) + int(number[2])
    return sum

sum = sum_of_digits_a(number)
print(sum)

print("***************************************************")
#**********************************************************

#b) without strings:
number1 = input("Введите трехзначное число: ")

def sum_of_digits_b(number1):
    result = int(number1) // 100 + int(number1) % 100 // 10 + int(number1) % 10
    return result

result = sum_of_digits_b(number1)
print(result)






