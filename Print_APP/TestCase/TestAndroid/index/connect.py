import unittest

from parameterized import parameterized

from Page.PageAndroid.Connect import TestMathOperations

devices = [
    ("PM230", "8A:BF:99:4D:F7:AB")
]


class connectTest(unittest.TestCase):
    def setUp(self):
        self.base = TestMathOperations()
        self.base.firstDownload_open()

    @parameterized.expand(devices)
    def test_connect(self, deviceName, deviceMac):
        self.base.connect(deviceName, deviceMac)
