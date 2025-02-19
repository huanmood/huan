import os


class DosCmd:
    # 获取执行命令的结果
    def excute_cmd_result(self, cmd):
        result_list = []
        result = os.popen(cmd).readlines()
        for i in result:
            if i == '\n':
                continue
            # strip() 方法用于移除字符串头尾指定的字符
            result_list.append(i.strip('\n'))
        return result_list

    # 直接执行命令
    def excute_cmd(self, cmd):
        os.system(cmd)


if __name__ == "__main__":
    dos = DosCmd()
    print(dos.excute_cmd_result('adb devices'))

