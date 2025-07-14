import hashlib
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.wait import WebDriverWait
import requests
import unittest
from Page.PageAndroid.Banner import Banner
from common.GlobalValue import GlobalVar
from TestCase.TestAndroid.share_devices import process_context
app_banner = r'D:\huan\Print_APP\screenshots\app_banner'
jieko_banner = r'D:\huan\Print_APP\screenshots\jieko_banner'


class BannerTest(unittest.TestCase):
    base = None

    global_var = GlobalVar()

    @classmethod
    def setUpClass(cls):
        cls.base = Banner()  # 实例化Base对象

    def test_01_jiekoPic(self):
        # 保存接口返回image到文件夹
        # 发送请求获取图片
        url1 = 'http://app.nelko.net/api/user/login'
        data1 = {
            "email": "1508908114@qq.com",
            "password": "111111"
        }
        headers1 = {
            "language": "zh",
        }
        login = requests.post(url=url1, json=data1, headers=headers1)
        login = login.json()
        accessToken = login['data']['accessToken']
        language = login['data']['language']
        url2 = 'http://app.nelko.net/api/banner/list'
        data2 = {
            "dev": "P21",
            "position": 1
        }
        header2 = {
            "accessToken": accessToken,
            "language": language
        }
        response = requests.post(url=url2, json=data2, headers=header2)
        data = response.json()
        data_len = len(data['data'])
        self.global_var.set_value("banner_Len", data_len)
        for i in range(data_len):
            imageUrl = data['data'][i]['image']
            image_response = requests.get(imageUrl)
            if image_response.status_code == 200:
                file_name = os.path.basename(imageUrl)
                bannerPicPath = jieko_banner
                if not os.path.exists(bannerPicPath):
                    os.makedirs(bannerPicPath)
                save_path = os.path.join(bannerPicPath, file_name)
                with open(save_path, 'wb') as file:
                    # 将响应内容写入文件
                    file.write(image_response.content)
                    process_context.log(f"保存接口返回的第{i + 1}个图片")
        self.base.log(f"一共{len(data['data'])}张图片")

    def test_02_banner(self):
        # 定位到banner图片的元素
        banner_element = self.base.find_element(
            (By.XPATH, '//androidx.viewpager.widget.ViewPager[@resource-id="com.nelko.printer:id/viewpager_inner"]'))
        # 创建一个空集合来存储已经保存过的图片的哈希值
        saved_hashes = set()
        # 创建保存截图的目录
        screenshot_folder = app_banner
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        wait = WebDriverWait(self.base.driver, 25)
        while len(saved_hashes) < self.global_var.get_value("banner_Len"):  #
            try:
                wait.until(EC.presence_of_element_located((By.XPATH,
                                                           '//androidx.viewpager.widget.ViewPager[@resource-id="com.nelko.printer:id/viewpager_inner"]')))
                # 等待轮播到下一张图片
                # 获取屏幕截图并加载到内存
                screenshot = self.base.driver.get_screenshot_as_png()
                # 获取元素的位置信息
                location = banner_element.location
                size = banner_element.size
                # 打开截图并裁剪到banner图片的区域
                image = Image.open(BytesIO(screenshot))
                left = location['x']
                top = location['y']
                right = location['x'] + size['width']
                bottom = location['y'] + size['height']
                banner_image = image.crop((left, top, right, bottom))

                # 将裁剪后的图片转换为字节流
                buffer = BytesIO()
                banner_image.save(buffer, format="PNG")
                banner_image_bytes = buffer.getvalue()

                # 计算裁剪后图片的哈希值
                banner_hash = hashlib.md5(banner_image_bytes).hexdigest()

                # 检查哈希值是否已经存在于集合中
                if banner_hash in saved_hashes:
                    process_context.log("图片已经被保存过，跳过。")
                    continue

                # 将哈希值添加到集合中，表示已经保存过
                saved_hashes.add(banner_hash)

                # 保存每次截图到本地
                timestamp = int(time.time())
                image_path = os.path.join(screenshot_folder, f"banner_{timestamp}.png")

                # 保存图片并确保成功
                banner_image.save(image_path)
                if os.path.exists(image_path):
                    process_context.log(f"成功保存截图到：{image_path}")
                else:
                    process_context.log(f"保存截图失败：{image_path}")

                # 等待一段时间以确保文件系统有时间处理保存操作
                time.sleep(2)

            except Exception as e:
                self.base.log(f"捕获到异常：{e}")
                pass

        self.base.log(f"共截取并保存了 {len(saved_hashes)} 张唯一的banner截图。")

    def test_03_getPicList(self):
        confirmNum = 0
        image_files1 = self.base.get_images_from_folder(app_banner)
        image_files2 = self.base.get_images_from_folder(jieko_banner)
        for image_file1 in image_files1:
            for image_file2 in image_files2:
                if self.base.images_are_similar(image_file1, image_file2, threshold=0.95):
                    process_context.log("APP保存的图片与接口返回的图片有95%以上相似，无需手动确认")
                    confirmNum += 1
        if confirmNum == self.global_var.get_value("banner_Len"):
            self.base.clear_images_in_folder(app_banner)
            self.base.clear_images_in_folder(jieko_banner)
        if confirmNum < self.global_var.get_value("banner_Len"):
            self.base.log(f"APP保存的图片与接口返回的图片存在不相似，需要手动确认")

    @classmethod
    def tearDownClass(cls):
        pass
