# import os
# import glob
#
#
#
#
#
# def get_file_count_and_match(package_path, match_pattern=None):
#     # 获取所有文件
#     all_files = []
#     for root, dirs, files in os.walk(package_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             all_files.append(file_path)
#
#     # 如果有匹配条件，则筛选出符合条件的文件
#     if match_pattern:
#         matched_files = [file for file in all_files if match_pattern in file]
#         for file in matched_files:
#             print(os.path.basename(file))
#         print(f"Number of matched files: {len(matched_files)}")
#     else:
#         matched_files = []
#     return [os.path.basename(file) for file in matched_files]
#
# # 使用示例
# pwd = os.path.join(os.getcwd(), 'config')
# print(pwd)
# package_path = pwd  # 替换为包的路径
# match_pattern = 'Android_'  # 替换为你想匹配的文件名（可以是部分文件名或通配符）
# matched_file_names = get_file_count_and_match(package_path, match_pattern)
# print(f"Matched file names: {matched_file_names}")
# import os
# #
# # package_path = os.path.join(os.getcwd(), 'TestCase\TestAndroid')
# # A=os.path.join(package_path, 'index')
# # print(A)
# test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TestCase","TestAndroid")
# print(test_dir)
# import requests
#
# url = f'https//app.nelko.net/api/template/getCategory/P21'
# headers1 = {
#     "language": "zh",
# }
# data = requests.get(url=url, headers=headers1, verify=False)
# data = data.json()['data']
# for i in data:
#     name.append(i['name'])
# if devIndex > 6:
#     self.drag_location(906, 3371, 906, 412)
import asyncio
import json
import threading
import time
from random import random
from xml import etree

import aiofiles
import aiohttp
import requests
import ujson
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from selenium.webdriver.common.by import By

# dev_01=["P21","P31S","PM220","PM220S","PM360","P22"]
# a="P21"
# print(a in dev_01)

# def login(self):
#     def login():
#         self.email = self.base.wait_for_element(self.base.buttonElement.MyPage_email[1])
#         self.email.click()
#         self.email.send_keys(login_data[0])
#         self.password = self.base.wait_for_element(self.base.buttonElement.MyPage_password[1])
#         self.password.click()
#         self.password.send_keys(login_data[1])
#         self.agree = self.base.wait_for_element(self.base.buttonElement.MyPage_agree[1])
#         self.agree.click()
#         self.loginButton = self.base.wait_for_element(self.base.buttonElement.MyPage_loginButton[1])
#         self.loginButton.click()
#
#         # self.base.click(self.base.buttonElement.MyPage_email)
#         # self.base.send_key(self.base.buttonElement.MyPage_email, login_data[0])
#         # self.base.click(self.base.buttonElement.MyPage_password)
#         # self.base.send_key(self.base.buttonElement.MyPage_password, login_data[1])
#         # self.base.click(self.base.buttonElement.MyPage_agree)
#         # self.base.click(self.base.buttonElement.MyPage_loginBtn)
#         time.sleep(2)
#         if self.base.is_element_present(self.base.buttonElement.MyPage_Cloud_sync):
#             self.base.click(self.base.buttonElement.MyPage_open)
#     login_data = getCaps_data("../Data/login.txt")
#     print("login_data::::", login_data)
#     if self.base.is_element_present(self.base.buttonElement.MyPage_email):
#         login()
#         return
#     if self.base.is_element_present(self.base.buttonElement.Homepage_myTemplate):
#         self.base.click(self.base.buttonElement.MyPage_my)
#         time.sleep(1)
#         self.base.click(self.base.buttonElement.MyPage_login)
#         login()
#         time.sleep(1)
#         self.base.click(self.base.buttonElement.Homepage_Homepage)
#         return
# Homepage_connect = (
# By.XPATH, '//android.view.ViewGroup[@resource-id="com.nelko.printer:id/constraint"]/android.widget.LinearLayout[2]')
# print(Homepage_connect[0], Homepage_connect[1])
# import random
# print("gg")
# # print(a)
# import random
# a=['14x40', '40x14', '40x15']
# raNum=random.randint(0,len(a))
# print(raNum)
# import logging
# logger = logging.getLogger('my.logger.namespace')
#
# fh = logging.FileHandler('test.log')  # 可以向文件发送日志
#
# ch = logging.StreamHandler()  # 可以向屏幕发送日志
#
# fm = logging.Formatter('%(asctime)s %(message)s')  # 打印格式
#
# fh.setFormatter(fm)
# ch.setFormatter(fm)
#
# logger.addHandler(fh)
# logger.addHandler(ch)
# logger.setLevel(logging.ERROR)  # 设置级别
#
#
# logger.error('debug 喜喜')
# print('\na')
import logging

