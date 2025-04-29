import glob
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

from Page.BasePage import Action



class Banner(Action):

    def capture_element_screenshot(self, element) -> np.ndarray:
        """
        截取指定元素的屏幕截图，并返回裁剪后的图像。

        :param element: WebElement 对象（需确保元素在屏幕内）。
        :return: 裁剪后的元素截图（NumPy 数组），失败返回 None。
        """
        try:
            # 确保元素在可视区域内
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # 获取全屏截图并转换为 RGB 格式
            screenshot = self.driver.get_screenshot_as_png()
            screenshot = np.frombuffer(screenshot, dtype=np.uint8)
            screenshot = cv2.imdecode(screenshot, cv2.IMREAD_COLOR)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)  # BGR 转 RGB
            print("screenshot:",screenshot)
            # 获取元素位置和大小
            location = element.location
            print("location:",location)
            size = element.size
            print("size:", size)
            # 计算裁剪区域（防止越界）
            y_start = max(0, int(location['y']))
            print(y_start)
            y_end = min(screenshot.shape[0], int(location['y'] + size['height']))
            print(y_end)
            x_start = max(0, int(location['x']))
            print(x_start)
            x_end = min(screenshot.shape[1], int(location['x'] + size['width']))
            print(x_end)
            # 裁剪元素区域
            element_screenshot = screenshot[y_start:y_end, x_start:x_end]
            return element_screenshot

        except Exception as e:
            self.log_error(f"截取元素截图失败: {e}")
            return None

    def compare_images(self, img1: np.ndarray, img2: np.ndarray, threshold: float = 0.95) -> bool:
        """
        比较两张图片的相似度，返回是否一致。

        :param img1: 第一张图片（NumPy 数组）。
        :param img2: 第二张图片（NumPy 数组）。
        :param threshold: 相似度阈值（默认 0.95，即 95% 相似视为一致）。
        :return: True（一致）或 False（不一致）。
        """
        if img1 is None or img2 is None:
            self.log_error("输入图像为空")
            return False

        if img1.shape != img2.shape:
            self.log_error("图像尺寸不一致")
            return False

        try:
            # 转换为灰度图以提高计算效率
            gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

            # 计算结构相似性指数（SSIM）
            similarity, _ = ssim(gray1, gray2, full=True)
            return similarity >= threshold

        except Exception as e:
            self.log_error(f"图片比较失败: {e}")
            return False

    def get_images_from_folder(self, folder_path):
        """从指定文件夹中获取所有图片文件"""
        image_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                    file_path = os.path.join(root, file)
                    image_files.append(file_path)
        return image_files

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
                        self.log_debug(f"Deleted: {image_path}")
                    except Exception as e:
                        self.log_debug(f"Failed to delete {image_path}. Reason: {e}")
        else:
            self.log_error(f"{folder_path}文件夹不存在")

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
