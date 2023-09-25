items = [
    {
        'product': 'camisa',
        'price': '100',
    },
    {
        'product': 'pantalones',
        'price': '300'
    },
    {
        'product': 'chamarras',
        'price': '700'
    }
]

# crea una lista que armada con la funcion map, esta recibe una lambda function con el item, el key que nos interesa y la lista de donde la vamos a iterar
prices = list(map(lambda item : item['price'], (items)))
print(prices)


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = float(item['price']) * .16
    return new_item

new_items = list(map(add_taxes, items))


print(items)
print(new_items)