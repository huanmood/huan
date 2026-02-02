# -*- coding:utf-8 -*-
# @Time   : 2025-03-05 14:52
# @Author : TestTeam

import yaml
import os

# 获取当前文件的上一层路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
caps_path = os.path.join(os.path.join(cur_path, 'config'), 'android_caps.yaml')

# def read_caps():
#     with open(caps_path, 'r', encoding='utf-8') as f:
#         print("我是")
#         print(f)
#         data = yaml.load(f)
#         return data

def read_caps(caps_path):
    with open(caps_path, 'r', encoding='utf-8') as f:
        # print("读取 YAML 文件内容：")
        # print(f.read())  # 先打印文件内容，帮助调试
        f.seek(0)  # 将文件指针重置到文件开头
        data = yaml.safe_load(f)  # 再读取文件内容
        return data


