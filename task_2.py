# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


# вводит число в секундах
time = int(input('How many time in seconds now? '))

# получаем часы
hours = time // 3600
print('Seconds value in hours = ', hours)

# получаем минуты
time = time % 3600
minutes = time // 60
print('Seconds value in minutes = ', minutes)

# получение секунд
seconds = time % 3600

print('Time: ', "%02d:%02d:%02d" % (hours, minutes, seconds))



