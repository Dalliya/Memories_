#Dictionaries
#Сервис укорачивания адресов

import pprint

#initialization
dict_en_es = {'world' : 'mundo',
              'language' : 'idioma',
              'See you later' : 'Hasta la vista'}

print(dict_en_es)
print(type(dict_en_es))

print(dict_en_es['world'])

if 'world' in dict_en_es:
    print('Found!')

    capitals = {'UA' : 'Kyiv'}
    print(capitals)
    capitals['US'] = 'Washington'
    print(capitals)
    capitals['IT'] = 'Rome'
    print(capitals)

population = {}
population['UA'] = 48*10**6
population['US'] = 300e6
pprint.pprint(population)
population['UA'] *= 10
pprint.pprint(population)
population['UA'] += 10
pprint.pprint(population)

products = {}
products['BMW'] = ['X1', 'X5', 'X6']
products['Audi'] = ['A1', 'A8']
products['L\'Oreal'] = ['Product1', 'Product2']

pprint.pprint(products)


#add product

products['BMW'].append('X7')
products['Audi'].append('A10')
products['L\'Oreal'].append('Product3')

pprint.pprint(products)

#del product

del products['BMW'] #удаление пары из словаря по ключу
pprint.pprint(products)

if 'BMW' in products:
    print('Found and deleted!')
    del products['BMW']
else:
    print('Not found!')

##################################################################

print('***************************************************************')

for word_en in dict_en_es.keys(): #перебор всех ключей в словаре
    print("%-15s -> %s" % (word_en, dict_en_es[word_en]))

for word_en in dict_en_es:#перебор ключей словаря
    print("%-15s -> %s" % (word_en, dict_en_es[word_en]))

for word_es in dict_en_es.values():#перебор значений словаря
    print("%s" % (word_es))

for k, v in dict_en_es.items():#перебор ключей и значений словаря
    print("%-15s -> %s" % (k, v))

unicode = {i : chr(i) for i in range(10000)}
pprint.pprint(unicode)