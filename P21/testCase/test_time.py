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
timeBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[6]']
# 素材位置
timeEle = ['XPATH',
           '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout']

times = r'//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout'


class classtime(function, align, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def test_01_rotate(self):
        rotate = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]']
        super().rotate(timeBtn, timeEle, rotate)

    def test_02_lock(self):
        lock = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]']
        super().lock(timeBtn, timeEle, lock)

    def test_03_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]']
        super().center(timeBtn, timeEle, center)

    def test_04_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]']
        super().copy(timeBtn, times, copy)

    def test_05_choose(self):
        timeStr = self.base.get_current_date()
        location1 = ['XPATH', '(//android.widget.TextView[@text="' + str(timeStr) + '"])[1]']
        location2 = ['XPATH', '(//android.widget.TextView[@text="' + str(timeStr) + '"])[2]']
        super().choose(timeBtn, location1, location2, times)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


if __name__ == "__main__":
    unittest.main()
