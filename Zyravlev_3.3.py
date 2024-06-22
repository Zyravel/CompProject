import requests
import datetime

access_token = 'vk1.a.BFNf2GsigyNZa_f4mL5rSR6U0bTNmgEm97DcUkzzaU6tCPQMEa78LAnOWyaj0gw59ErzTOy1x9C7_Eoa7S8emLQppXbfDKB3hs3o1yUA0aWxt04t8H4wiCdZV3AndO7a5RToLim_Yhj3JQxpyKqKiwLt8BpZl6Uqy1HGQVMbGwsEtuCZXGoXWxHSrfSR7eyU'

user_input = input('Введиите id или screen_name пользователя: ')

url_friends = "https://api.vk.com/method/users.get"


if  type(user_input) !=  int:
    params_to_int = {
    "user_ids": user_input,
    "access_token": access_token,
    "v": "5.131"
    }
    response = requests.get(url_friends, params=params_to_int).json()['response'][0]
    user_input = response['id']

url_friends = "https://api.vk.com/method/friends.get"

params = {
"user_id": user_input,
"fields" : "last_seen",
"order": 'name',
"access_token": access_token,
"v": "5.131"
}
response = requests.get(url_friends, params=params)

user_info = response.json()
# print(user_info)

# print(user_info['response'])
cnt = 0
try:
    for i in user_info['response']['items']:
        cnt += 1
        name = i['first_name']
        l_name = i['last_name']
        date = datetime.datetime.fromtimestamp(i['last_seen']['time'])
        print(f"{name} {l_name} был в сети: {date}")
        # print(i['first_name'], i['last_name'], datetime.datetime.fromtimestamp(i['last_seen']['time']))
except :
    cnt += 1
print(f'Всего {cnt} друзей')

