import requests


url = 'https://fakestoreapi.com/products/categories'
cat = requests.get(url).json()
for i in cat:
    print(cat.index(i) + 1, i)
num = int(input('Введите номер интересующец карегории: '))
num = cat[num - 1]
category = requests.get(url[0: -3] + 'y/' + num).json()
print(f'Товары категории {num}:')
for lot in category:
    print (f' id товара: {lot['id']}, Название: {lot['title']}, Цена: {lot['price']}')