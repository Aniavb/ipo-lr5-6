with open('D:\ИПО\ipo-lr5-3\Текстовый документ.txt', 'r') as file:  #открываем файл для чтения
    text = file.read()   #считываем файл
    words = text.split()  #делим текст по разделителю 
unique = []   #создаём пустой список для хранения уникальных слов
for word in words:   #перебираем элементы word в words
    if word not in unique:  #если элементов word нет в списке unique
        unique.append(word)  # то добавляем элемент
res = ' '.join(unique)   #соединяем список в строку
with open('Уникальные слова.txt', 'w') as f:   #открыввваем новый файл для записи
    f.write(res)    #записываем в файл уникальные слова
print(res)   #выводим уникальные слова