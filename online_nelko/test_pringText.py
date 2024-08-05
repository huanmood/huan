import os
import sys
import time

from appium.webdriver import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from parameterized import parameterized

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from appium import webdriver
from selenium.webdriver.common.by import By
import unittest

from unittestreport import TestRunner

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.nelko.printer",
    "appium:appActivity": "com.print.android.zhprint.home.SplashActivity",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": "true"
}
url = 'http://192.168.17.130:4723/wd/hub'

# 清除所有元素
clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
# 添加文本按钮
textBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[1]']
connect = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_connect"]']  # 首页右上角连接
back = ['XPATH',
        '//android.widget.ImageView[@resource-id="com.nelko.printer:id/iv_back"]']  # 返回：如果进入首页自动连接，则‘返回’，无需再次进行连接
refresh = ['XPATH', '//android.widget.TextView[@text="刷新"]']  # 连接页面的刷新
disconnect = '//android.widget.TextView[@resource-id="com.nelko.printer:id/act_two_inch_bt_disconnect_tv"]'  # 取消连接：如果出现‘取消连接’，则说明已经自动连接，无需再次连接
connectFail = '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_message"]'  # 判断是否连接失败：连接失败（P21、P31S）晶振问题
sure = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]']  # 是否切换BLE连接的确认按钮


