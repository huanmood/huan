# -*- coding:utf-8 -*-

import os
import threading
import unittest

from TestCase.TestAndroid.share_devices import thread_context
from common.read_json import read_json_nokey
from appium import webdriver

driver_lock = threading.Lock()
from common.read_caps import read_caps

cur_path = os.getcwd()
caps_path = os.path.join(os.path.join(cur_path, 'config'), 'android_caps.yaml')
"""
执行用例并发送报告，分四个步骤:
第一步：加载用例
第二步：执行用例
第三步：获取最新的测试报告
第四步：发送邮件
"""

# 获取当前脚本的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(devices_data_file, testPyName):  # 第一个参数是（json文件名）用于获取不同手机的版本号，第二个参数是（测试用例的包名）
    devices_data = read_json_nokey(devices_data_file)
    data = read_caps(caps_path=caps_path)
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': str(devices_data[0][0]),
        'deviceName': str(devices_data[0][1]),
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noSign': data['noSign'],
        'noReset': data['noReset']
    }
    driver = webdriver.Remote('http://' + data['ip'] + ':' + str(devices_data[0][2]) + '/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    with thread_context.set_driver(driver):
        device_info = f"设备: {desired_caps['deviceName']}, 版本: {desired_caps['platformVersion']}"
        thread_context.log(f"测试开始 - {device_info}")
        test_loader = unittest.TestLoader()
        # 加载测试用例方式1（同一个包不同py名称）
        # testPyName1 = os.path.splitext(testPyName)[0]
        # test_suite = test_loader.loadTestsFromName(testPyName1)
        # 加载测试用例方式2（不同包）
        test_suite = test_loader.discover(testPyName, pattern='test_*.py')
        test_runner = unittest.TextTestRunner()
        result = test_runner.run(test_suite)
        thread_context.log(f"测试结束 - {device_info}. 结果: {len(result.errors)}错误, {len(result.failures)}失败")


    driver.quit()
if __name__ == '__main__':
    threads = []
    # 方式2
    matched_file_names = [
        ["Android_12.json", r"D:\huan\Print_APP\TestCase\TestAndroid\index"],
        ["Android_11.json", r"D:\huan\Print_APP\TestCase\TestAndroid\mypage"]
    ]
    # 方式1
    # matched_file_names = [
    #     ["Android_12.json", "TestCase.TestAndroid.index.test_Banner.py"]
    #     # ["Android_11.json", "TestCase.TestAndroid.index.test_AiPrint.py"]
    #
    # ]

    for i in matched_file_names:
        thread = threading.Thread(target=add_case, args=(i[0], i[1]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

