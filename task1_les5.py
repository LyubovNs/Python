# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open('file.txt', 'w')
line = input('Введите текст \n')
while line:
    file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

file.close()
file = open('file.txt', 'r')
content = file.readlines()
print(content)
file.close()