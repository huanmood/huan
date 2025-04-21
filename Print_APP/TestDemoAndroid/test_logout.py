# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam
import unittest

from Print_APP.TestCase.TestAndroid.mypage.test_logout import TestLogout
from Print_APP.common.logger import Log


class TestLogout(TestLogout):
    log = Log()
    def test_logout_success(self):
        '''正常退出'''
        try:
            self.app_logout()
            self.log.info('退出成功')
        except Exception as e:
            self.getScreenShot()
            self.log.error(e)

if __name__ == '__main__':
    unittest.main()