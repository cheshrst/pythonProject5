less = {}
with open('task6.txt', 'r', encoding= "UTF-8") as file_obj:
    for line in file_obj:
        lesson, time1, time2, time3 = line.split()
        less[lesson] = int(time1) + int(time2) + int(time3)
    print(f"{less} общее время")