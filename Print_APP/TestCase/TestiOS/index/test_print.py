import time

import pytest

from Page.PageiOS.iOS_Rfid_tab import rfid_tab
from Page.PageiOS.iOS_Connect import ios_Connect

devices = [

    ("P21", "43:2C:42:48:63:5F"),
    ("PM220", "31:9D:16:24:B1:78"),
    ("P31S", "77:3F:34:E4:6D:51")
]


@pytest.fixture(scope="session")
def print_System_Testing(action):
    """返回 Action 对象"""
    return rfid_tab(action)


@pytest.fixture(scope="session")
def print_ios_Connect(action):
    """获取ios_Connect类方法"""
    return ios_Connect(action)


@pytest.mark.parametrize("deviceName,deviceMac", devices)
def test_connected_print(print_ios_Connect, print_System_Testing, take_app_screenshot, deviceName, deviceMac,
                         setup_teardown):
    try:
        print_ios_Connect.check_connect()
        print_ios_Connect.connect(deviceName, deviceMac)
        print_System_Testing.connected_print()
    except Exception as e:
        take_app_screenshot(f"error_{deviceName}")
        pytest.fail(f"设备 {deviceName} 测试失败: {str(e)}")

