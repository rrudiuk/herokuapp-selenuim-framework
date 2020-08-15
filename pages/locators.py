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
