# Определить в тексте предложения, которые являются палиндромами

# после каждого действия можно написать принт, чтобы посмотреть, что получается в итоге одного или другого действия и лучше понять
text = '''1988 год специальным решением ЮНЕСКО был объявлен годом Макаренко в связи с его 100-летним юбилеем. Меня истина манит сияньем.
Тогда же были названы имена четырёх великих учителей, определивших способ педагогического мышления XX века.
Произведения Макаренко были переведены почти на все языки народов мира, а его главный труд - «Педагогическую поэму» (1935) - сравнивают с лучшими романами воспитания.
названа одной из десяти самых значительных книг по воспитанию XX века.
 Это ли не свидетельство международного уважения и признания заслуг?
А в России десять лет назад к 115-ой годовщине Макаренко было выпущено 10 000 экземпляров первого полного издания «Педагогической поэмы».
Вы скажете, что за странный тираж для многомиллионной читающей страны? Однако издатели до сих пор ломают голову, как реализовать «непродаваемую» книгу.
Несовременно? Неактуально? Коту скоро сорок суток.
Наверное, не осталось в педагогике нерешённых проблем, благовоспитанные девочки и мальчики послушно ходят в школу, а детская преступность на нуле?
Почти сто лет назад, заканчивая Полтавский учительский институт, Макаренко писал диплом на тему «Кризис современной педагогики».
Кто возьмёт на себя смелость утверждать, что сейчас ситуация в корне изменилась? Ешь немытого ты меньше!
Он был странным человеком, этот Макаренко. Аргентина манит негра.

Он руководил ею с 1920 до 1928 гг. и постигал педагогику перевоспитания в боевых условиях, как солдат на поле боя.
Что двигало этим человеком? Ведь было очевидно, что своим решительным поступком он ставит крест на спокойной размеренной жизни. А в Енисее синева.
 Может быть, та самая активная жизненная позиция, о которой стало немодно говорить в последнее время?
В начале 20-х годов прошлого века в России, пережившей революцию и гражданскую войну, насчитывалось более 7 миллионов беспризорных детей.
Они представляли собой огромную социальную беду и опасность. А луна канула. Громилы мыли морг.
Изобретённая им система перевоспитания полезным производительным трудом в коллективе превращала сборище малолетних преступников в дружную сплочённую команду.
В колонии не было охраны, заборов, карцера.'''
text = text.lower()                                 # переводим текст в нижний регистр, потому что в питоне А не равно а
text = text.replace('!', '.')                       # чтобы разделить текст одним действием, меняем ! на точки
text = text.replace('?', '.')                       # то же самое делаем с ?
text = text.replace('\n', ' ')                      # энтер меняем на пробел
sentences = text.split('. ')                        # а теперь делим текст по принципу: если есть ". ", то это - отдельное предложение, выводим его в строку в списке
sentences = [i.rstrip('.') for i in sentences]      # в последнем предложении после предыдущего действия останется ".", ее надо убрать, этим действием ее убираем
sentences_new = []                                  # создаем пустой список, он нам позже понадобится
sentences_new_1 = []                                # и этот пустой список нам тоже еще понадобится дальше

for i in sentences:
    words_1 = list(i)                               # теперь каждую слитную строку мы снова разделяем, теперь каждая переменная в списке - буква, пробел или знак препинания
    for a in words_1:                               # проверяем каждый символ (буква, пробел или знак препинания) в списке
        if a in ',:; ':                             # если символ - знак препинания или  пробел
            words_1.remove(a)                       # мы его удаляем
    words_2 = ''.join(words_1)                      # теперь делаем это одним сплошным словом (все слова просто написаны слитно в одно)
    sentences_new.append(words_2)                   # и добавляем это одно сплошное слово в первый пустой список

for i in sentences_new:
    words_3 = list(i)                               # теперь каждую слитную строку мы снова разделяем, теперь каждая переменная в списке - буква
    words_3.reverse()                               # а теперь буквы мы переворачиваем
    words_4 = ''.join(words_3)                      # и снова объединяем в одну слитную строку без пробелов
    sentences_new_1.append(words_4)                 # добавляем перевернутое сплошное слово во второй пустой список

compare = dict(zip(sentences_new, sentences_new_1)) # zip объединяет два списка по принципу
                                                    # [а, б, с]+[1, 2, 3] ->[(а, 1),(б, 2),(с, 3)], dict это все преобразует
                                                    # в словарь {а:1, б:2, с:3}, первоначальное слитное предложение : перевернутое слитное предложение

for sent in compare:                                # теперь для каждой переменной в словаре
    if sent == compare[sent]:                       # если ключ и значение (а : б, а=б) равны между собой, то получается, что изначальное предложение и его перевернутая форма равны
        ind = sentences_new.index(sent)             # находим порядковый номер этого предложения в словаре (он будет таким же, что и в списке sentence, где у нас предложения бещз преобразований)
        print(sentences[ind])                       # и выводим в печать именно первоначальное предложение (чтобы оно выглядело читабельно и презентабельно)


