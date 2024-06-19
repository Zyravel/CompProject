import requests
import pprint


access_токеn = 'vk1.a.a3Yl8wn08zpqLPhPjVSr2vRVaCz7NMXi5rZQyWxaaOq5kM_qsFPMWyQuZDVRBSCmshVYJmBkLEF0IaqlZJUldGVVFuxwCNkYO6vYPkkEHprLXP_5r1j4loKyawnb1GZyL4tzaC8lOgixRocQ_dGe8pBMI7bOsw8FvKfhMWxUr_UAWsPPSNnYSjHB4vVt5tPX'


user_input = input('VK: ')


url = "https://api.vk.com/method/users.get"

params = {
    "user_ids": user_input,
    "access_token": access_токеn,
    "v": "5.131"
}
response = requests.get(url, params=params).json()
pprint.pprint(response)
