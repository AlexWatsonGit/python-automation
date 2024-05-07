from pages.base_page import Page
from time import sleep
class MainPage(Page):

    def open_main(self):
        self.driver.get('https://www.target.com/')
        sleep(5)