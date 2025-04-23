import unittest
from parameterized import parameterized
from Page.PageAndroid.Template import Template
from TestCase.TestAndroid.share_devices import thread_context

dev = [("P21"), ("P31S"), ("PM220"), ("PM220S"), ("PM230"), ("PL70e-BT"), ("PM360"), ("P22"),
       ("PL80E")]


class TemplateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = Template()  # 实例化Base对象
        cls.base.firstDownload_open()

    @parameterized.expand(dev)
    def test_getTempleList(self, devName):
        thread_context.log(devName)
        self.base.get_getCategory(devName)

    @classmethod
    def tearDownClass(cls):
        pass
