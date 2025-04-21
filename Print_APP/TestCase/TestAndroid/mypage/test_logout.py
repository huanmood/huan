# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam

import unittest

from Print_APP.Page.PageAndroid.LogoutPage import LoginOut
from Print_APP.common.logger import Log


class TestLogout(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.base = LoginOut()

    def test_logout_success(self):
        pass
        # '''正常退出'''
        # try:
        #     self.base.click_mein()
        #     self.log.info('退出成功')
        # except Exception as e:
        #
        #     self.log.error(e)


if __name__ == '__main__':
    unittest.main()
