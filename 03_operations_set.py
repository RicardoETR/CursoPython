
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# UNION
#metodo
set_c = set_a.union(set_b)
print(set_c)
#operador
set_c = (set_a | set_b)
print(set_c)


#INTERSECCION
#metodo
set_c = set_a.intersection(set_b)
print(set_c)
#operador
set_c = (set_a&set_b)
print(set_c)

print('esta')
#DIFERENCIA
set_c = set_a.difference(set_b)
print(set_c)
set_c = (set_a - set_b)
print(set_c)

#DIFERENCIA SIMETRICA (UNION SIN ELEMENTOS QUE CONCIDEN)
set_c = set_a.symmetric_difference(set_b)
print(set_c)
set_c = set_a ^ set_b
print(set_c)


#ejercicio de union
countries = {'mex', 'col', 'arg', 'usa'}
nothAm = {'usa', 'canada'}
centralAm = {'mex', 'gt', 'bz'}
southAm = {'col', 'bz', 'arg'}

new_set = countries.union(nothAm, centralAm, southAm)
print(new_set)
