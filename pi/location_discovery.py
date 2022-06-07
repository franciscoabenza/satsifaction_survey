from getmac import get_mac_address
from requests import get

#we are going to do a get request to http://localhost:8000/devices/{deviceId}/location
def get_location(device_id):
    mac_address = device_id
    url = "http://localhost:8000/devices/{}/location".format(mac_address)
    location = get(url).text[1:-1]#need to remove the first and last character '" "'
    return location