# logging.basicConfig(
#     format='%(threadName)s: %(message)s',
#     level=logging.INFO
# )
# logging.info("这是打印内容")
# 为不同线程使用不同颜色
# import threading
#
#
# class ColoredPrinter:
#     def __init__(self):
#         self.local = threading.local()
#         self.colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
#         self.color_index = 0
#         self.lock = threading.Lock()
#
#     def get_color(self):
#         if not hasattr(self.local, 'color'):
#             with self.lock:
#                 self.local.color = self.colors[self.color_index % len(self.colors)]
#                 self.color_index += 1
#         return self.local.color
#
#     def print(self, message):
#         color = self.get_color()
#         reset = '\033[0m'
#         print(f"{color}[Thread-{threading.get_ident()}]: {message}{reset}")
#
#
# # 使用示例
# printer = ColoredPrinter()
#
#
# def worker(printer):
#     printer.print("第一条消息")
#     printer.print("第二条消息")
#
#
# threads = []
# for _ in range(5):
#     t = threading.Thread(target=worker, args=(printer,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
# response=requests.get()
# large_data = [{"id": i} for i in range(100000)]
# print(large_data)
# ujson.dumps(large_data)
# from bs4 import BeautifulSoup
# url='https://admin.nelko.net/resource/systemTempFolder/template'
# header={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
#     'referer':'https://admin.nelko.net/member/tuser',
#     'cookie':'username=test_lsh; rememberMe=true; password=iahmr3dj34Uy3w26cnX5Nv+56whGhr7GYj5MkyG5b69ksa8o4eYNWEeBdttRmM53iMscIgWCZkrlgXw39tlZUA==',
#     'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxNzQ5NzIxOTY0NjM2Mjg2OTc3Iiwicm5TdHIiOiJMdTRsc0x4cnJvUFBPUWxjNkY3NUhTUk5GQzl3T3d6eiIsInVzZXJJZCI6MTc0OTcyMTk2NDYzNjI4Njk3N30.qEviBTtOlgpJtMABi2zykaf8ccmi98SMPcr7OoqhWmQ'
# }
# response=requests.get(url=url,headers=header)
# email_text=BeautifulSoup(response.text,'lxml')
# print(email_text)
#
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://admin.nelko.net/member/tuser")
# 获取页面内容（即使需要登录，可能看到部分 HTML）
# print(driver.page_source)
# driver.quit()
# from bs4 import BeautifulSoup
#
# # 从字符串创建
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" id="test"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <div><a href="http://example.com/tillie" class="sister" id="link3">Tillie</a></div>;
# <div><a>aaa</a></div>
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc, 'lxml')  # 使用lxml解析器
# divs = soup.find_all('div')        # 获取所有的div标签
# for div in divs:                   # 循环遍历div中的每一个div
#     a = div.find_all('a')[0]      # 查找div标签中的第一个a标签
#     print(a.string)              # 输出a标签中的内容
#
# # 如果结果没有正确显示，可以转换为list列表
# # ?

