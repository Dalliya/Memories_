#Boolean значения: True or False

#********************************************************
def print_delimeter_stars(symbol = '*', num_repeat=23):
    print(symbol * num_repeat)

def pretty_print(value):
    print_delimeter_stars()
    print('Answer:', value)
    print_delimeter_stars()
#********************************************************

a = 23
b = 5
c = 10

equal_to_zero = a == 0
denominator_is_zero = (a + c) == 0

def is_zero(number):
    return number == 0
 #   if number == 0:
 #      return True
 #  else:
 #       return False

if (a + c) != 0:
    result = b / (a + c)
    pretty_print(result)
else:
    print('Devision by zero!')

#************************************

if is_zero(42):
    print('Devision by zero!')
else:
    result = b / (a + c)
    pretty_print(result)

#************************************

year_of_birth = 1999

def is_millenial(year_of_birth):
    return 1981 <= year_of_birth >= 2000

if is_millenial(year_of_birth):
    pretty_print("I'm Millenial")
else:
    pretty_print("I'm not Millenial")

#    if year_of_birth >= 1981 and year_of_birth <= 2000:
#        pretty_print("I'm Millenial")
#        return True
#    else:
#        pretty_print("I'm not Millenial")
#        return False

#************************************

s1 = 'Hillel'

if 'h' in s1 or 'x' in s1:
    pretty_print('h/H inside')
else:
    pretty_print('h/H not inside')

#****************************************

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap_year(2017))

#*****************************************

name = input("Enter your name: ")
print(name, type(name))

age = int(input("Enter your age: "))
print(age, type(age))