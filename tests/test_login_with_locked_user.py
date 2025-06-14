import time
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.BurgerPage import BurgerPage

def test_login_with_locked_user(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    burger_page = BurgerPage(setup)

    #visualiser le titre mydemoApp
    home_page.verifier_que_le_logo_est_visible()

    #click on menu burger
    home_page.click_button_burger()
    burger_page.verifier_que_le_titre_est_visible_dans_burger_menu("Log In")

    #se connecter
    burger_page.click_login_button_In_burger()
    login_page.verifier_login_title_est_visible()

    login_page.click_on_user(login_page.username_2)
    login_page.click_button_login()

    #verify alert message
    login_page.verify_error_message_locked_user()
