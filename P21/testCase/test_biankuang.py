import os
import sys

# from unittestreport import TestRunner

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from P21.View.Function import function

import unittest

# 清除所有元素
clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']

# 添加边框按钮
biankuangBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[7]']
# 添加边框后，边框的位置
biankuangEle = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
# 添加边框后，边框的位置（无XPATH）
biankuang = r'//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'


class Biankuang(function, unittest.TestCase):

    # 运行测试用例（test_***）之前执行的方法，只执行一次
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    # 运行测试用例（test_***）之前执行的方法，每条测试用例运行前都执行一次
    def setUp(self):
        super().setUp()

    def test_01_rotate(self):
        # 旋转功能按钮
        rotateBtn = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]/android.widget.ImageView']
        super().rotate(biankuangBtn, biankuangEle, rotateBtn)

    def test_02_lock(self):
        lock = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]/android.widget.ImageView']
        super().lock(biankuangBtn, biankuangEle, lock)

    def test_03_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]/android.widget.ImageView']
        super().center(biankuangBtn, biankuangEle, center)

    def test_04_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]/android.widget.ImageView']
        super().copy(biankuangBtn, biankuang, copy)

    def test_05_choose(self):
        # 复制前第一个元素的位置
        location1 = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]']
        # 复制后第二个元素的位置
        location2 = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[2]']
        super().choose(biankuangBtn, location1, location2, biankuang)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    # 第一步：收集测试用例


# pwd = os.getcwd()
# print(pwd)
#
# # case_path = os.path.join(pwd,"unittestreport数据驱动之列表.py")
# suite = unittest.defaultTestLoader.discover(pwd)  # 自动获取测试用例类
# print("测试套件中的测试用例数量是：", suite.countTestCases())
# # 第二步：运行用例生成测试报告
# runner = TestRunner(suite,
#                     filename="自动化测试报告.html",
#                     report_dir=r"C:\Users\YZY\Desktop\nelko\P21\testCase",  # 放桌面
#                     title='nelko版本上线测试报告',
#                     tester='欢',
#                     desc="学习项目测试生成的报告",
#                     templates=2  # 报告的风格，有三种，取值是1,2,3
#                     )
# runner.run()
