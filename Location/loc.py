import requests
import json
from geopy.distance import great_circle 
send_url = 'http://api.ipstack.com/2409:4052:709:640c:71c6:76f6:6bdf:cef2?access_key=b6d88bf3e75b6649440117254013178d&format=1'
r = requests.get(send_url)
j = json.loads(r.text)
#print(j)
lat = j['latitude']
lon = j['longitude']


#send_urll = 'http://api.ipstack.com/2409:4052:709:640c::122e:ac?access_key=b6d88bf3e75b6649440117254013178d&format=1'
send_urll = 'http://api.ipstack.com/14.139.243.170?access_key=b6d88bf3e75b6649440117254013178d&format=1'
rr = requests.get(send_urll)
jj = json.loads(rr.text)
latt = jj['latitude']
lonn = jj['longitude']
print(lat,lon)
print(latt,lonn)

from geopy.distance import great_circle 
  
a = (11.62339973449707,92.72650146484375)
b = (11.62339973449700, 92.72650146484370)
  
# Print the distance calculated in km 
print(great_circle(a, b).m)
