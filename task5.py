try:
        with open('my_file.txt', 'w') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
except IOError:
        print('Ошибка в файле')
except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')