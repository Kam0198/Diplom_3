import allure

from data import email
from pages.forgot_password_page import ForgotPassword
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPassword
from urls import Urls


class TestForgotPassword:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_open_forgot_password_page(self, driver):
        forgot_password_page = LoginPage(driver)
        forgot_password_page.go_to_site(Urls.login_page_url)
        forgot_password_page.wait_header_enter()
        forgot_password_page.click_password_recovery_button_auth()
        assert Urls.password_forgot_url in forgot_password_page.get_current_url()

    @allure.title("Проверка ввода почты и клика по кнопке «Восстановить»")
    def test_enter_email_and_click_reset_button(self, driver):
        forgot_password_page = LoginPage(driver)
        forgot_password_page.go_to_site(Urls.login_page_url)
        forgot_password_page.click_password_recovery_button_auth()
        enter_email = ForgotPassword(driver)
        enter_email.enter_text_email_forgot_password(email)
        enter_email.click_login_button_auth()
        password_reset = ResetPassword(driver)
        password_reset.wait_for_invisibility_code()
        assert Urls.password_reset_url in forgot_password_page.get_current_url()

    @allure.title("Проверка, что кнопка скрыть/показать пароль делает поле активным и подсвечивает его")
    def test_click_to_icon_password(self, driver):
        forgot_password_page = LoginPage(driver)
        forgot_password_page.go_to_site(Urls.login_page_url)
        forgot_password_page.click_password_recovery_button_auth()
        enter_email = ForgotPassword(driver)
        enter_email.enter_text_email_forgot_password(email)
        enter_email.click_login_button_auth()
        reset_password = ResetPassword(driver)
        reset_password.wait_for_load_show_hide_password_button()
        reset_password.click_to_icon_password()
        assert reset_password.get_active_password()

