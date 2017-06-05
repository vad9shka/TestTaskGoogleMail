import unittest
from selenium import webdriver
import GMailTask.pages

class ListWebElements(unittest.TestCase):

    def setUp(self):
        # create user with login and password in database
        #---------------------------------#

        self.driver = webdriver.Chrome("/Users/vadim/Desktop/Autotests/chromedriver")
        self.driver.get("https://www.google.ru/")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(30)

    def test_list_web_element(self):

        list_web_el_def = ["Поиск в Google", "Мне повезёт!"]

        list_web_elements = self.driver.find_elements_by_xpath(".//div[@class='tsf-p']//center/input")

        print(list_web_elements)

        print(len(list_web_elements))

        iterator = 0
        for i in list_web_elements:
            text_web_el = i.get_attribute("value")
            if text_web_el != list_web_el_def[iterator]:
                print("Error!")
                assert False
            else:
                assert True

            iterator = iterator + 1

        iterator = 0
        for i in list_web_elements:
            text_web_el = i.get_attribute("value")
            # not is '!' in java
            # == is equals() in java
            if not text_web_el == list_web_el_def[iterator]:
                print("Error!")
                assert False
            else:
                assert True

            iterator = iterator + 1

        # in / not in are contains() in java
        list_web_el_def2 = ["Поиск", "повезёт!"]
        iterator = 0
        for i in list_web_elements:
            text_web_el = i.get_attribute("value")
            if list_web_el_def2[iterator] in text_web_el:
                print("True")
            else:
                print("False")
            iterator = iterator + 1