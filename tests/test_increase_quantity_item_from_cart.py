import time
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.CartPage import CartPage
from pagesObjects.ProductDetails_Page import ProductDetails_Page
from tests.test_add_item_in_cart import test_add_item_in_cart


def test_increase_quantity_item_from_cart(setup):
    home_page = HomePage(setup)
    cart_page = CartPage(setup)

    #add item in cart
    test_add_item_in_cart(setup)

    #increase quantity
    cart_page.click_on_increase_quantity()

    #verify total items
    cart_page.verify_total_items("2 Items")

    #decrease quantity
    cart_page.click_on_decrease_quantity()

    # verify total items
    cart_page.verify_total_items("1 Items")

