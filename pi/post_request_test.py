from pydoc import locate
from getmac import get_mac_address
from datetime import datetime
import requests
import json
from location_discovery import get_location

def post_satisfaction():
    url = "http://localhost:8000/satisfactions"
    survey = input('insert your satisfaction level: ')
    time = datetime.now().isoformat()
    device_id = get_mac_address()
    location = get_location(device_id)
    myobj = {
        "satisfaction": survey,
        "deviceId": device_id,
        "insertedAt": time,
        "location": location,
        "comment" : "the guy was very rude"
        }
    print(myobj)
    x = requests.post(url, data = json.dumps(myobj)) #json.dumps converts the dictionary to a string because the server needs a string

post_satisfaction()