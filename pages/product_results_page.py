from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class Results(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _product_images = '[class*="s-image-square-aspect"]'

    def product_images(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self._product_images)