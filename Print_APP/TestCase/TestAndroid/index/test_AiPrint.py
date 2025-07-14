# testcase.py
import unittest

from parameterized import parameterized

from Page.PageAndroid.AiPrint import AiPrint
from TestCase.TestAndroid.share_devices import process_context

dev = [("P21"), ("P31S"), ("PM220")]


class AiPrintTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = AiPrint()
        cls.base.firstDownload_open()

    @parameterized.expand(dev)
    def test_AiPrint(self, devName):
        self.base.log(f"开始测试设备: {devName}")
        self.base.get_aiprint(devName)
        self.base.log(f"设备 {devName} 测试完成")

    def test_AiPrint_list(self):
        self.base._compare_templates()

    def test_aa(self):
        self.base.log("执行第二个测试用例")
