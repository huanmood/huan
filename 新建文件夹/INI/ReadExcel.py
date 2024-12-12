import os.path
import pandas as pd
# import xlrd此库只适合xls，xlsx已经不再适配
from Config import globalconfig
from Config.globalconfig import project_path

DataPath = globalconfig.DataPath
print(DataPath)


class ReadExcel():
    def __init__(self, filename, sheetname):
        self.project_path = os.path.join(DataPath, filename)
        self.data = pd.read_excel(self.project_path, sheet_name=sheetname,header=None)

    def read_excel(self):
        self.nrow, self.ncol = self.data.shape
        print("self.data.shape为", self.data.shape)
        for i in range(self.nrow):
            for j in range(self.ncol):
                value = self.data.iloc[i, j]
                print(value)


if __name__ == '__main__':
    readexcel = ReadExcel("test.xlsx", "Sheet1")
    readexcel.read_excel()
