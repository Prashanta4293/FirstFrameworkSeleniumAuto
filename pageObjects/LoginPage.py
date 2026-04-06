from selenium.webdriver.common.by import By

class LoginPage:
    text_username_xpath = "//input[@id='username']"
    text_password_xpath = "//input[@id='password']"
    text_captcha_xpath = "//input[@id='captcha']"
    button_login_xpath = "//button[text()=' Login ']"   # also fixed typo

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def clickCaptch(self):
        self.driver.find_element(By.XPATH, self.text_captcha_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()