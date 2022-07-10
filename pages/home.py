from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.product_results_page import Results


class Home(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_field = "//input[@id='twotabsearchtextbox']"

    def search_field(self):
        return self.driver.find_element(By.XPATH, self._search_field)

    @property
    def results_page(self):
        return Results(self.driver)