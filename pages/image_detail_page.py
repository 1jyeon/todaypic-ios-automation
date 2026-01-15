from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ImageDetailPage(BasePage):
    BTN_DETAIL_CANCEL = (AppiumBy.ACCESSIBILITY_ID, "btn_detail_cancel")

    def is_detail_cancel_displayed(self):
        return self.find_element(self.BTN_DETAIL_CANCEL).is_displayed()