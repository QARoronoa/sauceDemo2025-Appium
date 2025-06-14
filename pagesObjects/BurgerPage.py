from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BurgerPage:

    def __init__(self, driver):
        self.driver = driver

    #locators
    button_login_In = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    logout_button = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")
    logout_warning_message = (AppiumBy.ID, "android:id/message")




    #methodes
    def verifier_que_le_titre_est_visible_dans_burger_menu(self, texte):
        title_burger_menu = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{texte}")')
        try :
            titre = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(title_burger_menu))
        except TimeoutError:
            raise AssertionError(f"{texte} n'est pas visible")
        print(titre.get_attribute("text"))



    def click_on_logout_button(self):
        self.driver.find_element(*BurgerPage.logout_button).click()

    def click_login_button_In_burger(self):
        self.driver.find_element(*BurgerPage.button_login_In).click()

    def verify_popin_logout_is_open(self):
        warning_message = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(BurgerPage.logout_warning_message))
        warning_message_text = warning_message.text
        assert warning_message_text == "Are you sure you want to logout"
