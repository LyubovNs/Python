# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

# def check():
#     work = float(input('Ведите выработку сотрудика в часах: '))
#     cost = float(input('Ведите ставку сотрудика в час: '))
#     happy = float(input('Ведите премию, начисленную сотрудику:'))
#
#     pay = (work * cost) + happy
#     print(f'Размер заработной платы: {pay}')
#
# command = sys.argv[1]
# if command == 'check':
#     check()

def check():
    try:
     time, rate, bon = map(float, argv[1:])
     print(f'check - {time * rate + bon}')
    except ValueError:
        print('Введите 3 числа')

