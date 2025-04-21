# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam
import time
import unittest
from parameterized import parameterized
from Print_APP.Page.PageAndroid.LoginPage import Login
from Print_APP.common.logger import Log
from Print_APP.common.read_json import read_json
class TestLogin(Login):
    log = Log()
    @parameterized.expand(read_json("data.json", "userinfo"))
    def test_login_success(self, email, pwd):
        '''正常登录'''
        try:
            self.app_login(email, pwd)
            time.sleep(5)
            self.assertEqual(self.login_success(),'首页')
            self.log.info('登录成功')
        except Exception as e:
            self.getScreenShot()
            self.log.error(e)


if __name__ == '__main__':
    unittest.main()