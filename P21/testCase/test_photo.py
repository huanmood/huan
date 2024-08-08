import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from P21.View.Function import function
from P21.View.Align import align
from P21.View.Font import font
import unittest

clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']

# 添加素材按钮
phoneBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[5]']
# 素材位置
phoneEle = ['XPATH',
           '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']

phone = r'//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'


class Photo(function, align, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def test_01_rotate(self):
        rotate = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]']
        super().rotate(phoneBtn, phoneEle, rotate)

    def test_02_lock(self):
        lock = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]']
        super().lock(phoneBtn, phoneEle, lock)

    def test_03_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]']
        super().center(phoneBtn, phoneEle, center)

    def test_04_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]']
        super().copy(phoneBtn, phone, copy)

    def test_05_choose(self):

        location1 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]']
        location2 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[2]']
        super().choose(phoneBtn, location1, location2, phone)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

