# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = float(input('Введите результат пробежки в первый день в километрах: '))
b = float(input('Введите ожидаемый результат пробежки в километрах: '))
days = 1
km = a
while km < b:
        a = a + 0.1 * a
        days += 1
        km = km + a
print(f"Вы достигнете требуемых показателей на %.d день" % days)