# import requests
# from bs4 import BeautifulSoup
#
# url = "https://movie.douban.com/top250"
# headers = {"User-Agent": "Mozilla/5.0"}
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
#
# movies = []
# for item in soup.find_all("div", class_="item"):
#     print(item)
#     title = item.find("span", class_="title").text
#     rating = item.find("span", class_="rating_num").text
#
#     comment_num = item.find("div",class_='bd').find_all("span")[-2].text.replace('人评价','')
#     movies.append({"title": title, "rating": rating, "comment_num": comment_num})
#
# print(movies[:3])  # 输出前3条数据
#

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from common.GlobalValue import GlobalVar
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com")
# cookies=driver.get_cookies()
# print(cookies)
# GlobalVar().set_value('cookies',cookies)
# # 输入关键词并搜索
# search_box = driver.find_element(By.ID, "key")
# search_box.send_keys("Python编程")
# search_box.send_keys(Keys.ENTER)
#
# # 等待加载并解析数据
# driver.implicitly_wait(10)  # 隐式等待
# prices = driver.find_elements(By.CSS_SELECTOR, ".p-price strong")
# for price in prices[:5]:
#     print(price.text)
# driver.quit()
#
# 下载单个ts文件
# async def download_one(url):
#    print("正在下载:"+url)
#    # 重试10次 防止下载失败
#    for i in range(10):
#        try:
#            file_name=url.split("/")[-1]
#            async with aiohttp.ClientSession() as session:
#                async with session.get(url) as resp:
#                    content=await  resp.content.read()
#                    async with aiofiles.open(f"./TsFiles/{file_name}",mode="wb") as f:
#                        await f.write(content)
#            break
#        except:
#            print("下载失败:"+url)
#            await asyncio.sleep((i+1)*5)
#
#
#
# async def download_all_ts():
#    # 准备好任务列表
#    tasks=[]
#    # 读取m3u8文件
#    with open("m3u8.txt",mode="r",encoding="utf-8") as f:
#        for line in f:
#            # 排除所有#开头的
#            if line.startswith("#"):
#                continue
#            line=line.strip()
#            task=asyncio.create_task(download_one(line))
#            tasks.append(task)
#
#    # 等待任务全部结束
#    await asyncio.wait(tasks)
#
# def getfirstM3u8Url():
#     url='https://www.dandantu.cc/vodplay/73688-1-1.html'
#     response=requests.get(url)
#     response.encoding='utf-8'
#     tree = BeautifulSoup(response.text,"html.parser")
#     print(tree)
# # 解析出url
# script_content = tree.xpath('//script[contains(text(), "player_aaaa")]/text()')[0]
#
# # 我们需要从脚本中提取JSON部分
# json_str = script_content[script_content.find('{'):script_content.rfind('}') + 1]
#
# # 解析JSON字符串
# data = json.loads(json_str)
#
# # 提取URL值
# url_value = data.get("url", "")
#
# print(url_value)

