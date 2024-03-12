import allure

from pages.base_page import BasePage
from locators.locators import ResetPasswordPageLocators


class ResetPassword(BasePage):
    @allure.step("Ожидание кнопки показать/скрыть пароль")
    def wait_for_load_show_hide_password_button(self):
        self.wait_for_clickable(ResetPasswordPageLocators.password_icon_action)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_to_icon_password(self):
        self.find_element_located_click(ResetPasswordPageLocators.password_icon_action)

    @allure.step("Достаем поле с подсветкой")
    def get_active_password(self):
        return self.get_element(ResetPasswordPageLocators.recovery_password_field)

    @allure.step("Ожидаем поле 'Код из письма'")
    def wait_for_invisibility_code(self):
        self.wait_for_visibility(ResetPasswordPageLocators.code_password_recovery_field)
