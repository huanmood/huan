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
from TestCase.share_devices import process_context
from selenium.common.exceptions import TimeoutException, NoSuchElementException

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path), 'screenshots')
if not os.path.exists(screenshot_path): os.mkdir(screenshot_path)


class Action:
    def __init__(self, driver):
        self.driver = driver

    def tap_click(self, loc, sleep=1):
        try:
            ele_list = self.driver.find_elements(*loc)
            if ele_list != '[]':
                location = ele_list[0].location
                size = ele_list[0].size
                x = location['x'] + size['width'] / 2
                y = location['y'] + size['height'] / 2
                self.driver.tap([(x, y)], 100)
                try:
                    element_text = ele_list[0].text
                    if not element_text:
                        element_text = "[无可见文本]"
                except Exception:
                    element_text = "[无法获取文本]"

                process_context.log(f"点击=>{element_text}  {loc}")
                time.sleep(sleep)
                return
            else:
                print("ele_list为空：：：：", ele_list)
        except Exception as e:
            process_context.log(f"点击失败: {loc}")

    def find_element(self, loc):
        """重写查找元素方法"""
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except TimeoutException:
            self.log_error(f"元素 {loc}超时未找到")
        except NoSuchElementException:
            self.log_error(f"元素 {loc} 不存在")
        except Exception as e:
            self.log_error(f"其他错误: {e}")

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
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def click_button(self, loc, timeout=10):
        """
        点击按钮元素
        :param loc: (by, value) 元组
        :param timeout: 等待时间
        """
        try:
            # 等待元素可点击
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(loc)
            )
            element_text = element.text if element.text else "[无可见文本]"
            process_context.log(f"点击 {element_text} => 定位值: {loc}")
            element.click()
            return True
        except Exception as e:
            error_msg = f" 点击元素失败 {loc}, 原因: {e}"
            process_context.log(error_msg)
            return False

    def back_button(self):
        """点击返回按钮"""
        self.driver.back()
        time.sleep(0.5)
        self.log_error("执行返回")

    def exists_element(self, loc):
        """移动端最佳实践：判断元素是否存在"""
        self.driver.implicitly_wait(0)  # 临时禁用隐式等待
        elements = self.driver.find_elements(loc[0], loc[1])
        self.driver.implicitly_wait(10)  # 恢复默认等待
        return len(elements) > 0

    def getScreenShot(self):
        """重写截图方法"""
        self.sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d_%H_%M_%S'))
        self.driver.get_screenshot_as_file(self.sh_file)

    def get_windows_size(self):
        """获取屏幕大小"""
        windows_size = self.driver.get_window_size()
        return windows_size

    def ios_swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        iOS专用滑动方法
        :param duration: 滑动持续时间(ms)
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        time.sleep(1)

    # def first_connect(self):
    #     """
    #     首次点击右上角连接的授权
    #     :return:
    #     """
    #     if self.exists_element(self.buttonElement.connectPage_shouquan):
    #         # 授权
    #         self.click_button(self.buttonElement.connectPage_shouquan)
    #         # 始终允许
    #         self.click_button(self.buttonElement.connectPage_Allow_in_use)
    #
    # def firstDownload_open(self):
    #     """
    #      首次下载打开APP的授权
    #     :return:
    #     """
    #     # 判断元素是否存在
    #     a = self.exists_element(self.buttonElement.firstDownload_UserAgreementPrivacyPolicy)  # 用户协议和隐私政策
    #     if a:
    #         if self.exists_element(self.buttonElement.firstDownload_sure):  # 用户协议和隐私政策->确认
    #             self.click_button(self.buttonElement.firstDownload_sure)
    #         if self.exists_element(self.buttonElement.firstDownload_afterConnect):  # 稍后连接
    #             self.click_button(self.buttonElement.firstDownload_afterConnect)
    #         if self.exists_element(self.buttonElement.firstDownload_confirm):  # 确定
    #             self.click_button(self.buttonElement.firstDownload_confirm)
    #         if self.exists_element(self.buttonElement.skip):  # 关闭
    #             self.click_button(self.buttonElement.skip)
    #         if self.exists_element(self.buttonElement.connect_Dev_know):
    #             self.click_button(self.buttonElement.connect_Dev_know)

    def wait_for_element(self, locator, timeout=20) -> object:
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

    # def refresh_connection_page(self):
    #     self.click_button(self.buttonElement.connectPage_refresh)
    #     self.drag_location(start_x=539, start_y=1711, end_x=539, end_y=475)
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
    # 软键盘执行搜索操作
    def search(self):
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    # def isConnect(self):
    #     if self.exists_element(self.buttonElement.myTemplate):
    #         print("现在位置是首页")
    #         text = self.find_element_android(self.buttonElement.connectState)
    #         if text.text == "已连接":
    #             print("打印机已连接")
    #         if text.text == '未连接':
    #             print("打印机未连接")
    #         return True
    #     else:
    #         print("当前不在首页位置，无法判断是否处于连接状态")
    #         return False

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

    # def tap_click(self, loc):
    #
    #     location = self.driver.find_element(loc[0], loc[1]).location
    #     size = self.driver.find_element(loc[0], loc[1]).size
    #     x = location['x'] + size['width'] / 2
    #     y = location['y'] + size['height'] / 2
    #
    #     self.driver.tap([(x, y)], 100)

    # def compare_images(self, img1, img2):
    #     """
    #     比较两张图片是否一致，调用一次方法生成一张
    #     和capture_element_screenshot()方法联用
    #     :param img1:
    #     :param img2:
    #     :return:Unknown
    #     """
    #
    #     difference = np.subtract(img1, img2)
    #     return not np.any(difference)
    #
    # if not redis.hget('getDeviceList', "P21"):  # 检查 "P21" 是否已存在
    #     print("redis没有机型列表数据")  # 如果不存在，则重新获取数据
    #     # 获取设备列表
    #     url = 'http://app.nelko.net/api/templateVip/getDeviceList'
    #     resp = requests.get(url).json().get('data', [])
    #     if not resp:
    #         print("设备列表 API 返回数据为空！")
    #         exit()
    #
    #     # 获取字典数据
    #     url1 = 'https://admin.nelko.net/prod-api/system/dict/data/list?pageNum=1&pageSize=30&dictType=model_index_show'
    #     header1 = {
    #         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxNzQ5NzIxOTY0NjM2Mjg2OTc3Iiwicm5TdHIiOiJycWhLSzVudURFME14bGRuYUNsMXdUWnZwb09UNGVqNSIsInVzZXJJZCI6MTc0OTcyMTk2NDYzNjI4Njk3N30.mesDoGSA9ra5UpN8vYukxPkHvD9aaoKjTKbM70JbydI'
    #     }
    #     resp1 = requests.get(url1, headers=header1).json().get('rows', [])
    #     if not resp1:
    #         print("字典数据 API 返回数据为空！")
    #         exit()
    #
    #     # 遍历设备列表，匹配 indexShow 和 dictSort
    #     for device in resp:
    #         device_name = device['deviceName']
    #         index_show_values = device['indexShow'].split(',')  # 如 ["0", "13", "14", ...]
    #
    #         # 存储匹配的 dictLabel
    #         matched_labels = []
    #         for dict_item in resp1:
    #             if str(dict_item['dictSort']) in index_show_values:
    #                 matched_labels.append(dict_item['dictLabel'])
    #
    #         # 将匹配的 dictLabel 存入 Redis（用逗号连接）
    #         if matched_labels:
    #             redis.hset('getDeviceList', device_name, ', '.join(matched_labels))
    #         else:
    #             print(f"警告：设备 {device_name} 的 indexShow 未匹配到字典数据！")

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
