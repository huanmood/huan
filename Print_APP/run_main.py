# -*- coding:utf-8 -*-

import os
import threading
import unittest
from TestCase.TestAndroid.share_devices import thread_local
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
    thread_local.driverName = driver
    test_loader = unittest.TestLoader()
    # 加载测试用例方式1（同一个包不同py名称）
    testPyName1 = os.path.splitext(testPyName)[0]
    test_suite = test_loader.loadTestsFromName(testPyName1)
    # 加载测试用例方式2（不同包）
    # test_suite = test_loader.discover(testPyName, pattern='test_*.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)


if __name__ == '__main__':
    threads = []
    # 方式2
    # matched_file_names = [
    #     ["Android_12.json", r"D:\huan\huan\Print_APP\TestCase\TestAndroid\index"]
    #     # ["Android_11.json", r"D:\test\Print_APP\TestCase\TestAndroid\mypage"]
    # ]
    # 方式1
    matched_file_names = [
        ["Android_12.json", "TestCase.TestAndroid.index.test_AiPrint.py"]
        # ["Android_11.json", "TestCase.TestAndroid.index.test_AiPrint.py"]

    ]
    for i in matched_file_names:
        thread = threading.Thread(target=add_case, args=(i[0], i[1]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("All threads completed.")
# if __name__ == '__main__':
#     unittest.main()
# 加载用例
# all_case = add_case()
# # 执行用例
# run_case(all_case)
# 获取最新的测试报告
# report_path = os.path.join(cur_path, 'reports')
# report_file = get_report_file(report_path)
# # 邮箱配置

# 在同一个线程中加载并执行测试用例


# def run_case(all_case, reportName='reports'):
#     '''
#     作用：执行所有的用例，并把执行结果写入HTML测试报告中
#     :param all_case:
#     :param reportName:
#     :return:
#     '''
#     now = time.strftime('%Y_%m_%d_%H_%M_%S')
#     report_path = os.path.join(cur_path, reportName)
#     if not os.path.exists(report_path): os.mkdir(report_path)
#     # report_abspath = os.path.join(report_path, now + 'result.html')
#     report_abspath = os.path.join(report_path, 'result.html')
#     with open(report_abspath, 'wb') as fp:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='用例执行情况')
#         runner.run(all_case)


# def get_report_file(report_path):
#     '''
#     作用: 获取最新的测试报告
#     :param report_path:
#     :return:
#     '''
#     lists = os.listdir(report_path)
#     lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
#     print('最新测试报告：' + lists[-1])
#     # 找到最新的测试报告文件
#     report_file = os.path.join(report_path, lists[-1])
#     return report_file


# def send_mail(subject, sender, psw, receiver, smtpserver, report_file, port):
#     """
#     作用：将最新的测试报告通过邮件进行发送
#     :param sender:发件人
#     :param psw:QQ邮箱授权码
#     :param receiver:收件人
#     :param smtpserver:QQ邮箱服务
#     :param report_file:
#     :param port:端口
#     :return:
#     """
#     with open(report_file, 'rb') as f:
#         mail_body = f.read()
#     # 定义邮件内容
#     msg = MIMEMultipart()
#     body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
#     msg['Subject'] = subject
#     msg['from'] = sender
#     msg['to'] = ','.join(receiver)
#     msg.attach(body)
#
#     # 添加附件
#     att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename= "report.html"'
#     msg.attach(att)
#     try:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#     except:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver, port)
#     # 用户名和密码
#     smtp.login(sender, psw)
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
#     log.info('测试报告邮件发送成功')
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
