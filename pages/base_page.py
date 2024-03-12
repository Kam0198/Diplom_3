from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element_located_click(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
             EC.presence_of_element_located(locator),
             message=f'Element not found in {locator}')
        element.click()

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def scrolldown(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(locator))
    def wait_for_invisibility(self, locator):
        WebDriverWait(self.driver, 40).until(EC.invisibility_of_element(locator))

    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def drag_and_drop_on_element(self, locator_1, locator_2):
        draggable = self.driver.find_element(*locator_1)
        droppable = self.driver.find_element(*locator_2)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    def wait_for_invisibility_overlay(self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element(locator))


