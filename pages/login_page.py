import allure

from pages.base_page import BasePage
from locators.locators import LoginPageLocators, ResetPasswordPageLocators


class LoginPage(BasePage):
    @allure.step("Ожидаем загрузки заголовка 'Вход'")
    def wait_header_enter(self):
        self.wait_for_visibility(LoginPageLocators.header_enter)

    @allure.step("Заполнить поле 'Email' при авторизации")
    def enter_text_email_auth(self, email):
        enter_email = self.find_element_located(LoginPageLocators.email_field_auth)
        enter_email.click()
        enter_email.send_keys(email)

    @allure.step("Заполнить поле 'Пароль' при авторизации")
    def enter_text_password_auth(self, password):
        enter_password = self.find_element_located(LoginPageLocators.password_field_auth)
        enter_password.click()
        enter_password.send_keys(password)

    @allure.step("Клик по кнопке 'Войти' при авторизации")
    def click_login_button_auth(self):
        self.find_element_located_click(LoginPageLocators.login_button_auth)

    @allure.step("Клик по кнопке 'Зарегистрироваться' при авторизации")
    def click_registration_button_auth(self):
        self.find_element_located_click(LoginPageLocators.registration_button_auth)

    @allure.step("Клик по кнопке 'Восстановить пароль' при авторизации")
    def click_password_recovery_button_auth(self):
        self.find_element_located_click(LoginPageLocators.password_recovery_auth)

    @allure.step("Ожидаем отображение кнопки 'Войти'")
    def wait_for_invisibility_enter_button(self):
        self.wait_for_clickable(LoginPageLocators.login_button_auth)



