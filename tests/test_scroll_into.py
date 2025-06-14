import time

from pagesObjects.CartPage import CartPage
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage
from pagesObjects.CheckoutPage import CheckoutPage
from pagesObjects.ProductDetails_Page import ProductDetails_Page
from tests.test_add_item_in_cart import test_add_item_in_cart


def test_scroll_into(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)
    productDetails_page = ProductDetails_Page(setup)


    #scroller to purple item
    home_page.scroller_to_violet_back()

    #click on detail violet item
    home_page.click_on_violet_item_back()
    productDetails_page.verifyRedirectionToProductDetails("Sauce Labs Backpack (violet)")
