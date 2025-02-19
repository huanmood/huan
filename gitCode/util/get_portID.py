import threading

from gitCode.util.dos_cmd import DosCmd
from gitCode.util.port import Port
from gitCode.util.write_device_yaml import WriteDeviceCommand


class Driver:
    def __init__(self):
        self.cmd = DosCmd()
        # 重点7，将device_list放到构造函数里，因为get_driver的作用就是获取devices_list，那么就需要把所有的调用get_driver的地方都替换成devices_list
        self.devices_list = self.get_driver()
        ## 将WriteDeviceCommand放到构造函数里来
        self.write_file = WriteDeviceCommand()
    def get_driver(self):
        devices_list = []
        device_info = self.cmd.excute_cmd_result('adb devices')
        # 第一部分为一段文案，从第二段开始才是设备信息，所以只有大于等于2的时候才有设备连接到电脑
        if len(device_info) >= 2:
            for i in device_info:
                if 'List' in i:
                    continue
                # 将一条设备信息分割成一个list,第一部分为设备信息，第二部分为device，也就是设备的状态
                device = i.split('\t')
                # 只有状态为device的时候这个设备才是可用的
                if device[1] == 'device':
                    devices_list.append(device[0])
            return devices_list
        else:
            return None

    def creat_port_list(self, start_port):
        port = Port()
        # 重点8，这里用到了get_driver，要替换一下
        # port_list = port.create_port_list(start_port, self.get_driver())
        port_list = port.create_port_list(start_port, self.devices_list)
        return port_list

    def create_command(self, i):
        def create_command(self, i):
            # 重点4，既然我们把i传进来了，就把所有调用这个地方的都加上i这个参数
            # appium -p 4700 -bp 4901 -U JPF4C19123011893
            ## 已经添加到了构造函数里，所以直接用self即可
            ## write = WriteDeviceCommand()
            write = self.write_file
            command_list = []
            appium_port_list = self.creat_port_list(4700)
            bp_port_list = self.creat_port_list(4900)
            # 重点9，这里用到了get_driver，要替换一下
            # driver_list = self.get_driver()
            driver_list = self.devices_list

            if driver_list is not None:
                # 重点3， 既然在多线程的时候我们已经循环过create_command了，那这里就不应该再根据driver_list的长度循环了
                # 而这个i其实我们在多线程那块已经有了，我们可以直接拿来用，并将for循环删除掉
                # for i in range(len(driver_list)):
                # 　　--no-reset 不要每次都安装apk
                #    --session-override 是指覆盖之前的session
                command = "appium -a 127.0.0.1 -p {}".format(appium_port_list[i])
                command_list.append(command)
                # 重点3， 每一次调用create_command都会写入文件一次，调用两次，写了两次
                write.write_data(i, driver_list[i], bp_port_list[i], appium_port_list[i])
                return command_list
            else:
                return None


    def start_driver(self, i):
        # 重点5，这里要加上i
        # start_list = self.create_command()
        start_list = self.create_command(i)
        # 重点12，上面已经是的时候我们已经通过i来控制了start_list的内容了，就只可能是1条，那我们下面这一行就不能用i了，直接用0即可
        # self.cmd.excute_cmd(start_list[i])
        self.cmd.excute_cmd(start_list[0])


    def main(self):
        # 重点1，我们在这里循环了一次create_command
        # 重点6， start_driver里面有i，可是在main的入参里可没有i怎么办，我们加上了这个i就会报错。我们发现每次需要获取设备个数的时候都要执行self.create_command(i)
        # 我们可以把设备个数这一部分放到构造函数里，设备个数即为devices_list，在get_driver方法里
        # 重点10，既然我们已经有了devices_list，就不用再调用create_command获取长度了，换成devices_list即可
        for i in range(len(self.devices_list)):
            # 重点2，这里的target是多线程的，并没有直接调用
            # 重点11，我们这里start_driver传的是什么，传的是多线程,如果我们有两个手机，那么这里就会i就会是0，1
            appium_start = threading.Thread(target=self.start_driver, args=(i,))
            appium_start.start()


if __name__ == "__main__":
    driver = Driver()
    print(driver.main())

