import mysql.connector
from gitCode.page.ReadiNi import connectDataBase
from result.log import MyLog
log = MyLog().get_log()#获取Log对象
logger = log.get_logger()#利用Log对象调用里面的log生产对象（looger）
class selectMysql():
    def __init__(self,filename,section):
        self.con = connectDataBase(filename)#获取配置文件类对象(传入ini文件)
        self.data = self.con.connect(section=section)  #
        try:
            self.connection = mysql.connector.connect(
                host=self.data[0][1],
                user=self.data[1][1],
                password=self.data[2][1],
                database=self.data[3][1]
            )
        except Exception as e:
            logger.error(e)
        self.cursor = self.connection.cursor()
    def sql_execute(self,sql):
        self.cursor.execute(sql)
        # 获取所有结果
        results = self.cursor.fetchall()
        for row in results:
            print(row)
    def sql_close(self):
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    c = selectMysql("../Config/data.ini", "dataBase")
    c.sql_execute("show databases;")
    c.sql_close()