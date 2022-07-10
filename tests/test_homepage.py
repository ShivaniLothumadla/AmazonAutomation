import unittest
import pytest
import logging
from time import sleep
from selenium.webdriver.common.keys import Keys
from pages.home import Home
from utils.utils import utilities
from ddt import *

logging.basicConfig(level=logging.DEBUG, filename='..\\logging\logd.log', filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')


@ddt
@pytest.mark.usefixtures('setup')
class TestHomepage(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = Home(self.driver)
        self.ut = utilities()

    # hardcoded data
    # @data(('shoes', ), ('pants', ), ('lehenga', ))
    # @unpack
    # yaml file
    # @file_data('../testdata/test.yaml')
    # json file
    @file_data('../testdata/test.json')
    def test_home_page(self, product):
        search_field = self.hp.search_field()
        search_field.click()
        search_field.send_keys(product)
        search_field.send_keys(Keys.ENTER)
        # driver.find_element(By.LINK_TEXT, 'Women').click()
        self.hp.scroll_to()
        product_images = self.hp.results_page.product_images()
        log = self.ut._loggers()
        log.debug(product_images)
        # print(product_images)
        for image in product_images:
            sleep(5)
            image.click()
            log.info(self.driver.title)
            break
