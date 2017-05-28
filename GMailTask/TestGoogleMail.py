import unittest
from selenium import webdriver
import GMailTask.pages


class CheckGMail(unittest.TestCase):

    def setUp(self):
        # create user with login and password in database
        #---------------------------------#

        self.driver = webdriver.Chrome("/Users/vadim/Desktop/Autotests/chromedriver")
        self.driver.get("https://www.google.ru/")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(30)

    def test_gmail(self):
        # methods and assertions

        login = "ivanivanoff777test@gmail.com"
        password = "ivanovtest"

        main_page = GMailTask.pages.GoogleHomePage(self.driver)
        main_page.enter_button_click()

        auth_page = GMailTask.pages.AuthorizationPage(self.driver)
        auth_page.login(login)
        auth_page.password(password)

        main_page.redirect_to_mail()

        letters_list_page = GMailTask.pages.LettersListPage(self.driver)
        letters_list_page.enter_the_last_letter()

        check_object = GMailTask.pages.LetterPage(self.driver)
        check_text = check_object.check_data_body()
        # text validation in the body of the message
        self.assertEqual(check_text, "Hello! This is simple text")

        check_text = check_object.check_title_body()
        # checking the text in the title body of the letter
        self.assertEqual(check_text, "Test")

        # message body is present
        xpath_expression_for_body = ".//*[@class='adn ads']//*[@class='gs']/div[7]/div[1]"
        self.assertTrue(check_object.is_element_present_by_xpath(xpath_expression_for_body))

        # title body of the letter is present
        xpath_expression_for_title = ".//*[@class='ha']/h2"
        self.assertTrue(check_object.is_element_present_by_xpath(xpath_expression_for_title))

    def tearDown(self):
        self.driver.quit()
        # remove user from database

if __name__ == "__main__":
    unittest.main()
