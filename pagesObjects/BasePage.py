from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_when_visible(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        element.click()

    def is_visible(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def assert_element_displayed(self, locator):
        element = self.driver.find_element(*locator)
        element.is_displayed(), f"element {locator} is not visibible"

    def verifier_title_page_is_visible(self, locator, title_page):
        title = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        title_text = title.get_attribute('text')
        assert title_text == title_page

    def fill_input_field(self, locator, text, timeout=10):
        self.is_visible(locator, timeout)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def scroller_to_element(self, text):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,f"new UiScrollable(new UiSelector()).scrollIntoView(text(\"{text}\"));")