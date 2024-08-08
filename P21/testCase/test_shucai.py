import os
import random
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from P21.View.Function import function
import unittest

clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']

# 添加素材按钮
shucaiBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[4]']
# 素材位置
shucaiEle = ['XPATH',
             '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']

shucai = r'//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'


class Sucai(function, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()


    def test_rotate(self):
        rotateBtn = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]']
        super().rotate(shucaiBtn, shucaiEle, rotateBtn)

    def test_lock(self):
        lock = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]']
        super().lock(shucaiBtn, shucaiEle, lock)

    def test_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]']
        super().center(shucaiBtn, shucaiEle, center)

    def test_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]']
        super().copy(shucaiBtn, shucai, copy)
    def test_choose(self):
        location1 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]']
        location2 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[2]']
        super().choose(shucaiBtn,location1,location2,shucai)
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()



