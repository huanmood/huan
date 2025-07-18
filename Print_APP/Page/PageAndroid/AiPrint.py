import time

import requests
from selenium.webdriver.common.by import By
from Page import PageAndroid
from Page.BasePage import Action
from common.GlobalValue import GlobalVar
from Page.PageAndroid.LoginPage import Login
from common.DB_utils import get_redis_conn
from Page import PageAndroid
from Page.PageAndroid.LoginPage import login_api

DEVICE_TEMPLATE_MAPPING = {
    # 模板位置位于首页第1个位置的设备
    "P21": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI图库"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 1
    },
    "P31S": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 1
    },
    "PM220": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 1
    },
    "PM220S": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 1
    },
    "PM230": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "moreFeatures",
                "action": "sure"
            }
        ]
    },
    "PL70e-BT": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "replacePrintPaper",
                "action": "know"
            }
            # {
            #     "element": "moreFeatures",
            #     "action": "sure"
            # }
        ]
    },
    "PM360": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 1
    },
    "P22": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),

        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 1
    },
    "PL80E": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "AiPrint_Picture": (
            By.XPATH,
            '//android.widget.TextView[@text="AI图库"]'),
        "position": 2,
        # "special_handlers": [
        #     {
        #         "element": "moreFeatures",
        #         "action": "sure"
        #     },
        #     {
        #         "element": "replacePrintPaper",
        #         "action": "know"
        #     }
        # ]
    }
}
# AI图库第一张图
AiPrint_01 = (By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/item_aigallery_image"])[1]')
# 点击爱心添加到收藏
add_Favourite = (By.ID, 'com.nelko.printer:id/act_ai_detail_cv_tv')
# 收藏
collect = (By.XPATH, '//android.widget.TextView[@text="收藏"]')
# 全部类型
all_type = (By.XPATH, '//android.widget.TextView[@text="全部"]')
global_var = GlobalVar()
login = Login()
favourite_Num = 0


class AiPrint(Action):
    def print(self):
        pass

    def get_aiprint(self, devName):
        self.redis = get_redis_conn()
        self.log(f"开始处理设备: {devName}")
        self._select_device(devName)
        self._handle_device_template(devName)
        self._compare_templates()
        self._add_Favourite()
        self._remove_Favourite()
        self.back_button()
        self.back_button()
        self.log(f"设备 {devName} 处理完成")

    def check_login(element):
        def my_decorator(func):
            def wrapper(self, *args, **kwargs):  # 显式传递 self
                self.click_button(element)
                if not self.redis.get("token"):
                    time.sleep(3)
                    if self.exists_element(PageAndroid.email_loc):
                        login.app_login('1508908114@qq.com', '111111')
                        token = "success"
                        self.redis.setnx("token", token)
                    else:
                        return func(self, *args, **kwargs)  # 注意传递 self
                return func(self, *args, **kwargs)
            return wrapper
        return my_decorator

    # 选择机器
    def _select_device(self, devName):
        """选择指定设备"""
        self.log(f"正在选择设备: {devName}")
        self.click_button(PageAndroid.deviceName_loc)
        device_locator = (By.XPATH,
                          f'//android.widget.TextView[@resource-id="com.nelko.printer:id/text_device_name" and @text="{devName}"]')
        self.click_button(device_locator)
        self.click_button(PageAndroid.deviceConfirm)
        self.log(f"设备 {devName} 选择完成")

    # 处理提示
    def _handle_device_template(self, devName):
        """处理设备特定模板"""
        F = '•'
        i = 1
        """处理设备特定模板"""
        device_config = DEVICE_TEMPLATE_MAPPING.get(devName)
        if not device_config:
            raise ValueError(f"未知设备: {devName}")
        # 处理特殊操作（如弹窗等）
        if "special_handlers" in device_config:
            print(f"正在查找是否有引导提示中", end='')
            for handler in device_config["special_handlers"]:
                print(f"{F * i}", end='')
                element = getattr(self.buttonElement, handler["element"])
                if self.exists_element(element):
                    print('\n')
                    getattr(self, f"click_button")(getattr(self.buttonElement, handler["action"]))
                else:
                    i += 5
        if devName == 'PM230':
            self.click_button(self.buttonElement.moreButton)
            self.click_button(device_config['AiPrint_locator'])
            # self.click_button(device_config['AiPrint_Picture'])
        else:
            self.click_button(device_config['AiPrint_locator'])
            # self.click_button(device_config['AiPrint_Picture'])

    # 获取AI图库类型 ：APP
    def _get_app_Aiprints(self):
        """从APP界面获取模板数据"""
        parent_locator = (By.XPATH,
                          '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/act_ai_category_rcv"]')
        parent = self.find_element(parent_locator)
        children = parent.find_elements(By.XPATH,
                                        './/android.widget.LinearLayout[@resource-id="com.nelko.printer:id/text_category"]/*')
        return [child.text for child in children[5:] if child.text]

    # 获取AI图库类型 ：API
    def _get_api_Aiprints(self):
        headers = {
            "language": "zh-Hans"
        }
        response = requests.get('https://app.nelko.net/api/picture/getPictureTypeList', headers=headers)
        response.raise_for_status()

        return [i['name'] for i in response.json().get('data', [])]

    # 比较 AI图库类型
    def _compare_templates(self):
        """比较API和APP的模板数据"""
        get_app_Aiprints = self._get_app_Aiprints()
        get_api_Aiprints = self._get_api_Aiprints()

        api_set = set(get_app_Aiprints)
        app_set = set(get_api_Aiprints)

        diff_in_api = api_set - app_set
        diff_in_app = app_set - api_set

        if not diff_in_api and not diff_in_app:
            print(f"所有模板类型与接口返回一致")
        else:
            if diff_in_api:
                self.log_debug(f"AI图库类型在接口但不在APP中: {', '.join(diff_in_api)}")
            if diff_in_app:
                self.log_debug(f"AI图库类型在APP但不在接口中: {', '.join(diff_in_app)}")

        self.log(f"完整API模板: {get_api_Aiprints}")
        self.log(f"完整APP模板: {get_app_Aiprints}")
        self.click_button(all_type)
        self.click_button(AiPrint_01)

    #  增加收藏数量
    @check_login(add_Favourite)
    def _add_Favourite(self):
        global favourite_Num
        self.click_button(add_Favourite)
        favourite_Num += 1
        self.back_button()

    # def _remove_Favourite(self):
    #     global favourite_Num
    #     self.click_button(all_type)
    #     self.click_button(AiPrint_01)
    #     self.click_button(add_Favourite)
    #     favourite_Num -= 1
    #     self.back_button()
