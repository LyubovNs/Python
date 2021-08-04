# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month <0 or month >12:
    print('Error')
month_dict = {1:"Январь", 2:"Февраль", 3:"Март",
              4:"Апрель",5:"Май", 6:"Июнь",
              7:"Июль", 8:"Август", 9:"Сентябрь",
              10:"Октябрь", 11:"Нобрь", 12:"Декабрь"}

month_list = list(month_dict.values())
for i, el in enumerate(month_list):
        if i == month - 1:
            print(f"Month from list is {month_list[i]}")
            break
print(f"Month from dict is {month_dict[month]}")
