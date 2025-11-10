import pytest

from Page.PageAndroid.Connect import android_Connect

# 设备列表
devices = [
    ("PM230", "25:41:63:A5:40:73"),
    ("PM220", "31:9D:16:24:B1:78"),
    ("P21", "43:2C:42:48:63:5F")
]


@pytest.fixture(scope="module")
def connect_page(action):
    """返回 Action 对象"""
    return android_Connect(action)


# def test_01check_connect(connect_page):
#     connect_page.aaa()


# @pytest.mark.parametrize("deviceName,deviceMac", [
#     ("PM230", "25:41:63:A5:40:73"),
#     ("PM220", "31:9D:16:24:B1:78")
# ])
# def test_02connect(Unit_Testing, deviceName, deviceMac):
#     Unit_Testing.connect(deviceMac)
