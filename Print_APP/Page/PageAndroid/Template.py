import json
import time
import requests
from selenium.webdriver.common.by import By
from Page import PageAndroid
from Page.BasePage import Action
from common.DB_utils import get_redis_conn

# 设备配置映射表（更易维护和扩展）
# DEVICE_TEMPLATE_MAPPING = {  # 模板位置位于首页第1个位置的设备
#     "P21": {"template_locator": (By.XPATH,
#                                  '//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),
#             "position": 1},
#     "P31S": {"template_locator": (By.XPATH,
#                                   '//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),
#              "position": 1},
#     "PM220": {"template_locator": (By.XPATH,
#                                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),
#               "position": 1},
#     "PM220S": {"template_locator": (By.XPATH,
#                                     '//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),
#                "position": 1},
#     "PM230": {"template_locator": (By.XPATH,
#                                    '//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),
#               "position": 2, "special_handlers": [{"element": "moreFeatures", "action": "sure"}]}}
# 模板位置位于首页第2个位置的设备"PL70e-BT": {"template_locator": (By.XPATH,'//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),"position": 2,"special_handlers": [{"element": "moreFeatures","action": "sure"},{"element": "replacePrintPaper","action": "know"}]},"PM360": {"template_locator": (By.XPATH,'//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),"position": 1},"P22": {"template_locator": (By.XPATH,'//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),"position": 1},"PL80E": {"template_locator": (By.XPATH,'//android.widget.TextView[@resource-id="com.nelko.printer:id/item_home_menu_name_tv" and @text="系统模板"]'),"position": 2,# "special_handlers": [#     {#         "element": "moreFeatures",#         "action": "sure"#     },#     {#         "element": "replacePrintPaper",#         "action": "know"#     }# ]}}


