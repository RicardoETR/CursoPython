# hight order function

# FORMA NORMAL
def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment)
print(result)


# LAMBDA ASIGNADA A UNA VARIABLE PARA DESPUES OCUPAR UN HIGHT ODER FUNCTION
increment_v2 = lambda x: x+1
high_ord_func_v2 = lambda x, func: x + func(x)
result = high_ord_func_v2(2,increment_v2)
print(result)


#LAMBDA CREADA DIRECTO EN LOS PARAMETROS DE LA FUNCION 
result = high_ord_func_v2(10, lambda x: x*x)
print(result)


