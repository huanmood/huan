import unittest

from parameterized import parameterized

from Page.PageAndroid.Connect import Connect

devices = [
    ("PM230", "11:FB:AF:F5:6F:52")
]


class ConnectTest(unittest.TestCase):
    def setUp(self):
        self.base = Connect()
        self.base.firstDownload_open()

    @parameterized.expand(devices)
    def test_connect(self, deviceName, deviceMac):
        self.base.connect(deviceName, deviceMac)
