# -*- coding:utf-8 -*-
import random
from multiprocessing import Pool, Process
import os
import unittest
from appium.options.android import UiAutomator2Options

from Page.BasePage import Action
from common.read_json import read_json_nokey
from appium import webdriver
from common.read_caps import read_caps
from TestCase.TestAndroid.share_devices import process_context

cur_path = os.getcwd()
caps_path = os.path.join(os.path.join(cur_path, 'config'), 'android_caps.yaml')


def add_case(devices_data_file, testPyName):

    devices_data = read_json_nokey(devices_data_file)
    data = read_caps(caps_path=caps_path)
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': str(devices_data[0][0]),
        'deviceName': str(devices_data[0][1]),
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        'automationName': 'UiAutomator2',
        'resetKeyboard': data['resetKeyboard'],
        'ignoreHiddenApiPolicyError': True
    }

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(devices_data[0][2]) + '/wd/hub',
                              options=UiAutomator2Options().load_capabilities(desired_caps))
    with process_context.set_driver(driver):
        process_context.log("Driver initialized, starting test cases")
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(testPyName, pattern='test_*.py')
        test_runner = unittest.TextTestRunner()
        test_runner.run(test_suite)
        process_context.log("Test case execution finished")

matched_file_names = [
    # ("Android_11.json", r"D:\huan\Print_APP\TestCase\TestAndroid\index"),
    ("Android_12.json", r"D:\huan\Print_APP\TestCase\TestAndroid\mypage")
]
# 构建进程组
desired_process = []
# 加载进程
for i in matched_file_names:
    desired = Process(target=add_case, args=(i[0], i[1]))
    desired_process.append(desired)
if __name__ == '__main__':
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
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