# getfirstM3u8Url()
# import aiohttp
# import aiofiles
# import asyncio
#
# # getm3u8=requests.get('https://vip.ffzy-online6.com/20240202/25627_f9c6348c/2000k/hls/mixed.m3u8')
# # getm3u8.encoding='utf-8'
# # with open("m3u8.txt", mode="w", encoding="utf-8") as f:
# #     f.write(getm3u8.text)
#
# # 下载单个ts文件
# async def download_one(url):
#    print("正在下载:"+url)
#    # 重试10次 防止下载失败
#    for i in range(10):
#        try:
#            file_name=url.split("/")[-1]
#            async with aiohttp.ClientSession() as session:
#                async with session.get(url) as resp:
#                    content=await  resp.content.read()
#                    async with aiofiles.open(f"./TsFiles/{file_name}",mode="wb") as f:
#                        await f.write(content)
#            break
#        except:
#            print("下载失败:"+url)
#            await asyncio.sleep((i+1)*5)
#
#
#
# async def download_all_ts():
#    # 准备好任务列表
#    tasks=[]
#    # 读取m3u8文件
#    with open("m3u8.txt",mode="r",encoding="utf-8") as f:
#        for line in f:
#            # 排除所有#开头的
#            if line.startswith("#"):
#                continue
#            line=line.strip()
#            line = 'https://vip.ffzy-online6.com/20240202/25627_f9c6348c/' + line
#            task=asyncio.create_task(download_one(line))
#            tasks.append(task)
#
#    # 等待任务全部结束
#    await asyncio.wait(tasks)
#
# if __name__ == "__main__":
#     asyncio.run(download_all_ts())
# from selenium import webdriver
#
# driver=webdriver.Chrome()#将options传入到webdriver中
# driver.get('www.baidu.com')
# time.sleep(2)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from common.GlobalValue import GlobalVar
# from selenium.webdriver.chrome.options import Options
# options = Options()  # 先声明一个options变量
# options.add_argument("--disable-blink-features=AutomationControlled") # 隐藏自动化控制标头
# options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 隐藏自动化标头
# options.add_argument('--ignore-ssl-errosr')  # 忽略ssl错误
# options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.jd.com")
# # time.sleep(3)
# import json
#
# # 这里假设我们已经有一个设定好的webdriver
# cookies = driver.get_cookies()
# with open('cookies.json', 'w')as cookies:  # 将当前页面的cookie保存到本地json文件中
#     json.dump(cookies)
# def fun(args,*arg,**kwargs):
#     print(args)
#     print(arg)
#     print(kwargs)
# fun(1,2,1,2,3,a=4)
# import requests
# from bs4 import BeautifulSoup
#
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
#     'Cookies':'NMTID=00OgN_K88jFNaCEHUmQsXIqWW9LVXIAAAGWzJCQRA; JSESSIONID-WYYY=s%2BRYkeMhPewOVnZ7Chyg1raj45DVxytwMwl8E1q%5CVhiIR5T%2Bwt8wjn6Z8Igy1Y1g7%2FS8xa9hhd8w6UEh6OjmAIbkU9V36RrGSpsXgdnrnkMA8qG%2Bw%2FskGVfpXVtuBn%5C7%2BwnKyJ8fHSeRh5Nd%2BBiKWSrRM7e1WCCgAKnzyxsToHGUV%5Cjs%3A1747190548475; _iuqxldmzr_=32; _ntes_nnid=a1dd91386c5be3ccd86cf553e20e6f04,1747188748490; _ntes_nuid=a1dd91386c5be3ccd86cf553e20e6f04; WEVNSM=1.0.0; WNMCID=tyhrkg.1747188748677.01.0; WM_NI=QNz6EcM5rvyXhXXDXJZ%2BZbKEta1empwlM5FawLV6oXDSbi9%2Fv0PXPxg%2F4es0ZqGYp%2BNCa5x0tUt5DO3MB%2Bo0insPd3Olt54TIzOr%2FhIelWSDc4WSaz72yYKNp8rLCKawVm8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2ed43a9a9b788e24d93b88eb6c14b868b8bb0db41a798ff98b45d95babc84d72af0fea7c3b92a9392b6d7c8698febbe97fc54ac8898a5db429af59683ca4fb8bfff86f07cb5b483d6c56bb5949ad7ee54888dae8abc25b6f0a0b9d374a5f1fc86f23c9aaf89baf3218e9dafd6fb3cb88bbcd6c745f1938eccee3cabb2bdb1e7398db4bcd6b7608ba68193ae648bbba4b8d250a1ec99b4e472f5eeb7baca46b4e8beadc241a3a99a8ebb37e2a3; WM_TID=82%2FyZ5nzBIdAFAUUERKCaLXk00XXKoMC; sDeviceId=YD-4tkMvlX5pelBU1QQEBaGLOS0x1XSxNZ5; ntes_utid=tid._.ft7k3XfqIjNBEgABQQeHbfGx0xCW1cJo._.0; __snaker__id=pSnXBDRH33B7tGEn; gdxidpyhxdE=2D59oBRs5bsdJv%5CpTHN0yB8or4CjdDaDUTEuglb5yStbzOjl3Wbb5YtszWbTZvRD%2FWBTm805iroHMT0Il81b6AxBw%2BWaNhCP9AuQYrAoV3gVLnbkS3OqB0GBCkQ8lqvsxRR5Y3w%5CdkC0gNv5obLbv5TeuOXtznEkIfVU%2FqMr0x9U5vQD%3A1747189824258; MUSIC_U=007964EA8B68F441DA3C0316532F206D92511F1A98E9770B392D041F8385657BACC235B12E35E48775592454D15A0C2BB2A82835DE724EC3590D9E2B60610BEB336FD34E98CA5C4D14F4572803314DADDB618F667601018A8B8BA27DF7257C72E87C1CA0B6D75F8ADB7C6C406266E84AC1E4063B3138F3F2DE5420F467410B68F67F1800CF24DB1F103A073256E94494FBE19F8AC29614D4136E329682682E4A74868CEAE33A20CB8222D5EA6EBEB68D170699DF01D92B06A30907CA5C382EA5DE16FD746D5C9BA86B4B108EA1E5F15D63192F44005B39695E7D652F0798245CA23968FB4B3EC75F71D4C47754C590D60E8662651FFE6F490755414BA95A28C7C6D921204C51154A45247178B2352913840B246F87351CEB6BF429CCC8658A7C17DEC413073859793BFDDAFAF688190055CA8448C59CD8ABE2E6693C4CBD49354298636CF140486F24D34CF366B23D1E9906D066476636102D20A4B32BFF317881; __csrf=535863bd8aba28341894ccc9f18db3f2; ntes_kaola_ad=1'
# }
# url = 'https://music.163.com/discover/toplist?id=3778678'
# response = requests.get(url=url, headers=header)
# # print(response.text)
# host = url.split('/d')[0]
# soup = BeautifulSoup(response.text, 'lxml')
# name_list=soup.select('ul.f-hide > li > a')
# url_list=[]
# for i in name_list:
#     id=i.get('href')
#     url=host+id
#     name=i.string
#     url_name=[url,name]
#     url_list.append(url_name)
# for i in url_list:print(i)
# response=requests.get(url=i[0],headers=header)
# with open('screenshots'+i[1]+'mp3','wb') as f:
#     f.write(response.content)

