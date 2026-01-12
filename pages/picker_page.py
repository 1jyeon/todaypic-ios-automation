from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PickerPage(BasePage):
    PICKER_YEAR = (AppiumBy.ACCESSIBILITY_ID, "picker_year")
    PICKER_MONTH = (AppiumBy.ACCESSIBILITY_ID, "picker_month")
    BTN_PICKER_CANCEL = (AppiumBy.ACCESSIBILITY_ID, "btn_picker_cancel")
    BTN_PICKER_CONFIRM = (AppiumBy.ACCESSIBILITY_ID, "btn_picker_comfirm")

    def is_cancel_button_displayed(self):
        return self.find_element(self.BTN_PICKER_CANCEL).is_displayed()
    
    def is_confirm_button_displayed(self):
        return self.find_element(self.BTN_PICKER_CONFIRM).is_displayed()
    
    def select_year_and_month(self, target_year, target_month):
        year_wheel = self.find_element(self.PICKER_YEAR)
        month_wheel = self.find_element(self.PICKER_MONTH)
        year_wheel.send_keys(target_year)        
        month_wheel.send_keys(target_month)
        
        self.click(self.BTN_PICKER_CONFIRM)