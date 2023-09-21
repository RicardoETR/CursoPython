#diccionarios

# Manera normal
dict = {}
for i in range (1,11):
    dict[i] = i * 2
print(dict)

#comprehasion
dict_v2 = {i:i*2 for i in range(1,11)}
print(dict_v2)

# ----------------------------------------------
#segundo ejemplo
import random

# Manera normal

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

#comprehasion
population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)


# ----------------------------------------------
#tercer ejemplo
names = ['nico', 'zule', 'sant']
ages = [12,56, 98]

people_zip = list(zip(names, ages))
people = {name:age for name, age in people_zip}
print(people)
