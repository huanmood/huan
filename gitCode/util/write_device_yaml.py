import os

import yaml
from yaml import FullLoader


class WriteDeviceCommand:
    def read_data(self):
        file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config"),
                                 "deviceconfig.yaml")
        with open(file_path) as f:
            data = yaml.load(f, Loader=FullLoader)
            print("data",data)
        return data

    # 拼接数据
    def join_data(self, i, device, bp, port):
        data = {
            "device_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def write_data(self, i, device, bp, port):
        data = self.join_data(i, device, bp, port)
        file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config"),
                                 "deviceconfig.yaml")
        with open(file_path, 'a') as f:
            yaml.dump(data, f)

    def get_value(self, key, port):
        dataone = self.read_data()
        value = dataone[key][port]
        return value

    # 清空数据
    def clear_data(self):
        file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config"),
                                 "deviceconfig.yaml")
        # 注意这里是w
        with open(file_path, 'w') as f:
            f.truncate()

    # 返回数据长度，这样多线程循环的时候才知道循环多少次
    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == "__main__":
    file = WriteDeviceCommand()
    data = file.read_data()


    # print(file.get_value("device_info_0", "port"))

