import ast
import os
import random
import re
import string
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import cv2
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.support.wait import WebDriverWait



class Base(unittest.TestCase):
    def __init__(self):
        self.driver = None


    def is_element_present(self, what):
        """
        寻找元素是否存在
        :param what: 传入元素位置
        :return: 布尔值
        """
        try:
            self.driver.find_element_by_xpath(what)
        except NoSuchElementException:
            return False
        return True

    def open(self, url, data):
        """
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
        if self.is_element_present('//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]'):
            # 授权
            authorization = self.driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]')
            authorization.click()
            # 允许获取位置
            allow_location = self.driver.find_element_by_xpath(
                '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
            allow_location.click()

    def first_open(self):
        """
         首次下载打开APP的授权
        :return:
        """
        # 判断元素是否存在
        if self.is_element_present('//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_message_message"]'):
            agree = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ui_confirm"]']
            self.click(agree)
        if self.is_element_present('//android.widget.TextView[@resource-id="com.nelko.printer:id/connect_later_tv"]'):
            # 如果元素存在，则执行操作
            # 稍后连接
            nextTime = self.driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/connect_later_tv"]')
            nextTime.click()
            # 选择P21
            device_P21 = self.driver.find_element_by_xpath(
                '(//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/rl_bg"])[1]')
            device_P21.click()
            # 确认
            confirm = self.driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ok"]')
            confirm.click()
            # 跳过
            skip = self.driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_right"]')
            skip.click()

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

    def click(self, element):
        """
        点击事件
        :param element: ['XPATH','xxxxx']
        :return: 无
        """
        self.findElement(element).click()

    def sendKeys(self):
        """
        输入内容方法，暂未使用
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//android.widget.TextView[@resource-id="com.nelko.printer:id/codeContent"]'))
        )
        self.click(['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/codeContent"]'])
        element.send_keys("value")
        time.sleep(3)

    def quit(self):
        """
        关闭对象
        :return: 无
        """
        self.driver.quit()


    def waitElement(self, ele1):
        """
        等待元素出现，特定用于蓝牙
        :param ele1:
        :return:
        """
        wait = WebDriverWait(self.driver, 20)  # 设置最大等待时间为10秒
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, ele1)))  # 等待直到元素出现
            CC = self.findElement(['XPATH',
                                   '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="6D:B4:8E:49:43:6D"]'])
            CC.click()
        except:
            # 定义双击的元素的坐标
            bounds=self.findElement(['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]'])
            self.double_tap_element(bounds)

    def waitElementAppear(self, ele):
        """
        等待元素出现
        :param ele: 传入元素位置
        :return: 无
        """
        wait = WebDriverWait(self.driver, 20)  # 设置最大等待时间为10秒
        wait.until(EC.presence_of_element_located((By.XPATH, ele)))  # 等待直到元素出现

    def waitElementLost(self, element):
        """
        等待元素消失
        :param element: 传入元素位置
        :return: 布尔值，如果消失了就是Ture,否则就是False
        """
        try:
            # 显式等待，直到元素消失（最多等待10秒）
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, element)))
            print("Element has disappeared")
            return True
        except TimeoutException:
            print("Element did not disappear within the given time")
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
        return location

    # 断言两个位置是否一致（字典格式）
    def assertTextBoxMoved(self, initial_location, final_location):
        try:
            # 使用 assertDictEqual 来比较两个字典
            self.assertDictEqual(initial_location, final_location)
            # 如果没有抛出错误，表示两个字典相等，即位置没有变化
            return True  # 没有发生变化时返回
        except AssertionError:
            # 如果抛出了 AssertionError 错误，表示两个字典不相等，即位置发生了变化
            return False  # 发生变化时返回 True

    def assertStr(self, initial_location, final_location):
        try:
            # 使用 assertDictEqual 来比较两个字典
            assert initial_location == final_location
            # 如果没有抛出错误，表示两个字典相等，即位置没有变化
            return True  # 没有发生变化时返回 False
        except AssertionError:
            # 如果抛出了 AssertionError 错误，表示两个字典不相等，即位置发生了变化
            return False  # 发生变化时返回 True
    def matchingElement(self, ele):
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

    def tap_at_coordinates(self, x, y):
        """
        点击一次指定位置
        :param x: 元素x位置
        :param y: 元素y位置
        :return: 无
        """
        action = TouchAction(self.driver)
        action.tap(None, x, y).perform()  # 100ms delay can be adjusted as per your requirement

    def tap_at_coordinate(self, ele):
        """
         点击元素中心
        :param ele: 传入元素位置加查找方式
        :return: 无
        """
        action = TouchAction(self.driver)
        ele = self.centerLocation(ele)
        action.tap(None, ele[0], ele[1]).perform()

    def tap_at_Windows(self, x, y):
        """
        点击屏幕的百分比位置。
        传入小数1代表全屏，例如点击屏幕x轴的一半就传0.5
        :param x: 小数，0.5就是点击中心
        :param y: 小数,0.5就是点击中心
        :return: 无
        """
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_size()
        location = window_rect["width"], window_rect["height"]
        action.tap(None, location[0] * x, location[1] * y).perform()

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

    # 获取元素属性
    def getAttribute(self, ele, value):
        element = self.findElement(ele).get_attribute(value)
        return element

    # 将元素拖到x、y位置
    def drag_element(self, ele, end_x, end_y):
        """
        拖动操作
        :param start_x: 起始位置的X坐标
        :param start_y: 起始位置的Y坐标
        :param end_x: 结束位置的X坐标
        :param end_y: 结束位置的Y坐标
        """

        action = TouchAction(self.driver)
        ele = self.centerLocation(ele)
        action.long_press(x=ele[0], y=ele[1]).move_to(x=end_x, y=end_y).release().perform()  # 将元素拖到x、y位置

    def drag_location(self, start_x, start_y, end_x, end_y):
        """
        拖动操作
        :param start_x: 起始位置的X坐标
        :param start_y: 起始位置的Y坐标
        :param end_x: 结束位置的X坐标
        :param end_y: 结束位置的Y坐标
        """

        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def test_01_connectP21(self):
        print("\n连接P21功能开始测试\n")
        connect = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_connect"]']
        back = ['XPATH', '//android.widget.ImageView[@resource-id="com.nelko.printer:id/iv_back"]']
        refresh = ['XPATH', '//android.widget.TextView[@text="刷新"]']
        disconnect = '//android.widget.TextView[@resource-id="com.nelko.printer:id/act_two_inch_bt_disconnect_tv"]'
        connectFail = '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_message"]'
        sure = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]']
        self.click(connect)
        time.sleep(2)
        if self.is_element_present(disconnect):
            self.click(back)
        else:
            self.first_connect()
            # 连接
            self.click(refresh)
            connectTitle = self.findElement(
                ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]'])
            self.double_tap_element(connectTitle)
            self.double_tap_element(connectTitle)
            device = ['XPATH',
                      '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="6D:B4:8E:49:43:6D"]']
            self.click(device)
            time.sleep(2)
            if self.is_element_present(connectFail):
                time.sleep(2)
                self.click(sure)
                self.double_tap_element(connectTitle)
                self.double_tap_element(connectTitle)
                device = ['XPATH',
                          '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="6D:B4:8E:49:43:6D"]']
                self.click(device)
            time.sleep(3)
            deviceName = self.findElement(
                ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_printer_model"]'])
            connectStatus = self.findElement(
                ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_connect"]'])
            if deviceName.text == 'P21' and connectStatus.text == '已连接':
                print("P21连接成功")
            else:
                print("P21连接失败")
            time.sleep(3)
            print("\n连接P21功能结束测试\n")

    def test_02_openEditor(self):
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

    def twoStpe_shucai(self):
        if self.is_element_present(
                '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[1]'):
            # 生成一个范围在 [a, b] 之间的随机整数
            ele = r'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout'
            num = self.matchingElement(ele)
            raNum = random.randint(1, len(num))
            eleNum = ['XPATH',
                      '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout' + '[' + str(
                          raNum) + ']']
            self.click(eleNum)
            location = ['XPATH',
                        '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
            self.tap_at_coordinate(location)

    def twoStpe_biankuang(self):
        if self.is_element_present(
                '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout[1]'):
            # 生成一个范围在 [a, b] 之间的随机整数
            ele = r'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout'
            num = self.matchingElement(ele)
            raNum = random.randint(1, len(num))
            eleNum = ['XPATH',
                      '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout' + '[' + str(
                          raNum) + ']']
            self.click(eleNum)
            location = ['XPATH',
                        '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
            self.tap_at_coordinate(location)

    def twoStpe_tuya(self):
        if self.is_element_present(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]'):
            tuyaLocation = self.getAttribute(
                ['XPATH', '//android.view.View[@resource-id="com.nelko.printer:id/db_view"]'], 'bounds')
            tuyaBounds = '[' + tuyaLocation.replace('][', '],[') + ']'
            result = ast.literal_eval(tuyaBounds)

            raNum = []
            for i in range(0, 2):
                a = random.randint(result[0][0], result[1][0])
                raNum.append(a)
            for i in range(0, 2):
                a = random.randint(result[0][1], result[1][1])
                raNum.append(a)

            self.drag_location(start_x=raNum[0], start_y=raNum[2], end_x=raNum[1], end_y=raNum[3])
            time.sleep(3)
            self.click(['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_right"]'])
            print('raNum为', raNum)

    def threeStep_photo(self):
        # phoneBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[5]']
        if self.is_element_present(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_text" and @text="拍照"]'):
            takePhoto = ['XPATH',
                         '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_text" and @text="拍照"]']  # 点击图片后的拍照选项
            permission = ['XPATH',
                          '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ui_confirm"]']  # 前往授权
            allow = ['XPATH',
                     '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]']  # 允许Nelko拍照（使用该应用时允许）
            press = ['XPATH', '//android.view.View']  # 拍照快门
            confirm = ['XPATH',
                       '//android.widget.FrameLayout[@resource-id="com.nelko.printer:id/capture_layout"]/android.view.View[2]']  # 按下快门后的确认
            if self.is_element_present(
                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_text" and @text="拍照"]'):
                self.click(takePhoto)
            if self.is_element_present(
                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_message_message"]'):
                self.click(permission)
            if self.is_element_present(
                    '//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]'):
                self.click(allow)
            self.click(press)
            self.click(confirm)

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
