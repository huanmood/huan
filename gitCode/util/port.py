from gitCode.util.dos_cmd import DosCmd


class Port:
    def __init__(self):
        self.cmd = DosCmd()

    def windows_port_was_used(self, port):
        # 但是上面这个命令在Mac上是没有的
        result = self.cmd.excute_cmd_result('netstat -ano | findstr ' + str(port))
        if len(result) > 0:
            return True
        else:
            return False

    def mac_port_was_used(self, port):
        result = self.cmd.excute_cmd_result('netstat -anp  tcp| grep ' + str(port))
        if len(result) > 0:
            return True
        else:
            return False

    def create_port_list(self, start_port, device_list):
        # start_port，我们从哪个端口开始占用端口,但是注意，我们传进来的这个值是
        # device_list，我们有了设备的个数，就知道占用多少个端口
        port_list = []

        # 只有设备信息不为空的时候我们才继续
        if device_list is not None:
            # for i in len(device_list):
            # 我们不能用for循环来决定，因为如果有端口被占用了怎么办，那就会报错，所以我们用while
            # 只要我们的端口个数不等于设备个数，那我们就继续
            while len(port_list) != len(device_list):
                # 当初始端口没有被占用的时候我们才继续
                if not self.windows_port_was_used(start_port):
                    port_list.append(start_port)

                # 由于我们这里是需要进行假发运算，所以这里是int类型的，但是mac_port_was_used里的port需要的是str类型的
                # 所以我们需要修改一下mac_port_was_used里的port参数
                start_port = start_port + 4

            return port_list
        else:
            print("生成端口失败")
            return None


if __name__ == "__main__":
    port = Port()
    listone = [1, 2, 3, 4]
    print(port.create_port_list(8888, listone))
