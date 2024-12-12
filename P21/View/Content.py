import time

from Method.Base import Base
import unittest

desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "13",
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


class content(unittest.TestCase):
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

    def content(self, Btn):
        random_string = self.base.generate_random_string()
        self.base.tap_at_Windows(0.5, 0.3)
        self.base.click(clear)
        self.base.click(Btn)
        time.sleep(5)
        # self.base.click(move)
        self.base.sendKeys()
