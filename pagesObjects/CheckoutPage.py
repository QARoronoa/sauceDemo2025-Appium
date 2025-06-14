from appium.webdriver.common.appiumby import AppiumBy
from pagesObjects.BasePage import BasePage


class CheckoutPage(BasePage):

    #locator adress checkout
    checkout_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutTitleTV")
    fullName_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
    adressLine1_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
    city_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
    zipCode_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
    country_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
    payment_button = (AppiumBy.ACCESSIBILITY_ID, "Saves user info for checkout")

    #locators payment checkout
    title_payment_page = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV")
    card_full_name = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    cardNumber_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
    expirationDate_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
    secrityCode_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
    reviewOrder_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")

    #locators review order
    title_review_order = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
    item_name = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    place_order_button = (AppiumBy.ACCESSIBILITY_ID, "Completes the process of checkout")
    mess_thanks_for_order = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/thankYouTV")
    continue_shopping_button = (AppiumBy.ACCESSIBILITY_ID, "Tap to open catalog")


    #methodes

    def verify_title_checkout_is_visible(self):
        self.verifier_title_page_is_visible(CheckoutPage.checkout_title, "Checkout")

    def fill_adress_checkout(self, fullName, adressLine1, country, city, zipCode):
        self.fill_input_field(CheckoutPage.fullName_field, fullName)
        self.fill_input_field(CheckoutPage.adressLine1_field, adressLine1)
        self.fill_input_field(CheckoutPage.city_field, city)
        self.fill_input_field(CheckoutPage.zipCode_field, zipCode)
        self.fill_input_field(CheckoutPage.country_field, country)

        self.click_when_visible(CheckoutPage.payment_button)

    def verify_payment_page(self):
        self.verifier_title_page_is_visible(CheckoutPage.title_payment_page, "Enter a payment method")

    def fill_payment_checkout(self, fullName, cardNumber, expirationDate, securityCode):
        self.fill_input_field(CheckoutPage.card_full_name, fullName)
        self.fill_input_field(CheckoutPage.cardNumber_field, cardNumber)
        self.fill_input_field(CheckoutPage.expirationDate_field, expirationDate)
        self.fill_input_field(CheckoutPage.secrityCode_field, securityCode)

        self.click_when_visible(CheckoutPage.reviewOrder_button)

    def verify_review_order_page(self):
        self.verifier_title_page_is_visible(CheckoutPage.title_review_order,"Review your order")

    def verify_item_is_present(self):
        self.verifier_title_page_is_visible(CheckoutPage.item_name, "Sauce Labs Backpack (orange)")

    def click_place_order_button(self):
        self.click_when_visible(CheckoutPage.place_order_button)

    def verify_message_continue_shopping_is_visible(self):
        self.verifier_title_page_is_visible(CheckoutPage.mess_thanks_for_order, "Thank you for your order")

    def click_on_button_continue_shopping(self):
        self.click_when_visible(CheckoutPage.continue_shopping_button)

