# Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно.
# Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
#		def sum_symbol_codes(first, last): # returns int
#			pass

first = input('')
last = input('')

def sum_symbol_codes(first, last):
    sum_total = 0
    for char in range(ord(first), ord(last) + 1):
        sum_total += char
    return sum_total

print(sum_symbol_codes(first, last))

