import logging
import os
from datetime import datetime
from contextlib import contextmanager
import threading

class ProcessContext:
    def __init__(self):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self.driver = None
        self.logger = None
        self.color = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m'][
            os.getpid() % 5
        ]
        self.process_thread_id = f"Process-{os.getpid()}-Thread-{threading.get_ident()}"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.log_dir, f"{timestamp}_{self.process_thread_id}.log")

        self.logger = logging.getLogger(self.process_thread_id)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)

    @contextmanager
    def set_driver(self, driver):
        self.driver = driver
        try:
            yield
        finally:
            if self.driver:
                self.driver.quit()
            for handler in self.logger.handlers[:]:
                handler.close()
                self.logger.removeHandler(handler)

    def log(self, message, level=logging.INFO):
        print(f"{self.color}[{self.process_thread_id}]: {message}\033[0m")
        self.logger.log(level, message)
process_context = ProcessContext()