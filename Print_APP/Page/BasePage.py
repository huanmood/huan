# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam
import time
import os
import unittest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page import PageAndroid
from TestCase.TestAndroid.share_devices import thread_local
import traceback
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from common.logger import Log

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path), 'screenshots')
if not os.path.exists(screenshot_path): os.mkdir(screenshot_path)


class Action(unittest.TestCase):
    logger=Log()
    def __init__(self):
        self.driver = thread_local.driverName
        self.buttonElement = PageAndroid

    def find_element(self, loc):
        """重写查找元素方法"""
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except TimeoutException:
            self.logger.error(f"元素 {loc} 超时未找到")
        except NoSuchElementException:
            self.logger.error(f"元素 {loc} 不存在")
        except Exception as e:
            self.logger.error(f"其他错误: {e}")

    def find_elements(self, loc):
        """重写查找元素方法"""
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except Exception:
            self.logger.error('%s 页面中未能找到%s 元素' % (self, loc))

    def clear_key(self, loc):
        """重写清空文本输入法"""
        time.sleep(1)
        self.find_element(loc).clear()

    def send_keys(self, loc, value):
        """重写在文本框中输入内容的方法"""
        self.clear_key(loc)  # 先调用
        self.find_element(loc).send_keys(value)

    def click_button(self, loc):
        element = self.find_element(loc)  # 先获取元素对象
        try:
            # 尝试获取元素文本（兼容空文本情况）
            element_text = element.text if element.text else "[无可见文本]"
            # 打印定位器类型+定位值 + 元素文本
            self.logger.debug(f"点击文本:{element_text}=>定位值: {loc[1]}, ")
            element.click()  # 再执行点击
        except:
            self.logger.error(f"获取位置失败{loc[1]},点击事件执行失败")

    def back_button(self):
        """点击返回按钮"""
        self.driver.back()

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
        if self.exists_element(self.buttonElement.accredit):
            # 授权
            self.click_button(self.buttonElement.accredit)
            # 允许获取位置
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

    def wait_for_element(self, locator, timeout=10):
        """
        等待元素出现
        :param driver: WebDriver 实例
        :param locator: 元素定位器，例如 (By.ID, "element_id")
        :param timeout: 最大等待时间，默认10秒
        :return: 找到的元素
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator[0], locator[1])))

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
