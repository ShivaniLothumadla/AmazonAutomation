class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self):
        pageLength = self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return document.body.scrollHeight')
        match = False
        while not match:
            lastcount = pageLength
            pageLength = self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return document.body.scrollHeight')
            if lastcount == pageLength:
                match = True
