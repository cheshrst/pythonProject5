file_name = "my_file.txt"
with open(file_name, "r", encoding= "UTF-8") as f:
    sal = []
    poor = []
    text = f.read()
    my_list = text.split(",")
    print(my_list)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
