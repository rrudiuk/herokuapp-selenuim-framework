import pytest
from pages.add_remove_elements_page import AddRemoveElementsPage


class TestAddRemoveElementsPage:

    def test_should_be_correct_page_title(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.should_be_correct_page_title()

    def test_should_add_one_element_after_single_click(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.should_be_one_added_element()

    def test_delete_single_element(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_first_element()
        add_remove_element_page.should_be_empty_elements_list()

