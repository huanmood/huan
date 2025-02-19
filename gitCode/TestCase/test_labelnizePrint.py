import threading
import unittest
from gitCode.page.GlobalVar import GlobalVar
from gitCode.Base.Base import Base
import time

lock = threading.Lock()
globalVar = GlobalVar()
globalVar.set_value("i", 0)
current_position = 0
devices = [
    [("P21", "8B:90:08:6F:38:B9")],
    [("P21", "F6:41:6C:1F:1A:13")],
]


def getCaps_data(file):
    global current_position
    dict_list = []
    with lock:
        with open(file) as f:
            f.seek(current_position)
            data = f.readline()
            current_position = f.tell()
            data = data.strip().split(";")
            for i in range(len(data)):
                dict_list.append(data[i])
    return dict_list


# 获取设备列表
def get_devices_list():
    with lock:
        i = globalVar.get_value("i")
        print("当前是I是", i)
        devices_list = devices[i % len(devices)]
        i += 1
        globalVar.set_value("i", i)
        return devices_list


class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.base = Base()
        self.base.firstDownload_open()

    def test_01_login(self):
        def login():
            self.email = self.base.wait_for_element(self.base.buttonElement.MyPage_email[1])
            self.email.click()
            self.email.send_keys(login_data[0])
            self.password = self.base.wait_for_element(self.base.buttonElement.MyPage_password[1])
            self.password.click()
            self.password.send_keys(login_data[1])
            self.agree = self.base.wait_for_element(self.base.buttonElement.MyPage_agree[1])
            self.agree.click()
            self.loginButton = self.base.wait_for_element(self.base.buttonElement.MyPage_loginButton[1])
            self.loginButton.click()

            # self.base.click(self.base.buttonElement.MyPage_email)
            # self.base.send_key(self.base.buttonElement.MyPage_email, login_data[0])
            # self.base.click(self.base.buttonElement.MyPage_password)
            # self.base.send_key(self.base.buttonElement.MyPage_password, login_data[1])
            # self.base.click(self.base.buttonElement.MyPage_agree)
            # self.base.click(self.base.buttonElement.MyPage_loginBtn)
            time.sleep(2)
            if self.base.is_element_present(self.base.buttonElement.MyPage_Cloud_sync):
                self.base.click(self.base.buttonElement.MyPage_open)
        login_data = getCaps_data("../Data/login.txt")
        print("login_data::::", login_data)
        if self.base.is_element_present(self.base.buttonElement.MyPage_email):
            login()
            return
        if self.base.is_element_present(self.base.buttonElement.Homepage_myTemplate):
            self.base.click(self.base.buttonElement.MyPage_my)
            time.sleep(1)
            self.base.click(self.base.buttonElement.MyPage_login)
            login()
            time.sleep(1)
            self.base.click(self.base.buttonElement.Homepage_Homepage)
            return

    def test_02_connect(self):
        # 获取设备列表和递增 i
        devices_list = get_devices_list()
        for deviceName, deviceMac in devices_list:
            print(f"Detail: {deviceName} - {deviceMac}")
            time.sleep(3)
            a=self.base.buttonElement.Homepage_connect
            self.connectButton = self.base.wait_for_element(a)
            self.connectButton.click()
            self.base.first_connect()
            connectTitle = self.base.findElement(self.base.buttonElement.connectPage_title)
            deviceMac = ['XPATH',
                         f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{deviceMac}"]']
            print("deviceMac是：：：", deviceMac)
            while True:
                if self.base.is_element_present(deviceMac):
                    self.base.click(deviceMac)
                    print('连接成功')
                    if self.base.is_element_present(self.base.buttonElement.connectPage_connectFail):
                        self.base.click(self.base.buttonElement.connectPage_sure)
                        self.base.click(self.base.buttonElement.connectPage_refresh)
                        self.base.double_tap_element(connectTitle)
                        self.base.double_tap_element(connectTitle)
                        self.base.click(deviceMac)
                    else:
                        break
                else:
                    print(f"找不到{deviceName}--{deviceMac}进入else")
                    self.base.click(self.base.buttonElement.connectPage_refresh)
                    time.sleep(2)
                    self.base.double_tap_element(connectTitle)
                    self.base.double_tap_element(connectTitle)
                    if self.base.is_element_present(deviceMac):
                        self.base.click(deviceMac)
                        print('连接成功')
                        break
                    self.base.drag_location(start_x=539, start_y=1711, end_x=539, end_y=475)
                    time.sleep(3)

        print("Successful")
        time.sleep(3)

    def tearDown(self):
        pass
