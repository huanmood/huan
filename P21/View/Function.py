import ast
import random
import re
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
url = 'http://192.168.17.130:4723/wd/hub'

# 清空按钮
clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
# 删除
delete = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_delete_btn"]']


class function(unittest.TestCase):
    base = None
    @classmethod
    def setUpClass(cls):
     try:
        cls.base = Base()  # 实例化Base对象
        cls.base.open(url, desired_caps)  # 启动Appium会话
        cls.base.first_open()  # 处理初次连接逻辑
        cls.base.connectP21()
        cls.base.connectP21()
     except Exception as e:
         print(e)
    def setUp(self):
        time.sleep(2)
    def rotate(self, Btn, Location, rotateBtn):
        try:
            # 对文本进行测试
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
            self.base.click(Btn)
            self.twoStpe_shucai()
            self.twoStpe_biankuang()
            self.threeStep_photo()
            self.twoStpe_tuya()
            for i in range(4):
                location = self.base.getAttribute(Location, 'bounds')
                matches = re.findall(r'\[(.*?)\]', location)  # 匹配中括号内的内容
                result = [[int(num) for num in match.split(',')] for match in matches]
                leftTop = result[0]
                rightTop = [result[1][0], result[0][1]]
                leftUnder = [result[0][0], result[1][1]]
                rightUnder = result[1]
                print("\n第", i + 1, "次")
                print("左上", leftTop)
                print("右上", rightTop)
                print("左下", leftUnder)
                print("右下", rightUnder)
                self.base.click(rotateBtn)

            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)

        except Exception as e:
            print("旋转功能测试失败: ", e)
            self.base.open(url, desired_caps)  # 启动Appium会话
            self.base.connectP21()
            self.base.connectP21()
            return

    def lock(self, Btn, Location, lockBtn):
        try:
            # 锁定功能
            print("\n锁定功能开始测试\n")
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
            self.base.click(Btn)
            self.twoStpe_shucai()
            self.twoStpe_biankuang()
            self.threeStep_photo()
            self.twoStpe_tuya()
            time.sleep(2)
            self.base.drag_element(ele=Location, end_x=402, end_y=478)  # 拖动文本元素（证明可拖动）
            location1 = self.base.elementBoundary(Location)  # 获取文本元素的位置1
            self.base.click(lockBtn)  # 锁定文本元素
            self.base.drag_element(ele=Location, end_x=614, end_y=910)  # 再次拖动
            location2 = self.base.elementBoundary(Location)  # 获取文本元素的位置2
            if self.base.assertTextBoxMoved(location1, location2):  # 断言再次拖动后位置是否更改，如果没有更改说明锁定成功
                print("锁定元素后无法位移判断成功")

            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
            print("\n锁定功能结束测试\n")

        except Exception as e:
            print("锁定功能测试失败: ", e)
            self.base.open(url, desired_caps)  # 启动Appium会话
            self.base.connectP21()
            self.base.connectP21()
            return

    def center(self, Btn, location, centerBtn):
        try:
            # 对文本进行测试
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
            self.base.click(Btn)
            self.twoStpe_shucai()
            self.twoStpe_biankuang()
            self.threeStep_photo()
            self.twoStpe_tuya()
            # 居中功能
            print("\n居中功能开始测试\n")
            location1 = self.base.elementBoundary(location)  # 获取居中前文本元素的位置
            self.base.drag_element(ele=location, end_x=302, end_y=478)
            self.base.elementBoundary(location)  # 获取居中前文本元素的位置
            self.base.click(centerBtn)
            location3 = self.base.elementBoundary(location)  # 获取居中前文本元素的位置
            if self.base.assertTextBoxMoved(location1, location3):
                print("元素已居中")
            else:
                print("元素位置不重合")

            print("\n居中功能结束测试\n")
            time.sleep(3)
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
        except Exception as e:
            print("居中功能测试失败: ", e)
            self.base.open(url, desired_caps)  # 启动Appium会话
            self.base.connectP21()
            self.base.connectP21()
            return

    def copy(self, Btn, location, copyBtn):
        try:
            print("\n复制功能开始测试\n")
            # 生成一个范围在 [a, b] 之间的随机整数
            # 复制功能
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
            self.base.click(Btn)
            self.twoStpe_shucai()
            self.twoStpe_biankuang()
            self.threeStep_photo()
            self.twoStpe_tuya()
            self.base.click(copyBtn)
            # 使用 XPath 查找所有匹配的元素
            elements = self.base.matchingElement(location)
            print('\n复制后共有', len(elements), '条文本\n')
            if len(elements) == 2:
                print("复制成功")
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
        except Exception as e:
            print("复制功能测试失败: ", e)
            self.base.open(url, desired_caps)  # 启动Appium会话
            self.base.connectP21()
            self.base.connectP21()
            return

    """     choose（）
            需要两步才能把内容添加到编辑器
            1、素材
            2、边框
    """

    def choose(self, Btn, location1, location2, ele):
        try:
            self.base.tap_at_Windows(0.5, 0.3)
            self.base.click(clear)
            self.base.click(Btn)
            self.twoStpe_shucai()
            self.twoStpe_biankuang()
            self.threeStep_photo()
            self.twoStpe_tuya()
            copy = ['XPATH',
                    '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]/android.widget.ImageView']
            self.base.click(copy)
            time.sleep(1)
            self.base.tap_at_coordinate(location2)
            self.base.drag_element(location2, 400, 400)
            # 多选按钮
            chooses = ['XPATH',
                       '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_multi_btn"]/android.widget.ImageView']
            self.base.click(chooses)
            self.base.tap_at_coordinate(location2)
            self.base.tap_at_coordinate(location1)
            delete = ['XPATH',
                      '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_delete_btn"]/android.widget.ImageView']
            self.base.click(delete)
        except Exception as e:
            print("复制功能测试失败: ", e)
            self.base.open(url, desired_caps)  # 启动Appium会话
            self.base.connectP21()
            self.base.connectP21()
            return
    def twoStpe_shucai(self):
        if self.base.is_element_present(
                '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[1]'):
            # 生成一个范围在 [a, b] 之间的随机整数
            ele = r'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout'
            num = self.base.matchingElement(ele)
            raNum = random.randint(1, len(num))
            eleNum = ['XPATH',
                      '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout' + '[' + str(
                          raNum) + ']']
            self.base.click(eleNum)
            location = ['XPATH',
                        '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
            self.base.tap_at_coordinate(location)

    def twoStpe_biankuang(self):
        if self.base.is_element_present(
                '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout[1]'):
            # 生成一个范围在 [a, b] 之间的随机整数
            ele = r'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout'
            num = self.base.matchingElement(ele)
            raNum = random.randint(1, len(num))
            eleNum = ['XPATH',
                      '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout' + '[' + str(
                          raNum) + ']']
            self.base.click(eleNum)
            location = ['XPATH',
                        '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
            self.base.tap_at_coordinate(location)

    def twoStpe_tuya(self):
        if self.base.is_element_present(
                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]'):
            tuyaLocation = self.base.getAttribute(
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

            self.base.drag_location(start_x=raNum[0], start_y=raNum[2], end_x=raNum[1], end_y=raNum[3])
            time.sleep(3)
            self.base.click(['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_right"]'])
            print('raNum为', raNum)

    def threeStep_photo(self):
        # phoneBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[5]']
        if self.base.is_element_present(
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
            if self.base.is_element_present(
                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_text" and @text="拍照"]'):
                self.base.click(takePhoto)
            if self.base.is_element_present(
                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_message_message"]'):
                self.base.click(permission)
            if self.base.is_element_present(
                    '//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]'):
                self.base.click(allow)
            self.base.click(press)
            self.base.click(confirm)
    @classmethod
    def tearDownClass(cls):
        cls.base.driver.quit()