# text_list=[i.get('href') for i in text.find_all('a', class_='left-title_q9Hgi')]
#
# for i in text_list:
#         url ='http://'+ host  + i
#         print(url)
#         content=requests.get(url)
#         content=BeautifulSoup(content.text,'lxml')
#         content=[i.get_text(strip=True)  for i in content.find_all('div',class_='c-single-text-ellipsis')]
#         print(content)
#         print("************************************************************")


# 导入了必要的模块requests和os
# import requests
# import os
#
#
# # 定义了一个函数get_html(url)，
# # 用于发送GET请求获取指定URL的响应数据。函数中设置了请求头部信息，
# # 以模拟浏览器的请求。函数返回响应数据的JSON格式内容
# def get_html(url):
#         header = {
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#         }
#         response = requests.get(url=url, headers=header)
#         # print(response.json())
#         html = response.json()
#         return html
#
#
# # 定义了一个函数parse_html(html)，
# # 用于解析响应数据中的图片信息。通过分析响应数据的结构，
# # 提取出每个图片的URL和标题，并将其存储在一个字典中，然后将所有字典组成的列表返回
# def parse_html(html):
#         rl_list = html['data']['rl']
#         # print(rl_list)
#         img_info_list = []
#         for rl in rl_list:
#                 img_info = {}
#                 img_info['img_url'] = rl['rs1']
#                 img_info['title'] = rl['nn']
#                 # print(img_url)
#                 # exit()
#                 img_info_list.append(img_info)
#         # print(img_info_list)
#         return img_info_list
#
#
# # 定义了一个函数save_to_images(img_info_list)，用于保存图片到本地。
# # 首先创建一个目录"directory"，如果目录不存在的话。然后遍历图片信息列表，
# # 依次下载每个图片并保存到目录中，图片的文件名为标题加上".jpg"后缀。
# def save_to_images(img_info_list):
#         dir_path = 'directory'
#         if not os.path.exists(dir_path):
#                 os.makedirs(dir_path)
#         for img_info in img_info_list:
#                 img_path = os.path.join(dir_path, img_info['title'] + '.jpg')
#                 res = requests.get(img_info['img_url'])
#                 res_img = res.content
#                 with open(img_path, 'wb') as f:
#                         f.write(res_img)
#                 # exit()
#
#
# # 在主程序中，设置了要爬取的URL，并调用前面定义的函数来执行爬取、解析和保存操作。
# if __name__ == '__main__':
#         url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'
#         html = get_html(url)
#         img_info_list = parse_html(html)
#         save_to_images(img_info_list)
# import os
# import requests
# from lxml import etree
# import string
# # 创建保存简历的文件夹
# folder_name = 'resumes'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
# }
# url = 'https://sc.chinaz.com/jianli/free.html'
#
# try:
#     response = requests.get(url=url, headers=header)
#     response.encoding = 'utf-8'
#     tree = etree.HTML(response.text)
#     img_elements = tree.xpath('//*[@id="container"]/div/a')
#
#     for element in img_elements:
#         try:
#             # 获取图片src并处理成下载URL
#             img_src = str(element.xpath('./img/@src')[0]).split('c/')[1].split('_s')[0]
#             host = 'https://downsc.chinaz.net/Files/DownLoad/'
#             download_url = host + img_src + '.rar'
#
#             # 获取文件名并清理非法字符
#             img_name = element.xpath('./img/@alt')[0]
#
#             # 构建保存路径
#             file_path = os.path.join(folder_name, f"{img_name}.rar")
#
#             # 下载文件
#             print(f"正在下载: {img_name}")
#             response = requests.get(download_url, stream=True)
#
#             # 检查请求是否成功
#             if response.status_code == 200:
#                 with open(file_path, 'wb') as f:
#                     for chunk in response.iter_content(1024):
#                         f.write(chunk)
#                 print(f"成功保存: {file_path}")
#             else:
#                 print(f"下载失败，HTTP状态码: {response.status_code}")
#
#         except Exception as e:
#             print(f"处理元素时出错: {str(e)}")
#             continue
#
# except Exception as e:
#     print(f"程序出错: {str(e)}")
# from hashlib import md5
# a='sadwqq'
# m=md5()
# m.update(a.encode('utf-8'))
# nonce=m.hexdigest()
# print(nonce)

