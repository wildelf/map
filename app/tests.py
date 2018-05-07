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

# def get_location():
#     location = []
#     url = 'http://api.map.baidu.com/location/ip'
#     par = {'ak':'YN2ajqOcsFnsZI2qbsYulnL6u9iU9dhF'}
#     my_ip_info = requests.get(url)
#     info_dict = my_ip_info.json()
#     print(my_ip_info)
#     location.append(info_dict['x'])
#     location.append(info_dict['y'])
#     return location
#
#
#     if __name__ == '__main__':
#       location = get_location()
#       print(location)

