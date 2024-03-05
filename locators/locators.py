from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_account_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # кнопка "Личный кабинет" на
    # главной странице
    login_button = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # кнопка "Войти в аккаунт" на главной
    # странице
    main_page_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]


class PersonalAccountPageLocators:
    personal_account_button_enter = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # кнопка "Личный кабинет"
    # внутри ЛК
    order_history = (By.XPATH, "//a[contains(text(),'История заказов')]")  # кнопка "История заказов" внутри ЛК
    exit_button = (By.XPATH, "// button[contains(text(), 'Выход')]")  # кнопка "Выход" внутри ЛК

    constructor_button = (By.XPATH, "//p[contains(., 'Конструктор')]")  # кнопка "Конструктор" внутри ЛК
    order_feed = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # кнопка "Лента заказов" внутри ЛК

    ingredients = (By.CSS_SELECTOR, "[class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'] "
                                    "[alt='Флюоресцентная булка R2-D3']")  # номер заказа
    basket = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket']")
    counter_1 = (By.CSS_SELECTOR, "[class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'] "
                                  "[class*='counter_counter'] p")  # счетчик 1
    ingredients_details = (By.XPATH, "// h2[contains(text(), 'Детали ингредиента')]")  # модальное окно с деталями
    ingredients_details_close = (
        By.CSS_SELECTOR, "[class*='Modal_modal__close_modified']")  # кнопка крестика модального окна
    ordering_button = (By.XPATH, "// button[contains(text(), 'Оформить заказ')]")  # кнопка "Оформить заказ" внутри ЛК
    accept_order_modal_window = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")  # модальное окно с
    # подтверждением заказа


class LoginPageLocators:
    email_field_auth = (By.XPATH, "//input[@type='text']")  # поле для ввода email на странице авторизации
    password_field_auth = (By.XPATH, "//input[@type='password']")  # поле для ввода пароля на странице авторизации
    login_button_auth = (By.XPATH, "//button[contains(text(),'Войти')]")  # кнопка "Войти"" на странице авторизации
    registration_button_auth = (
        By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")  # кнопка зарегистрироваться на странице авторизации
    password_recovery_auth = (
        By.XPATH, "// a[contains(text(), 'Восстановить пароль')]")  # кнопка восстановить пароль на странице авторизации
    header_enter = (By.XPATH, "//h2[contains(text(),'Вход')]")  # заголовок "Вход" на странице авторизации


class ForgotPasswordPageLocators:
    password_recovery_email_field = (
        By.CSS_SELECTOR,
        "[class='text input__textfield text_type_main-default'][type='text']"
    )  # поле для ввода email на странице восстановления пароля
    password_recovery_button = (By.XPATH, "//button[contains(text(),'Восстановить')]")  # кнопка "Восстановить" на
    # странице восстановления пароля


class ResetPasswordPageLocators:
    recovery_password_field = (By.XPATH, '//div[contains(@class, "input_status_active")]')
    code_password_recovery_field = (
        By.XPATH, "// label[contains(text(), 'Введите код из письма')]")  # поле для ввода кода из письма
    password_icon_action = (
        By.CSS_SELECTOR,
        "[class='input__icon input__icon-action'] [xmlns='http://www.w3.org/2000/svg']"
    )  # иконка скрытия пароля


class OrderFeedPageLocators:
    order_card = (
        By.CSS_SELECTOR,
        "[class='OrderHistory_listItem__2x95r mb-6']"
    )  # карточка заказа в списке
    all_time_order = (
        By.CSS_SELECTOR, "[class='undefined mb-15'] p:nth-child(2)")  # выполнено за все время
    today_order = (By.XPATH, "//div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")  # выполнено
    # за сегодня
    order_in_progress = (By.XPATH, "//div/div[1]/div[1]/div[1]/ul[2]/li[1]"
                                   "[@class='text text_type_digits-default mb-2']")  # в работе
    details_modal_window = (By.XPATH, "//p[contains(text(),'Cостав')]")  # состав внутри карточки заказа
    constructor_button = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # кнопка конструктора

