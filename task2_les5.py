# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

text = open ('2.txt', 'w')
text.write('Monday\n' 'sanday\n' 'Thursday\n')
text.close()

num_lines = 0
num_words = 0
num_chars = 0

with open('2.txt', 'r') as text:
    for line in text:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print(f'Количество строк: {num_lines}, количество слов: {num_words}')

text.close()