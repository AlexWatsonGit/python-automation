# Part One (Amazon)----------------------------------------------------------
#Practice with locators. Create locators + search strategy for these page elements of Amazon Sign in page:

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

# open the url
driver.get('https://www.Amazon.com/')



# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# Email field
driver.find_element(By.XPATH, "//input[@type='email']")
# Continue button
driver.find_element(By.ID,'continue')
# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# Forgot your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
# Create your Amazon account button
driver.find_element(By.XPATH, '//a[@id="createAccountSubmit"]')





# Part two (Automate target login)----------------------------------------------


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

# open the url
driver.get('https://www.target.com/')

sleep(6)
# Click sign in button
driver.find_element(By.XPATH, '//span[@class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]').click()
sleep(3)
# Click SignIn from side navigation
driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()
sleep(6)
# Verify SignIn page opened:
driver.find_element(By.XPATH, '//h1[@class="styles__StyledHeading-sc-1xmf98v-0'
                              ' styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa"]')
driver.find_element(By.XPATH, '//button[@type="submit"]')

# If test passed print "Pass", else test will fail with exception
print('Test Passed')
driver.quit()


