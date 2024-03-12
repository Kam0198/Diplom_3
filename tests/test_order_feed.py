import allure

from data import email, password
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeed
from pages.personal_account_page import PersonalAccount
from urls import Urls


class TestOrderFeed:
    @allure.title("Проверка появления окна с деталями при клике на заказ")
    def test_window_with_details(self, driver):
        main_page = LoginPage(driver)
        main_page.go_to_site(Urls.main_page_url)
        personal_account = PersonalAccount(driver)
        personal_account.click_order_feed_button()
        order_feed = OrderFeed(driver)
        order_feed.click_top_order()
        modal_window_text = order_feed.get_modal_window_details().text
        assert modal_window_text == "Cостав"

    @allure.title("Проверка увеличения счетчика 'Выполнено за всё время' ")
    def test_counter_all_time(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_order_feed_button()
        order_feed = OrderFeed(driver)
        old_order_number = int(order_feed.get_all_time_number().text)
        order_feed.click_to_constructor_button()
        personal_account.drag_and_drop_elements()
        personal_account.click_ordering_button()
        personal_account.wait_close_window_button()
        personal_account.click_on_close_window_button_details()
        personal_account.click_order_feed_button()
        new_order_number = int(order_feed.get_all_time_number().text)
        assert old_order_number < new_order_number

    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' ")
    def test_counter_today(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.click_order_feed_button()
        order_feed = OrderFeed(driver)
        old_order_number = int(order_feed.get_time_today().text)
        order_feed.click_to_constructor_button()
        personal_account.drag_and_drop_elements()
        personal_account.click_ordering_button()
        personal_account.wait_close_window_button()
        personal_account.click_on_close_window_button_details()
        personal_account.click_order_feed_button()
        new_order_number = int(order_feed.get_time_today().text)
        assert old_order_number < new_order_number

    @allure.title("Проверка появления номера заказа 'В работе' ")
    def test_order_in_progress(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site(Urls.login_page_url)
        login_page.enter_text_email_auth(email)
        login_page.enter_text_password_auth(password)
        login_page.click_login_button_auth()
        personal_account = PersonalAccount(driver)
        personal_account.wait_personal_account_page()
        personal_account.drag_and_drop_elements()
        personal_account.click_ordering_button()
        personal_account.wait_close_window_button()
        personal_account.click_on_close_window_button_details()
        personal_account.click_order_feed_button()
        order_feed = OrderFeed(driver)
        order_in_progress = order_feed.get_order_in_progress()
        assert order_in_progress.is_displayed()
