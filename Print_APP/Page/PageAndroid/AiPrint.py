from selenium.webdriver.common.by import By
from Page import PageAndroid
from Page.BasePage import Action

DEVICE_TEMPLATE_MAPPING = {
    # 模板位置位于首页第1个位置的设备
    "P21": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "position": 1
    },
    "P31S": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "position": 1
    },
    "PM220": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "position": 1
    },
    "PM220S": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "position": 1
    },
    "PM230": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
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
        "position": 1
    },
    "P22": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
        "position": 1
    },
    "PL80E": {
        "AiPrint_locator": (
            By.XPATH,
            '//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="AI打印"]'),
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
# testpage.py


class AiPrint(Action):
    def get_aiprint(self, devName):
        self.log(f"开始处理设备: {devName}")
        self._select_device(devName)
        self._handle_device_template(devName)
        self.back_button()
        self.log(f"设备 {devName} 处理完成")

    def _select_device(self, devName):
        """选择指定设备"""
        self.log(f"正在选择设备: {devName}")
        self.click_button(PageAndroid.deviceName_loc)
        device_locator = (By.XPATH,
                        f'//android.widget.TextView[@resource-id="com.nelko.printer:id/text_device_name" and @text="{devName}"]')
        self.click_button(device_locator)
        self.click_button(PageAndroid.deviceConfirm)
        self.log(f"设备 {devName} 选择完成")


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
        else:
            self.click_button(device_config['AiPrint_locator'])
# class AiPrint(Action):
#
#     def get_aiprint(self, devName):
#         # 执行
#         self._select_device(devName)
#         self._handle_device_template(devName)
#
#         self.back_button()
#
#     def _select_device(self, devName):
#         """选择指定设备"""
#         self.click_button(PageAndroid.deviceName_loc)
#         device_locator = (By.XPATH,
#                           f'//android.widget.TextView[@resource-id="com.nelko.printer:id/text_device_name" and @text="{devName}"]')
#         self.click_button(device_locator)
#         self.click_button(PageAndroid.deviceConfirm)