class online(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(url, desired_caps)  # 打开APP
        self.driver.implicitly_wait(10)

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

    def double_tap_element(self, element):
        """
        对指定的元素执行双击操作。
        参数:
        - element: 传入元素位置加查找方式。
        - return: 无
        """
        action = TouchAction(self.driver)
        action.tap(element).wait(100).tap(element, 100).perform()

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

    def click(self, element):
        """
        点击事件
        :param element: ['XPATH','xxxxx']
        :return: 无
        """
        self.findElement(element).click()

    def openEditor(self):
        print("\n打开自定义模板功能开始测试\n")
        editor = ['XPATH',
                  '//android.widget.ImageView[@resource-id="com.nelko.printer:id/act_home_new_img"]']
        self.click(editor)
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

    def quit(self):
        self.driver.quit()

    def drag_location(self, start_x, start_y, end_x, end_y):
        """
        拖动操作
        :param start_x: 起始位置的X坐标
        :param start_y: 起始位置的Y坐标
        :param end_x: 结束位置的X坐标
        :param end_y: 结束位置的Y坐标
        """

        self.driver.swipe(start_x, start_y, end_x, end_y)

    @parameterized.expand([
        ("P20", "A6:ED:FC:24:DE:DD"),
        # ("PM220", "00:84:00:00:B7:DD"),
        # ("PM220S", "31:9D:28:23:32:BE"),
        # ("PM230", "E4:1A:E9:A1:84:41"),
        # ("PL70e-BT", "DC:1D:30:54:27:3C"),
        # ("PL80W", "00:12:42:84:8B:AA"),
        # ("PM360", "31:9D:4E:B2:E7:D5"),
        # ("R11", "93:0D:F7:3A:78:61"),
        # ("P22", "83:80:04:9E:88:38"),
        # ("P21(jieLi)", "6D:B4:8E:49:43:6D"),
        # ("P21(GD)", "60:6E:41:8C:8B:30"),
        # ("P31S", "DC:80:0C:83:9D:C8"),
        # 添加更多测试用例
    ])
    def test_print(self, devicesName, devicesBuletooth):
        """
        :return:
        """
        key = devicesName
        value = devicesBuletooth
        print(devicesName, "开始测试\n")
        self.click(connect)  # 点击右上角连接
        time.sleep(4)  # 等待打印机蓝牙加载
        if self.is_element_present(disconnect):  # 判断是否自动连接，如果是则返回，无需再次连接
            self.click(back)
        # 以下是没有自动连接，需要手动连接
        time.sleep(5)
        self.click(refresh)  # 刷新一下连接页面方便下面的双击排序
        connectTitle = self.findElement(
            ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]'])  # 安卓的双击连接对打印机排序
        self.double_tap_element(connectTitle)  # 双击连接对打印机排序
        self.double_tap_element(connectTitle)  # 双击连接对打印机排序
        if not self.is_element_present(
                f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]'):  # 如果没有找到对应的蓝牙地址连接
            while True:  # 一直循环找对应的蓝牙地址
                window_rect = self.driver.get_window_size()  # 获取屏幕的大小
                location = window_rect["width"], window_rect["height"]  # 接收屏幕大小
                startX, startY, endX, endY = location[0] * 0.5, location[1] * 0.85, location[0] * 0.5, location[
                    1] * 0.3  # 对所需要操作的位置进行赋值
                self.drag_location(startX, startY, endX, endY)  # 拖动屏幕寻找蓝牙进行连接
                time.sleep(3)
                self.click(refresh)  # 刷新连接页面，防止蓝牙没有加载出来
                self.double_tap_element(connectTitle)  # 双击连接对打印机排序
                self.double_tap_element(connectTitle)  # 双击连接对打印机排序
                if self.is_element_present(
                        f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]'):  # 如果找到了就退出循环
                    break
        self.click(['XPATH',
                    f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]'])  # 找到了就点击蓝牙进行连接
        time.sleep(10)  # 连接需要等待时间
        if self.is_element_present(connectFail):  # 如果连接失败（P21、P31S）晶振问题
            time.sleep(2)
            self.click(sure)  # 点击确认进行切换连接模式
            time.sleep(2)
            self.click(refresh)  # 刷新连接页面
            if not self.is_element_present(  # 与上面一致
                    f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]'):
                while True:
                    window_rect = self.driver.get_window_size()
                    location = window_rect["width"], window_rect["height"]

                    startX, startY, endX, endY = location[0] * 0.5, location[1] * 0.85, location[0] * 0.5, \
                                                 location[
                                                     1] * 0.3
                    self.drag_location(startX, startY, endX, endY)
                    time.sleep(3)
                    self.click(refresh)
                    if self.is_element_present(
                            f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]'):
                        break
            self.click(['XPATH',
                        f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]'])
        time.sleep(5)
        deviceName = self.findElement(
            ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_printer_model"]'])
        connectStatus = self.findElement(
            ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_connect"]'])
        if deviceName.text == key and connectStatus.text == '已连接':
            print(f"{key}连接成功")
        else:
            print(f"{key}连接失败")

        self.openEditor()  # 点击首页的+号，创建自定义模板
        if key == 'PM230':  # PM230初始模板宽高太长，需要修改短一点，使用重新添加文本解决
            self.click(clear)
            time.sleep(1)
            self.click(textBtn)
        self.click(['XPATH', '//android.widget.TextView[@text="打印"]'])  # 直接点击打印
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id="com.nelko.printer:id/etAmount"]').clear()  # 清空打印的份数（默认是1）
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id="com.nelko.printer:id/etAmount"]').send_keys(
            "5")  # 清空后输入份数为5
        self.click(['XPATH',
                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/act_print_mult_print_btn"]'])  # 点击打印
        print(f'{key}打印5份完成')
        time.sleep(15)  # 等待打印时间
        if key == 'PM230':
            self.click(['XPATH', '//android.widget.TextView[@text="关闭"]'])  # 打印完成的关闭：PM230需要手动点击完成
        print(f"\n连接{key}功能结束测试\n")
        self.click(['XPATH',
                    '//android.widget.ImageView[@resource-id="com.nelko.printer:id/iv_back"]'])  # 打印完成的返回（左上角的x）
        self.click(
            ['XPATH', '//android.widget.ImageView[@resource-id="com.nelko.printer:id/act_edit_back_img"]'])  # 模板左上角的返回
        self.click(
            ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_cancel"]'])  # 从模板返回，不保存
        self.click(connect)  # 重新进入连接页面
        time.sleep(3)
        self.click(['XPATH', disconnect])  # 取消上一台连接的打印机连接状态
        time.sleep(2)
        self.click(['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]'])  # 点击确认（取消连接的确认）
        time.sleep(3)
        self.driver.quit()

    # 第一步：收集测试用例


pwd = os.getcwd()
# case_path = os.path.join(pwd,"unittestreport数据驱动之列表.py")
suite = unittest.defaultTestLoader.discover(pwd)  # 自动获取测试用例类
print("测试套件中的测试用例数量是：", suite.countTestCases())
# 第二步：运行用例生成测试报告
runner = TestRunner(suite,
                    filename="自动化测试报告.html",
                    report_dir=r"C:\Users\YZY\Desktop\nelko\online_nelko\report",  # 放桌面
                    title='nelko版本上线测试报告',
                    tester='欢',
                    desc="测试",
                    templates=2  # 报告的风格，有三种，取值是1,2,3
                    )
runner.run()
sys.exit()
