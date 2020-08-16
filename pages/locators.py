from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class AddRemoveElementsLocators:
    ALL_ADDED_ELEMENTS = (By.CSS_SELECTOR, ".added-manually")
    BUTTON_ADD_ELEMENT = (By.CSS_SELECTOR, ".example > button")
    ELEMENTS_CONTAINER = (By.CSS_SELECTOR, "#elements")
    FIRST_ADDED_ELEMENT = (By.CSS_SELECTOR, ".added-manually:nth-child(1)")
    HUNDRED_ADDED_ELEMENT = (By.CSS_SELECTOR, ".added-manually:nth-child(100)")
    PAGE_HEADER = (By.CSS_SELECTOR, "#content h3")
    SECOND_ADDED_ELEMENT = (By.CSS_SELECTOR, ".added-manually:nth-child(2)")
    THIRD_ADDED_ELEMENT = (By.CSS_SELECTOR, ".added-manually:nth-child(3)")


class LoginPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, ".example h2")
    PAGE_DESCRIPTION = (By.CSS_SELECTOR, ".subheader")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".fa-sign-in")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".icon-signout")
    ERROR_LOGIN = (By.CSS_SELECTOR, "#flash-messages > .error")
    SUCCESS_LOGIN = (By.CSS_SELECTOR, "#flash-messages > .success")
