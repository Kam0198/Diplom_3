import allure

from locators.locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPassword(BasePage):
    @allure.step("Заполнить поле 'Email' на странице 'Забыли пароль'")
    def enter_text_email_forgot_password(self, email):
        enter_email = self.find_element_located(ForgotPasswordPageLocators.password_recovery_email_field)
        enter_email.click()
        enter_email.send_keys(email)

    @allure.step("Клик по кнопке 'Восстановить' на странице 'Забыли пароль'")
    def click_login_button_auth(self):
        self.find_element_located_click(ForgotPasswordPageLocators.password_recovery_button)