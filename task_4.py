# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
maxnumb = number % 10
if number < 0:
    print('Err!')
else:
    print(number)

while number >= 1:
    number = number // 10
    if number % 10 > maxnumb:
        maxnumb = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра ", maxnumb)
        break