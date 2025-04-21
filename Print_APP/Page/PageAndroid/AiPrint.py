from selenium.webdriver.common.by import By

from Page import PageAndroid
from Page.BasePage import Action

DEVICE_TEMPLATE_MAPPING = {
    # 模板位置位于首页第1个位置的设备
    "P21": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[3]'),
        "position": 1
    },
    "P31S": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "PM220": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "PM220S": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "PM360": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    "P22": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[1]'),
        "position": 1
    },
    # 模板位置位于首页第2个位置的设备
    "PL70e-BT": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[2]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "replacePrintPaper",
                "action": "know"
            },
            {
                "element": "moreFeatures",
                "action": "sure"
            }
        ]
    },
    "PL80E": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[2]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "moreFeatures",
                "action": "sure"
            },
            {
                "element": "replacePrintPaper",
                "action": "know"
            }
        ]
    },
    "PM230": {
        "template_locator": (
            By.XPATH, '(//android.widget.ImageView[@resource-id="com.nelko.printer:id/view_menu_icon"])[2]'),
        "position": 2,
        "special_handlers": [
            {
                "element": "moreFeatures",
                "action": "sure"
            }
        ]
    }
}


class AiPrint(Action):

    def get_aiprint(self, devIndex, devName):
        self._select_device(devIndex, devName)
        self._handle_device_template(devName)

    def _select_device(self, devIndex, devName):
        """选择指定设备"""
        self.click_button(PageAndroid.deviceName_loc)
        device_locator = (By.XPATH,
                          f'(//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/rela"])[{devIndex}]')
        self.click_button(device_locator)
        self.click_button(PageAndroid.deviceConfirm)

    def _handle_device_template(self, devName):
        """处理设备特定模板"""
        device_config = DEVICE_TEMPLATE_MAPPING.get(devName)
        if not device_config:
            raise ValueError(f"未知设备: {devName}")

        # 处理特殊操作（如弹窗等）
        if "special_handlers" in device_config:
            for handler in device_config["special_handlers"]:
                element = getattr(self.buttonElement, handler["element"])
                if self.exists_element(element):
                    getattr(self, f"click_button")(getattr(self.buttonElement, handler["action"]))

