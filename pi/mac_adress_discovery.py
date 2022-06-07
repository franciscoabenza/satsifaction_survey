from getmac import get_mac_address
import requests
import json

try:
    test_device = "2f:8b:11:b4:b8:00"
    eth_mac = test_device
    url = 'http://localhost:8000/devices'
    location = "KITCHEN"
    device_mac = {'deviceId' : eth_mac, 'location': location}
    
    x = requests.post(url, data = json.dumps(device_mac))
    
except:
    #we will print the error
    print("it may be that")
    print("the device is already created: ", eth_mac)



# def getUser(): 
#     return { "admin": False, "pictures": 1 }

# def makeAdmin(user):
#     # 3 seconds
#     user['admin'] = True

# def makeAdminFunc(user):
#     newUser = user.copy()
#     newUser['admin'] = True
#     return newUser

# def increasePicture():
#     # 3 second
#     user['pictures'] = user.get('pictures') + 1

# user = getUser()

# user.get('admin')
# increasePicture(user) # get current pictures (0), increment 0 by 1
# increasePicture(user) # get current pictures (0), increment 0 by 1
# user.get('admin')


# user.get('admin')
# newUser = increasePicture(user)
# doubleIncrementUser = increasePicture(newUser)
# user.get('admin'), doubleIncrementUser.get('picture')