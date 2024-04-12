from selenium import webdriver
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.by import By


@given('Open target')
def Open_Target(context):
    context.driver.get('https://www.target.com/')
    sleep(6)
@when('Click on cart')
def Click_Cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]').click()
    sleep(6)

@then('Verify “Your cart is empty” message is shown')
def Verify_CartIsEmpty(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"]')
    sleep(5)

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