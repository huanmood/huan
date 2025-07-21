import unittest

import requests
from parameterized import parameterized
from Page.PageAndroid.Template import Template
from TestCase.TestAndroid.share_devices import process_context
from common.DB_utils import get_redis_conn

dev = []
url = 'http://app.nelko.net/api/templateVip/getDeviceList'
resp = requests.get(url).json().get('data', [])
for i in resp:
    index_show_values = i['indexShow'].split(',')
    print(index_show_values)
    for j in index_show_values:
        if j == '0':
            dev.append(i['deviceName'])

class TemplateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = Template()  # 实例化Base对象
        cls.base.firstDownload_open()

    @parameterized.expand(dev)
    def test_getTempleList(self, devName):
        self.base.log_error(devName)
        self.base.get_getCategory(devName)

    @classmethod
    def tearDownClass(cls):
        pass