class Template(Action):

    def get_getCategory(self, devName):
        """获取并比较模板类型和尺寸"""
        try:
            # 1. 选择设备
            # self._select_device(devName)
            #
            # # 2. 处理设备特定模板
            # self._handle_device_template(devName)

            # 3. 获取并比较模板类型
            self._compare_template_types(devName)

            # 4. 获取并比较模板尺寸
            self._compare_template_sizes(devName)

            # 5. 获取比较模板尺寸并输入模板名称

            self.back_button()
            # 6. 搜索模板名称后比较是否正确

            self._get_app_templateName()

            self.back_button()

        except Exception as e:
            self.log_error(f"测试失败: {str(e)}")
            raise

    def _get_app_templateName(self):

        """获取APP模板名称并验证搜索和尺寸筛选功能"""
        # 常量定义（集中管理定位器）
        TEMPLATE_NAME_LOCATOR = (
            By.XPATH, '(//android.widget.TextView[@resource-id="com.nelko.printer:id/btv_name"])[1]')
        SIEZ_NAME_LOCATOR = (
            By.XPATH, '(//android.widget.TextView[@resource-id="com.nelko.printer:id/btv_size"])[1]')
        SIZE_CHECKBOX_LOCATOR = (By.XPATH, '//android.widget.CheckBox[contains(@text, "x")]')

        # --- 第一部分：模板名称验证 ---
        # 获取初始模板名称
        template_name = self.find_element(TEMPLATE_NAME_LOCATOR).text
        self.log_debug(f"获取到模板名称: {template_name}")

        # 执行搜索操作（双击搜索框+输入内容）
        for _ in range(2):
            self.click_button(self.buttonElement.search)
            time.sleep(1)
        self.send_keys(self.buttonElement.search, template_name)
        self.search()

        # 验证搜索结果(模板名称)
        searched_name = self.find_element(TEMPLATE_NAME_LOCATOR).text
        comparison = "一致" if template_name == searched_name else "不一致"
        self.log_debug(f"名称比对: 原始[{template_name}] vs 搜索[{searched_name}] {comparison}")

        # 验证搜索结果(模板尺寸)
        searched_size = self.find_element(SIEZ_NAME_LOCATOR).text
        cleaned_size = searched_size.replace('(', '').replace(')', '').replace('mm', '').replace(' ', '')
        # --- 第二部分：尺寸筛选验证 ---
        # 打开尺寸选择弹窗
        self.click_button(self.buttonElement.templateSize)
        # 选择特定尺寸
        self.click_button((By.XPATH, f'//android.widget.CheckBox[@text="{cleaned_size}"]'))
        self.click_button(self.buttonElement.templateSize_sure)
        # 验证显示的尺寸
        a, b = cleaned_size.split('x')
        if cleaned_size in (f"{a}x{b}", f"{b}x{a}"):
            self.log_debug(f"尺寸验证通过: 选择[{cleaned_size}] ↔ 显示[{cleaned_size}]")
        else:
            self.log_error(f"尺寸验证失败: 选择[{cleaned_size}] ↔ 显示[{cleaned_size}]")

        # --- 公共操作：返回上级 ---
        for _ in range(2):
            self.back_button()

    def _compare_template_types(self, devName):
        """比较模板类型"""
        # 获取API模板数据
        self.redis = get_redis_conn()
        api_templates = self._get_api_templates(devName)

        # 获取APP界面模板数据
        app_templates = self._get_app_templates()

        # 比较结果
        api_set = set(api_templates)
        app_set = set(app_templates)

        diff_in_api = api_set - app_set
        diff_in_app = app_set - api_set

        if not diff_in_api and not diff_in_app:
            self.log_debug(f"{devName}所有模板类型与接口返回一致")
        else:
            if diff_in_api:
                self.log_error(f"{devName}模板类型在接口但不在APP中: {', '.join(diff_in_api)}")
            if diff_in_app:
                self.log_error(f"{devName}模板类型在APP但不在接口中: {', '.join(diff_in_app)}")

        self.log(f"{devName}完整API模板: {api_templates}")
        self.log(f"{devName}完整APP模板: {app_templates}")

    def _select_device(self, devName):
        """选择指定设备"""
        self.redis = get_redis_conn()
        self.click_button(PageAndroid.deviceName_loc)
        device_locator = (By.XPATH,
                          f'//android.widget.TextView[@resource-id="com.nelko.printer:id/text_device_name" and @text="{devName}"]')
        self.click_button(device_locator)
        self.click_button(PageAndroid.deviceConfirm)

    # def _handle_device_template(self, devName):
    #     F = '•'
    #     i = 1
    #     """处理设备特定模板"""
    #     device_config = DEVICE_TEMPLATE_MAPPING.get(devName)
    #     if not device_config:
    #         raise ValueError(f"未知设备: {devName}")
    #     # 处理特殊操作（如弹窗等）
    #     if "special_handlers" in device_config:
    #         print(f"正在查找是否有引导提示中", end='')
    #         for handler in device_config["special_handlers"]:
    #             print(f"{F * i}", end='')
    #             element = getattr(self.buttonElement, handler["element"])
    #             if self.exists_element(element):
    #                 print('\n')
    #                 getattr(self, f"click_button")(getattr(self.buttonElement, handler["action"]))
    #             else:
    #                 i += 5
    #
    #     # 点击模板
    #     self.click_button(device_config["template_locator"])

    def _get_app_templates(self):
        """从APP界面获取模板数据"""
        self.click_button(self.buttonElement.System_Templates)
        parent_locator = (By.XPATH,
                          '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/act_ai_category_rcv"]')
        parent = self.find_element(parent_locator)
        children = parent.find_elements(By.XPATH,
                                        './/android.widget.LinearLayout[@resource-id="com.nelko.printer:id/group"]/*')
        return [child.text for child in children[1:] if child.text]

    def _compare_templates(self, devName, api_templates, app_templates):
        """比较API和APP的模板数据"""
        api_set = set(api_templates)
        app_set = set(app_templates)

        diff_in_api = api_set - app_set
        diff_in_app = app_set - api_set

        if not diff_in_api and not diff_in_app:
            print(f"{devName}所有模板类型与接口返回一致")
        else:
            if diff_in_api:
                self.log_debug(f"{devName}模板类型在接口但不在APP中: {', '.join(diff_in_api)}")
            if diff_in_app:
                self.log_debug(f"{devName}模板类型在APP但不在接口中: {', '.join(diff_in_app)}")

            self.log(f"{devName}完整API模板: {api_templates}")
            self.log(f"{devName}完整APP模板: {app_templates}")

    def _get_api_templates(self, devName):
        """从API获取模板数据"""
        redis_key = f"Template_{devName}"
        Template = []

        if not self.redis.exists(redis_key):
            url = f'https://app.nelko.net/api/template/getCategory/{devName}'
            headers = {"language": "zh-Hans"}
            try:
                response = requests.get(url=url, headers=headers, timeout=10)
                response.raise_for_status()
                data = response.json().get('data', [])
                for i in data:
                    Template.append(i['name'])
                if Template:
                    self.redis.hset(redis_key, "name", json.dumps(Template, ensure_ascii=False))
                    self.redis.expire(redis_key, 300)
            except requests.exceptions.RequestException as e:
                self.log_error(f"API请求失败: {str(e)}")
        data = self.redis.hget(redis_key, "name")
        data = data.decode()
        return json.loads(data)

    def _compare_template_sizes(self, devName):
        """比较模板尺寸"""
        # 获取APP展示的尺寸
        redis_key = f"Template_{devName}"
        self.click_button(self.buttonElement.templateSize)
        size_elements = self.find_elements(
            (By.XPATH, '//android.widget.CheckBox[contains(@text, "x")]')
        )
        app_sizes = [elem.text for elem in size_elements]

        # 获取接口返回的尺寸
        if not self.redis.hget("redis_key", "size"):
            response = requests.get(
                url=f"https://app.nelko.net/api/template/getSizeCategory/{devName}",
                timeout=10
            )
            response.raise_for_status()
            api_sizes = [item['idString'] for item in response.json().get('data', [])]
            self.redis.hset(redis_key, "size", json.dumps(api_sizes))
            self.redis.expire(redis_key, 300)
        data = self.redis.hget(redis_key, "size")
        data = json.loads(data.decode())
        api_sizes = data

        # 比较尺寸
        api_size_set = set(api_sizes)
        app_size_set = set(app_sizes)

        if api_size_set == app_size_set:
            self.log_debug(f"{devName}所有模板尺寸与接口返回一致")
        else:
            # 找出不一致的尺寸
            diff_in_api = api_size_set - app_size_set
            diff_in_app = app_size_set - api_size_set

            if diff_in_api:
                self.log_error(f"{devName}接口返回但APP未展示的尺寸: {', '.join(diff_in_api)}")
            if diff_in_app:
                self.log_error(f"{devName}APP展示但接口未返回的尺寸: {', '.join(diff_in_app)}")

        self.log(f"{devName}接口返回尺寸: {api_sizes}")
        self.log(f"{devName}APP展示尺寸: {app_sizes}")
