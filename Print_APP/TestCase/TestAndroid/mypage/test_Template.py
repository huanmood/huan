import unittest

import requests
from parameterized import parameterized
from Page.PageAndroid.Template import Template

from Page.PageAndroid.Connect import Connect
# dev = []
# url = 'http://app.nelko.net/api/templateVip/getDeviceList'
# resp = requests.get(url).json().get('data', [])
# for i in resp:
#     index_show_values = i['indexShow'].split(',')
#     for j in index_show_values:
#         if j == '0':
#             dev.append(i['deviceName'])
# print(dev)
dev = [
    ("PM230", "25:41:63:A5:40:73"),
    ("PM220", "31:9D:16:24:B1:78"),
    ("P21", "43:2C:42:48:63:5F")

]
class Test_Template(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base = Template()  # 实例化Base对象
        cls.base.firstDownload_open()
        cls.connect_test=Connect()

    @parameterized.expand(dev)
    def test_getTempleList(self, devName,devMac):
        self.base.log_error(devName)
        self.connect_test.connect(deviceName=devName,deviceMac=devMac)
        self.base.get_getCategory(devName)


    @classmethod
    def tearDownClass(cls):
        pass
