# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text4.txt', 'w', encoding='utf-8') as new_num:
    with open('text_4_txt', encoding='utf-8') as numbs:
        new_num.writelines([line.replace(line.split()[0], num.get(line.split()[0])) for line in numbs])
