import pprint
import string

def words_count(path_to_file, path_to_stop_words, top_n = 10):

    #text = open('hhgttg.txt', encoding='utf8').read().lower() #открыть файл и прочесть его содержимое/ опущение результата в нижний регистр функцией .lower()
    text = open(path_to_file, encoding='utf8').read().lower()
    word_list = text.split()#нарезка строки на слова

    #stop_words = open('stop_words_list.txt', encoding='utf8').read().lower() #открыть файл и прочесть его содержимое/ опущение результата в нижний регистр функцией .lower()
    stop_words = open(path_to_stop_words, encoding='utf8').read().lower()
    stop_word_list = text.split()#нарезка строки на слова

    #print(text[:100]) #распечатка первых 100 символов текста
    #print(len(word_list))#длина списка
    word_count = {} #заводим пустой словарь, куда запишем количество вхождений слова в текст
    for word in word_list: #создание цикла
        word = word.strip(string.punctuation) #метод отсечения слева и справа того, что я ему передам/ string.punctuation - передача пунктуации
                                          # из библиотеки string/ смена исходной строчки введением нового присваивания word
        #if word in stop_word_list:
        #     continue #если слово в списке stop_words_list, то пропускаем его, ничего не делаем, никуда не записываем и продолжаем цикл
        #или
        if word not in stop_word_list: #если слово не в списке stop_word_list, то начинаем цикл
            if word: #если слово не пустое
                word_count[word] = word_count.get(word, 0) + 1 #возврат 0, если значения по заданному ключу word нет


                #if word in word_count:#если слово находится в словаре
                #    word_count[word] += 1 #значение ассоциированное со словом увеличиваем на 1
                #else:
                #    word_count[word] = 1



    #pprint.pprint(word_count)#Посчитать количество повторений каждого слова в тексте

    for word in sorted(word_count, key=word_count.get, reverse=True)[:top_n]: #sorted()возврат отсортированного списка через функцию/ вычленение подсписка *если мне нужно провести
        print('%s -> %d' % (word, word_count[word])) #сортировку списка, то просто взять этот фрагмент кода и пользоваться им

words_count(r'C:\Users\utilisateur\PycharmProjects\Memories\hhgttg.txt', r'C:\Users\utilisateur\PycharmProjects\Memories\stop_words_list.txt')


print('******************************************************************************************')

# Функция hash()

#hash() - функция, которая преобразует строковое значение в числовое
#Например: hash('abc')
##########################################################################################################"

#Modul Dictionaries:

#real examples:
person_1 = {'name': 'Richard Feynman',
            'age': 99,
            'birth_place': 'USA',
            'birth_date': "1918-01-01",
            'awards': ('Nobel Prize in Physics', 'USA Science Medal')}

person_2 = {'name': 'Albert Einstein',
            'age': 138,
            'birth_place': 'Germany',
            'birth_date': "1879-03-14",
            'awards': ('Nobel Prize in Physics', 'Planck Medal')}

person_3 = {'name': 'Nicola Tesla',
            'age': 161,
            'birth_place': 'Croatia',
            'birth_date': "1856-07-10",
            'awards': ('Edison Medal')}

physicits = (person_1, person_2, person_3)
pprint.pprint(physicits)

#add new key_value pairs
person_1['hobby'] = "painting"
person_2['hobby'] = "violin"
person_3['hobby'] = "pigeons"
pprint.pprint(physicits)

#get with default
employee_1 = {"name": "Alex", "salary": 10000, "dep": "Sales", "bonus": 200}
employee_2 = {"name": "Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name": "Sue", "salary": 50000, "dep": "IT", "bonus": 500}
employee_4 = {"name": "Phil", "salary": 5000, "dep": "BoardOfDirectors", "bonus": 100}

employees = [employee_1, employee_2, employee_3, employee_4]
for i in range(len(employees)):
    # current_salary = employees[i]['salary']
    # new_salary = current_salary * 2
    # employees[i]['salary'] = new_salary
    employees[i]['salary'] *= 2

pprint.pprint(employees)

for i in range(len(employees)):
    if 'bonus' in employees[i]:
        employees[i]['bonus'] *= 2
    else:
        employees[i]['bonus'] = 1000

pprint.pprint(employees)
employees.sort(key=lambda elem: elem['name'])
pprint.pprint(employees)

employees.sort(key=lambda elem: elem['bonus'])
pprint.pprint(employees)



