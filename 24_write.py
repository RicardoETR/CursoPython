with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('Nueva linea en el arcvhivo')