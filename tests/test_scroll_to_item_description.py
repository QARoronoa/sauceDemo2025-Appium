from pagesObjects.BurgerPage import BurgerPage
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage
from pagesObjects.ProductDetails_Page import ProductDetails_Page


def test_srcoll_to_item_description(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    burger_page = BurgerPage(setup)
    productDetails_page = ProductDetails_Page(setup)

    # visualiser le titre mydemoApp
    home_page.verifier_que_le_logo_est_visible()

    # click on menu burger
    home_page.click_button_burger()
    burger_page.verifier_que_le_titre_est_visible_dans_burger_menu("Log In")

    # se connecter
    burger_page.click_login_button_In_burger()
    login_page.verifier_login_title_est_visible()
    login_page.click_on_user(LoginPage.username_3)
    login_page.click_button_login()

    #cliquer sur le premier article
    home_page.click_on_item_pictures(1)

    #scroll to item description and verify title and text
    productDetails_page.scroll_to_product_descriptions()
