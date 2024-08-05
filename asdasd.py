# # # # # def calculate_average(list):
# # # # #     for i in list:
# # # # #         total=total+i
# # # # #     avg=sum/len(list)
# # # # #     return avg
# # # #
# # # #
# # # # # def count_vowels(str):
# # # # #     count = 0
# # # # #     for i in str:
# # # # #         if i == 'a' or i == 'A' or i == 'e' or i == 'E'or i == 'o' or i == 'O'or i == 'i' or i == 'I'or i == 'u' or i == 'U':
# # # # #             count += 1
# # # # #     return count
# # # # def unique_list(lst):
# # # #     return list(set(lst))
# # # # # def test_multipleChoice(self,):
# # #     #     try:
# # #     #         # 对文本进行测试
# # #     #         # 点击多选按钮
# # #     #         print("\n多选功能开始测试\n")
# # #     #         text1 = ['XPATH', '(//android.widget.TextView[@text="双击文本框编辑"])[1]']
# # #     #         text2 = ['XPATH', '(//android.widget.TextView[@text="双击文本框编辑"])[2]']
# # #     #         self.base.tap_at_coordinates(876, 545)
# # #     #         self.base.tap_at_coordinates(641, 937)
# # #     #         self.base.dragEle(570, 536, text2)
# # #     #         self.base.click(multiBtn)
# # #     #         self.base.click(text1)
# # #     #         self.base.click(text2)
# # #     #         print("\n多选功能结束测试\n")
# # #     #     except Exception as e:
# # #     #         print("多选功能测试失败: ", e)
# # #     #         self.base.open(url, desired_caps)  # 启动Appium会话
# # #     #         self.base.test_01_connectP21()
# # #     #         self.base.test_02_openEditor()
# # #     #         return
# # #
# # # # class TestAlignView(unittest.TestCase):
# # # #     @classmethod
# # # #     def setUpClass(cls):
# # # #         cls.base = Base()  # 实例化Base对象
# # # #         cls.base.open(url, desired_caps)  # 启动Appium会话
# # # #         cls.base.first_open()  # 处理初次连接逻辑
# # # #         cls.base.test_01_connectP21()
# # # #         cls.base.test_02_openEditor()
# # # #     def topAlign(self, Btn):
# # # #         # try:
# # # #             # 对齐按钮
# # # #             alignBtn = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tab_1"]']
# # # #             #上对齐按钮
# # # #             topAlignBtn = ['XPATH', '//android.widget.RelativeLayout[@resource-id="com.nelko.printer:id/alignTop"]']
# # # #             self.base.tap_at_Windows(0.5, 0.3)
# # # #             self.base.click(clear)
# # # #             self.base.click(Btn)
# # # #             self.base.twoStpe_shucai()
# # # #             self.base.twoStpe_biankuang()
# # # #             self.base.click(alignBtn)
# # # #
# # # # print(unique_list([1, 2, 2, 3, 3, 4, 5]))
# # # #
# # # # def test_delete(self):
# # # #     try:
# # # #         # 对文本进行测试
# # # #         self.base.click(deleteBtn)
# # # #         textEleNum = self.base.matchingElement(text)
# # # #         if len(textEleNum) == 0:
# # # #             print("所有元素以被选中并删除")
# # # #         print("\n删除功能结束测试\n")
# # # #     except Exception as e:
# # # #         print("删除功能测试失败: ", e)
# # # #         self.base.open(url, desired_caps)  # 启动Appium会话
# # # #         self.base.test_01_connectP21()
# # # #         self.base.test_02_openEditor()
# # # #         return
# # # import random
# # # import re
# # #
# # # # a='//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'
# # # # b='//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'
# # # # c='//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView'
# # # # a='//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView
# # # #
# # # # raNum = random.randint(1, 12)
# # # # eleNum='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout'+'['+str(raNum)+']'
# # # # print(type(eleNum))
# # # # matches = re.findall(r'\[(.*?)\]', location)  # 匹配中括号内的内容
# # # # result = [[int(num) for num in match.split(',')] for match in matches]
# # #
# # # # //android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="全部"]
# # #
# # #
# # # # //android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView
# # # #
# # # # //androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[6]
# # # # //androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.LinearLayout[5]
# # # # //android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]
# # # # //android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]
# # # # //android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView
# # #
# # # import os
# # # import sys
# # # # q=sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# # # # //android.widget.ImageView[@resource-id="com.nelko.printer:id/btv_font_name"]
# # # # //androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[2]
# # # # //androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[3]
# # # # num=9
# # # # ra = random.randint(1, num)
# # # # ele = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.nelko.printer:id/leer_rcv"]/android.widget.RelativeLayout[' +str(ra) + ']'
# # # # print(ele)
# # # import requests
# # from PIL import Image
# # from io import BytesIO
# #
# 图片的URL
# from io import BytesIO
#
# from PIL import Image
#
# url = 'https://upload.nelko.net/img/32024053008502800025002.jpg'
#
# # 发送GET请求获取图片数据
# import requests
#
# response = requests.get(url)
#
# # 确保请求成功
# if response.status_code == 200:
#     # 将图片数据转换为BytesIO对象
#     img_data = BytesIO(response.content)
#
#     # 使用Pillow打开图片
#     img = Image.open(img_data)
#
#     # 显示图片
#     img.show()
#
#     # 可选：保存图片到本地
#     img.save('downloaded_image.jpg')
# else:
#     print("Failed to retrieve the image")
# import os
# import random
# from json.decoder import JSONObject
# from typing import List
#
#
# import cv2
# import numpy as np
#
# #
# # import random
# # import string
# #
# # def generate_random_string():
# #     # 生成一个包含大小写字母和数字的所有字符集合
# #     characters = string.ascii_letters + string.digits
# #     # 使用random模块的choices函数从字符集合中随机选取8个字符，并将它们连接起来
# #     random_string = ''.join(random.choices(characters, k=8))
# #     return random_string
# #
# # # 调用函数生成随机字符串，并打印输出
# # random_string = generate_random_string()
# # print("随机生成的8位字母+数字形式的随机数为:", random_string)
# # from datetime import datetime
# # #
# #
# # current_date = datetime.now().date()
# # print(current_date)
# # location1 = ['XPATH', '(//android.widget.TextView[@text="'+str(current_date)+'"])[2]']
# # print(location1)
# # def get_current_hour():
# #     # 获取当前小时
# #     current_hour = datetime.now().strftime('%H:%M:%S')
# #     return current_hour
# #
# # # 调用函数获取当前小时并打印输出
# # current_hour = get_current_hour()
# # print("当前小时为:", current_hour)
# import string
# from datetime import datetime
#
# # def format_date(input_date):
# #     # 将输入日期字符串转换为 datetime 对象
# #     date_obj = datetime.strptime(input_date, '%Y-%m-%d')
# #
# #     # 格式化为指定格式的字符串
# #     formatted_date = date_obj.strftime('%d-%m-%Y')
# #
# #     return formatted_date
# # format_date()
# # def get_current_date():
# #     current_date = datetime.now().strftime('%d-%m-%Y')
# #     print(current_date)
# # get_current_date()
# # characters = string.ascii_letters + string.digits
# # print(characters)
# #####################################################################################################################
# #                                   判断两张图片是否相同
# # import cv2
# # import numpy as np
# #
# #
# # def resize_image(img, width=None, height=None):
# #     if width is not None and height is not None:
# #         return cv2.resize(img, (width, height))
# #     elif width is not None:
# #         h, w = img.shape[:2]
# #         new_height = int(h * (width / w))
# #         return cv2.resize(img, (width, new_height))
# #     elif height is not None:
# #         h, w = img.shape[:2]
# #         new_width = int(w * (height / h))
# #         return cv2.resize(img, (new_width, height))
# #     else:
# #         return img
# #
# #
# # def images_are_similar(img1_path, img2_path, threshold=0.2):
# #     img1 = cv2.imread(img1_path)
# #     img2 = cv2.imread(img2_path)
# #
# #     # 调整图片尺寸
# #     img2_resized = resize_image(img2, width=img1.shape[1], height=img1.shape[0])
# #
# #     # 计算两个图像之间的差异
# #     diff = cv2.absdiff(img1, img2_resized)
# #
# #     # 将差异矩阵转换为灰度图像
# #     gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
# #
# #     # 计算差异的平均值
# #     mean_diff = np.mean(gray_diff)
# #
# #     # 设定阈值，判断平均差异是否在可接受范围内
# #     similarity = 1 - mean_diff / 255.0
# #     return similarity >= threshold
# #
# #
# # # 示例图片路径
# # img1_path = 'D:/a.jpg'
# # img2_path = 'D:/b.jpg'
# #
# # # 比较图片
# # if images_are_similar(img1_path, img2_path, threshold=0.98):  # 80% 相似度阈值
# #     print("两张图片相似")
# # else:
# #     print("两张图片不同")
# ###############################################################################################################
# #                                            保存接口返回image到文件夹
# # import requests
# # # 发送请求获取图片
# # url = 'http://app.nelko.net/api/banner/list'
# # data = {
# #     "dev": "P21",
# #     "position": 1
# # }
# # header = {
# #     "accessToken": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlZDExYTEyYS1kZjExLTQyODItYmY0Mi00YTVmZTY3NDZhMTAiLCJzdWIiOiIxMDAwMDQ5NzEyIiwiaXNzIjoiYWRtaW4iLCJpYXQiOjE3MTk5MTI1NDYsImV4cCI6NDI0Mjc5MjU0Nn0.eoH5TsAslK4kH0EV-ThiVh6aJqUypROeqdW1k9Gwyrg",
# #     "language": "en"
# # }
# # response = requests.post(url=url, json=data, headers=header)
# # data = response.json()
# # print()
# # for i in range(len(data['data'])):
# #     imageUrl=data['data'][i]['image']
# #     image_response = requests.get(imageUrl)
# #     if image_response.status_code == 200:
# #         file_name = os.path.basename(imageUrl)
# #         bannerPicPath='D:/bannerPic'
# #         if not os.path.exists(bannerPicPath):
# #              os.makedirs(bannerPicPath)
# #         save_path = os.path.join(bannerPicPath, file_name)
# #         with open(save_path, 'wb') as file:
# # #         # 将响应内容写入文件
# #             file.write(image_response.content)
# ###############################################################################################################################
# #                                            获取APP的banner
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ###############################################################################################################
# import os
#
# import requests
# from PIL import Image
# #
# # def get_images_from_folder(folder_path):
# #     """从指定文件夹中获取所有图片文件"""
# #     image_files = []
# #     for root, dirs, files in os.walk(folder_path):
# #         for file in files:
# #             if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
# #                 file_path = os.path.join(root, file)
# #                 image_files.append(file_path)
# #     return image_files
# #
# # # 示例用法
# # folder_path = 'D:/bannerPic'
# #
# # image_files = get_images_from_folder(folder_path)
# #
# # for image_file in image_files:
# #     try:
# #         with Image.open(image_file) as img:
# #             # 在这里处理图片，例如打印图片信息或显示图片
# #             print(f"Processing image: {image_file}")
# #             # 你可以在这里添加其他的图片处理逻辑
# #     except Exception as e:
# #         print(f"无法处理图片 {image_file}：{e}")
# # url1 = 'http://app.nelko.net/api/user/login'
# # data1 = {
# #     "email": "1508908114@qq.com",
# #     "password": "111111"
# # }
# # header={
# #     "language":"zh",
# #
# # }
# # login = requests.post(url=url1, json=data1,headers=header)
# # login = login.json()
# #
# # accessToken=login['data']['accessToken']
# # print(accessToken)
#
# # def find_longest_substring(s):
# #     s1 = None
# #     strLen = ""
# #     strList=list(s)
# #     for i in strList:
# #        if s1!=i:
# #            s1 = i
# #            strLen = strLen+i
# #        else:
# #            break
# #     return strLen
# #
# #
# #
# # str=input("请输入字符串")
# # a=find_longest_substring(str)
# # print(a)
# # print(len(a))
# # def find_longest_substring(s):
# #     longest = 0  # 最长无重复字符子串的长度
# #     current = 0  # 当前正在检查的无重复字符子串的长度
# #     seen = {}    # 记录字符最后出现的位置
# #     start = 0    # 当前无重复字符子串的起始位置
# #
# #     for i, char in enumerate(s):
# #         if char in seen and seen[char] >= start:
# #             # 如果字符已经出现过，并且在当前正在检查的子串范围内
# #             start = seen[char] + 1  # 更新子串的起始位置为重复字符的下一个位置
# #             current = i - seen[char]  # 更新当前子串的长度
# #         else:
# #             current += 1  # 当前无重复字符子串长度加一
# #             if current > longest:
# #                 longest = current  # 更新最长子串长度
# #
# #         seen[char] = i  # 记录字符最后出现的位置
# #
# #     return longest
# #
# # # 测试示例
# # input_str = input("请输入字符串：")
# # length = find_longest_substring(input_str)
# # print("最长无重复字符子串的长度为：", length)
#
# # def l(l1:list,l2:list):
# #     l1=set(l1)
# #     l2=set(l2)
# #     return l1.intersection(l2)
# # a=l([1,2,3],[2,3,4])
# #
# # print(list(a))
# ############################################################################
# # def average_word_length(text:str):
# #     return text.split(" ")
# # a=input("输入")
# # b=average_word_length(a)
# # count=0
# # le=0
# # for i in b :
# #     le=le+len(i)
# #     count+=1
# # c=int(le/count)
# # print("平均长度",c)
# ###############################################################################
# # def fbnqsl(num:int):
# #     sums=0
# #     for i in range(num):
# #         sums=sums+(num-i)
# #     return sums
# # a=fbnqsl(10)
# # print(a)
# ###############################################################################
# # def count_lines_in_file(file_path: str):
# #     with open(file_path,'r',encoding='utf-8') as f:
# #          filelines=f.readlines()
# #          return len(filelines)
# # num=count_lines_in_file('D:\Android\dqdaaa.txt')
# # print(num)
# ###############################################################################
#
#
# # transposed = [[0] * 3 for _ in range(5)]
# # print(transposed)
# # string.punctuation 是一个字符串，包含了所有的标点符号，如句号、逗号、感叹号等。
# # str.maketrans('', '', string.punctuation) 创建了一个转换表，用于将字符串中标点符号对应的字符映射为空字符，即移除标点符号。
# # text.translate(...) 将 text 中符合转换表规则的字符进行转换或移除，这里就是将文本中的标点符号移除掉。
# # text='asda,iaoshd auhd,qwq'
# # text = text.translate(str.maketrans('', '', string.punctuation))
# # print(text)
# # ###############################################################################
# # def erfenfa(l:list,traget:int):
# #     left,right=0,len(l)-1
# #     count=0
# #     while left<=right:
# #         middle = (left + right) // 2
# #         if l[middle]==traget:
# #             return middle,count
# #         elif l[middle]<traget:
# #             left=middle+1
# #             count+=1
# #         else:
# #             right=middle-1
# #             count += 1
# #     return -1
# # a,b=erfenfa([1,2,3,4,5,6,7,8,9,10,11],10)
# # print(a)
# # print(b)
# #######################################################################################
#
# # // JSON对象
# import json
# # from Crypto.Cipher import AES
# # from Crypto.Util.Padding import pad, unpad
# # from Cry.Random import get_random_bytes
# # import base64
# #
# # # AES加密函数
# # def aes_encrypt(data, key):
# #     cipher = AES.new(key, AES.MODE_CBC)
# #     ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
# #     iv = base64.b64encode(cipher.iv).decode('utf-8')
# #     ct = base64.b64encode(ct_bytes).decode('utf-8')
# #     return iv + ct
# #
# # # 示例用法
# # json_obj = {
# #     "username": "Alice",
# #     "password": "123456",
# #     "balance": 1000
# # }
# #
# # # 使用AES加密，key为密钥（16字节）
# # key = get_random_bytes(16)
# # sensitive_data = json_obj["password"]
# # encrypted_sensitive_data = aes_encrypt(sensitive_data, key)
# import calendar

# def print_calendar(year, month):
#     cal = calendar.month(year, month)
#     print(f"Calendar for {calendar.month_name[month]} {year}:")
#     print(cal)

# 示例用法
# print_calendar(2024, 7)  # 打印2024年7月的日历
# import random
#
# print(random.randint(47, 245))
# a=['XPATH',
#            '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
# b=['XPATH', '//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_edit_editlayout"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView']
# print(a != b)
# import string
#
# a=random.choice(string.)
# print(a)

# devices = {
#     "P20": "",
#     "P21(降本)": "6D:B4:8E:49:43:6D",
#     "P21(GD)": "60:6E:41:8C:8B:30",
#     "P22": "83:80:04:9E:88:38",
#     "P31S": "DC:80:0C:83:9D:C8",
#     "PM220": "00:84:00:00:B7:DD",
#     "PM220S": "31:9D:28:23:32:BE",
#     "PM230": "E4:1A:E9:A1:84:41",
#     "PL70e-BT": "DC:1D:30:54:27:3C"
#     # "PL80W": "",
#     # "PM360": "",
#     # "R11": "",
#
# }
# for key,value in devices.items():
#
#     device = ['XPATH',
#               f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{value}"]']
#     print(device)
