import glob
import hashlib
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.wait import WebDriverWait
import requests

import unittest


from Page.PageAndroid.Banner import Banner
from common.logger import Log

app_banner = r'D:\test\Print_APP\screenshots\app_banner'

jieko_banner = r'D:\test\Print_APP\screenshots\jieko_banner'


class BannerTest(unittest.TestCase):
    base = None
    log=Log()

    def setUp(self):

        self.base = Banner()  # 实例化Base对象
        self.base.firstDownload_open()
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
        url2 = 'http://app.labelnize.com/api/banner/list'
        data2 = {
            "dev": "P21",
            "position": 2
        }
        header2 = {
            "accessToken": accessToken,
            "language": language
        }
        response = requests.post(url=url2, json=data2, headers=header2)
        data = response.json()
        for i in range(len(data['data'])):
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
                    self.log.debug(f"保存接口返回的第{i+1}个图片")
        self.log.debug(f"一共{len(data['data'])}张图片")

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
        wait = WebDriverWait(self.base.driver, 5)
        while len(saved_hashes) < 5:  #
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
                    self.log.debug("图片已经被保存过，跳过。")
                    continue

                # 将哈希值添加到集合中，表示已经保存过
                saved_hashes.add(banner_hash)

                # 保存每次截图到本地
                timestamp = int(time.time())
                image_path = os.path.join(screenshot_folder, f"banner_{timestamp}.png")

                # 保存图片并确保成功
                banner_image.save(image_path)
                if os.path.exists(image_path):
                    self.log.debug(f"成功保存截图到：{image_path}")
                else:
                    self.log.debug(f"保存截图失败：{image_path}")

                # 等待一段时间以确保文件系统有时间处理保存操作
                time.sleep(2)

            except Exception as e:
                self.log.debug(f"捕获到异常：{e}")
                pass

        self.log.debug(f"共截取并保存了 {len(saved_hashes)} 张唯一的banner截图。")

    def resize_image(self, img, width=None, height=None):
        if width is not None and height is not None:
            return cv2.resize(img, (width, height))
        elif width is not None:
            h, w = img.shape[:2]
            new_height = int(h * (width / w))
            return cv2.resize(img, (width, new_height))
        elif height is not None:
            h, w = img.shape[:2]
            new_width = int(w * (height / h))
            return cv2.resize(img, (new_width, height))
        else:
            return img

    def images_are_similar(self, img1_path, img2_path, threshold=0.2):

        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)

        # 调整图片尺寸
        img2_resized = self.resize_image(img2, width=img1.shape[1], height=img1.shape[0])

        # 计算两个图像之间的差异
        diff = cv2.absdiff(img1, img2_resized)

        # 将差异矩阵转换为灰度图像
        gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # 计算差异的平均值
        mean_diff = np.mean(gray_diff)

        # 设定阈值，判断平均差异是否在可接受范围内
        similarity = 1 - mean_diff / 255.0
        return similarity >= threshold

    def test_03_getPicList(self):
        image_files1 = self.base.get_images_from_folder(app_banner)
        image_files2 = self.base.get_images_from_folder(jieko_banner)
        for image_file1 in image_files1:
            for image_file2 in image_files2:
                if self.images_are_similar(image_file1, image_file2, threshold=0.95):
                    self.log.debug("APP保存的图片与接口返回的图片有95%以上相似，无需手动确认")
                else:
                    self.log.debug("APP保存的图片与接口返回的图片不相似，需要手动确认")
        time.sleep(1)
        self.clear_images_in_folder(app_banner)
        self.clear_images_in_folder(jieko_banner)

    def clear_images_in_folder(self, folder_path):
        # 支持的图片文件扩展名
        image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

        # 检查文件夹是否存在
        if os.path.exists(folder_path):
            # 遍历所有支持的图片文件
            for ext in image_extensions:
                # 使用 glob 匹配文件夹中的所有图片文件
                for image_path in glob.glob(os.path.join(folder_path, ext)):
                    try:
                        # 删除图片文件
                        os.remove(image_path)
                        print(f"Deleted: {image_path}")
                    except Exception as e:
                        print(f"Failed to delete {image_path}. Reason: {e}")
        else:
            self.log.debug(f"The folder {folder_path} does not exist.")
    def tearDown(self):
        pass