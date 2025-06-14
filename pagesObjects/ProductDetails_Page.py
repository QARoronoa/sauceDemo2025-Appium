from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pagesObjects.BasePage import BasePage


class ProductDetails_Page(BasePage):

    #locators
    add_to_cart_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    number_item_in_cart = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)')
    cart_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
    title_page_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    product_highlights_id = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productHeightLightsTV")
    product_highlights_description = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/descTV")
    #methodes

    def click_on_add_to_cart(self):
        self.driver.find_element(*ProductDetails_Page.add_to_cart_button).click()

    def verifyRedirectionToProductDetails(self, article_titre):
        title = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProductDetails_Page.title_page_item))
        title_text =title.text
        assert title_text == article_titre


    def checkCartIconShowsItemCount(self):
        quantity = self.driver.find_element(*ProductDetails_Page.number_item_in_cart)
        assert quantity.is_displayed()

    def click_on_cart_button(self):
        self.driver.find_element(*ProductDetails_Page.cart_button).click()

    def scroll_to_product_descriptions(self):
        self.scroller_to_element("Product Highlights")
        self.verifier_title_page_is_visible(ProductDetails_Page.product_highlights_id,"Product Highlights")
        self.scroller_to_element("carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
        item_description = self.driver.find_element(*ProductDetails_Page.product_highlights_description)
        assert "carry" in item_description.text