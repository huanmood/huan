import time
import pytest
from common.DB_utils import DB
import pytest
import requests
from appium import webdriver
from Page.BasePage import Action
from TestCase.share_devices import process_context
from appium.options.common import AppiumOptions

options = AppiumOptions()


@pytest.fixture(scope="function")
def driver():
    """获取启动APP时的 driver"""
    return process_context.driver


# -----------------------------自动截图--------------------------------------------
# @pytest.fixture
# def take_app_screenshot(driver):
#     """APP 截图工具"""
#
#     def _take_screenshot(name):
#         filename = f"screenshots/TestFailed/{name}.png"
#         driver.save_screenshot(filename)
#         print(f"📸 APP截图保存: {filename}")
#         return filename
#
#     return _take_screenshot
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """APP测试报告钩子 - 失败时自动截图"""
#     outcome = yield
#     report = outcome.get_result()
#
#     # 只在测试执行阶段失败时截图
#     if report.when == "call" and report.failed:
#         print(f"❌ APP测试失败，自动截图: {item.name}")
#
#         # 获取 APP driver
#         driver = item.funcargs.get('driver')
#         if driver:
#             # 创建截图目录
#             # APP 截图
#             filename = f"screenshots/TestFailed/app_failure_{item.name}.png"
#             driver.save_screenshot(filename)
#             print(f"📸 APP自动截图: {filename}")
#
#             # 还可以获取更多 APP 信息
#             try:
#                 current_activity = driver.current_activity
#                 page_source = driver.page_source[:500]  # 前500字符
#                 print(f"📱 当前Activity: {current_activity}")
#                 print(f"📄 页面内容片段: {page_source}...")
#             except Exception as e:
#                 print(f"⚠️ 获取APP信息失败: {e}")


# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def action(driver):
    """传入一个driver 返回 Action 对象"""
    return Action(driver)


'''ios单元测试'''
@pytest.fixture(scope="session")
def ios_Testing():
    options.load_capabilities({
        "platformName": "iOS",
        "platformVersion": "15.4.1",
        "deviceName": "iPhone 11",
        "udid": "00008030-0001314236E9802E",
        "bundleId": "com.nelko.printer",
        "automationName": "XCUITest",
        "noReset": True,
        "useXctestrunFile": False,
        "skipLogCapture": True,
        "wdaLocalPort": 8200,
        'usePrebuiltWDA': True,  # 使用已安装的 WDA
        'useNewWDA': False,  # 不要每次都卸载重装 WDA
        'startWDA': False,  # Windows 无法启动 WDA，所以设为 False
        'webDriverAgentUrl': 'http://127.0.0.1:8200',
    })

    print("初始化 driver ...")
    try:
        driver = webdriver.Remote(
            command_executor=f"http://127.0.0.1:4723",
            options=options
        )
        time.sleep(4)
    except Exception as e:
        import traceback
        print("❌ driver 初始化失败:", repr(e))
        traceback.print_exc()
        raise
    return Action(driver)


'''android单元测试'''


# @pytest.fixture(scope="session")
# def android_Testing():
#     desired_caps = {
#         "platformName": "Android",
#         "platformVersion": "12",
#         "appPackage": "com.nelko.printer",
#         "appActivity": "com.ezink.app.nelko.ui.SplashActivity",
#         "deviceName": "6ebb6b77",
#         "automationName": "UiAutomator2"
#     }
#     driver = webdriver.Remote(f"http://127.0.0.1:4726", desired_caps)
#     driver.implicitly_wait(15)
#     action = Action(driver)
#     return android_Connect(action)



import pymysql
import redis
import pytest




@pytest.fixture(scope="session", autouse=True)
def db():
    print("🔧 初始化数据库与 Redis ...")
    d = DB()

    yield d

    print("🔧 关闭数据库连接 ...")
    d.close()

@pytest.fixture(scope="session")
def setup_teardown(action):
    """每个测试用例的前置和后置操作"""
    yield
    action.back_button()

@pytest.fixture(scope="class")
def class_setup_teardown():
    """测试类的前置和后置操作"""
    print("类setup")
    yield
    print("类teardown")


@pytest.fixture(scope="session")
def get_driver_list():
    """获取机型列表"""
    response = requests.get('http://app.nelko.net/api/templateVip/getDeviceList')
    # 假设response是你的HTTP响应数据
    data = response.json()["data"]
    return {device["deviceName"]: device for device in data if device.get("deviceName")}
