import os
import time
import unittest
import multiprocessing

from gitCode.util.get_portID import Driver
from gitCode.util.BaseDriver import Base_Driver

from gitCode.util.write_device_yaml import WriteDeviceCommand


class ParamTestCase(unittest.TestCase):
    # 重写TestCase的构造函数，添加上一个param，用来放我们的i
    def __init__(self, methodName='runTest', param=None):
        # 其他的构造函数内容不变。
        super(ParamTestCase, self).__init__(methodName)
        # 但是这样还不行，因为setUpClass是类方法，我们这里是self，setUpClass是取不到这个值的，需要将param设置为全局变量
        # self.param = param
        global params
        params = param


# class CaseTest(unittest.TestCase):
# 这样我们也不继承unittest了，直接继承ParamTestCase
class CaseTest(ParamTestCase):
    @classmethod
    def setUp(self):
        Base_Driver.get_android_driver()
        print("测试开始")

    def test_select(self):
        time.sleep(3)

    @classmethod
    def tearDown(cls):

        print("测试结束")


def get_suite(z):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_select"))
    print("执行了没")

    # 使用 TextTestRunner 代替 HTMLTestRunner
    html_file = os.path.join(os.path.dirname(__file__), "report", f"report{z}.txt")

    # 确保report目录存在
    os.makedirs(os.path.dirname(html_file), exist_ok=True)

    with open(html_file, 'w', encoding='utf-8') as f:
        # 使用 TextTestRunner 输出到文件
        runner = unittest.TextTestRunner(f)
        runner.run(suite)


# 将driver引进并封装成一个方法，这样只要在这里调用这个方法，就可以直接执行appium服务端命令，并写入文件，这样BaseDriver才会拿到数据
def start_server():
    driver = Driver()
    # 由于真正启动appium服务端不会很快，所以我们在main函数最后加上一个time.sleep(20)
    driver.main()


def get_count():
    write_device_command = WriteDeviceCommand()
    count = write_device_command.get_file_lines()
    return count


if __name__ == "__main__":
    start_server()
    threads = []
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
