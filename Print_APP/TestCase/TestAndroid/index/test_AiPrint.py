import unittest
from parameterized import parameterized
from Page.PageAndroid.AiPrint import AiPrint
dev = [(1, "P21"), (2, "P31S"), (3, "PM220"), (2, "PM220S"), (3, "PM230"), (2, "PL70e-BT"), (3, "PM360"), (2, "P22"),
       (3, 'PL80E')]

class AiPrintTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = AiPrint()
        cls.base.firstDownload_open()

    @parameterized.expand(dev)
    def test_AiPrint(self, devIndex, devName):
        print(devName)
        self.base.get_aiprint(devIndex, devName)
    def test_aa(self):
        print("第二个case")