from getmac import get_mac_address
from datetime import datetime
import requests
import json

def get_satisfaction():
    url = "http://localhost:8000/satisfactions"
    survey = input('insert your satisfaction level: ')
    time = datetime.now().isoformat()
    device_id = get_mac_address()
    
    myobj = {
        "satisfaction": survey,
        "deviceId": device_id,
        "insertedAt": time
        }
    print(myobj)
    x = requests.post(url, data = json.dumps(myobj))

get_satisfaction()