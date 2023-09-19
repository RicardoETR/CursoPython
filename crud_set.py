#apuntes para el crud de los set

set_countries = {'col', 'mex', 'bol'}

#tamaio conjunto
size = len(set_countries)
print(size)

# esta en el conjunto?
print('col' in set_countries)

#agragar elementos
set_countries.add('pe')
print(set_countries)

#actualizar elementos
set_countries.update({'arg', 'ecua', 'pe'})
print(set_countries)

#eliminar elementos
set_countries.remove('col')
print(set_countries)

#eliminar elemento si no sabemos que existe
set_countries.discard('mex')
print(set_countries)

#eliminar todos los elementos
set_countries.clear()
print(set_countries)