import requests
import pprint


url_cart = 'https://fakestoreapi.com/carts'
url_product = 'https://fakestoreapi.com/products'
url_user = 'https://fakestoreapi.com/users'
response_cart = requests.get(url_cart).json()
# pprint.pprint(response_cart)
response_product = requests.get(url_product).json()
# pprint.pprint(response_product)
response_user = requests.get(url_user).json()
pprint.pprint(response_user)

user = input('Введите имя пользователя или его ID: ')
# if user.isalpha():
    