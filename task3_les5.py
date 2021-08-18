# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# запись фамилий и окладов
surname = open('3.txt', 'w')
surname.write('Vasilkov: 2500\n' 'Tulpanov: 3600\n' 'Gvozdikov: 1700\n')
surname.close()

# вывод записанного
with open ('text3.txt', 'r', encoding='utf-8') as text:
    dict = {line.split()[0]: float(line.split()[1]) for locals() in text}
    print(f'Средний доход {round((sum(dict.values()) / len(dict), 3))}\n'
    f'Сотрудник с окладом менее 20к {[e[0] for e in dict.items() if e[1] < 20000]}')