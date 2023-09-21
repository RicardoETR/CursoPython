import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = {country:random.randint(1,100) for country in countries if population_v2 > 10}
print(population_v2)