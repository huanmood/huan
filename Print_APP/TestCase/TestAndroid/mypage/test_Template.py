import unittest
from parameterized import parameterized
from Page.PageAndroid.Template import Template
from TestCase.TestAndroid.share_devices import process_context

dev = [("P21"), ("PM220"), ("PM230")]

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
