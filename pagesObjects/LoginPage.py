from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pagesObjects.BasePage import BasePage


class LoginPage(BasePage):

    #locators

    username_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    password_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    button_login = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")
    login_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV")
    username_1 = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username1TV")
    username_2 = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username2TV")
    username_3 = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username3TV")
    logout_button_popin = (AppiumBy.ID, "android:id/button1")
    alert_error_locked_user = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")

    #methodes
    def verifier_login_title_est_visible(self):
        title_login = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(LoginPage.login_title))
        title_login_text = title_login.get_attribute('text')
        assert title_login_text == "Login"


    def enter_username(self, username):
        self.driver.find_element(*LoginPage.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.password_field).send_keys(password)

    def click_button_login(self):
        self.click_when_visible(LoginPage.button_login)

    def click_on_logout_button_in_popin(self):
        self.click_when_visible(LoginPage.logout_button_popin)

    def click_on_user(self, user):
        self.driver.find_element(*user).click()

    def verify_error_message_locked_user(self):
        alert_mess = self.driver.find_element(*LoginPage.alert_error_locked_user)
        assert alert_mess.text == "Sorry this user has been locked out."