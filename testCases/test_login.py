from operator import truediv
import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://jagadarshan-test.estpl.net:8889/officer/login"
    username = "Admin"
    password = "Bntyy@0912"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Scheme":
            assert True
        else:
            assert False

    def test_loginPage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickCaptch()
        time.sleep(10)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        print("Title is: ",act_title)
        # self.driver.close()
        if act_title == "Scheme":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page.png")
            assert False



