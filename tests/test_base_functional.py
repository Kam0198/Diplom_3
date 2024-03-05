import time

import allure

from data import email, password
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccount
from urls import Urls


class TestBaseFunctional:
    @allure.title("Проверка перехода авторизованного пользователя в раздел 'Конструктор'")
    def test_enter_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_order_feed_button()
        personal_account.click_constructor_button()
        assert Urls.main_page_url in driver.current_url

    @allure.title("Проверка перехода авторизованного пользователя в раздел 'Лента заказов'")
    def test_enter_to_order_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_order_feed_button()
        assert Urls.order_feed_url in driver.current_url

    @allure.title("Проверка появления всплывающего окна с деталями при клике на ингредиент")
    def test_get_modal_window_with_details(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_on_ingredient()
        text_ingredients = personal_account.get_ingredients_details().text
        assert text_ingredients == "Детали ингредиента"

    @allure.title("Проверка закрытия модального окна после нажатия на крестик")
    def test_close_modal_window_with_details(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_on_ingredient()
        personal_account.wait_for_invisibility_close_window()
        personal_account.click_on_close_window_button_details()
        time.sleep(2)
        text_ingredients = personal_account.get_ingredients_details().text
        time.sleep(3)
        assert text_ingredients != "Детали ингредиента"

    @allure.title("Проверка увеличения счетчика при добавлении ингредиента в заказ")
    def test_counter_ingredients(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        counter_1 = int(personal_account.first_counter().text)
        personal_account.drag_and_drop_elements()
        counter_2 = int(personal_account.first_counter().text)
        assert counter_1 + 2 == counter_2

    @allure.title("Проверка создания заказа под авторизованном пользователем")
    def test_create_order_auth(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.drag_and_drop_elements()
        personal_account.click_ordering_button()
        personal_account.wait_for_invisibility_close_window()
        accept_text = personal_account.get_accept_order_text().text
        assert accept_text == "Ваш заказ начали готовить"



