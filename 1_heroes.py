import requests

url  = 'https://superheroapi.com/api/2619421814940190/'
heroes_list = ['Hulk', 'Captain America', 'Thanos']
heroes_dict = {}
iq_list = []

for hero_name in heroes_list:
    resp = requests.get(url + '/search/' + hero_name).json()
    id_ = resp['results'][0]['id']
    
    resp = requests.get(url + id_ + '/powerstats').json()
    iq = resp['intelligence']
    
    heroes_dict[iq] = [hero_name]
    iq_list.append(iq)

iq_list.sort()

print(heroes_dict[iq_list[0]])