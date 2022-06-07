from getmac import get_mac_address
from requests import get

info = get(url='https://medium.com/@fran.abenza/learning-by-the-way-fa33df432a1d').text

#find the characters "This article will be public soon" on info
print(info.find("will be public soon"))