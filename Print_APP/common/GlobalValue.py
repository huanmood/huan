# -*- coding:utf-8 -*-
"""
定义全局变量，并且全局变量需要跨文件使用时，可以用该类。

比如定义全局变量的时候可以这样：
global_var = GlobalVar()
global_var.set_value("name", "value")
使用该全局变量的时候这样：
global_var.get_value("name")

"""

class GlobalVar:
    def __init__(self):
        global _global_dict
        _global_dict = {}

    @staticmethod
    def set_value(name, value):
        _global_dict[name] = value

    @staticmethod
    def get_value(name, def_value=None):
        try:
            return _global_dict[name]
        except KeyError:
            return def_value