from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CalendarPage(BasePage):
    HEADER_DATE = (AppiumBy.ACCESSIBILITY_ID, "btn_header_date_picker")
    TODAY_BTN = (AppiumBy.ACCESSIBILITY_ID, "btn_today")
    ADD_BTN = (AppiumBy.ACCESSIBILITY_ID, "btn_add")
    PICKER_MOVE_BTN = (AppiumBy.ACCESSIBILITY_ID, "btn_picker_confirm")
    SUNDAY_LABEL = (AppiumBy.ACCESSIBILITY_ID, "sunday_label")
    SATURDAY_LABEL = (AppiumBy.ACCESSIBILITY_ID, "saturday_label")

    def is_header_date_displayed(self):
        return self.wait_for_element(self.HEADER_DATE).is_displayed()

    def click_header(self):
        self.click(self.HEADER)

    def is_today_button_enabled(self):
        return self.find_element(self.TODAY_BTN).is_enabled()

    def is_add_button_displayed(self):
        return self.find_element(self.ADD_BTN).is_displayed()
    
    def is_picker_move_button_displayed(self):
        return self.wait_for_element(self.PICKER_MOVE_BTN).is_displayed()
    
    def get_current_month_text(self):
        return self.wait_for_element(self.HEADER_DATE).spilt('')[1].replace('달','').is_displayed()