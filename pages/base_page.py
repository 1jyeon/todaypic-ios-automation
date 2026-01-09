from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from PIL import Image
import io

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def input_text(self, element, text):
        element.click()
        element.send_keys(text)
    
    def swipe_calendar(self, direction="right"):
        """
        direction: 'left' (다음 달), 'right' (이전 달)
        """
        self.driver.execute_script('mobile: swipe', {
            'direction': direction
    })

    def get_element_color(self, locator):
        element = self.find_element(locator)
        location = element.location  # {'x': 100, 'y': 200}
        size = element.size          # {'width': 50, 'height': 50}

        png = self.driver.get_screenshot_as_png()
        img = Image.open(io.BytesIO(png))
        
        center_x = location['x'] + (size['width'] / 2)
        center_y = location['y'] + (size['height'] / 2)
        
        rgb_img = img.convert('RGB')
        return rgb_img.getpixel((center_x, center_y))