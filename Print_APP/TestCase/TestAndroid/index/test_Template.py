import unittest

from parameterized import parameterized

from Page.PageAndroid.Template import Template

dev = [(1, "P21"), (2, "P31S"), (3, "PM220"), (2, "PM220S"), (3, "PM230"), (2, "PL70e-BT"), (3, "PM360"), (2, "P22"),
       (3, 'PL80E')]


class TemplateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = Template()  # 实例化Base对象
        cls.base.firstDownload_open()

    @parameterized.expand(dev)
    def test_getTempleList(self, devIndex, devName):
        self.base.get_getCategory(devIndex, devName)

    @classmethod
    def tearDownClass(cls):
        pass
