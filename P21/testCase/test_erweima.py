import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from P21.View.Function import function
import unittest
# 添加文本按钮
erweimaBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[3]']
# 一维码位置
erweimaEle = ['XPATH',
              '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']

erweima = r'//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'


class Erweima(function, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def test_rotate(self):
        rotate = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]']
        super().rotate(erweimaBtn, erweimaEle, rotate)

    def test_lock(self):
        lock = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]']
        super().lock(erweimaBtn, erweimaEle, lock)

    def test_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]']
        super().center(erweimaBtn, erweimaEle, center)

    def test_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]']
        super().copy(erweimaBtn, erweima, copy)
    def test_choose(self):
        location1 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]']
        location2 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[2]']
        super().choose(erweimaBtn,location1,location2,erweima)
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


