from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pagesObjects.BasePage import BasePage

class CartPage(BasePage):

    #locators
    title_page_cart = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    remove_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/removeBt")
    no_items_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noItemTitleTV")
    go_shopping_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/shoppingBt")
    button_increase_quantity = (AppiumBy.ACCESSIBILITY_ID, "Increase item quantity")
    button_decrease_quantity = (AppiumBy.ACCESSIBILITY_ID, "Decrease item quantity")
    cart_total_items = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemsTV")
    button_proceed_to_checkout = (AppiumBy.ACCESSIBILITY_ID, "Confirms products for checkout")

    #methodes

    def verifyRedirectionToCartPage(self):
        title = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(CartPage.title_page_cart))
        assert title.text == "My Cart"

    def click_on_remove_button(self):
        self.driver.find_element(*CartPage.remove_button).click()

    def verify_no_items_is_visible(self):
        title_no_Items = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(CartPage.no_items_title))
        assert title_no_Items.text == "No Items"

    def click_on_go_shopping_button(self):
        self.driver.find_element(*CartPage.go_shopping_button).click()

    def click_on_increase_quantity(self):
        self.driver.find_element(*CartPage.button_increase_quantity).click()

    def click_on_decrease_quantity(self):
        self.driver.find_element(*CartPage.button_decrease_quantity).click()

    def verify_total_items(self, total):
        total_itmes = self.driver.find_element(*CartPage.cart_total_items)
        assert total_itmes.text == total

    def click_on_proceed_to_checkout(self):
        self.click_when_visible(CartPage.button_proceed_to_checkout)
