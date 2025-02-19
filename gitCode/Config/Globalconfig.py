import os.path
from gitCode.page.ReadiNi import readini
def get_data_path(dir):
    filename = os.path.split(os.path.realpath(__file__))[0]  # 获取目录路径
    project_path = readini(os.path.join(filename, "dataPath.ini")).get_value("project_path", "project_path")
    # 测试数据Data
    DataPath = os.path.join(project_path, dir)
    return DataPath

