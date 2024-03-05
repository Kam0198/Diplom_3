import allure

from data import email, password
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccount
from urls import Urls


class TestAccountProfilePage:
    @allure.title("Проверка перехода авторизованного пользователя в 'Личный кабинет'")
    def test_enter_personal_account(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_personal_account_button()
        personal_account.wait_for_invisibility_logout_button()
        assert Urls.profile_url in driver.current_url

    @allure.title("Проверка перехода авторизованного пользователя в раздел 'История заказов'")
    def test_enter_to_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_personal_account_button()
        personal_account.click_history_order_button()
        assert Urls.order_history_url in driver.current_url

    @allure.title("Проверка выхода аккаунта авторизованного пользователя")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_personal_account_button()
        personal_account.click_logout_button()
        login_page.wait_for_invisibility_enter_button()
        assert Urls.login_page_url in driver.current_url