# print(ord('香'))


# import urllib.parse
# s='http://120.196.217.78:8484/swagger-ui.html?urls.primaryName=用户'
# print(urllib.parse.urlencode())

# from multiprocessing import Pool
#
# def add(x, y):
#     return x + y
#
# if __name__ == "__main__":
#     with Pool(processes=2) as pool:  # 使用2个进程
#         # 同步执行（自动阻塞等待）
#         results = pool.starmap(add, [(1, 2), (3, 4), (5, 6)])
#         print(results)  # 输出 [3, 7, 11]
#
#         # 对比异步版本（需手动调用 get()）
#         async_results = pool.starmap_async(add, [(10, 20), (30, 40)])
#         print(async_results.get())  # 输出 [30, 70]

from PIL import Image, ImageDraw
import numpy as np

from common.DB_utils import get_redis_conn

# 配置参数
# from PIL import Image, ImageDraw
# import re
#
#
# def hex_file_to_image(file_path, output_path="output.png", cell_size=20, scale=2):
#     """
#     将十六进制文件转换为点阵图像
#
#     参数:
#         file_path: 十六进制数据文件路径
#         output_path: 输出图像保存路径 (默认: output.png)
#         cell_size: 每个点的像素大小 (默认: 20x20)
#         scale: 最终图像缩放比例 (默认: 2倍)
#     """
#     # 读取并清理十六进制数据
#     with open(file_path, 'r') as file:
#         hex_data = re.sub(r'[^0-9A-Fa-f]', '', file.read())
#
#     # 将十六进制转换为二进制字符串
#     binary_str = bin(int(hex_data, 16))[2:].zfill(len(hex_data) * 4)
#
#     # 按每行80位分割数据
#     bits_per_row = 800
#     rows = [binary_str[i:i + bits_per_row] for i in range(0, len(binary_str), bits_per_row)]
#
#     # 最后一行补位处理
#     if len(rows[-1]) < bits_per_row:
#         rows[-1] = rows[-1] + '1' * (bits_per_row - len(rows[-1]))
#
#     # 创建图像
#     img_width = bits_per_row * cell_size
#     img_height = len(rows) * cell_size
#     img = Image.new("RGB", (img_width, img_height), "white")
#     draw = ImageDraw.Draw(img)
#
#     # 绘制每个点
#     for row_idx, row in enumerate(rows):
#         for col_idx, bit in enumerate(row):
#             x1 = col_idx * cell_size
#             y1 = row_idx * cell_size
#             x2 = x1 + cell_size
#             y2 = y1 + cell_size
#
#             # 0=黑色（打印），1=白色（不打印）
#             fill_color = "black" if bit == "0" else "white"
#             draw.rectangle([x1, y1, x2, y2], fill=fill_color, outline="black")
#
#     # 放大图像
#     if scale > 1:
#         img = img.resize((img_width * scale, img_height * scale), Image.NEAREST)
#
#     img.save(output_path)
#     return output_path
#
#
# # 使用示例
# if __name__ == "__main__":
#     input_file = r"C:\Users\YZY\Desktop\新建文本文档 (2)(已除冗余内容).txt"  # 替换为您的文件路径
#     output_image = hex_file_to_image(input_file)
#     print(f"图像已生成: {output_image}")
# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# ws.append(["姓名", "年龄", "城市"])
# ws.append(["张三", 25, "北京"])
# ws.append(["李四", 30, "上海"])
# wb.save("demo.xlsx")
#
# from common.DB_utils import get_redis_conn
# a=get_redis_conn()
# b=a.lrange('Template',0,-1)
# for i in b:
#     print(i.decode())

