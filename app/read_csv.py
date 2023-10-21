import csv

def read_csv(path):
    with open(path, 'r') as csvfile: #with open para cerrar el archivo una vez que acabe el metodo
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader) #iterar manualmente con next para ir por el cabecero
        # print(header)
        data = [] #variable donde se almancenara la info
        for row in reader: 
            iterable = zip(header, row) #hacer una relacion de los cabeceros con su valor 
            # print(list(iterable))
            country_dict = {key: value for key, value in iterable} #generar el diccionarion con un comprenhation dictionary
            # print(country_dict)
            data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv('data.csv')
    # print(data[0]) 