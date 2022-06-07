import requests
import json
from getmac import get_mac_address
import datetime
from location_discovery import get_location
from GPT-3 import generate_text

payload = {}
n=0
for i in range (9000):
    try:
        server_url = "http://192.168.1.239:{}".format(n)
        n+=1
        payload['location'] = requests.get(server_url+'/devices').text
    except:
        print(server_url)

#insert the input on the payload
payload['review'] = input('write about your experience: ')
payload['deviceId'] = get_mac_address()
payload['insertedAt'] = datetime.now().isoformat()
payload['location'] = get_location(payload['deviceId'])
payload['category'] = 
#doing a http get request to the server
#we will fetch the location from the server localhost:8000/deviceId/location
#payload['location'] = requests.get(server_url+'/devices/'+payload['deviceId']+'/location').text



#now we will dump everthing with json and post it to the server
#requests.post('http://localhost:8000/satisfactions', data = json.dumps(payload))


