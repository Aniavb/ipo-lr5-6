with open('Текстовый документ.txt', 'r', encoding="utf-8") as file:  #открываем файл для чтения
    text = file.read()   #считываем файл
unique = set(text.split())#создаём множество для хранения уникальных слов
with open('Уникальные слова.txt', 'w', encoding="utf-8") as f:   #открываем новый файл для записи
    for word in unique: #перебираем слова в множестве
        f.write(word + ' ')    #записываем в файл уникальные слова
print(unique)   #выводим уникальные слова