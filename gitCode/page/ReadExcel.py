import os.path
import pandas as pd
from gitCode.Config.Globalconfig import get_data_path


class ReadExcel():
    def __init__(self,filename,sheetname):
        self.get_path=get_data_path("Data")
        self.project_path = os.path.join(self.get_path, filename)
        print(self.project_path)
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
