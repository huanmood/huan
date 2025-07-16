import unittest

from parameterized import parameterized
from TestCase.TestAndroid.share_devices import process_context
from Page.PageAndroid.Connect import Connect

devices = [
    ("PM230", "11:FB:AF:F5:6F:52"),
    ("PM220", "31:9D:6D:1A:51:BF"),
    ("P21", "43:2C:42:48:63:5F")

]


class ConnectTest(unittest.TestCase):
    def setUp(self):
        self.base = Connect()
        self.base.firstDownload_open()

    @parameterized.expand(devices)
    def test_connect(self, deviceName, deviceMac):
        self.base.connect(deviceName, deviceMac)
