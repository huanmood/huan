from selenium.webdriver.common.by import By
import time
from Page.BasePage import Action

class Connect(Action):

    def connect(self, deviceName, deviceMac):
        self.click_button(self.buttonElement.Homepage_connect)
        if self.exists_element(self.buttonElement.disconnect):
            self.click_button(self.buttonElement.disconnect)
            self.click_button(self.buttonElement.connectFaile_sure)
        self.first_connect()
        connectTitle = self.find_element(self.buttonElement.connectPage_title)
        deviceMacs = (By.XPATH,f'//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ble_address" and @text="{deviceMac}"]')
        while True:
            if self.exists_element(deviceMacs):
                self.click_button(deviceMacs)
                if self.exists_element(self.buttonElement.alertTitle):
                    self.click_button(self.buttonElement.accept_button)
                self.log_debug('连接成功')
                self.cut_connect()
                break
                # if self.exists_element(self.buttonElement.connectPage_connectFail):
                #     self.click_button(self.buttonElement.connectPage_sure)
                #     self.click_button(self.buttonElement.connectPage_refresh)
                #     self.double_tap_element(connectTitle)
                #     self.double_tap_element(connectTitle)
                #     self.click_button(deviceMac)
                # else:
                #     break

            else:
                self.log_error(f"找不到{deviceName}--{deviceMac}进入else")
                self.click_button(self.buttonElement.connectPage_refresh)
                time.sleep(2)
                self.double_tap_element(connectTitle)
                self.double_tap_element(connectTitle)
                if self.exists_element(deviceMacs):
                    self.click_button(deviceMacs)
                    self.log_debug('连接成功')
                    self.cut_connect()
                    break
                self.drag_location(start_x=539, start_y=1711, end_x=539, end_y=475)
                time.sleep(1)

        self.log_debug("Successful")
    def cut_connect(self):
        self.click_button(self.buttonElement.connectState)
        self.click_button(self.buttonElement.disconnect)
        self.click_button(self.buttonElement.connect_sure)
        self.back_button()
    def tearDown(self):
        self.quit()
