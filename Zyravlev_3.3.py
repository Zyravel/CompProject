import requests
import pprint
import datetime

access_token = 'vk1.a.BFNf2GsigyNZa_f4mL5rSR6U0bTNmgEm97DcUkzzaU6tCPQMEa78LAnOWyaj0gw59ErzTOy1x9C7_Eoa7S8emLQppXbfDKB3hs3o1yUA0aWxt04t8H4wiCdZV3AndO7a5RToLim_Yhj3JQxpyKqKiwLt8BpZl6Uqy1HGQVMbGwsEtuCZXGoXWxHSrfSR7eyU'


user_input = 443217


url = "https://api.vk.com/method/friends.get"

params = {
"user_id": user_input,
"fields" : "last_seen",
"order": 'name',
"access_token": access_token,
"v": "5.131"
}
response = requests.get(url, params=params)



user_info = response.json()
pprint.pprint(user_info)

# print(user_info['response'])
# for i in user_info['response']['items']:
    # print(i)
    # print(i['first_name'], i['last_name'], datetime.datetime.fromtimestamp(i['last_seen']['time']))
