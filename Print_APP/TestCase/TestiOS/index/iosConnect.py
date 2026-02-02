import pytest

from Page.PageiOS.iOS_Connect import ios_Connect

# 设备列表
devices = [
    ("PM230", "25:41:63:A5:40:73"),
    ("P21", "43:2C:42:48:63:5F")

]


@pytest.fixture(scope="module")
def connect_Unit_Testing(ios_Testing):
    """单元测试"""
    return ios_Testing


@pytest.fixture(scope="session")
def connect_System_Testing(action):
    """系统测试"""
    return ios_Connect(action)


# 测试检查连接
def test_check_connect(connect_System_Testing):
    connect_System_Testing.check_connect()



@pytest.mark.parametrize("deviceName,deviceMac", devices)
def test_connect(connect_System_Testing, deviceName, deviceMac):
    connect_System_Testing.connect(deviceName,deviceMac)






