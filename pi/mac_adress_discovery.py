from getmac import get_mac_address
import requests
import json

try:

    eth_mac = get_mac_address()
    url = 'http://localhost:8000/devices'
    device_mac = {'deviceId' : eth_mac}
    x = requests.post(url, data = json.dumps(device_mac))
except:
    #we will print the error
    print("device already created: ", eth_mac)
