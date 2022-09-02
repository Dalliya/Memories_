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
                if word in word_count:#если слово находится в словаре
                    word_count[word] += 1 #значение ассоциированное со словом увеличиваем на 1
                else:
                    word_count[word] = 1
    #pprint.pprint(word_count)#Посчитать количество повторений каждого слова в тексте

    for word in sorted(word_count, key=word_count.get, reverse=True)[:top_n]: #sorted()возврат отсортированного списка через функцию/ вычленение подсписка
        print('%s -> %d' % (word, word_count[word]))

words_count(r'C:\Users\utilisateur\PycharmProjects\Memories\hhgttg.txt', r'C:\Users\utilisateur\PycharmProjects\Memories\stop_words_list.txt')
