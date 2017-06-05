from selenium.webdriver.common.by import By

class GoogleHomePageLocators:
    REDIRECT_TO_MAIL_BUTTON = (By.XPATH, ".//div[@id='gb']//a[@href='https://mail.google.com/mail/?tab=wm']")
    ENTER_BUTTON = (By.XPATH, ".//*[@id='gb_70']")

class AuthorizationPageLocators:
    LOGIN_TEXT_FIELD = (By.XPATH, ".//*[@id='identifierId']")
    LOGIN_NEXT_BUTTON = (By.XPATH, ".//*[@id='identifierNext']/content/span")
    PASSWORD_TEXT_FIELD = (By.XPATH, ".//*[@id='password']/div[1]/div/div[1]/input")
    PASSWORD_NEXT_BUTTON = (By.XPATH, ".//*[@id='passwordNext']/content/span")
    INVIS_EL_WAIT = (By.XPATH, ".//*[@id='initialView' and aria-busy='true']")

class LettersListPageLocators:
    WAIT_LOADING_MASK = (By.XPATH, ".//*[@id='loading' and @style='display: none;']")
    LAST_LETTER = (By.XPATH, ".//*[@class='UI']//*[contains(@class, 'zA')][1]")

class LetterPageLocators:
    DATA_BODY_LOCATOR = (By.XPATH, ".//*[@class='adn ads']//*[@class='gs']/div[7]/div[1]/div[1]")
    TITLE_BODY_LOCATOR = (By.XPATH, ".//*[@class='ha']/h2")