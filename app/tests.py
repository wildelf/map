from django.test import TestCase

# Create your tests here.
import requests

#获取设备经纬值

def GetOuterIP():
    location = []
    my_ip = requests.get('http://freegeoip.net/json/')
    info_dict = my_ip.json()
    print(info_dict)
    location.append(info_dict['longitude'])
    location.append(info_dict['latitude'])
    return location


if __name__ == '__main__':
  location = GetOuterIP()
  print(location)

# AK = 'YN2ajqOcsFnsZI2qbsYulnL6u9iU9dhF'
#
# def get_location(ak):
#     location = {}
#     my_ip_info = requests.get('https://api.map.baidu.com/location/ip?ak=%s'%ak)
#     print(my_ip_info.text['content']['address_detail'])
#     info_dict = my_ip_info.json()
#     location['longitude'] = round(float(info_dict['content']['point']['y'])/100000,2)
#     location['latitude'] = round(float(info_dict['content']['point']['x'])/100000,2)
#
#     return location
#
#
# if __name__ == '__main__':
#     location = get_location(AK)
#     print(location)