# a.close()
# a=set()
# a.add("1")
# a.add("2")
# a.add("3")
# b=set()
# b.add("2")
# b.add("1")
# print(a)
# print(b)
# print(a-b)
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# class login_api:
#     def get_token(self):
#         data = {
#             "password": "111111",
#             "email": "1508908114@qq.com"
#         }
#         header={
#             "User-Agent":"Nelko/4.1.0 (com.nelko.printer; build:436; iOS 18.5.0) Alamofire/5.10.2",
#             "language":"zh-Hans"
#         }
#         return requests.post("https://app.nelko.net/api/user/login", json=data,headers=header,verify=False).json()['data']['accessToken']
# a=login_api()
# print(a.get_token())
requests.packages.urllib3.disable_warnings()
# url='https://admin.nelko.net/prod-api/system/dict/data/list?pageNum=1&pageSize=10&dictType=model_index_show'
# header={
#     'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxNzQ5NzIxOTY0NjM2Mjg2OTc3Iiwicm5TdHIiOiJycWhLSzVudURFME14bGRuYUNsMXdUWnZwb09UNGVqNSIsInVzZXJJZCI6MTc0OTcyMTk2NDYzNjI4Njk3N30.mesDoGSA9ra5UpN8vYukxPkHvD9aaoKjTKbM70JbydI'
# }
# resp=requests.get(url,headers=header,verify=False)
# print(resp.text)
# resp=resp.json().get('data','')
# for i in resp:
#     data=i['deviceName']
#     print(data)


# session=requests.session()
# session.get('https://admin.nelko.net/index',headers=header)


# url1 = 'https://admin.nelko.net/prod-api/system/dict/data/list?pageNum=1&pageSize=10&dictType=model_index_show'
# header1 = {
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxNzQ5NzIxOTY0NjM2Mjg2OTc3Iiwicm5TdHIiOiJycWhLSzVudURFME14bGRuYUNsMXdUWnZwb09UNGVqNSIsInVzZXJJZCI6MTc0OTcyMTk2NDYzNjI4Njk3N30.mesDoGSA9ra5UpN8vYukxPkHvD9aaoKjTKbM70JbydI'
# }
# resp1 = requests.get(url1, headers=header1).json()['rows']
# print(resp1)
dev = []
url = 'http://app.nelko.net/api/templateVip/getDeviceList'
resp = requests.get(url).json().get('data', [])
for i in resp:
    index_show_values = i['indexShow'].split(',')
    print(index_show_values)
    for j in index_show_values:
        if j == '0':
            dev.append(i['deviceName'])

print(dev)