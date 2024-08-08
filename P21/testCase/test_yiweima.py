import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from P21.View.Function import function
from P21.View.Content import content
import unittest
# 添加文本按钮
yiweimaBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[2]']
# 一维码位置
yiweimaEle = ['XPATH',
              '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout']

yiweima = r'//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'
class Yiweima(function ,unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def test_rotate(self):
        rotateBtn = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]']
        super().rotate(yiweimaBtn, yiweimaEle, rotateBtn)

    def test_lock(self):
        lock = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]']
        super().lock(yiweimaBtn, yiweimaEle, lock)

    def test_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]']
        super().center(yiweimaBtn, yiweimaEle, center)

    def test_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]']
        super().copy(yiweimaBtn, yiweima, copy)
    def test_choose(self):
        location1 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]']
        location2 = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[2]']
        super().choose(yiweimaBtn,location1,location2,yiweima)
    # def test_content(self):
    #     super().content(yiweimaBtn)
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


# if __name__ == "__main__":
#     unittest.main()
