from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
class Header(Page):
    SearchInput = (By.CSS_SELECTOR, 'input#search')
    SearchButton = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    CartButton = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')
    Ps5Image = (By.CSS_SELECTOR, 'img[alt="PlayStation 5 Digital Edition Console (Slim)"]')
    Addps5ToCart = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor90188800')
    ConfirmPs5Add = (
    By.CSS_SELECTOR, '.styles__StyledBaseButtonInternal-sc-ysboml-0.styles__ButtonPrimary-sc-5fh6rr-0.hCWYcY.bEdlr')

    def add_product(self):
        self.input_text('Ps5', *self.SearchInput)
        self.click(*self.SearchButton)
        self.click(*self.Addps5ToCart)
        sleep(5)
        self.click(*self.ConfirmPs5Add)
