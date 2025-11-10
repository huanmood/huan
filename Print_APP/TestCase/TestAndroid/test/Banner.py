import hashlib
import os
import threading
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.wait import WebDriverWait
import requests
import unittest
from Page.PageAndroid.Banner import Banner
from TestCase.share_devices import process_context
from common.DB_utils import get_redis_conn

app_banner = r'D:\huan\Print_APP\screenshots\app_banner'
jieko_banner = r'D:\huan\Print_APP\screenshots\jieko_banner'

requests.packages.urllib3.disable_warnings()


class Test_Banner(unittest.TestCase):
    base = None

    # global_var = GlobalVar()

    @classmethod
    def setUpClass(cls):
        # cls.mysql = get_mysql_conn()
        cls.redis = get_redis_conn()
        cls.base = Banner()  # 实例化Base对象

    def jiekoPic(self):
        jieko_banner_img = []
        # 先判断redis有没有数据，如果没有就请求获取
        if not self.redis.exists("jieko_banner_img"):
            url = 'http://app.nelko.net/api/banner/list'
            data = {
                "dev": "P21",
                "position": 1
            }

            response = requests.post(url=url, json=data, verify=False)
            response_data = response.json()

            if response_data.get('ret') != 200:
                self.fail(f"API请求失败: {response_data}")
            banners = response_data.get('data', [])  # 如果获取不到数据就返回一个空列表
            for banner in banners:
                img_url = banner.get('image')
                if img_url:
                    jieko_banner_img.append(img_url)
                    self.redis.rpush('jieko_banner_img', img_url)  # 使用rpush保持顺序 右放左拿lrang
            if banners:  # 确保列表非空
                self.redis.expire("jieko_banner_img", 3000)
        # 从Redis获取所有图片URL，注意编码，直接拿是一个字节内容，需要编码
        image_urls = [url.decode('utf-8') if isinstance(url, bytes) else url
                      for url in self.redis.lrange('jieko_banner_img', 0, -1)]
        # 确保保存目录存在
        os.makedirs(jieko_banner, exist_ok=True)
        # 下载并保存图片
        success_count = 0
        for i, url in enumerate(image_urls, 1):
            try:
                response = requests.get(url, stream=True, verify=False)
                response.raise_for_status()
                file_name = os.path.basename(url)
                save_path = os.path.join(jieko_banner, file_name)

                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)

                self.base.log(f"成功保存第{i}张图片: {file_name}")
                success_count += 1
            except Exception as e:
                self.base.log(f"下载第{i}张图片失败: {str(e)}")

        self.base.log(f"图片处理完成，共尝试下载{len(image_urls)}张，成功{success_count}张")
        self.assertGreater(success_count, 0, "至少应该成功下载一张图片")

    def banner(self):
        # 定位到banner图片的元素

        banner_element = self.base.find_element(
            (
            By.XPATH, '    //androidx.viewpager.widget.ViewPager[@resource-id="com.nelko.printer:id/viewpager_inner"]'))
        # 创建一个空集合来存储已经保存过的图片的哈希值
        saved_hashes = set()
        # 创建保存截图的目录
        screenshot_folder = app_banner
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        wait = WebDriverWait(self.base.driver, 25)
        while len(saved_hashes) < self.redis.llen("jieko_banner_img"):  #
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

    def test_02_getPicList(self):
        confirmNum = 0
        image_files1 = self.base.get_images_from_folder(app_banner)
        image_files2 = self.base.get_images_from_folder(jieko_banner)
        for image_file1 in image_files1:
            for image_file2 in image_files2:
                if self.base.images_are_similar(image_file1, image_file2, threshold=0.95):
                    process_context.log("APP保存的图片与接口返回的图片有95%以上相似，无需手动确认")
                    confirmNum += 1
        if confirmNum == self.redis.llen('jieko_banner_img'):
            self.base.clear_images_in_folder(app_banner)
            self.base.clear_images_in_folder(jieko_banner)
        if confirmNum < self.redis.llen('jieko_banner_img'):
            self.base.log(f"APP保存的图片与接口返回的图片存在不相似，需要手动确认")

    def run_in_thread(self, target_func, name):
        t = threading.Thread(target=target_func, name=name)
        t.start()
        return t

    def test_01_parallel(self):
        """同时运行 test_01_jiekoPic 和 test_02_banner 的逻辑"""

        # 把方法体封装到函数中
        def jieko_logic():
            self.jiekoPic()

        def banner_logic():
            self.banner()

        # 启动两个线程
        t1 = self.run_in_thread(jieko_logic, "JiekoThread")
        t2 = self.run_in_thread(banner_logic, "BannerThread")

        # 等待两个线程执行完
        t1.join()
        t2.join()

    @classmethod
    def tearDownClass(cls):
        cls.redis.close()
