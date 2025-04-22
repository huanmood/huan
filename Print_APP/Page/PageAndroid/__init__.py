# -*- coding:utf-8 -*-
# @File  : __init__.py.py
# @Time  : 2025/03/06/13:45
# @Author: TestTeam
from selenium.webdriver.common.by import By

'''首页页面'''
# 我的
mein_button_loc = ('xpath', "//*[@text='我的']")
# 打印机名称
deviceName_loc = (By.ID, 'com.nelko.printer:id/tv_printer_model')
# 选择打印机后的确认
deviceConfirm = (By.ID, 'com.nelko.printer:id/tv_ok')
# 点击查看更多功能(提示语)
moreFeatures = (By.ID, 'com.nelko.printer:id/text_view')
#更多按钮
moreButton=(By.XPATH,'//android.widget.TextView[@resource-id="com.nelko.printer:id/view_menu_title" and @text="更多"]')
# 确定
sure = (By.ID, 'com.nelko.printer:id/more_btn_ok')
# 点击更换打印纸
replacePrintPaper = (By.ID, 'com.nelko.printer:id/btn_replace_label_paper')
# 我知道了
know = (By.ID, 'com.nelko.printer:id/btn_ok')
#未连接/连接
connectState=(By.ID,'com.nelko.printer:id/tv_connect')
#我的模板
myTemplate=(By.XPATH,'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="我的模板"]')
'''我的页面'''
# 点击登录/用户名称
username_button_loc = ('id', 'com.nelko.printer:id/text_user_name')
# 首页连接
Homepage_connect = (By.ID, 'com.nelko.printer:id/tv_connect')
'''登录页面'''
# 邮箱
email_loc = ('id', 'com.nelko.printer:id/edit_email')
# 密码
pwd_loc = ('id', 'com.nelko.printer:id/edit_password')
# 登录
login_button_loc = ('id', 'com.nelko.printer:id/sign_in')
# 勾选
ticked_button_loc = ('id', 'com.nelko.printer:id/checkBox_agreement')

# 登录成功后的菜单首页
login_success_loc = ('xpath',
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView')

'''帐号管理'''
# 退出
logout_loc = ('id', 'com.nelko.printer:id/btn_login_out')
# 确认退出
confirm_loc = ('id', 'com.nelko.printer:id/tv_sure')

'''首次下载APP进入首页的授权'''
# 用户协议和隐私政策
firstDownload_UserAgreementPrivacyPolicy = (By.ID, 'com.nelko.printer:id/tv_ui_title')
# 同意
firstDownload_sure = (By.ID, 'com.nelko.printer:id/tv_ui_confirm')
# 稍后连接
firstDownload_afterConnect = (By.ID, 'com.nelko.printer:id/connect_later_tv')
# 选择机型处的确认
firstDownload_confirm = (By.ID, 'com.nelko.printer:id/tv_ok')
# 首次下载获取权限页面：跳过
skip = (By.ID, 'com.nelko.printer:id/iv_back')
# 我知道了
connect_Dev_know = (By.ID, 'com.nelko.printer:id/hint_more_btn_ok')


'''连接页面'''
#连接附件的设备->始终允许
connectPage_Allow_in_use = (By.ID, 'com.lbe.security.miui:id/permission_allow_button_1')
#授权
connectPage_shouquan=(By.ID,'com.nelko.printer:id/tv_sure')
# 顶部排序连接
connectPage_title = (By.XPATH, '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]')
#刷新
connectPage_refresh = (By.XPATH, '//android.widget.TextView[@text="刷新"]')
#连接失败
connectFaile=(By.ID,'com.nelko.printer:id/tv_title')
#连接失败->确认
connectFaile_sure=(By.ID,'com.nelko.printer:id/tv_sure')
#要与***配对吗？
alertTitle=(By.ID,'com.android.settings:id/alertTitle')
#要与***配对吗？->配对
accept_button=(By.ID,'com.android.settings:id/pairing_accept_button')

'''模板'''
#搜索
search=(By.ID,'com.nelko.printer:id/view_et_content')
#模板尺寸列表
templateSize=(By.ID,'com.nelko.printer:id/text_size')
#选择尺寸的确定
templateSize_sure=(By.ID,'com.nelko.printer:id/btn_selected')

