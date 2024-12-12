import os
import unittest

from unittestreport import TestRunner

if __name__ == '__main__':
    # pwd = os.getcwd()
    # pwd = pwd + "testCase"
    # print(pwd)
    # case_path = os.path.join(pwd,"unittestreport数据驱动之列表.py")
    suite = unittest.defaultTestLoader.discover(r"C:\Users\YZY\Desktop\nelko\P21\testCase")  # 自动获取测试用例类
    print("测试套件中的测试用例数量是：", suite.countTestCases())
    # 第二步：运行用例生成测试报告
    runner = TestRunner(suite,
                        filename="自动化测试报告.html",
                        report_dir=r"C:\Users\YZY\Desktop\nelko\P21\report",  # 放桌面
                        title='nelko版本上线测试报告',
                        tester='欢',
                        desc="学习项目测试生成的报告",
                        templates=2  # 报告的风格，有三种，取值是1,2,3
                        )
    runner.run()
