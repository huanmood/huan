import pytest

from Page.PageiOS.iOS_Connect import ios_Connect
from Page.PageiOS.iOS_aiPicture import aiPicture

devices = [

    ("P21", "43:2C:42:48:63:5F"),
    ("PM220", "31:9D:16:24:B1:78"),
    ("P31S", "77:3F:34:E4:6D:51")
]

@pytest.fixture(scope="function")
def ai_Picture(action):
    """获取ios_Connect类方法"""
    return aiPicture(action)

@pytest.fixture(scope="function")
def print_ios_Connect(action):
    """获取ios_Connect类方法"""
    return ios_Connect(action)


@pytest.mark.parametrize("deviceName,deviceMac", devices)
def test_connected_print(print_ios_Connect, ai_Picture, deviceName, deviceMac):
    try:
        # print_ios_Connect.check_connect()
        # print_ios_Connect.connect(deviceName, deviceMac)
        ai_Picture.run_compare_app_vs_api(deviceName)
    except Exception as e:

        pytest.fail(f"设备 {deviceName} 测试失败: {str(e)}")
