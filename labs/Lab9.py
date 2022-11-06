import json
import requests

r = requests.get('http://localhost:3000/')
data =r.json()
name0 = data[0]['name']
color0 = data[0]['color']
name1 = data[1]['name']
color1 = data[1]['color']
name2 = data[2]['name']
color2 = data[2]['color']
name3 = data[3]['name']
color3 = data[3]['color']


print( name0 +' is ' + color0)
print( name1 +' is ' + color1)
print( name2 +' is ' + color2)
print( name3 +' is ' + color3)