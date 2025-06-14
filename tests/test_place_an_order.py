from pagesObjects.CartPage import CartPage
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage
from pagesObjects.CheckoutPage import CheckoutPage
from pagesObjects.ProductDetails_Page import ProductDetails_Page
from tests.test_add_item_in_cart import test_add_item_in_cart


def test_place_an_order(setup, fill_adress_form, fill_payment_form):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)
    productDetails_page = ProductDetails_Page(setup)

    #add item in cart
    test_add_item_in_cart(setup)

    #click on proceed to checkout
    cart_page.click_on_proceed_to_checkout()

    #verifier redirection to login page
    login_page.verifier_login_title_est_visible()

    #enter valide credentials and click on login button
    login_page.click_on_user(login_page.username_1)
    login_page.click_button_login()

    #verify redirection to checkout page
    checkout_page.verify_title_checkout_is_visible()

    #fill shipping adress form and click payment button
    checkout_page.fill_adress_checkout(**fill_adress_form)

    #verify redirection to payment page and fill form
    checkout_page.verify_payment_page()
    checkout_page.fill_payment_checkout(**fill_payment_form)

    #verify redirection to review order and confirm order
    checkout_page.verify_review_order_page()
    checkout_page.verify_item_is_present()
    checkout_page.click_place_order_button()

    #verify redirection to checkout complete page and click on continue shopping
    checkout_page.verify_message_continue_shopping_is_visible()
    checkout_page.click_on_button_continue_shopping()
    home_page.verifier_que_le_logo_est_visible()
