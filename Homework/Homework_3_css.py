from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements:
# logo(By class)
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account(BY class)
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name(by ID)
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

# email (By attribute)
driver.find_element(By.CSS_SELECTOR, 'input[type="email')

# Password(BY ID)
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

# Password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.a-alert-inline-info.auth-'
                                     'inlined-information-message.a-spacing-top-mini')

# Re-enter password(By, attribute)
driver.find_element(By.CSS_SELECTOR, 'label[for="ap_password_check"]')

# Create your amazon account(BY class)
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# privacy notice (BY attribute portion (*))
driver.find_element(By.CSS_SELECTOR,
                    'a[href*="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice"]')


# conditions of use
driver.find_element(By.CSS_SELECTOR,
                    "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

# sign in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")

