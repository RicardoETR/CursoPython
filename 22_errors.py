
try:
    age = 10
    print(0/0)
    assert 1 != 1, 'Es incorrecto'
    if age < 18:
        raise Exception("no cumple con la edad")

except ZeroDivisionError as error:
    print(error)    
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)


print("hola")
