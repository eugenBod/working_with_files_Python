with open('data.txt', 'w') as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

with open('data.txt', 'r') as file:
    print(file.read())

with open('data.txt', 'a') as file:
    file.write("Четвертая строка добавлена\n")
    file.write("Пятая строка добавлена\n")

with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('data.txt', 'rb') as sourse_file:
    data = sourse_file.read()

with open ('data_copy.txt', 'wb') as destination_file:
    destination_file.write(data)