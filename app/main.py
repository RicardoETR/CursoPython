import utils

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

def run ():
    keys, values = utils.get_populations()
    print(keys, values)
    country = input('Type Country => ')
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()