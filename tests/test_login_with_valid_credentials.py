import time
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.BurgerPage import BurgerPage



def test_connexion(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    burger_page = BurgerPage(setup)

    #visualiser le titre mydemoApp
    home_page.verifier_que_le_logo_est_visible()

    #cliquer sur le bouton burger
    home_page.click_button_burger()
    burger_page.verifier_que_le_titre_est_visible_dans_burger_menu("Log In")

    #cliquer sur login
    burger_page.click_login_button_In_burger()
    login_page.verifier_login_title_est_visible()

    #saisir cresentials
    login_page.enter_username("bod@example.com")
    login_page.enter_password("10203040")

    #cliquer sur login
    login_page.click_button_login()
    home_page.verifier_que_products_title_is_visible()
