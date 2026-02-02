# -*- coding:utf-8 -*-
import time

from appium.webdriver.common.appiumby import AppiumBy
from TestCase.share_devices import process_context
from Page import PageiOS


class ios_Connect:
    def __init__(self, action):
        """
        Connect 页面对象
        :param action: Action 对象，用于操作 App
        """
        self.action = action
        self.driver = action.driver
        self.ios = PageiOS

    def check_connect(self):
        process_context.log('进入check_connect')
        """检查是否已连接，如果未连接则连接"""
        ele_list = self.driver.find_elements(*self.ios.not_connect_btn)
        if ele_list:
            state = ele_list[0].get_attribute("label")
            if state == "未连接":
                self.action.tap_click(self.ios.not_connect_btn)
        else:
            self.action.tap_click(self.ios.connect_btn)
            self.cut_connect()

    def cut_connect(self):
        process_context.log('进入cut_connect')
        self.action.tap_click(self.ios.disconnect, 2)
        self.action.tap_click(self.ios.sure, sleep=4)

    def connect(self, deviceName, deviceMac, max_retry=1000):
        process_context.log(f"进入connect，目标设备: {deviceName}:{deviceMac}")
        device_locator = (AppiumBy.XPATH, "//*[@label='{}']".format(deviceMac))

        retry_count = 0
        while retry_count < max_retry:
            elements1 = self.driver.find_elements(*device_locator)
            if elements1:
                self.action.tap_click(device_locator, sleep=5)
                process_context.log(f" 找到并点击设备: {deviceName}:{deviceMac}")
                return True
            else:
                # 滑动页面
                self.action.ios_swipe(start_x=204, start_y=830, end_x=206, end_y=162)
                elements2 = self.driver.find_elements(*device_locator)
                if elements2:
                    self.action.tap_click(device_locator, sleep=5)
                    return True
                refresh_btns = self.driver.find_elements(*self.ios.refresh)
                if refresh_btns:
                    self.action.tap_click(self.ios.refresh, sleep=2)
                    process_context.log(" 点击刷新按钮")
                retry_count += 1

        process_context.log(f"❌ 未找到设备: {deviceMac}，已重试 {max_retry} 次")
        return False
