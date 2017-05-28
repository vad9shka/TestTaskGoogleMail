from selenium.common.exceptions import WebDriverException
import time
import logging
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from GMailTask.PagesLocators import *
from selenium.common.exceptions import NoSuchElementException


class Base:

    def __init__(self, driver):
        self.driver = driver


class GoogleHomePage(Base):

    def redirect_to_mail(self):

        try:
            web_element = self.driver.find_element(*GoogleHomePageLocators.REDIRECT_TO_MAIL_BUTTON)
            web_element.click()
        except WebDriverException as e:
            #traceback.print_tb(e.__traceback__)
            #traceback.print_exc(e.__traceback__)
            #traceback.print_stack(e.__traceback__)
            print(e)
            assert False

    def enter_button_click(self):

        try:
            web_element = self.driver.find_element(*GoogleHomePageLocators.ENTER_BUTTON)
            web_element.click()
        except WebDriverException as e:
            print(e)
            assert False


class AuthorizationPage(Base):

    def login(self, login):

        try:
            web_element = self.driver.find_element(*AuthorizationPageLocators.LOGIN_TEXT_FIELD)
            web_element.send_keys(login)

            web_element = self.driver.find_element(*AuthorizationPageLocators.LOGIN_NEXT_BUTTON)
            web_element.click()
        except WebDriverException as e:
            print(e)
            assert False
        # time.sleep(5)

    def password(self, password):

        try:
            self.driver.implicitly_wait(1)
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.invisibility_of_element_located((AuthorizationPageLocators.INVIS_EL_WAIT)))
            web_element = self.driver.find_element(*AuthorizationPageLocators.PASSWORD_TEXT_FIELD)
            web_element.send_keys(password)

            web_element = self.driver.find_element(*AuthorizationPageLocators.PASSWORD_NEXT_BUTTON)
            web_element.click()
        except WebDriverException as e:
            print(e)
            assert False

class LettersListPage(Base):

    def enter_the_last_letter(self):

        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(lambda driver: self.driver.find_element(*LettersListPageLocators.WAIT_LOADING_MASK))
            web_element = self.driver.find_element(*LettersListPageLocators.LAST_LETTER)
            web_element.click()
        except WebDriverException as e:
            print(e)
            assert False

class LetterPage(Base):

    def is_element_present_by_xpath(self, xpath_expression):
        try:
            self.driver.find_element_by_xpath(xpath_expression)
            return True
        except NoSuchElementException:
            return False

    def check_data_body(self):
        try:
            web_element = self.driver.find_element(*LetterPageLocators.DATA_BODY_LOCATOR).text
            return web_element
        except WebDriverException as e:
            print(e)
            assert False

    def check_title_body(self):
        try:
            web_element = self.driver.find_element(*LetterPageLocators.TITLE_BODY_LOCATOR).text
            return web_element
        except WebDriverException as e:
            print(e)
            assert False
