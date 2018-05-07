from django.test import TestCase

# Create your tests here.
# import requests
#
# #获取外网IP
#
# def GetOuterIP():
#     my_ip = requests.get('http://ip.42.pl/raw')
#     print(type(my_ip.text))
# if __name__ == '__main__':
#   GetOuterIP()


with open('text.txt','r') as f:
    for line in f:
        print(line)
