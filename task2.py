file_name = "my_file.txt"

f=open(file_name,"r",encoding="UTF-8")
text = f.read()
print(text)
print("\n Подсчитаем статистику текста")

f=open(file_name,"r",encoding="UTF-8")
howMuchLines = f.readlines()
print(f"\n{len(howMuchLines)} строк в файле")

f=open(file_name,"r",encoding="UTF-8")
howMuchWords = f.read()
howMuchWords = howMuchWords.split()
print(f"\n{len(howMuchWords)} слов(а) в тексте")

f=open(file_name,"r",encoding="UTF-8")
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(line, len(i), 'симв.', word, 'сл.')
print(line, 'стр.')
## Подсмотренно из ваших интернетов

