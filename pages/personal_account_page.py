import allure

from locators.locators import PersonalAccountPageLocators, MainPageLocators
from pages.base_page import BasePage


class PersonalAccount(BasePage):
    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_personal_account_button(self):
        self.find_element_located_click(PersonalAccountPageLocators.personal_account_button_enter)

    @allure.step("Ожиданием загрузки страницы ЛК")
    def wait_personal_account_page(self):
        self.wait_for_visibility(MainPageLocators.main_page_locator)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_ordering_button(self):
        self.find_element_located_click(PersonalAccountPageLocators.ordering_button)

    @allure.step("Получить текст 'Ваш заказ начали готовить' после оформления заказа")
    def get_accept_order_text(self):
        return self.get_element(PersonalAccountPageLocators.accept_order_modal_window)

    @allure.step("Клик по кнопке 'История заказов'")
    def click_history_order_button(self):
        self.find_element_located_click(PersonalAccountPageLocators.order_history)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.find_element_located_click(PersonalAccountPageLocators.ingredients)

    @allure.step("Получить текст 'Детали ингредиента'")
    def get_ingredients_details(self):
        return self.get_element(PersonalAccountPageLocators.ingredients_details)

    @allure.step("Клик по крестику в модальном окне в деталях ингредиента")
    def click_on_close_window_button_details(self):
        self.find_element_located_click(PersonalAccountPageLocators.ingredients_details_close)

    @allure.step("Перенос ингредиента в заказ")
    def drag_and_drop_elements(self):
        self.drag_and_drop_on_element(PersonalAccountPageLocators.ingredients, PersonalAccountPageLocators.basket)

    @allure.step("Получение первого счетчика")
    def first_counter(self):
        return self.find_element_located(PersonalAccountPageLocators.counter_1)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.find_element_located_click(PersonalAccountPageLocators.order_feed)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.find_element_located_click(PersonalAccountPageLocators.constructor_button)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_button(self):
        return self.find_element_located_click(PersonalAccountPageLocators.exit_button)

    @allure.step("Ожидаем элемент закрытия модального окна")
    def wait_for_invisibility_close_window(self):
        self.wait_for_visibility(PersonalAccountPageLocators.ingredients_details_close)

    # @allure.step("Ожидаем отображение кнопки 'Оформить заказ'")
    # def wait_for_invisibility_ordering_button(self):
    #     self.wait_for_clickable(PersonalAccountPageLocators.ordering_button)
    #
    # @allure.step('Проверяем наличие модального окна "Детали ингредиента"')
    # def find_ingredient_details_window(self):
    #     return self.find_element_located(MainPageLocators.main_page_locator)

    @allure.step("Ожидаем отображение кнопки 'Выход'")
    def wait_for_invisibility_logout_button(self):
        self.wait_for_clickable(PersonalAccountPageLocators.exit_button)

    @allure.step("Ожидаем элемент закрытия модального окна")
    def wait_close_window_button(self):
        self.wait_for_clickable(PersonalAccountPageLocators.ingredients_details_close)

    @allure.step("Ожидаем элемент 'Оформить заказ'")
    def wait_ordering_button(self):
        self.wait_for_clickable(PersonalAccountPageLocators.ordering_button)
