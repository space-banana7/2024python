import requests
# city_name='울산'
city_name=input()
API_key='b6b1bfd4c7a1a0741886223e3b804ed5'
limit=5
url=f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'
res=requests.get(url)
data=res.json()
# print(len(data))
lat=data[0]['lat']
lon=data[0]['lon']
print(lat,lon)

url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
res=requests.get(url)
weather=res.json()
# print(weather)
des=weather['weather'][0]['description']
print(des)
# print("강지훈")