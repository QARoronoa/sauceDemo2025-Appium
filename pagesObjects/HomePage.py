from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pagesObjects.BasePage import BasePage


class HomePage(BasePage):

    #locators
    home_page_logo = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/mTvTitle")
    products_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    item_backPack_orange = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(2)')
    item_backPack_violet = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(0)')
    titre_backPack_violet = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Sauce Labs Backpack (violet)")')
    button_burger = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    bottom_message = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("© 2023 Sauce Labs All Rights Reserved. Terms of Service | Privacy Policy")')
    button_review = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.saucelabs.mydemoapp.android:id/start1IV"])[1]')
    message_success_review = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/sortTV")
    continue_button_review = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/closeBt")
    def verifier_que_le_logo_est_visible(self):
        try :
            WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(HomePage.home_page_logo))
        except TimeoutError:
            raise AssertionError(f"titre n'est pas visible")

    def click_button_burger(self):
        self.driver.find_element(*HomePage.button_burger).click()

    def verifier_que_products_title_is_visible(self):
        products_title = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(HomePage.products_title))
        products_title_text = products_title.text
        assert products_title_text == "Products"


    def add_backPack_orange_in_cart(self):
        self.driver.find_element(*HomePage.item_backPack_orange).click()

    def scroller_to_violet_back(self):
        self.scroller_to_element("Sauce Labs Backpack (violet)")


    def click_on_violet_item_back(self):
        self.click_when_visible(HomePage.item_backPack_violet)

    def click_on_item_pictures(self, number):
       self.driver.find_element(AppiumBy.XPATH, f'(//android.widget.ImageView[@content-desc="Product Image"])[{number}]').click()

    def click_on_star_review(self):
        self.click_when_visible(HomePage.button_review)

    def close_popin_review(self):
        self.verifier_title_page_is_visible(HomePage.message_success_review,"Thank you for submitting your review!")
        self.click_when_visible(HomePage.continue_button_review)