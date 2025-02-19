import os
import random
import re
import string
import threading
from datetime import datetime
import time
import cv2
import numpy as np
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from gitCode.Base.ButtonElement import nelko_buttonElement
from gitCode.page.GlobalVar import GlobalVar
from skimage.metrics import structural_similarity as ssim
from gitCode.TestCase.share_devices import thread_local

global_var = GlobalVar()
# 创建线程本地存储



class Base(unittest.TestCase):
    def __init__(self):
        self.driver = thread_local.driver
        self.buttonElement = nelko_buttonElement()

    def is_element_present(self, what):
        """
        寻找元素是否存在,存在返回True，不存在返回Flase
        :param what: 传入元素位置
        :return: 布尔值
        """

        elements = self.driver.find_elements(By.XPATH, what[1])
        if len(elements) > 0:
            return True
        else:
            return False

    def open(self, url, data):
        """
        打开APP
        :param url: 地址
        :param data: 配置
        :return: 无
        """
        if url != '':
            self.driver = webdriver.Remote(url, data)
            self.driver.implicitly_wait(5)
        else:
            raise ValueError('please input localhost')

    def first_connect(self):
        """
        首次点击右上角连接的授权
        :return:
        """
        if self.is_element_present(self.buttonElement.accredit):
            # 授权
            self.click(self.buttonElement.accredit)
            # 允许获取位置
            self.click(self.buttonElement.connectPage_Allow_in_use)

    def firstDownload_open(self):
        """
         首次下载打开APP的授权
        :return:
        """
        # 判断元素是否存在
        if self.is_element_present(self.buttonElement.firstDownload_UserAgreementPrivacyPolicy):
            self.click(self.buttonElement.firstDownload_sure)
            # 稍后连接
            self.click(self.buttonElement.firstDownload_afterConnect)
            # 选择机型的确认
            self.click(self.buttonElement.firstDownload_confirm)
            # 跳过
            self.click(self.buttonElement.firstDownload_skip)

    def findElement(self, element):
        """
        寻找元素的方法
        :param element: ['XPATH','xxxxx']
        :return: driver对象
        """
        elem = None  # 初始化elem
        try:
            type = element[0]
            value = element[1]
            if type == 'id' or type == 'ID' or type == 'Id':
                elem = self.driver.find_element(By.ID, value)
            elif type == 'name' or type == 'NAME' or type == 'Name':
                elem = self.driver.find_element(By.NAME, value)
            elif type == 'class' or type == 'CLASS' or type == 'Class':
                elem = self.driver.find_element(By.CLASS_NAME, value)
            elif type == 'link_text' or type == 'LINK_TEXT' or type == 'Link_Text':
                elem = self.driver.find_element(By.LINK_TEXT, value)
            elif type == 'css' or type == 'CSS' or type == 'Css':
                elem = self.driver.find_element(By.CSS_SELECTOR, value)
            elif type == 'xpath' or type == 'XPATH' or type == 'Xpath':
                elem = self.driver.find_element(By.XPATH, value)
            elif type == 'elements' or type == 'ELEMENTS' or type == 'Elements':
                elem = self.driver.find_elements(By.XPATH, value)
        except Exception:
            raise NameError('This element not found !' + str(element))
        return elem

    def send_key(self, element, value):
        self.findElement(element).send_keys(value)

    def click(self, element):
        """
        点击事件
        :param element: ['XPATH','xxxxx']
        :return: 无
        """
        self.findElement(element).click()

    def quit(self):
        """
        关闭对象
        :return: 无
        """
        self.driver.quit()

    # def connect(self, deviceName, device_Bluetooth):

    def waitElementAppear(self, ele1, ele2):
        """
        等待元素出现，特定用于蓝牙
        :param ele1:
        :return:
        """
        wait = WebDriverWait(self.driver, 20)  # 设置最大等待时间为10秒
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, ele1)))  # 等待直到元素出现
            self.click(ele1)
        except:
            # 定义双击的元素的坐标
            bounds = self.findElement(ele2)
            self.double_tap_element(bounds)

    def wait_for_element(self, locator, timeout=15):
        """
        等待元素出现
        :param driver: WebDriver 实例
        :param locator: 元素定位器，例如 (By.ID, "element_id")
        :param timeout: 最大等待时间，默认10秒
        :return: 找到的元素
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, locator)))

    def waitElementLost(self, element):
        """
        等待元素消失
        :param element: 传入元素位置
        :return: 布尔值，如果消失了就是Ture,否则就是False
        """
        try:
            # 显式等待，直到元素消失（最多等待10秒）
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, element)))
            print("元素消失了")
            return True
        except TimeoutException:
            print("元素未消失")
            return False

    def elementBoundary(self, element):
        """
         获取元素的location或size位置
        :param element: 需要传入元素位置加查找方式['','']
        :return: 返回location {x:,y:}
        """
        text_box = self.findElement(element)
        # 使用element.size和element.location
        # size = text_box.size  # 获取元素的大小
        location = text_box.location  # 获取元素的位置
        return {
            'x': location['x'],
            'y': location['y']
        }

    # 断言两个位置是否一致
    def assertTextBoxMoved(self, initial_location, final_location):
        try:
            # 使用 assertDictEqual 来比较两个字典
            self.assertDictEqual(initial_location, final_location)
            # 如果没有抛出错误，表示两个字典相等，即位置没有变化
            return True  # 没有发生变化时返回
        except AssertionError:
            # 如果抛出了 AssertionError 错误，表示两个字典不相等，即位置发生了变化
            return False  # 发生变化时返回 True

    def matchingElementXpath(self, ele):
        """
        查找一共有多少个（ele）这样的XPATH元素传
        :param ele: 传入元素位置
        :return: 数量
        """
        elements = self.driver.find_elements(By.XPATH, ele)
        return elements

    def matchingElementID(self, ele):
        """
        查找一共有多少个（ele）这样ID的元素
        :param ele: 传入元素位置
        :return: 数量
        """
        elements = self.driver.find_elements(By.ID, ele)
        return elements
        # 查找一共有多少个（ele）这样的元素

    def double_tap_element(self, element):
        """
        对指定的元素执行双击操作。
        参数:
        - element: 传入元素位置加查找方式。
        - return: 无
        """
        action = TouchAction(self.driver)
        action.tap(element).wait(100).tap(element).perform()

    # def tap_at_coordinates(self, x, y):
    #     """
    #     点击一次指定位置
    #     :param x: 元素x位置
    #     :param y: 元素y位置
    #     :return: 无
    #     """
    #     action = TouchAction(self.driver)
    #     action.tap(None, x, y).perform()  # 100ms delay can be adjusted as per your requirement

    # def tap_at_coordinate(self, ele):
    #     """
    #      点击元素中心
    #     :param ele: 传入元素位置加查找方式
    #     :return: 无
    #     """
    #     action = TouchAction(self.driver)
    #     ele = self.centerLocation(ele)
    #     action.tap(None, ele[0], ele[1]).perform()

    # def tap_at_Windows(self, x, y):
    #     """
    #     点击屏幕的百分比位置。
    #     传入小数1代表全屏，例如点击屏幕x轴的一半就传0.5
    #     :param x: 小数，0.5就是点击中心
    #     :param y: 小数,0.5就是点击中心
    #     :return: 无
    #     """
    #     action = TouchAction(self.driver)
    #     window_rect = self.driver.get_window_size()
    #     location = window_rect["width"], window_rect["height"]
    #     action.tap(None, location[0] * x, location[1] * y).perform()

    def capture_element_screenshot(self, element) -> np.ndarray:
        """
        截取指定元素的屏幕截图，并返回裁剪后的图像。

        :param element: WebElement 对象（需确保元素在屏幕内）。
        :return: 裁剪后的元素截图（NumPy 数组），失败返回 None。
        """
        try:

            # 确保元素在可视区域内
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # 获取全屏截图并转换为 RGB 格式
            screenshot = self.driver.get_screenshot_as_png()
            screenshot = np.frombuffer(screenshot, dtype=np.uint8)
            screenshot = cv2.imdecode(screenshot, cv2.IMREAD_COLOR)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)  # BGR 转 RGB

            # 获取元素位置和大小
            location = element.location
            size = element.size

            # 计算裁剪区域（防止越界）
            y_start = max(0, int(location['y']))
            y_end = min(screenshot.shape[0], int(location['y'] + size['height']))
            x_start = max(0, int(location['x']))
            x_end = min(screenshot.shape[1], int(location['x'] + size['width']))

            # 裁剪元素区域
            element_screenshot = screenshot[y_start:y_end, x_start:x_end]
            return element_screenshot

        except Exception as e:
            print(f"截取元素截图失败: {e}")
            return None

    def compare_images(self, img1: np.ndarray, img2: np.ndarray, threshold: float = 0.95) -> bool:
        """
        比较两张图片的相似度，返回是否一致。

        :param img1: 第一张图片（NumPy 数组）。
        :param img2: 第二张图片（NumPy 数组）。
        :param threshold: 相似度阈值（默认 0.95，即 95% 相似视为一致）。
        :return: True（一致）或 False（不一致）。
        """
        if img1 is None or img2 is None:
            print("输入图像为空")
            return False

        if img1.shape != img2.shape:
            print("图像尺寸不一致")
            return False

        try:
            # 转换为灰度图以提高计算效率
            gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

            # 计算结构相似性指数（SSIM）
            similarity, _ = ssim(gray1, gray2, full=True)
            return similarity >= threshold

        except Exception as e:
            print(f"图片比较失败: {e}")
            return False

    # 获取元素属性
    def getAttribute(self, ele, value):
        element = self.findElement(ele).get_attribute(value)
        return element

    # 将元素拖到x、y位置
    # def drag_element(self, ele, end_x, end_y):
    #
    #     action = TouchAction(self.driver)
    #     ele = self.centerLocation(ele)
    #     action.long_press(x=ele[0], y=ele[1]).move_to(x=end_x, y=end_y).release().perform()  # 将元素拖到x、y位置

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

    def openEditor(self):
        print("\n打开自定义模板功能开始测试\n")
        editor = ['XPATH',
                  '//android.widget.ImageView[@resource-id="com.nelko.printer:id/act_home_new_img"]']
        self.click(editor)
        self.first_connect()
        if self.is_element_present('//android.widget.TextView[@text="自定义空白标签纸"]'):
            # 自定义空白标签纸
            customTag = ['XPATH', '//android.widget.TextView[@text="自定义空白标签纸"]']
            self.click(customTag)
            confirm = ['XPATH', '//android.widget.TextView[@text="确定"]']
            self.click(confirm)
        if self.is_element_present('//android.widget.TextView[@text="双击文本框编辑"]'):
            print("打开自定义模板成功")
        time.sleep(2)
        print("\n打开自定义模板功能结束测试\n")

    # 获取元素中心
    def centerLocation(self, ele):
        location = self.getAttribute(ele, 'bounds')
        matches = re.findall(r'\[(.*?)\]', location)  # 匹配中括号内的内容
        result = [[int(num) for num in match.split(',')] for match in matches]
        leftTop = result[0]
        rightTop = [result[1][0], result[0][1]]
        leftUnder = [result[0][0], result[1][1]]
        rightUnder = result[1]
        centerPoint = []
        centerPointX = int(int(result[0][0]) + int(result[1][0])) // 2
        centerPointY = int(int(result[0][1]) + int(result[1][1])) // 2
        centerPoint.append(centerPointX)
        centerPoint.append(centerPointY)
        return centerPoint

    def generate_random_string(self):
        # 生成一个包含大小写字母和数字的所有字符集合
        characters = string.ascii_letters + string.digits

        # 使用random模块的choices函数从字符集合中随机选取8个字符，并将它们连接起来
        random_string = ''.join(random.choices(characters, k=8))
        return random_string

    # 获取当前小时
    def get_current_date(self):
        current_date = datetime.now().strftime('%d-%m-%Y')
        return current_date

    def get_images_from_folder(self, folder_path):
        """从指定文件夹中获取所有图片文件"""
        image_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                    file_path = os.path.join(root, file)
                    image_files.append(file_path)
        return image_files

    def Tutorials(self):
        """
        处理首页开箱教程
        """
        if self.is_element_present(self.buttonElement.Tutorials_connectDevices):
            self.click(self.buttonElement.Tutorials_connectDevices)
            self.click(self.buttonElement.Tutorials_Ikonw)
