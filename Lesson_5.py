#Repeat of Lesson 4

def print_delimeter_stars(symbol = '*', num_repeat=23):
    print(symbol * num_repeat)

def pretty_print(value):
    print_delimeter_stars()
    print('Value:', value)
    print_delimeter_stars()

#*************************************************************

def faren2celc(degrees):
    return (degrees - 32) / 1.8

def celc2faren(degrees):
    return degrees *1.8 + 32

pretty_print(faren2celc(36.6))

#Work with GitHub & Slack



