from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    CloseButton = (By.CSS_SELECTOR, 'button[aria-label="close"]')
    CartButton = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')
    Ps5Image = (By.CSS_SELECTOR, 'img[alt="PlayStation 5 Digital Edition Console (Slim)"]')
    def Verification_for_ps5(self):
        self.click(*self.CloseButton)
        self.click(*self.CartButton)
        self.find_element(*self.Ps5Image)

        