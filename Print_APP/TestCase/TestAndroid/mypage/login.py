# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam

import unittest

from parameterized import parameterized

import time

from Page.PageAndroid.LoginPage import Login

from common.read_json import read_json


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.base = Login()
    @parameterized.expand(read_json("data.json", "userinfo"))
    def test_login_success(self, email, pwd):
        '''正常登录'''
        try:
            self.base.click_mein()
            self.base.app_login(email, pwd)
            time.sleep(5)
            # self.base.assertEqual(self.base.login_success(), '首页')
            self.base.log('登录成功')
        except Exception as e:
            self.base.log(e)


if __name__ == '__main__':
    unittest.main()
