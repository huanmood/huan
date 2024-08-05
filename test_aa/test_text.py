import time
import unittest
from unittestreport import TestRunner
import unittest, os
import unittestreport
from unittestreport import TestRunner


class aa(unittest.TestCase):
    def test_aa(self):
        time.sleep(2)
        assert 1 + 1 > 1




# 第一步：收集测试用例
pwd = os.getcwd()
print(pwd)

# case_path = os.path.join(pwd,"unittestreport数据驱动之列表.py")
suite = unittest.defaultTestLoader.discover(pwd)  # 自动获取测试用例类
print("测试套件中的测试用例数量是：", suite.countTestCases())
# 第二步：运行用例生成测试报告
runner = TestRunner(suite,
                    filename="自动化测试报告.html",
                    report_dir=r"C:\Users\YZY\Desktop\nelko\test_aa",  # 放桌面
                    title='nelko版本上线测试报告',
                    tester='maoge',
                    desc="学习项目测试生成的报告",
                    templates=2  # 报告的风格，有三种，取值是1,2,3
                    )
runner.run()
