from getmac import get_mac_address
import requests
import json

try:
    test_device = "2f:8b:95:b4:b8:77"
    eth_mac = get_mac_address()
    url = 'http://localhost:8000/devices/2f:8b:95:b4:b8:77'
    location = "KITCHEN"
    device_mac = {'deviceId' : test_device, 'location': location}
    


    x = requests.post(url, data = json.dumps(device_mac))
except:
    #we will print the error
    print("it maybe that")
    print("the device is already created: ", eth_mac)

