# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam
import unittest

from Page import PageAndroid
from Page.BasePage import Action


class LoginOut(Action):

    def click_mein(self):
        '''点击我的按钮'''''
        self.click_button(PageAndroid.mein_button_loc)

    def click_user(self):
        '''进入帐号管理'''
        self.click_button(PageAndroid.username_button_loc)

    def click_logout(self):
        '''点击退出登录按钮'''
        self.click_button(PageAndroid.logout_loc)

    def click_confirm_logout(self):
        '''退出确认按钮'''
        self.click_button(PageAndroid.confirm_loc)

    def app_logout(self):
        '''组合业务方法'''
        self.click_mein()
        self.click_user()
        self.click_logout()
        self.click_confirm_logout()
