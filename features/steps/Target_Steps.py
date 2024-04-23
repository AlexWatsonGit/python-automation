from selenium import webdriver
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.by import By

benefit_cells = By.CSS_SELECTOR, "a[data-test='@web/slingshot-components/CellsComponent/Link']"
@given('Open the web page {target}')
def Open_Target(context, target):
    context.driver.get(target)
    sleep(10)
@when('Click on cart')
def Click_Cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]').click()
    sleep(6)

@then('Verify {Your_cart_is_empty} message is shown')
def Verify_CartIsEmpty(context, Your_cart_is_empty):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"]')
    sleep(10)

@when('Click sign in')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Account, sign in"]').click()
    sleep(2)
@when('From navigation menu, click sign in')
def sign_in_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]').click()
    sleep(2)

@then('Verify sign in opened')
def verify_sign_in_opened(context):
    context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0')



#this one below will verify something is there using the assert
# @then('Verify search worked for {expected_product}')
# def verify_search_worked(context, expected_product):
#     x = context.driver.find_element(By.XPATH, '').text
#     assert expected_product in x f'Expected "{expected_product}" not in {x}'

@then('Verify there are 10 benefit cells')
def verify_benefit_cells(context):
    context.driver.find_elements(*benefit_cells)
    links = context.driver.find_elements(*benefit_cells)
    assert len(links) == 10, f'Expected 10, There are {len(links)}'

@when('Search for {product}')
def click_search_bar(context, product):
    context.driver.find_element(By.CSS_SELECTOR, 'input#search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()
    sleep(6)



@when('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor90188800').click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, '.styles__StyledBaseButtonInternal-sc-ysboml-0.styles__ButtonPrimary-sc-5fh6rr-0.hCWYcY.bEdlr').click()

@then('Verify item was added to cart successfully')
def verify_item_added(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="close"]').click()
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]').click()
    context.driver.find_element(By.CSS_SELECTOR, 'img[alt="PlayStation 5 Digital Edition Console (Slim)"]')