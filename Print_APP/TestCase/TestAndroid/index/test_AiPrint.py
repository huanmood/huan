import unittest
from parameterized import parameterized
from Page.PageAndroid.AiPrint import AiPrint

dev = [("P21"), ("P31S"), ("PM220"), ("PM220S"), ("PM230"), ("PL70e-BT"), ("PM360"), ("P22"),
       ("PL80E")]


class AiPrintTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = AiPrint()
        cls.base.firstDownload_open()

    @parameterized.expand(dev)
    def test_AiPrint(self, devName):
        print(devName)
        self.base.get_aiprint(devName)

    def test_aa(self):
        print("第二个case")
