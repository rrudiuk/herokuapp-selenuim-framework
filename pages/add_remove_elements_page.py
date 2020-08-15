from .base_page import BasePage
from .locators import AddRemoveElementsLocators


class AddRemoveElementsPage(BasePage):
    def add_element(self):
        self.click_element(*AddRemoveElementsLocators.BUTTON_ADD_ELEMENT)

    def delete_first_element(self):
        self.click_element(*AddRemoveElementsLocators.FIRST_ADDED_ELEMENT)

    def delete_second_element(self):
        self.click_element(*AddRemoveElementsLocators.SECOND_ADDED_ELEMENT)

    def delete_third_element(self):
        self.click_element(*AddRemoveElementsLocators.THIRD_ADDED_ELEMENT)

    def delete_all_added_elements(self):
        number_of_elements = self.count_elements(*AddRemoveElementsLocators.ALL_ADDED_ELEMENTS)
        while number_of_elements > 0:
            self.click_element(*AddRemoveElementsLocators.FIRST_ADDED_ELEMENT)
            number_of_elements = number_of_elements - 1

        expected_result = 0
        actual_result = self.count_elements(*AddRemoveElementsLocators.ALL_ADDED_ELEMENTS)

        assert actual_result == expected_result, f"{actual_result} elements were not deleted"

    def first_element_should_be_deleted(self):
        expected_result = self.count_elements(*AddRemoveElementsLocators.ALL_ADDED_ELEMENTS)
        if expected_result <= 0:
            return False
        else:
            expected_result = expected_result - 1
        self.delete_first_element()
        actual_result = self.count_elements(*AddRemoveElementsLocators.ALL_ADDED_ELEMENTS)

        assert actual_result == expected_result, f"There are {actual_result} elements, should be {actual_result}"

    def should_be_empty_elements_list(self):
        assert self.is_not_element_present(*AddRemoveElementsLocators.ALL_ADDED_ELEMENTS), "Elements container" \
                                                                                           " was not deleted"

    def should_be_correct_page_title(self):
        expected_result = "Add/Remove Elements"
        actual_result = self.get_text(*AddRemoveElementsLocators.PAGE_HEADER)

        assert actual_result == expected_result, f"Incorrect header {actual_result}. " \
                                                 f"Should be {expected_result}"

    def should_not_be_added_elements_after_accessing_page(self):
        assert self.is_not_element_present(*AddRemoveElementsLocators.ELEMENTS_CONTAINER), "Elements container " \
                                                                                           "appears but is should not "

    def should_be_one_added_element(self):
        expected_result = 1
        actual_result = self.count_elements(*AddRemoveElementsLocators.ALL_ADDED_ELEMENTS)
        assert actual_result == expected_result, f"Should be {expected_result} element(s)" \
                                                 f" but it is {actual_result}"
