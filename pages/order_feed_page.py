import allure

from locators.locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeed(BasePage):
    @allure.step("Клик по верхнему заказу")
    def click_top_order(self):
        self.find_element_located_click(OrderFeedPageLocators.order_card)

    @allure.step("Получить текст в модальном окне с деталями")
    def get_modal_window_details(self):
        return self.get_element(OrderFeedPageLocators.details_modal_window)

    @allure.step("Получаем количество заказов за всё время")
    def get_all_time_number(self):
        return self.find_element_located(OrderFeedPageLocators.all_time_order)

    @allure.step("Получаем количество заказов за сегодня")
    def get_time_today(self):
        return self.find_element_located(OrderFeedPageLocators.today_order)

    @allure.step("Получаем номер заказа 'В работе'")
    def get_order_in_progress(self):
        return self.find_element_located(OrderFeedPageLocators.order_in_progress)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_to_constructor_button(self):
        self.find_element_located_click(OrderFeedPageLocators.constructor_button)