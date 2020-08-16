from pages.login_page import LoginPage


class TestLoginPage:

    def test_all_elements_appear_when_logged_out(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_correct_page_title_logged_out()
        login_page.should_be_correct_page_description_logged_out()
        login_page.should_appear_username_input_field()
        login_page.should_appear_password_input_field()
        login_page.should_appear_login_button()
        login_page.should_not_appear_error_message()
        login_page.should_not_appear_success_message()
        login_page.should_not_appear_logout_button()

    def test_should_not_login_with_empty_login_password(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_not_login_with_empty_password(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_correct_username()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_not_login_with_incorrect_password(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_correct_username()
        login_page.input_incorrect_password()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_not_login_with_empty_username(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_correct_password()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_not_login_with_incorrect_username(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_incorrect_username()
        login_page.input_correct_password()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_not_login_with_incorrect_credentials(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_incorrect_username()
        login_page.input_incorrect_password()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_not_login_with_injections(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_username_injection()
        login_page.input_password_injection()
        login_page.click_login_button()
        login_page.should_appear_error_message()

    def test_should_login_with_correct_credentials(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_correct_username()
        login_page.input_correct_password()
        login_page.click_login_button()
        login_page.should_be_correct_page_title_logged_in()
        login_page.should_appear_success_message()
        login_page.should_be_correct_page_description_logged_in()
        login_page.should_appear_logout_button()

    def test_should_be_able_to_logout(self, browser):
        link = "https://the-internet.herokuapp.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.input_correct_username()
        login_page.input_correct_password()
        login_page.click_login_button()
        login_page.should_appear_logout_button()
        login_page.click_logout_button()
        login_page.should_be_correct_page_title_logged_out()
        login_page.should_be_correct_page_description_logged_out()
        login_page.should_appear_username_input_field()
        login_page.should_appear_password_input_field()
        login_page.should_appear_login_button()
        login_page.should_not_appear_error_message()
        login_page.should_appear_success_message()
        login_page.should_not_appear_logout_button()
