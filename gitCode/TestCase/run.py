import unittest

from appium import webdriver
from gitCode.TestCase.share_devices import thread_local
from gitCode.TestCase.test_labelnizePrint import TestMathOperations
import ast
import threading

lock = threading.Lock()
current_position = 0


def getCaps_device(file):
    global current_position
    dict_list = []
    with lock:
        with open(file) as f:
            f.seek(current_position)
            data = f.readline()
            current_position = f.tell()
            data = data.strip().split(";")
            for i in range(len(data)):
                if i == 1:
                    dict_list.append(ast.literal_eval(data[i]))
                else:
                    dict_list.append(data[i])
    return dict_list


# 设置设备的desired capabilities
def run_device_2(getCaps):
    data = getCaps("../Data/desc.txt")
    driver = webdriver.Remote(data[0], data[1])
    thread_local.driver = driver  # 保存到线程本地变量
    driver.implicitly_wait(10)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathOperations)
    unittest.TextTestRunner().run(suite)
if __name__ == '__main__':
    threads = []
    for _ in range(2):
        thread = threading.Thread(target=run_device_2, args=(getCaps_device,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

