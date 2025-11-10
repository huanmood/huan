# -*- coding:utf-8 -*-
import time
from multiprocessing import Process
import os
from TestCase.share_devices import process_context
import re
import pytest
from appium.options.common import AppiumOptions
from appium import webdriver

cur_path = os.getcwd()
android_caps_path = os.path.join(os.path.join(cur_path, 'config'), 'android_caps.yaml')
ios_caps_path = os.path.join(os.path.join(cur_path, 'config'), 'ios_caps.yaml')

options = AppiumOptions()


def add_case(devices_data_file, testPyName):
    # if re.search(r'Android', devices_data_file):
    #     desired_caps = {
    #             "platformName": "Android",
    #             "platformVersion": "12",
    #             "appPackage": "com.nelko.printer",
    #             "appActivity": "com.ezink.app.nelko.ui.SplashActivity",
    #             "deviceName": "6ebb6b77",
    #             "automationName": "UiAutomator2"
    #     }
    #     driver = webdriver.Remote(f"http://172.16.130.63:4726", desired_caps)
    #     driver.implicitly_wait(15)
    global driver
    if re.search(r'IOS', devices_data_file):
        options.load_capabilities({
            "platformName": "iOS",
            "platformVersion": "15.4.1",
            "deviceName": "iPhone 11",
            "udid": "00008030-0001314236E9802E",
            "bundleId": "com.nelko.printer",
            "automationName": "XCUITest",
            "noReset": True,
            "useXctestrunFile": False,
            "skipLogCapture": True,
            "wdaLocalPort": 8200,
            'usePrebuiltWDA': True,  # 使用已安装的 WDA
            'useNewWDA': False,  # 不要每次都卸载重装 WDA
            'startWDA': False,  # Windows 无法启动 WDA，所以设为 False
            'webDriverAgentUrl': 'http://127.0.0.1:8200',
        })
        driver = webdriver.Remote(
            command_executor=f"http://127.0.0.1:4723",
            options=options
        )
        time.sleep(3)
    process_context.driver = driver
    pytest.main(["TestCase/TestiOS/index/test_aiPicture.py", "-s", "-q"])


matched_file_names = [
    ("IOS_11.json", r"D:\huan-pytest\Print_APP\TestCase\TestiOS\index"),
    # ("Android_12.json", r"D:\huan-pytest\Print_APP\TestCase\TestAndroid\test\test_androidConnect.py")
]

if __name__ == '__main__':
    desired_process = []
    for i in matched_file_names:
        desired = Process(target=add_case, args=(i[0], i[1]))
        desired_process.append(desired)

    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

# matched_file_names = [
#     ("IOS_11.json", r"D:\huan\Print_APP\TestCase\TestAndroid\index"),
#     ("Android_12.json", r"D:\huan\Print_APP\TestCase\TestAndroid\test")
# ]
# # 构建进程组
# desired_process = []
# # 加载进程
# for i in matched_file_names:
#     desired = Process(target=add_case, args=(i[0], i[1]))
#     desired_process.append(desired)
# if __name__ == '__main__':
#     for desired in desired_process:
#         desired.start()
#     for desired in desired_process:
#         desired.join()
# processes = []
# # 方式2
# matched_file_names = [
#     ("Android_11.json", r"D:\huan\Print_APP\TestCase\TestAndroid\index"),
#     ("Android_12.json", r"D:\huan\Print_APP\TestCase\TestAndroid\mypage")
# ]
# with Pool() as pool:
#     pool.starmap(add_case,matched_file_names)
# # 方式1
# matched_file_names = [
#     ["Android_11.json", "TestCase.TestAndroid.index.test_AiPrint.py"],
#     ["Android_12.json", "TestCase.TestAndroid.index.test_AiPrint.py"]
#
# ]

# for i in matched_file_names:
#     process = multiprocessing.Process(target=add_case, args=(i[0], i[1]))
#     processes.append(process)
#     process.start()
#
# for process in processes:
#     process.join()
