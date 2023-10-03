import utils

keys, values = utils.get_populations()



data = [
    {
        'Country': 'Colombia',
        'Population': 300,
    },
    {
        'Country': 'Bolivia',
        'Population': 200,
    }
]

# print(keys, values)

country = input('Type Country => ')


result = utils.population_by_country(data, country)

print(result)