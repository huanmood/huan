import time
import requests
from Method.Base import Base
import unittest
import random

desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.nelko.printer",
    "appium:appActivity": "com.print.android.zhprint.home.SplashActivity",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": "true"

}
url = 'http://192.168.17.130:4723/wd/hub'

# 清除所有元素
clear = ['XPATH',
         '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
# 删除
delete = ['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_action_delete_btn"]']


class font(unittest.TestCase):
    base = None

    @classmethod
    def setUpClass(cls):
        cls.base = Base()  # 实例化Base对象
        cls.base.open(url, desired_caps)  # 启动Appium会话
        cls.base.first_open()  # 处理初次连接逻辑
        cls.base.connectP21()
        cls.base.openEditor()

    def test_01_fontType(self):
        jiekoList = []
        # 语言view
        j = 0
        local = ['XPATH',
                 '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="本地"]']
        english = ['XPATH',
                   '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="English"]']
        japan = ['XPATH',
                 '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="日本語"]']
        languageViem = 'com.nelko.printer:id/tv_tab_title'
        font = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_3"]']
        self.base.tap_at_Windows(0.5, 0.3)
        self.base.click(clear)
        self.base.click(
            ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[1]'])
        self.base.click(font)

        APPList = []
        language1 = self.base.matchingElementID(languageViem)
        if len(language1) > 5:
            self.base.drag_element(language1[-1], 396, 1305)
            language2 = self.base.matchingElement(languageViem)
            for i in language2:
                if i.text not in [elem['name'] for elem in APPList]:
                    APPList.append({'id': j, 'name': i.text})
                    j = j + 1
        else:
            pass

        for i in language1:
            if i.text not in [elem['name'] for elem in APPList]:
                APPList.append({'id': j, 'name': i.text})
                j = j + 1
        header = {
            'accessToken': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNWQ1YTQyZC1jM2IzLTQ0Y2YtYjg3OS0wNmZiYWE3NzM3MzYiLCJzdWIiOiIxMDAwMDkzNjMxIiwiaXNzIjoiYWRtaW4iLCJpYXQiOjE3MjE2MzYzNDksImV4cCI6NDI0NDUxNjM0OX0.zqT_wl_lGQnCF7pJ4VxOHslqWhjssweZ2aCoMftfocM',
            'language': 'zh-Hans'
        }
        response = requests.get('http://app.nelko.net/api/font/getCategoryList', headers=header)
        if response.status_code == 200:
            data = response.json()  # 解析JSON数据
            jiekoList = [{'id': 0, 'name': '本地'}]
            for i in data['data']:
                jiekoList.append(i)
        else:
            print('Failed to retrieve data', response.status_code)
        for i in jiekoList:
            for j in APPList:
                if i['name'] == j['name']:
                    print('字体分类', {j['name']}, '正确')
        time.sleep(3)

    def test_02_downLoadFont(self):
        add = 0
        font = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_3"]']
        languageViem = 'com.nelko.printer:id/tv_tab_title'
        self.base.tap_at_Windows(0.5, 0.3)
        self.base.click(clear)
        self.base.click(
            ['XPATH', '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_menu_icon_img"])[1]'])
        self.base.click(font)
        language1 = self.base.matchingElementID(languageViem)
        for i in range(1, len(language1)):
            language1[i].click()
            ra = random.randint(1, 6)
            # ele = ['XPATH','//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[' + str(
            #     ra) + ']']
            # self.base.click(ele)
            downloadCloud = ['XPATH',
                             '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/iv_download_cloud"])[' + str(
                                 ra) + ']']

            if self.base.is_element_present(downloadCloud[1]):
                self.base.click(downloadCloud)
            else:
                continue
            downloadProgress = '//android.view.View[@resource-id="com.nelko.printer:id/iv_download_progressbar"]'
            if self.base.waitElementLost(downloadProgress):
                add += 1
        print(add)
        language1[0].click()
        num = self.base.matchingElement('(//android.widget.FrameLayout[@resource-id="com.nelko.printer:id/fl_select"])')
        if len(num) == 6:
            print("字体测试通过")

    @classmethod
    def tearDownClass(cls):
        cls.base.quit()
# if __name__ == "__main__":
#     unittest.main()
# #
# def test_33_template(self):
#     view = ['XPATH',
#             '//androidx.viewpager.widget.ViewPager[@resource-id="com.nelko.printer:id/font_viewpager"]/android.widget.RelativeLayout']
#     header = {
#         'accessToken': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyOWM2NzVjOC0xZjhiLTQzZGYtOTRkMy02MjI1MjkyODE4YTYiLCJzdWIiOiIxMDAwMDkzNjMxIiwiaXNzIjoiYWRtaW4iLCJpYXQiOjE3MTIxMDY0NjAsImV4cCI6NDIzNDk4NjQ2MH0.PaA6cl69TXQ1Q4RZdNKYkyHzGkF6pYAf_9N0GU_l-u4',
#         'language': 'zh-Hans'
#     }
#     json = {
#         'typeId': 1
#     }
#     self.base.tap_at_coordinates(875, 635)
#     self.base.click(clear)
#     self.base.click(textBtn)
#     font = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_3"]']
#     self.base.click(font)
#     english = ['XPATH',
#                '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="English"]']
#     self.base.click(english)
#     response = requests.post('http://app.nelko.net/api/font/getFontList', headers=header, json=json)
#     if response.status_code == 200:
#         data = response.json()  # 解析JSON数据
#         len = (data['data']['total']) // 6
#         while (True):
#             if self.base.detect_element_change(view[0]):
#                 count = count + 1
#                 self.base.drag_element(698, 1848, 702, 1545)
#
#         print(count)
