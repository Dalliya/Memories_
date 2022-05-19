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
    if number == 0:
        return True
    else:
        return False

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

year_of_birth = 1942

if year_of_birth >= 1981 and year_of_birth <= 2000:
    pretty_print("I'm Millenial")
else:
    pretty_print("I'm not Millenial")

#************************************

s1 = 'Hillel'

if 'h' in s1 or 'x' in s1:
    pretty_print('h/H inside')
else:
    pretty_print('h/H not inside')