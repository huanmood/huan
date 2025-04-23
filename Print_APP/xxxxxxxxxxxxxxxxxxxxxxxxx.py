# import os
# import glob
#
#
#
#
#
# def get_file_count_and_match(package_path, match_pattern=None):
#     # 获取所有文件
#     all_files = []
#     for root, dirs, files in os.walk(package_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             all_files.append(file_path)
#
#     # 如果有匹配条件，则筛选出符合条件的文件
#     if match_pattern:
#         matched_files = [file for file in all_files if match_pattern in file]
#         for file in matched_files:
#             print(os.path.basename(file))
#         print(f"Number of matched files: {len(matched_files)}")
#     else:
#         matched_files = []
#     return [os.path.basename(file) for file in matched_files]
#
# # 使用示例
# pwd = os.path.join(os.getcwd(), 'config')
# print(pwd)
# package_path = pwd  # 替换为包的路径
# match_pattern = 'Android_'  # 替换为你想匹配的文件名（可以是部分文件名或通配符）
# matched_file_names = get_file_count_and_match(package_path, match_pattern)
# print(f"Matched file names: {matched_file_names}")
# import os
# #
# # package_path = os.path.join(os.getcwd(), 'TestCase\TestAndroid')
# # A=os.path.join(package_path, 'index')
# # print(A)
# test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TestCase","TestAndroid")
# print(test_dir)
# import requests
#
# url = f'https//app.nelko.net/api/template/getCategory/P21'
# headers1 = {
#     "language": "zh",
# }
# data = requests.get(url=url, headers=headers1, verify=False)
# data = data.json()['data']
# for i in data:
#     name.append(i['name'])
# if devIndex > 6:
#     self.drag_location(906, 3371, 906, 412)
import threading
from random import random

from selenium.webdriver.common.by import By

# dev_01=["P21","P31S","PM220","PM220S","PM360","P22"]
# a="P21"
# print(a in dev_01)

# def login(self):
#     def login():
#         self.email = self.base.wait_for_element(self.base.buttonElement.MyPage_email[1])
#         self.email.click()
#         self.email.send_keys(login_data[0])
#         self.password = self.base.wait_for_element(self.base.buttonElement.MyPage_password[1])
#         self.password.click()
#         self.password.send_keys(login_data[1])
#         self.agree = self.base.wait_for_element(self.base.buttonElement.MyPage_agree[1])
#         self.agree.click()
#         self.loginButton = self.base.wait_for_element(self.base.buttonElement.MyPage_loginButton[1])
#         self.loginButton.click()
#
#         # self.base.click(self.base.buttonElement.MyPage_email)
#         # self.base.send_key(self.base.buttonElement.MyPage_email, login_data[0])
#         # self.base.click(self.base.buttonElement.MyPage_password)
#         # self.base.send_key(self.base.buttonElement.MyPage_password, login_data[1])
#         # self.base.click(self.base.buttonElement.MyPage_agree)
#         # self.base.click(self.base.buttonElement.MyPage_loginBtn)
#         time.sleep(2)
#         if self.base.is_element_present(self.base.buttonElement.MyPage_Cloud_sync):
#             self.base.click(self.base.buttonElement.MyPage_open)
#     login_data = getCaps_data("../Data/login.txt")
#     print("login_data::::", login_data)
#     if self.base.is_element_present(self.base.buttonElement.MyPage_email):
#         login()
#         return
#     if self.base.is_element_present(self.base.buttonElement.Homepage_myTemplate):
#         self.base.click(self.base.buttonElement.MyPage_my)
#         time.sleep(1)
#         self.base.click(self.base.buttonElement.MyPage_login)
#         login()
#         time.sleep(1)
#         self.base.click(self.base.buttonElement.Homepage_Homepage)
#         return
# Homepage_connect = (
# By.XPATH, '//android.view.ViewGroup[@resource-id="com.nelko.printer:id/constraint"]/android.widget.LinearLayout[2]')
# print(Homepage_connect[0], Homepage_connect[1])
# import random
# print("gg")
# # print(a)
# import random
# a=['14x40', '40x14', '40x15']
# raNum=random.randint(0,len(a))
# print(raNum)
# import logging
# logger = logging.getLogger('my.logger.namespace')
#
# fh = logging.FileHandler('test.log')  # 可以向文件发送日志
#
# ch = logging.StreamHandler()  # 可以向屏幕发送日志
#
# fm = logging.Formatter('%(asctime)s %(message)s')  # 打印格式
#
# fh.setFormatter(fm)
# ch.setFormatter(fm)
#
# logger.addHandler(fh)
# logger.addHandler(ch)
# logger.setLevel(logging.ERROR)  # 设置级别
#
#
# logger.error('debug 喜喜')
# print('\na')
import logging
# logging.basicConfig(
#     format='%(threadName)s: %(message)s',
#     level=logging.INFO
# )
# logging.info("这是打印内容")
# 为不同线程使用不同颜色
# import threading
#
#
# class ColoredPrinter:
#     def __init__(self):
#         self.local = threading.local()
#         self.colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
#         self.color_index = 0
#         self.lock = threading.Lock()
#
#     def get_color(self):
#         if not hasattr(self.local, 'color'):
#             with self.lock:
#                 self.local.color = self.colors[self.color_index % len(self.colors)]
#                 self.color_index += 1
#         return self.local.color
#
#     def print(self, message):
#         color = self.get_color()
#         reset = '\033[0m'
#         print(f"{color}[Thread-{threading.get_ident()}]: {message}{reset}")
#
#
# # 使用示例
# printer = ColoredPrinter()
#
#
# def worker(printer):
#     printer.print("第一条消息")
#     printer.print("第二条消息")
#
#
# threads = []
# for _ in range(5):
#     t = threading.Thread(target=worker, args=(printer,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()