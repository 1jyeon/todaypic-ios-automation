from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def input_text(self, element, text):
        element.click()
        element.send_keys(text)
    
    def swipe_left_to_right(driver):
        finger = PointerInput(PointerInput.TOUCH, "finger")
        actions = ActionBuilder(driver, mouse=finger)

        size = driver.get_window_size()
        start_x = int(size["width"] * 0.1)
        end_x = int(size["width"] * 0.9)
        y = int(size["height"] * 0.5)

        actions.pointer_action.move_to_location(start_x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(end_x, y)
        actions.pointer_action.release()

        actions.perform()

    def swipe_right_to_left(driver):
        finger = PointerInput(PointerInput.TOUCH, "finger")
        actions = ActionBuilder(driver, mouse=finger)

        size = driver.get_window_size()
        start_x = int(size["width"] * 0.9)
        end_x = int(size["width"] * 0.1)
        y = int(size["height"] * 0.5)

        actions.pointer_action.move_to_location(start_x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(end_x, y)
        actions.pointer_action.release()

        actions.perform()