numbers = [1,2,3,4,5]

numbers_v2 = []

for i in numbers:
    numbers_v2.append(i*2)

print(numbers)
print(numbers_v2)


numbers_v3 = list(map(lambda i: i * 4, numbers))
print(numbers_v3)


# ejercicio real que pasa en CB
contratos = ['123-2','12432-2','1997-1','32123-5','8234-4']
contratos_v2 = list(map(lambda contrato : contrato.replace("-",""),  contratos))
print(contratos)
print(contratos_v2)


# suma de dos listas diferentes, se queda con el tamaño de lista mas pequeña
numbers_1 = [1,2,3,4,5]
numbers_2 = [5,6,7]
result = list(map(lambda x,y : x + y, numbers_1, numbers_2))
print(result)

