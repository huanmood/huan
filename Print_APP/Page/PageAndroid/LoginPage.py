# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam
import time
from common.GlobalValue import GlobalVar
from Page import PageAndroid
from Page.BasePage import Action


class Login(Action):

    def click_mein(self):
        '''点击我的按钮'''''
        self.click_button(PageAndroid.mein_button_loc)

    def click_username(self):
        '''点击用户名称按钮'''''
        self.click_button(PageAndroid.username_button_loc)

    def click_use_email_login(self):
        '''使用email登录'''
        self.click_button(PageAndroid.uer_email_login)

    def input_email(self, email):
        '''输入邮箱'''
        self.click_button(PageAndroid.email_loc)
        time.sleep(2)
        self.send_keys(PageAndroid.email_loc, email)

    def input_pwd(self, pwd):
        '''输入密码'''
        self.click_button(PageAndroid.pwd_loc)
        self.send_keys(PageAndroid.pwd_loc, pwd)

    def click_login(self):
        '''点击登录按钮'''
        self.click_button(PageAndroid.login_button_loc)

    def click_ticked(self):
        '''点击勾选按钮'''
        self.click_button(PageAndroid.ticked_button_loc)

    def login_success(self):
        '''判断登录是否成功'''
        # login_success = self.driver.find_element_by_id('com.alipay.android.phone.discovery.o2ohome:id/tab_description').text
        login_success = self.find_element(PageAndroid.login_success_loc).text
        return login_success

    def app_login(self, email, pwd):
        '''组合业务方法'''
        try:
            self.click_use_email_login()
            self.input_email(email)
            self.input_pwd(pwd)
            self.back_button()
            self.click_ticked()
            self.click_login()
            self.login_status = GlobalVar.set_value("login_status", "ture")
        except:
            self.login_status = GlobalVar.set_value("login_status", "false")
