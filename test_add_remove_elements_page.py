from pages.add_remove_elements_page import AddRemoveElementsPage


class TestAddRemoveElementsPage:

    def test_should_be_correct_page_title(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.should_be_correct_page_title()

    def test_should_be_no_elements_after_opening(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.should_be_empty_elements_list()

    def test_should_add_one_element_after_single_click(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.should_be_one_added_element()

    def test_should_be_able_to_delete_single_element(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_first_element()
        add_remove_element_page.should_be_empty_elements_list()

    def test_should_be_able_to_delete_second_element(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_second_element()
        add_remove_element_page.should_be_one_added_element()

    def test_should_be_able_to_delete_multiple_elements(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.add_element()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_third_element()
        add_remove_element_page.delete_second_element()
        add_remove_element_page.should_be_one_added_element()

    def test_should_be_able_to_add_element_after_deletion(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_first_element()
        add_remove_element_page.add_element()
        add_remove_element_page.should_be_one_added_element()

    def test_should_be_able_to_add_elements_after_multiple_deletions(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_element()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_second_element()
        add_remove_element_page.delete_first_element()
        add_remove_element_page.add_element()
        add_remove_element_page.delete_first_element()
        add_remove_element_page.add_element()
        add_remove_element_page.should_be_one_added_element()

    def test_should_be_able_to_add_100_elements(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_100_elements()

    def test_should_be_able_to_delete_100_elements(self, browser):
        link = "https://the-internet.herokuapp.com/add_remove_elements/"
        add_remove_element_page = AddRemoveElementsPage(browser, link)
        add_remove_element_page.open()
        add_remove_element_page.add_100_elements()
        add_remove_element_page.delete_100_elements()
