# print(0/0)

print("hola")


suma = lambda x,y: x+y

assert suma(2,2) == 4


age = 10
if age < 18:
    raise Exception("no cumple con la edad")