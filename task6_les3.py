# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
import capitalize as capitalize


# def int_func(text):
#       if text in text.lower():
#        return(text.capitalize())
#       else:
#           print('Все буквы должны быть маленькие')
#
# print(int_func('lyubov'))


def int_func(text):
    if text in text.lower():
     str = (('{}'.format(text))).split(',')
     for i in str:
        return text.capitalize()
    else:
        print('Все буквы должны быть маленькие')

print(int_func('privet lyubov'))


