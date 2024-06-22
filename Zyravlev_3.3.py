import requests
import datetime
import pprint
access_token = 'vk1.a.BFNf2GsigyNZa_f4mL5rSR6U0bTNmgEm97DcUkzzaU6tCPQMEa78LAnOWyaj0gw59ErzTOy1x9C7_Eoa7S8emLQppXbfDKB3hs3o1yUA0aWxt04t8H4wiCdZV3AndO7a5RToLim_Yhj3JQxpyKqKiwLt8BpZl6Uqy1HGQVMbGwsEtuCZXGoXWxHSrfSR7eyU'

# user_input = input('Введиите id или screen_name пользователя: ')
user_input = 443217
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
pprint.pprint(user_info)


cnt = user_info['response']['count']


c = 0
test = list()
try:
    for i in user_info['response']['items']:
        test.append(i['last_name'])
        c += 1
        # if i['last_seen']['time']:
        #     print('yes')
except:
    c += 1

cc = 0
test2 = list()
try:
    for i in user_info['response']['items']:
        test2.append([i['last_name'] ,i['last_seen']['time']])
        cc += 1
        # if i['last_seen']['time']:
        #     print('yes')
except:
    cc += 1
print(len(test), len(test2))
for i in range(len(test2)):
    print(i+1, test[i], test2[i])
print(test)


x = 0
try:
    for i in user_info['response']['items']:
        x += 1

        name = i['first_name']
        l_name = i['last_name']
        date = i['last_seen']['time']
        print(f"{i['first_name']} {i['last_name']} был в сети: {date}")


except :
    x += 1



print(f'У пользователя {cnt} друга')
print(f'У пользователя {x} друга')
