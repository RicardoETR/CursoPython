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

# se trabajara asi

libro = 'Para aprender a hacer microservicios con C# te recomendaría tomar los siguientes cursos de Platzi: Curso de C# con .Net Core 2.1: Este curso te enseñará los fundamentos del lenguaje C# y cómo utilizarlo junto con .Net Core para desarrollar aplicaciones web y servicios. Curso de APIs con .NET: En este curso aprenderás a crear APIs utilizando el framework de desarrollo web de .NET. Te enseñarán cómo diseñar, implementar y documentar APIs RESTful utilizando C#. Curso de ASP.NET Core: Este curso te enseñará a desarrollar aplicaciones web utilizando el framework ASP.NET Core. Aprenderás a crear controladores, vistas y modelos utilizando C# y cómo implementar funcionalidades como autenticación y autorización. Estos cursos te proporcionarán los conocimientos necesarios para desarrollar microservicios utilizando C# y .NET. ¡Espero que te sean de ayuda!'
letras_libro = set(libro)
print(letras_libro)