# -*- coding:utf-8 -*-
# @File  : read_json.py
# @Time  : 2025/03/06/10:13
# @Author: TestTeam

import os, json

import config


# 读取json工具
def read_json(filename, key):
    file_path = config.DIR_PATH + os.sep + filename
    print(file_path)
    arrs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for data in json.load(f).get(key):
            arrs.append(tuple(data.values())[1:])
        # print(arrs)
        return arrs


def read_json_nokey(filename):
    file_path = config.DIR_PATH + os.sep + filename
    print(file_path)
    arrs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for data in json.load(f).get("add_device"):
            arrs.append(tuple(data.values())[1:])
        # print(arrs)
        return arrs
# read_json("data.json",'userinfo')
# read_json_nokey("Android_12.json")