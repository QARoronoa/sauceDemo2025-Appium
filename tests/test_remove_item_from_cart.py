import time
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.CartPage import CartPage
from pagesObjects.ProductDetails_Page import ProductDetails_Page
from tests.test_add_item_in_cart import test_add_item_in_cart


def test_remove_item_from_cart(setup):
    home_page = HomePage(setup)
    cart_page = CartPage(setup)
    productDetails_page = ProductDetails_Page(setup)

    #add item in cart
    test_add_item_in_cart(setup)

    #click on remove button
    cart_page.click_on_remove_button()
    cart_page.verify_no_items_is_visible()

    #click go shopping
    cart_page.click_on_go_shopping_button()
    home_page.verifier_que_products_title_is_visible()