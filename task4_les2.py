# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

phrase = str(input('Введите строку из нескольких слов, разделяя их пробелами: '))
print(phrase)
a = phrase.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. {el}")