from appium import webdriver
import time

from gitCode.util.write_device_yaml import WriteDeviceCommand


class Base_Driver:
    def __init__(self):
        # 已经把设备信息写入到了文件里，那我们就再从文件里取出来
        self.device_info = WriteDeviceCommand()

    # 由于获取device信息需要一个参数i，所以我们需要在方法的入参上添加i，并且从page到handle和bussiness全要新增这个i
    def get_android_driver(self):
        device_info_list = self.device_info.read_data()
        device = device_info_list.get("device_info_").get("deviceName")
        port = device_info_list.get("device_info_").get("port")


        # 需要定制化
        # server = 'http://localhost:4723/wd/hub'
        server = "http://127.0.0.1:" + str(port) + "/wd/hub"
        caps = {
            "platformName": "Android",
            "platformVersion": "11",
            "appPackage": "com.nelko.printer",
            "appActivity": "com.print.android.zhprint.home.SplashActivity",
            "deviceName": device,
            "noReset": "true"
        }
        android_driver = webdriver.Remote(server, caps)
        time.sleep(10)
        return android_driver

    def get_ios_driver(self):
        pass
