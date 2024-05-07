from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
class Header(Page):
    search_button = By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]'
    search = By.CSS_SELECTOR, 'input#search'
    def search_product(self):
        self.input_text('lemon ginger tea', *self.search)
        self.click(*self.search_button)
        sleep(8)

