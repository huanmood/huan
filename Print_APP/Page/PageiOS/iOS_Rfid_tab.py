# -*- coding:utf-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from Page import PageiOS


class rfid_tab:
    def __init__(self, action):
        """
        Connect 页面对象
        :param action: Action 对象，用于操作 App
        """
        self.action = action
        self.driver = action.driver
        self.ios=PageiOS
    def connected_print(self):
        self.action.tap_click(self.ios.rfid_tab_ele)
        self.action.tap_click(self.ios.printBT)
        self.action.tap_click(self.ios.printBT,4)
    def not_connect_print(self):
        pass
