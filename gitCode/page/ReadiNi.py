import configparser

class readini():
    """
    传入ini文件
    """

    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def get_section(self, section):
        """
        传入section，返回：列表包含元组形式的[(key,value),(key,value)]
        :param section:
        :return:
        """
        data = self.cf.items(section)
        return data

    def get_key(self, section):
        """
        传入section，返回该section下所有的key组成的列表
        :param section:
        :return: list of keys
        """
        keys = self.cf.options(section)
        return keys

    def get_value(self, section, key):
        """
        传入section和key，返回对应的value
        :param section:
        :param key:
        :return: value
        """
        value = self.cf.get(section, key)
        return value

if __name__ == '__main__':
    cdb = readini("../Config/data.ini")
    data=cdb.get_section(section="desired_caps")
    print(len(data))