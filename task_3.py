# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = (input('Write a number, please: '))
print(n)

n1 = n + n
print(n1)

n2 = n + n + n
print(n2)

sum = int(n) + int(n1) + int(n2)
print('Summa = ', sum)