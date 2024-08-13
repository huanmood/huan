import time
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Method.Base import Base

import unittest

desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.nelko.printer",
    "appium:appActivity": "com.print.android.zhprint.home.SplashActivity",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": "true"

}
url = 'http://localhost:4723/wd/hub'

# 清空按钮
clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
# 删除
delete = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_delete_btn"]']


class TestTextView(unittest.TestCase):
    base = None

    @classmethod
    def setUpClass(cls):
        cls.base = Base()  # 实例化Base对象
        cls.base.open(url, desired_caps)  # 启动Appium会话
        cls.base.first_open()  # 处理初次连接逻辑
        cls.base.connectP21()
        cls.base.openEditor()

    def setUp(self):
        time.sleep(2)

    def TextCompare(self, Btn, location, move):
        self.base.tap_at_Windows(0.5, 0.3)
        self.base.click(clear)
        self.base.click(Btn)
        element = self.base.findElement(location)
        screenshot1 = self.base.capture_element_screenshot(element)
        self.base.click(move)
        element = self.base.findElement(location)
        screenshot2 = self.base.capture_element_screenshot(element)
        result = self.base.compare_images(screenshot1, screenshot2)
        print("Images are identical" if result else "Images are different")

    # def AlignCompare(self, Btn, chanceView,location, move):
    #     self.base.tap_at_Windows(0.5, 0.3)
    #     self.base.click(clear)
    #     self.base.click(Btn)
    #     self.base.click(chanceView)
    #     element = self.base.findElement(location)
    #     screenshot1 = self.base.capture_element_screenshot(element)
    #     print("1,",screenshot1)
    #     self.base.click(move)
    #     element = self.base.findElement(location)
    #     screenshot2 = self.base.capture_element_screenshot(element)
    #     print("2,",screenshot2)
    #     result = self.base.compare_images(screenshot1, screenshot2)
    #     print("Images are identical" if result else "Images are different")
    # def test_fontType(self):
    #     super().fontType()

    @classmethod
    def tearDownClass(cls):
        cls.base.quit()
