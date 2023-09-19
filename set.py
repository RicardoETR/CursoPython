# apuntes sobre conjuntos

# los conjuntos no tienen un orden en especifico 
# no se permiten elemtos duplicados, aunque en la declaración se duplique, en funcionamiento lo quita.

set_countries = {'col', 'mex', 'bol'}
print(f"El conjunto es: {set_countries} y es de tipo {type(set_countries)}")

set_numbers = {1,2,3,4,5,6}
print(f"El conjunto es: {set_numbers} y es de tipo {type(set_numbers)}")

set_types = {1,'hola', False, 1234.32}
print(f"El conjunto es: {set_types} y es de tipo {type(set_types)}")

set_from_string = set('hola como estas')
print(f"El conjunto es: {set_from_string} y es de tipo {type(set_from_string)}")

set_from_tuples = set(('abc', 'cbd', 'as', 'abc'))
print(f"El conjunto es: {set_from_tuples} y es de tipo {type(set_from_tuples)}")

#lista
numbers = [1,2,3,4,5,1,3,4,5]

set_numbers = set(numbers)
print(f"El conjunto es: {set_numbers} y es de tipo {type(set_numbers)}")

unique_numbers = list(set_numbers)
print(f"La lista es: {unique_numbers} y es de tipo {type(unique_numbers)}")

