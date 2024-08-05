import re
import time
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Method.Base import Base

import unittest

desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "14",
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


class align(unittest.TestCase):
    base = None

    @classmethod
    def setUpClass(cls):
        cls.base = Base()  # 实例化Base对象
        cls.base.open(url, desired_caps)  # 启动Appium会话
        cls.base.first_open()  # 处理初次连接逻辑
        cls.base.test_01_connectP21()
        cls.base.test_02_openEditor()

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
    # def topAlign(self, Btn,location):
    #     # try:
    #     # 对齐按钮
    #     alignBtn = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_1"]']
    #     # 上对齐按钮
    #     topAlignBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/alignTop"]']
    #     self.base.tap_at_Windows(0.5, 0.3)
    #     self.base.click(clear)
    #     self.base.click(Btn)
    #     element=self.base.findElement(element)
    #
    #     self.base.twoStpe_shucai()
    #     self.base.twoStpe_biankuang()
    #     self.base.click(alignBtn)
    #     self.base.click(topAlignBtn)
    # 上对齐

    #     self.base.click(topAlignBtn)
    #     topAlignLcation = self.base.elementBoundary(textEle)
    #     if self.base.assertTextBoxMoved(topAlignLcation, topAlign):
    #         print("上对齐成功")
    # except Exception as e:
    #     print("字体上对齐功能测试失败: ", e)
    #     self.base.open(url, desired_caps)  # 启动Appium会话
    #     self.base.test_01_connectP21()
    #     self.base.test_02_openEditor()
    #     return
    #
    # def test_centerAlign(self):
    #     try:
    #         centerAlignBtn = ['XPATH',
    #                           '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/centerVertical"]']
    #         self.base.click(centerAlignBtn)
    #         centerAlignLcation = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(centerAlignLcation, centerAlign):
    #             print("上下居中成功")
    #     except Exception as e:
    #         print("字体上下居中功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_underAlign(self):
    #     try:
    #         # 下对齐
    #         underAlignBtn = ['XPATH',
    #                          '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/alignBottom"]']
    #         self.base.click(underAlignBtn)
    #         underAlignLcation = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(underAlignLcation, underAlign):
    #             print("下对齐成功")
    #             time.sleep(3)
    #     except Exception as e:
    #         print("字体下对齐功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_rightAlign(self):
    #     try:
    #         # 右对齐
    #         time.sleep(3)
    #         # 对齐按钮
    #         alignBtn = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_1"]']
    #         self.base.tap_at_coordinates(875, 635)
    #         self.base.click(clear)
    #         self.base.click(textBtn)
    #         self.base.click(alignBtn)
    #         self.base.drag_element(1019, 929, 850, 911)
    #         rightAlignBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/alignRight"]']
    #         self.base.click(rightAlignBtn)
    #         rightAlignBtn = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(rightAlignBtn, rightAlign):
    #             print("右对齐成功")
    #     except Exception as e:
    #         print("字体右对齐功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_middleAlign(self):
    #     try:
    #         # 左右居中
    #         middleAlignBtn = ['XPATH',
    #                           '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/centerHorizontal"]']
    #         self.base.click(middleAlignBtn)
    #         middleAlignLcation = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(middleAlignLcation, middleAlign):
    #             print("左右居中成功")
    #     except Exception as e:
    #         print("字体左右居中功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_leftAlign(self):
    #     try:
    #         # 左对齐
    #         leftAlignBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/alignLeft"]']
    #         self.base.click(leftAlignBtn)
    #         leftAlignLcation = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(leftAlignLcation, leftAlign):
    #             print("左对齐成功")
    #     except Exception as e:
    #         print("字体左对齐功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_up(self):
    #     try:
    #         self.base.tap_at_coordinates(875, 635)
    #         self.base.click(clear)
    #         self.base.click(textBtn)
    #         # 对齐按钮
    #         alignBtn = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_1"]']
    #         self.base.click(alignBtn)
    #         # 上对齐
    #         upBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/moveTop"]']
    #         for i in range(0, 20):
    #             self.base.click(upBtn)
    #         upLcation = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(upLcation, up):
    #             print("上对齐成功")
    #     except Exception as e:
    #         print("字体上移功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_down(self):
    #     try:
    #         # 下对齐
    #         downBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/moveBottom"]']
    #         for i in range(0, 20):
    #             self.base.click(downBtn)
    #         downLcation = self.base.elementBoundary(textEle)
    #         if self.base.assertTextBoxMoved(downLcation, down):
    #             print("下对齐成功")
    #     except Exception as e:
    #         print("字体下移功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_left(self):
    #     try:
    #         # 左对齐
    #         leftBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/moveLeft"]']
    #         for i in range(0, 20):
    #             self.base.click(leftBtn)
    #         leftLcation = self.base.elementBoundary(leftBtn)
    #         if self.base.assertTextBoxMoved(leftLcation, left):
    #             print("左对齐成功")
    #     except Exception as e:
    #         print("字体左移功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_right(self):
    #     try:
    #         # 右对齐
    #         rightBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/moveRight"]']
    #         for i in range(0, 20):
    #             self.base.click(rightBtn)
    #         rightLocation = self.base.elementBoundary(rightBtn)
    #         if self.base.assertTextBoxMoved(rightLocation, right):
    #             print("右对齐成功")
    #     except Exception as e:
    #         print("字体右移功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
