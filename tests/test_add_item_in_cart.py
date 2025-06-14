import time
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.CartPage import CartPage
from pagesObjects.ProductDetails_Page import ProductDetails_Page

def test_add_item_in_cart(setup):
    home_page = HomePage(setup)
    cart_page = CartPage(setup)
    productDetails_page = ProductDetails_Page(setup)

    # visualiser le titre mydemoApp
    home_page.verifier_que_le_logo_est_visible()

    #selectionner un article
    home_page.add_backPack_orange_in_cart()
    productDetails_page.verifyRedirectionToProductDetails("Sauce Labs Backpack (orange)")

    #click add to cart button
    productDetails_page.click_on_add_to_cart()
    productDetails_page.checkCartIconShowsItemCount()

    #click on cart button
    productDetails_page.click_on_cart_button()
    cart_page.verifyRedirectionToCartPage()
