# -*- coding:utf-8 -*-
# @File  : __init__.py.py
# @Time  : 2025/03/06/13:44
# @Author: TestTeam
'''连接页面'''
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import AppiumBy as By
# 首页元素
rfid_tab_ele = (AppiumBy.IOS_PREDICATE, 'name == "rfid tab new icon" OR label == "rfid tab new icon"')  # 首页+号
connect_btn = (AppiumBy.IOS_PREDICATE, 'name == "已连接" OR label == "已连接"')  # 首页已连接状态
not_connect_btn = (AppiumBy.IOS_PREDICATE, 'name == "未连接" OR label == "未连接"')  # 首页未连接状态


# 编辑器元素
printBT = (AppiumBy.IOS_PREDICATE, 'name == "打印" OR label == "打印"')  # 打印按钮

# 连接页面元素
refresh = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@label="刷新"]')  # 连接页面刷新按钮
sure = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@label="确定"]')  # 确定按钮
disconnect = (AppiumBy.IOS_PREDICATE, 'name == "断开连接" OR label == "断开连接"')  # 确定按钮
deviceName = (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText"')  # 需要find_elements()里面的[2]可以获取到打印机名称

# 系统模板元素
template = (AppiumBy.IOS_PREDICATE, 'name == "系统模板" OR label == "系统模板"')
# 尺寸
allSize = (AppiumBy.IOS_PREDICATE, 'name == "全部尺寸" OR label == "全部尺寸"')
nowSize = (AppiumBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeButton/XCUIElementTypeStaticText')#系统模板获取到的当前RFID的尺寸
showAllSize = (AppiumBy.XPATH, "//XCUIElementTypeOther/XCUIElementTypeStaticText")#展开所有尺寸按钮
# 类型
allType = (AppiumBy.IOS_PREDICATE, 'name == "全部场景" OR label == "全部场景"')
showAllType = "xpath", '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText'#展开所有模板类型按钮
#content
Template_preview = "xpath", '//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'#匹配系统模板页面有多少个img元素

#AI图库元素
aiPicture = (AppiumBy.IOS_PREDICATE, 'name == "AI图库" OR label == "AI图库"')
aiPicture_preview=(By.IOS_CLASS_CHAIN,'**/XCUIElementTypeCollectionView/**/XCUIElementTypeCell/**/XCUIElementTypeImage')