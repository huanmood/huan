from Page import PageiOS
import os
import re
import time
from io import BytesIO

import cv2
import requests
from PIL import Image
from skimage.metrics import structural_similarity as ssim

from Page import PageiOS
from TestCase.share_devices import process_context

class aiPicture:
    def __init__(self, action):
        """
        Connect 页面对象
        :param action: Action 对象，用于操作 App
        """
        self.action = action
        self.driver = action.driver
        self.ios = PageiOS

    def _API_getPictureList(self, devName):
            header = {'language': 'zh-Hans'}

            json_data = {
                'dev': f'{devName}',
                'page': 1,
                'pageSize': 10,
                'sizeIdStrings': ["0"]
            }
            data = requests.post('http://app.labelnize.com/api/templateVip/getSysTmpl2', headers=header, json=json_data)
            return data.json()
    #
    #     # ------------------------- 截图 -------------------------

    def _APP_getPreview(self, devName):
        screenshot_folder = fr'D:\huan-pytest\Print_APP\screenshots\{devName}\{devName}app_getPictureList'
        os.makedirs(screenshot_folder, exist_ok=True)
        self.action.tap_click(self.ios.aiPicture,4)
        elements = self.driver.find_elements(*self.ios.aiPicture_preview)
        process_context.log(f"找到 {len(elements)} 个元素")
        screenshot_png = self.driver.get_screenshot_as_png()
        full_img = Image.open(BytesIO(screenshot_png))
        img_w, img_h = full_img.size
        win_size = self.driver.get_window_size()
        scale_x = img_w / win_size['width']
        scale_y = img_h / win_size['height']

        captured = []
        for idx, el in enumerate(elements, start=1):
            try:
                loc, size = el.location, el.size
                left = int(loc['x'] * scale_x)
                top = int(loc['y'] * scale_y)
                right = int((loc['x'] + size['width']) * scale_x)
                bottom = int((loc['y'] + size['height']) * scale_y)
                left, top = max(0, left), max(0, top)
                right, bottom = min(img_w, right), min(img_h, bottom)
                if right <= left or bottom <= top:
                    process_context.log(f"[{idx}] 坐标异常，跳过")
                    continue

                crop_img = full_img.crop((left, top, right, bottom))
                filename = f"element_{idx}_{int(time.time() * 1000)}.png"
                path = os.path.join(screenshot_folder, filename)
                crop_img.save(path)
                captured.append(path)
                process_context.log(f"[{idx}] 截图成功: {path}")
            except Exception as e:
                process_context.log(f"[{idx}] 异常: {e}")
        return captured

        # ------------------------- 下载接口预览图 -------------------------

    # def download_previews(self, api_data, save_folder):
    #     os.makedirs(save_folder, exist_ok=True)
    #     rows = api_data.get("data", {}).get("rows", [])
    #     saved = []
    #
    #     for idx, row in enumerate(rows, start=1):
    #         url = row.get("preview")
    #         name = row.get("name", f"preview_{idx}").replace(" ", "_")
    #         if not url:
    #             continue
    #
    #         filename = f"{idx}_{name}.png"
    #         path = os.path.join(save_folder, filename)
    #
    #         try:
    #             resp = requests.get(url, timeout=10)
    #             if resp.status_code == 200:
    #                 with open(path, "wb") as f:
    #                     f.write(resp.content)
    #                 print(f"[下载成功] {path}")
    #                 saved.append(path)
    #             else:
    #                 print(f"[下载失败] {url} ({resp.status_code})")
    #         except Exception as e:
    #             print(f"[异常] {url}: {e}")
    #     return saved
    #
    #     # ------------------------- 单张图片比对 -------------------------
    #
    # def compare_images(self, img1_path, img2_path, threshold=0.85):
    #     img1 = cv2.imread(img1_path)
    #     img2 = cv2.imread(img2_path)
    #     if img1 is None or img2 is None:
    #         return 0, False
    #
    #     img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    #     gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #     gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #     gray1 = cv2.GaussianBlur(gray1, (3, 3), 0)
    #     gray2 = cv2.GaussianBlur(gray2, (3, 3), 0)
    #
    #     score, _ = ssim(gray1, gray2, full=True)
    #     return score, score >= threshold
    #
    #     # ------------------------- App截图与API图片比对 -------------------------
    #
    # def compare_app_vs_api(self, api_dir, api_data, app_imgs, threshold=0.85, min_keep_threshold=0.5):
    #     """
    #     对比 App 截图与接口模板图片
    #     threshold: 高匹配阈值（用于打印警告）
    #     min_keep_threshold: 删除阈值（低于此值的图片将保留）
    #     """
    #     api_imgs = self.download_previews(api_data, api_dir)
    #     results = []
    #     to_delete = []  # 延迟删除文件列表
    #     to_keep = []  # 保留文件列表
    #     deleted_count = 0
    #     kept_count = 0
    #
    #     for app_path in app_imgs:
    #         best_score, best_match = 0, None
    #         for api_path in api_imgs:
    #             score, _ = self.compare_images(app_path, api_path, threshold)
    #             if score > best_score:
    #                 best_score, best_match = score, api_path
    #
    #         results.append({
    #             "app_image": app_path,
    #             "best_match": best_match,
    #             "score": best_score
    #         })
    #
    #         print(f"[比对] {os.path.basename(app_path)} → {os.path.basename(best_match)} 相似度={best_score:.3f}")
    #
    #         # 判断是否删除或保留
    #         if best_score >= min_keep_threshold:
    #             to_delete.extend([app_path, best_match])
    #             deleted_count += 2
    #             print(f"✅ [通过] 相似度 {best_score:.3f}，标记删除")
    #         else:
    #             to_keep.extend([app_path, best_match])
    #             kept_count += 2
    #             print(f"⚠ [保留] 相似度 {best_score:.3f}，需人工复查")
    #
    #     # --- 统一删除 ---
    #     for path in to_delete:
    #         try:
    #             if os.path.exists(path):
    #                 os.remove(path)
    #         except Exception as e:
    #             print(f"❌ 删除文件时出错: {e}")
    #
    #     print("\n===== 比对完成 =====")
    #     print(f"✅ 已删除图片数: {deleted_count}")
    #     print(f"⚠ 保留图片数: {kept_count}")
    #
    #     return results
    #
    #     # ------------------------- 整体执行 -------------------------
    #
    def run_compare_app_vs_api(self, devName):
        self._APP_getPreview(devName)
        # api_data = self._API_getSysTmpl2(devName)
        # app_imgs = self._APP_getPreview(devName)
        # api_dir = fr"D:\huan-pytest\Print_APP\screenshots\{devName}jieko_Template"
        #
        # results = self.compare_app_vs_api(api_dir, api_data, app_imgs)
        #
        # print("\n===== 比对结果汇总 =====")
        # for r in results:
        #     print(f"{os.path.basename(r['app_image'])} → {os.path.basename(r['best_match'])} | 相似度={r['score']:.3f}")
        # low_matches = [r for r in results if r['score'] < 0.85]
        # if low_matches:
        #     print("\n⚠ 以下图片相似度较低:")
        #     for r in low_matches:
        #         print(f"  {r['app_image']} => {r['best_match']} ({r['score']:.2f})")
