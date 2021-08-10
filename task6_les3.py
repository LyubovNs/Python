# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(text):
    for letter in text:
        ns = 0
        for n in letter:
          if n.islower() and 97 <= ord(n) <= 122:
            ns += 1
    print(text.capitalize() if ns == len(letter) else 'Должны быть маленькие латинские буквы')


int_func('siпапhk ij PIJ j тт')
int_func('privet privet')






# def int_func(text):
#     for letter in text:
#         if letter.isupper() or ord(letter) <= 97 or ord(letter) >= 122:
#             print('Должны быть маленькие латинские буквы')
#             break
#         else:
#              continue
#              print(text.capitalize())
#
# int_func('fyn')


# def int_func(text):
#     if text.islower() and 97 <= ord(n) <= 122:
#      str = (('{}'.format(text))).split(',')
#      for i in str:
#         return text.capitalize()
#     else:
#         print('Должны быть латинские буквы в нижнем регистре')
#
# print(int_func('privet privet'))