import time
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.BurgerPage import BurgerPage




def test_logout(setup):
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
    login_page.click_on_user(LoginPage.username_1)
    login_page.click_button_login()

    #Redirection vers home page
    home_page.verifier_que_products_title_is_visible()

    #cliquer sur le bouton burger
    home_page.click_button_burger()
    burger_page.verifier_que_le_titre_est_visible_dans_burger_menu("Log Out")

    #se deconnecter
    burger_page.click_on_logout_button()
    burger_page.verify_popin_logout_is_open()
    login_page.click_on_logout_button_in_popin()

    #verify redirection to login page
    login_page.verifier_login_title_est_visible()
