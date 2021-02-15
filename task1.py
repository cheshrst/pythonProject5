file_name = "my_file.txt"
f=open(file_name,"w",encoding="UTF-8")
text = input("Введите данные: ")

while True:
    f.writelines(text)
    text = input("Введите данные: ")
    f.write("\n")
    if not text:
        break
f.close()