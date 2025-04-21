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
            # 获取元素位置和大小
            location = element.location
            size = element.size
            # 计算裁剪区域（防止越界）
            y_start = max(0, int(location['y']))
            y_end = min(screenshot.shape[0], int(location['y'] + size['height']))
            x_start = max(0, int(location['x']))
            x_end = min(screenshot.shape[1], int(location['x'] + size['width']))

            # 裁剪元素区域
            element_screenshot = screenshot[y_start:y_end, x_start:x_end]
            return element_screenshot

        except Exception as e:
            print(f"截取元素截图失败: {e}")
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
            print("输入图像为空")
            return False

        if img1.shape != img2.shape:
            print("图像尺寸不一致")
            return False

        try:
            # 转换为灰度图以提高计算效率
            gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

            # 计算结构相似性指数（SSIM）
            similarity, _ = ssim(gray1, gray2, full=True)
            return similarity >= threshold

        except Exception as e:
            print(f"图片比较失败: {e}")
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
