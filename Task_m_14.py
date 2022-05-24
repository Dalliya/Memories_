#Написать функцию, которая будет проверять четность некоторого числа.
#		def is_even(number): # returns boolean value
#			pass

number = int(input("Input any number: "))

def is_even(number):
    return (number % 2) == 0

result = is_even(number)
print(result)
