# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# запись фамилий и окладов
surname = open('3.txt', 'w')
surname.write('Vasilkov: 2500\n' 'Tulpanov: 3600\n' 'Gvozdikov: 1700\n')
surname.close()

# вывод записанного
with open ('3.txt', 'r') as text:
 for line in text.readlines():
     print(line, end='')
text.close()

# оклад менее 20 тыс