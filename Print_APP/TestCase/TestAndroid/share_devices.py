# share_driver.py
import threading
import os
from contextlib import contextmanager
import logging
from datetime import datetime


class ThreadContext:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.local = threading.local()
                cls._instance.colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
                cls._instance.color_index = 0
                cls._instance.init_lock = threading.Lock()
                cls._instance.log_dir = "logs"  # 日志目录
                os.makedirs(cls._instance.log_dir, exist_ok=True)
        return cls._instance

    def _init_thread(self):
        if not hasattr(self.local, 'initialized'):
            with self.init_lock:
                if not hasattr(self.local, 'initialized'):
                    # 分配颜色和线程ID
                    self.local.color = self.colors[self.color_index % len(self.colors)]
                    self.local.thread_id = f"Thread-{threading.get_ident()}"
                    self.color_index += 1

                    # 创建线程专属日志文件
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    self.local.log_file = os.path.join(
                        self.log_dir,
                        f"{timestamp}_{self.local.thread_id}.log"
                    )

                    # 配置日志记录器
                    self.local.logger = logging.getLogger(self.local.thread_id)
                    self.local.logger.setLevel(logging.INFO)

                    # 文件处理器
                    file_handler = logging.FileHandler(self.local.log_file,encoding='utf-8')
                    file_handler.setFormatter(logging.Formatter(
                        '%(asctime)s - %(levelname)s - %(message)s'
                    ))
                    self.local.logger.addHandler(file_handler)

                    self.local.initialized = True

    @property
    def driver(self):
        self._init_thread()
        if not hasattr(self.local, 'driver'):
            raise AttributeError("Driver not initialized in current thread")
        return self.local.driver

    @contextmanager
    def set_driver(self, driver):
        self._init_thread()
        self.local.driver = driver
        try:
            yield
        finally:
            # 清理日志处理器
            if hasattr(self.local, 'logger'):
                for handler in self.local.logger.handlers[:]:
                    handler.close()
                    self.local.logger.removeHandler(handler)
            del self.local.driver

    def log(self, message, level=logging.INFO):
        self._init_thread()
        # 控制台输出（带颜色）
        reset = '\033[0m'
        console_msg = f"{self.local.color}[{self.local.thread_id}]: {message}{reset}"
        print(console_msg)

        # 写入日志文件
        self.local.logger.log(level, message)


# 全局单例
thread_context = ThreadContext()