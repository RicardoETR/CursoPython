import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 50}
print(result)


text = 'Hola, soy Ricardo'

unique = {c:c.upper() for c in text if c in 'aeiou'}
print(unique)

# unique = {c:c.count for c in text if c in 'aeiou'}
# print(unique)

# # frecuencia
# unique = {vocal:frecuencia for vocal in text for frecuencia in text if vocal in 'aeiou' and vocal = }
# print(unique)
