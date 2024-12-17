# coding=utf-8
"""
通用模块，比如find_element,click,input等
"""
import base64
import os
import re
import allure
# import imagehash
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image
import math
import operator
from functools import reduce

from selenium.common.exceptions import TimeoutException

from gitProject.aa.Public.Common.log import MyLog

log = MyLog().get_log()
logger = log.get_logger()


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        """
        功能：找到loc对应的元素，点击它
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :return: 点击找到的元素
        """
        try:
            self.find_element(loc).click()
        except Exception:
            raise

    def click_s(self, loc, index):
        try:
            self.find_elements(loc)[index].click()
        except Exception:
            raise

    def tap(self, loc):
        """
        功能：找到loc对应的元素，轻敲它
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :return: 点击找到的元素
        """
        tc = TouchAction(self.driver)
        x_value = loc[0]
        y_value = loc[1]
        try:
            tc.tap(x=x_value, y=y_value).perform()
        except Exception as e:
            logger.error(str(e))
            raise

    def input_text(self, loc, text):
        """
         功能：找到loc对应的元素，输入text文字
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :param text: 要输入的字符串
        :return: 给找到的元素输入text值
        """
        try:
            self.find_element(loc).send_keys(text)
        except Exception:
            raise

    def find_element(self, loc, timeout=20.0, time=0.5):
        """
        查找元素
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :return: 返回一个元素
        """
        by = loc[0]
        value = loc[1]

        if by == By.XPATH:
            value = self.make_xpath_feature(value)


        try:
            ele = WebDriverWait(self.driver, timeout, time).until(lambda x: x.find_element(by, value))
            # logger.info(value)
        except TimeoutError:
            logger.error("没有找到元素：%s，或者寻找超时" % value)
            raise
        else:
            return ele
