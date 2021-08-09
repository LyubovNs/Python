# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# def my_func(x, y):
#       if y != abs(y):
#        result = x ** y
#        return  result
#       elif x != int(x):
#        print('x должно быть целым положительным числом числом!')
#       else:
#        print('y должно быть отрицательным числом числом!')
#
# print(my_func(0.2, -3))

import numbers

def my_func(x, y):
        if isinstance(x, numbers.Number):
         result = x ** y
         return result
        else:
         print('x > 0, y < 0')

print(my_func(-12.4, -5))