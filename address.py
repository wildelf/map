#_author:sanny
#date:2018-05-08

import requests
address = '葵潭'
AK = '61AXqFsoKHw58RR1KQOkataNB21qVWjy'

def get_location(ak,address):
    location = {}
    my_ip_info = requests.get('http://api.map.baidu.com/place/v2/search?query=%s&region=%s&output=json&ak=%s'%(address,address,ak))

    info_dict = my_ip_info.json()
    location['province'] = info_dict['results'][0]['province']
    location['city'] = info_dict['results'][0]['city']
    location['area'] = info_dict['results'][0]['area']
    return location
if __name__ == '__main__':
    location = get_location(AK,address)
    print(location)