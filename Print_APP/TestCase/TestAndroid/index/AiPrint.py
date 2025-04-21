import unittest

from parameterized import parameterized
from selenium.webdriver.common.by import By

from Page.PageAndroid.AiPrint import AiPrint

DEVICE_TEMPLATE_MAPPING = {
    # 模板位置位于首页第1个位置的设备
    "P21": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "P31S": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "PM220": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "PM220S": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "PM360": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "P22": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    # 模板位置位于首页第2个位置的设备
    "PL70e-BT": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[2]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "replacePrintPaper",
                "action": "know"
            },
            {
                "element": "moreFeatures",
                "action": "sure"
            }
        ]
    },
    "PL80E": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[2]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "moreFeatures",
                "action": "sure"
            },
            {
                "element": "replacePrintPaper",
                "action": "know"
            }
        ]
    },
    "PM230": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[2]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "moreFeatures",
                "action": "sure"
            }
        ]
    }
}


class AiPrintTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = AiPrint()
        cls.base.firstDownload_open()

    @parameterized.expand(DEVICE_TEMPLATE_MAPPING)
    def test_AiPrint(self, devIndex, devName):
        self.base.get_aiprint(devIndex, devName)
    def test_aa(self):
        print("第二个case")