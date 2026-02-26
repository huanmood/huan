import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # ✅ 修正这里
from datetime import datetime

# ------------------- 日志配置 -------------------
log_file = "selenium.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# ------------------- Chrome 配置 -------------------
chrome_options = Options()
chrome_options.add_argument("--headless")           # 无界面模式
chrome_options.add_argument("--no-sandbox")         # 适合Linux服务器
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# ------------------- 启动浏览器 -------------------
try:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    logging.info("Chrome 浏览器启动成功")
except Exception as e:
    logging.error(f"浏览器启动失败: {e}")
    exit(1)

# ------------------- 打开网页 -------------------
url = "https://www.google.com"
try:
    driver.get(url)
    logging.info(f"打开网页: {url}")
    logging.info(f"网页标题: {driver.title}")
except Exception as e:
    logging.error(f"打开网页失败: {e}")

# ------------------- 截图 -------------------
screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)
screenshot_path = os.path.join(screenshot_folder, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

try:
    driver.save_screenshot(screenshot_path)
    logging.info(f"截图已保存: {screenshot_path}")
except Exception as e:
    logging.error(f"截图失败: {e}")

# ------------------- 关闭浏览器 -------------------
driver.quit()
logging.info("浏览器已关闭")