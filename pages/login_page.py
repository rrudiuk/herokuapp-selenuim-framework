from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def click_login_button(self):
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click_element(*LoginPageLocators.LOGOUT_BUTTON)

    def input_incorrect_username(self):
        username = self.locate_element(*LoginPageLocators.USERNAME_INPUT)
        username.send_keys("some username")

    def input_correct_username(self):
        username = self.locate_element(*LoginPageLocators.USERNAME_INPUT)
        username.send_keys("tomsmith")

    def input_username_injection(self):
        username = self.locate_element(*LoginPageLocators.USERNAME_INPUT)
        username.send_keys('"" or ""=""')

    def input_incorrect_password(self):
        username = self.locate_element(*LoginPageLocators.PASSWORD_INPUT)
        username.send_keys("some password")

    def input_correct_password(self):
        username = self.locate_element(*LoginPageLocators.PASSWORD_INPUT)
        username.send_keys("SuperSecretPassword!")

    def input_password_injection(self):
        username = self.locate_element(*LoginPageLocators.PASSWORD_INPUT)
        username.send_keys('"" or ""=""')

    def should_appear_error_message(self):
        assert self.is_element_present(*LoginPageLocators.ERROR_LOGIN), "Error message doesn't appear," \
                                                                        " but it should"

    def should_not_appear_error_message(self):
        assert self.is_not_element_present(*LoginPageLocators.ERROR_LOGIN), "Error message appears," \
                                                                            " but it should not"

    def should_appear_success_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_LOGIN), "Success message doesn't appear," \
                                                                          " but it should"

    def should_not_appear_success_message(self):
        assert self.is_not_element_present(*LoginPageLocators.SUCCESS_LOGIN), "Success message appears," \
                                                                              " but it should not"

    def should_appear_username_input_field(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_INPUT), "Username input doesn't appear," \
                                                                           " but it should"

    def should_not_appear_username_input_field(self):
        assert self.is_not_element_present(*LoginPageLocators.USERNAME_INPUT), "Username input appears," \
                                                                               " but it should not"

    def should_appear_password_input_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), "Password input doesn't appear," \
                                                                           " but it should"

    def should_not_appear_password_input_field(self):
        assert self.is_not_element_present(*LoginPageLocators.PASSWORD_INPUT), "Password input appears," \
                                                                               " but it should not"

    def should_appear_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button doesn't appear,but it should"

    def should_not_appear_login_button(self):
        assert self.is_not_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button appears," \
                                                                             " but it should not"

    def should_appear_logout_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT_BUTTON), "Logout button doesn't appear," \
                                                                          " but it should"

    def should_not_appear_logout_button(self):
        assert self.is_not_element_present(*LoginPageLocators.LOGOUT_BUTTON), "Logout button appears," \
                                                                              " but it should not"

    def should_be_correct_page_title_logged_out(self):
        expected_result = "Login Page"
        actual_result = self.get_text(*LoginPageLocators.PAGE_HEADER)

        assert actual_result == expected_result, f"Incorrect header {actual_result}. " \
                                                 f"Should be {expected_result}"

    def should_be_correct_page_title_logged_in(self):
        expected_result = "Secure Area"
        actual_result = self.get_text(*LoginPageLocators.PAGE_HEADER)

        assert actual_result == expected_result, f"Incorrect header {actual_result}. " \
                                                 f"Should be {expected_result}"

    def should_be_correct_page_description_logged_out(self):
        expected_result = "This is where you can log into the secure area. Enter tomsmith for the username " \
                          "and SuperSecretPassword! for the password. If the information is wrong you should " \
                          "see error messages."
        actual_result = self.get_text(*LoginPageLocators.PAGE_DESCRIPTION)

        assert actual_result == expected_result, f"Incorrect header {actual_result}. " \
                                                 f"Should be {expected_result}"

    def should_be_correct_page_description_logged_in(self):
        expected_result = "Welcome to the Secure Area. When you are done click logout below."
        actual_result = self.get_text(*LoginPageLocators.PAGE_DESCRIPTION)

        assert actual_result == expected_result, f"Incorrect header {actual_result}. " \
                                                 f"Should be {expected_result}"
