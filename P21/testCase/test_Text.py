import os
import sys



sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from P21.View.Function import function
from P21.View.Font import font
import unittest

count = 0

# 添加文本按钮
textBtn = ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[1]']
# 默认文本位置
textEle = ['XPATH', '//android.widget.TextView[@text="双击文本框编辑"]']
# xpath文本位置
text = r'//android.widget.TextView[@text="双击文本框编辑"]'
# 清空按钮
clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
# 删除
delete = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_delete_btn"]']


class Text(function, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def test_rotate(self):
        rotateBtn = ['XPATH',
                     '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_rotate_btn"]']
        super().rotate(textBtn, textEle, rotateBtn)

    def test_lock(self):
        lock = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_lock_btn"]']
        super().lock(textBtn, textEle, lock)

    def test_center(self):
        center = ['XPATH',
                  '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_center_btn"]']
        super().center(textBtn, textEle, center)

    def test_copy(self):
        copy = ['XPATH',
                '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_copy_btn"]']
        super().copy(textBtn, text, copy)

    def test_choose(self):
        location1 = ['XPATH', '(//android.widget.TextView[@text="双击文本框编辑"])[1]']
        location2 = ['XPATH', '(//android.widget.TextView[@text="双击文本框编辑"])[2]']
        super().choose(textBtn, location1, location2, text)

    # def test_fontBold(self):
    #     bold = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_bold_layout"]']
    #     super().TextCompare(textBtn,textEle,bold)
    #
    # def test_italic(self):
    #     italic = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_italic_layout"]']
    #     super().TextCompare(textBtn,textEle,italic)
    #
    # def test_underline(self):
    #     underline = ['XPATH',
    #                  '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_underline_layout"]']
    #     super().TextCompare(textBtn,textEle,underline)
    #
    # #
    # def test_deleteline(self):
    #     deleteline = ['XPATH',
    #                   '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_underline_layout"]']
    #
    #     super().TextCompare(textBtn, textEle, deleteline)
    #
    # def test_leftJustified(self):
    #     leftJustified = ['XPATH',
    #                      '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_align_left_layout"]']
    #     super().TextCompare(textBtn, textEle, leftJustified)
    #
    # #
    # def test_centerJustified(self):
    #
    #     centerJustified = ['XPATH',
    #                      '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_align_center_layout"]']
    #     super().TextCompare(textBtn, textEle, centerJustified)
    #
    # def test_rightJustified(self):
    #     rightJustified = ['XPATH',
    #                       '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/ts_align_right_layout"]']
    #     super().TextCompare(textBtn, textEle, rightJustified)

    # def test_styleSubtract(self):
    #     add = ['XPATH',
    #            '//android.widget.ImageView[@resource-id="com.nelko.printer:id/seekbar_add_btn"]']
    #     sub = ['XPATH', '//android.widget.ImageView[@resource-id="com.nelko.printer:id/seekbar_sub_btn"]']
    #     self.base.tap_at_Windows(0.5, 0.3)
    #     self.base.click(clear)
    #     self.base.click(textBtn)
    #     element = self.base.findElement(textEle)
    #     screenshot = self.base.capture_element_screenshot(element)
    #     self.base.click(add)
    #     screenshot1 = self.base.capture_element_screenshot(element)
    #     print("Images are different" if not self.base.compare_images(screenshot, screenshot1) else "Images are identical")
    #     self.base.click(sub)
    #     element = self.base.findElement(textEle)
    #     screenshot2 = self.base.capture_element_screenshot(element)
    #     print("Images are different" if not self.base.compare_images(screenshot1, screenshot2) else "Images are identical")
    #
    #     # result = self.base.compare_images(screenshot1, screenshot2)
    #     # print("Images are identical" if result else "Images are different")
    #
    #     self.base.click(sub)
    #     element = self.base.findElement(textEle)
    #     screenshot3 = self.base.capture_element_screenshot(element)
    #     # result = self.base.compare_images(screenshot2, screenshot3)
    #     # print("Images are identical" if result else "缩小Images are different")

    # def test_topAlign(self):
    #     # 对齐按钮
    #     alignBtn = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_1"]']
    #     # 上对齐按钮
    #     topAlignBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/alignTop"]']
    #     super().AlignCompare(textBtn,alignBtn,textEle,topAlignBtn)
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


class TextFont(font, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    # def setUp(self):
    #     super().setUp()

    def ass(self):
        super().test_01_fontType()

    def bss(self):
        super().test_02_downLoadFont()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    # def test_18_wordSpaceAdd(self):
    #     try:
    #         self.base.click(deleteBtn)
    #         self.base.click(textBtn)
    #         space = ['XPATH',
    #                  '//android.widget.TextView[@resource-id="com.nelko.printer:id/btv_tab_title" and @text="间距"]']
    #         self.base.click(space)
    #         count = 0
    #         add = ['XPATH',
    #                '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/seekbar_add_btn"])[2]']  # 定位速度慢
    #         seekbar = ['XPATH', '(//android.view.View[@resource-id="com.nelko.printer:id/seekbar_speed"])[2]']
    #         element1 = self.base.findElement(seekbar)
    #         element2 = self.base.findElement(textEle)
    #         while True:
    #             # 检测元素是否发生变化
    #             if self.base.detect_element_change(element2):
    #                 print("间距已增加")
    #                 break
    #             else:
    #                 print("间距无增加")
    #                 for i in range(0, 50):
    #                     self.base.tap_at_coordinates(995, 1805)
    #                 count = count + 1
    #                 if count == 2:
    #                     break
    #             # 等待一段时间再继续检测
    #             time.sleep(1)
    #
    #     except Exception as e:
    #         print("字号间距放大功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_19_wordSpaceSubtract(self):
    #     try:
    #         count = 0
    #         subtract = ['XPATH',
    #                     '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/seekbar_sub_btn"])[1]']  # 定位速度慢
    #         seekbar = ['XPATH', '(//android.view.View[@resource-id="com.nelko.printer:id/seekbar_speed"])[1]']
    #         element1 = self.base.findElement(seekbar)
    #         element2 = self.base.findElement(textEle)
    #         while True:
    #             # 检测元素是否发生变化
    #             if self.base.detect_element_change(element2):
    #                 print("行距已减少")
    #                 break
    #             else:
    #                 print("行距无减少")
    #                 for i in range(0, 10):
    #                     self.base.tap_at_coordinates(205, 1837)
    #                 count = count + 1
    #                 if count == 2:
    #                     break
    #             # 等待一段时间再继续检测
    #             time.sleep(5)
    #     except Exception as e:
    #         print("字号间距减少功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_20_lineSpaceSubtract(self):
    #     try:
    #         count = 0
    #         seekbar = ['XPATH', '(//android.view.View[@resource-id="com.nelko.printer:id/seekbar_speed"])[1]']
    #         element1 = self.base.findElement(seekbar)
    #         element2 = self.base.findElement(textEle)
    #
    #         while True:
    #             # 检测元素是否发生变化
    #             if self.base.detect_element_change(element1) and self.base.detect_element_change(element2):
    #                 print("行距已减少")
    #                 break
    #             else:
    #                 print("行距无减少")
    #                 for i in range(0, 10):
    #                     self.base.tap_at_coordinates(210, 1682)
    #                 count = count + 1
    #                 if count == 2:
    #                     break
    #             # 等待一段时间再继续检测
    #             time.sleep(5)
    #     except Exception as e:
    #         print("字号行距减少功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
    #
    # def test_21_lineSpaceAdd(self):
    #     try:
    #         count = 0
    #         seekbar = ['XPATH', '(//android.view.View[@resource-id="com.nelko.printer:id/seekbar_speed"])[2]']
    #         element1 = self.base.findElement(seekbar)
    #         element2 = self.base.findElement(textEle)
    #
    #         while True:
    #             # 检测元素是否发生变化
    #             if self.base.detect_element_change(element1) and self.base.detect_element_change(element2):
    #                 print("行距已增加")
    #                 break
    #             else:
    #                 print("行距无增加")
    #                 for i in range(0, 60):
    #                     self.base.tap_at_coordinates(997, 1687)
    #                 count = count + 1
    #                 if count == 2:
    #                     break
    #             # 等待一段时间再继续检测
    #             time.sleep(5)
    #     except Exception as e:
    #         print("字号行距增加功能测试失败: ", e)
    #         self.base.open(url, desired_caps)  # 启动Appium会话
    #         self.base.test_01_connectP21()
    #         self.base.test_02_openEditor()
    #         return
