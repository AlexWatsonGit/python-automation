from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    lemon_tea = By.CSS_SELECTOR, 'a[aria-label="Bigelow Lemon Ginger Plus Probiotics Herbal Tea Bags - 18ct"]'
    def verify_search_results(self):
        self.find_element(*self.lemon_tea)