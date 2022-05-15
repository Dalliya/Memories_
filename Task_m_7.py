#Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
#Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
#Например: 'employee_first_name' -> 'EmployeeFirstName'

snake_case = 'python_zen_formula'
lst = snake_case.split('_')

CamelCase = str.capitalize(lst[0]) + str.capitalize(lst[1]) + str.capitalize(lst[2])

print(CamelCase)
