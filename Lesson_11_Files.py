import pprint
import string

text = open('hhgttg.txt', encoding='utf8').read().lower() #открыть файл и прочесть его содержимое/ опущение результата в нижний регистр функцией .lower()
word_list = text.split()#нарезка строки на слова

print(text[:100]) #распечатка первых 100 символов текста
print(len(word_list))#длина списка

word_count = {}#заводим пустой словарь, куда запишем количество вхождений слова в текст
for word in word_list: #создание цикла
    word = word.strip(string.punctuation) #метод отсечения слева и справа того, что я ему передам/ string.punctuation - передача пунктуации
                                          # из библиотеки string/ смена исходной строчки введением нового присваивания word
    if word in word_count:#если слово находится в словаре
        word_count[word] += 1 #значение ассоциированное со словом увеличиваем на 1
    else:
        word_count[word] = 1

#pprint.pprint(word_count)#Посчитать количество повторений каждого слова в тексте

for word in sorted(word_count, key=word_count.get, reverse=True):
    print('%s -> %d' % (word, word_count[word]))