# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam
import logging
import time
import os

import cv2
import numpy as np
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page import PageAndroid
from TestCase.TestAndroid.share_devices import process_context
from selenium.common.exceptions import TimeoutException, NoSuchElementException

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path), 'screenshots')
if not os.path.exists(screenshot_path): os.mkdir(screenshot_path)

import unittest


class Action(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.driver = process_context.driver
        self.buttonElement = PageAndroid

    def find_element(self, loc):
        """重写查找元素方法"""
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except TimeoutException:
            self.log_error(f"元素 {loc} 超时未找到")
        except NoSuchElementException:
            self.log_error(f"元素 {loc} 不存在")
        except Exception as e:
            self.log_error(f"其他错误: {e}")

    def find_elements(self, loc):
        """重写查找元素方法"""
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except Exception:
            self.log_error('%s 页面中未能找到%s 元素' % (self, loc))

    def log(self, message, level=logging.INFO):
        """统一的日志记录方法"""
        process_context.log(message, level)

    def log_debug(self, message):
        self.log(message, logging.DEBUG)

    def log_error(self, message):
        self.log(message, logging.ERROR)

    def log_fatal(self, message):
        self.log(message, logging.FATAL)

    def clear_key(self, loc):
        """重写清空文本输入法"""
        self.find_element(loc).clear()

    def send_keys(self, loc, value):
        """重写在文本框中输入内容的方法"""
        self.find_element(loc).send_keys(value)

    # def click_button(self, loc):
    #     element = self.find_element(loc)  # 先获取元素对象
    #     try:
    #         element_text = element.text if element.text else "[无可见文本]"
    #         self.log_error(f"点击{element_text}    =>定位值: {loc[1]}, ")
    #         element.click()
    #     except:
    #         error_msg = f"获取位置失败 {loc[1]}, 点击事件执行失败"
    #         self.log_error(error_msg)
    #         self.fail(error_msg)  # 这将使测试标记为失败
    def click_button(self, loc, timeout=10):

        element = self.find_element(loc)
        if element is None:
            error_msg = f"获取位置失败 {loc}, 点击事件执行失败"
            process_context.log(error_msg)
            self.fail(error_msg)  # 这将使测试标记为失败
        try:
            if self.wait_for_element(loc, timeout):
                element_text = element.text if element.text else "[无可见文本]"
                process_context.log(f"点击{element_text}    =>定位值: {loc}, ")
                element.click()
        except Exception as e:
            error_msg = f"点击元素失败 {loc}, 原因: {e}"
            process_context.log(error_msg)
            self.fail(error_msg)

    def back_button(self):
        """点击返回按钮"""
        self.driver.back()
        time.sleep(0.5)
        self.log_error("执行返回")

    def exists_element(self, loc):
        """判断元素是否存在 ==0为不存在  !=0为存在"""
        return self.driver.find_elements(*loc)

    def getScreenShot(self):
        """重写截图方法"""
        self.sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d_%H_%M_%S'))
        self.driver.get_screenshot_as_file(self.sh_file)

    def get_windows_size(self):
        """获取屏幕大小"""
        windows_size = self.driver.get_window_size()
        return windows_size

    def drag_location(self, start_x, start_y, end_x, end_y):
        """
        拖动操作
        :param start_x: 起始位置的X坐标
        :param start_y: 起始位置的Y坐标
        :param end_x: 结束位置的X坐标
        :param end_y: 结束位置的Y坐标
        """

        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def first_connect(self):
        """
        首次点击右上角连接的授权
        :return:
        """
        if self.exists_element(self.buttonElement.connectPage_shouquan):
            # 授权
            self.click_button(self.buttonElement.connectPage_shouquan)
            # 始终允许
            self.click_button(self.buttonElement.connectPage_Allow_in_use)

    def firstDownload_open(self):
        """
         首次下载打开APP的授权
        :return:
        """
        # 判断元素是否存在
        a = self.exists_element(self.buttonElement.firstDownload_UserAgreementPrivacyPolicy)  # 用户协议和隐私政策
        if a:
            if self.exists_element(self.buttonElement.firstDownload_sure):  # 用户协议和隐私政策->确认
                self.click_button(self.buttonElement.firstDownload_sure)
            if self.exists_element(self.buttonElement.firstDownload_afterConnect):  # 稍后连接
                self.click_button(self.buttonElement.firstDownload_afterConnect)
            if self.exists_element(self.buttonElement.firstDownload_confirm):  # 确定
                self.click_button(self.buttonElement.firstDownload_confirm)
            if self.exists_element(self.buttonElement.skip):  # 关闭
                self.click_button(self.buttonElement.skip)
            if self.exists_element(self.buttonElement.connect_Dev_know):
                self.click_button(self.buttonElement.connect_Dev_know)

    # def wait_for_element(self, locator, timeout=10):
    #     """
    #     等待元素出现
    #     :param driver: WebDriver 实例
    #     :param locator: 元素定位器，例如 (By.ID, "element_id")
    #     :param timeout: 最大等待时间，默认10秒
    #     :return: 找到的元素
    #     """
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.presence_of_element_located((locator[0], locator[1])))
    def wait_for_element(self, locator: object, timeout: object = 20) -> object:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except Exception as e:
            print(f"等待点击元素超时: {locator}")
            return False

    def double_tap_element(self, element):
        """
        对指定的元素执行双击操作。
        参数:
        - element: 传入元素位置加查找方式。
        - return: 无
        """
        action = TouchAction(self.driver)
        action.tap(element).wait(100).tap(element).perform()

    def quit(self):
        self.driver.quit()

    def refresh_connection_page(self):
        self.click_button(self.buttonElement.connectPage_refresh)
        self.drag_location(start_x=539, start_y=1711, end_x=539, end_y=475)

    # 软键盘执行搜索操作
    def search(self):
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})

    def isConnect(self):
        if self.exists_element(self.buttonElement.myTemplate):
            print("现在位置是首页")
            text = self.find_element(self.buttonElement.connectState)
            if text.text == "已连接":
                print("打印机已连接")
            if text.text == '未连接':
                print("打印机未连接")
            return True
        else:
            print("当前不在首页位置，无法判断是否处于连接状态")
            return False

    def capture_element_screenshot(self, element):
        """
        截取屏幕截图1
        :param element: 传入webdriver对象
        :return: 一张屏幕指定元素和大小的截图
        """
        screenshot = self.driver.get_screenshot_as_png()
        screenshot = np.frombuffer(screenshot, np.uint8)
        screenshot = cv2.imdecode(screenshot, cv2.IMREAD_COLOR)
        # 获取元素位置和大小
        location = element.location
        size = element.size
        # 根据元素位置和大小截取元素截图
        element_screenshot = screenshot[int(location['y']):int(location['y'] + size['height']),
                             int(location['x']):int(location['x'] + size['width'])]
        return element_screenshot

    def compare_images(self, img1, img2):
        """
        比较两张图片是否一致，调用一次方法生成一张
        和capture_element_screenshot()方法联用
        :param img1:
        :param img2:
        :return:Unknown
        """
        difference = np.subtract(img1, img2)
        return not np.any(difference)
