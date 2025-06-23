import time

from pagesObjects.HomePage import HomePage
from pagesObjects.ProductDetails_Page import ProductDetails_Page


def test_submit_review_product_details_page(setup):
    home_page = HomePage(setup)
    productDetails_page = ProductDetails_Page(setup)

    # visualiser le titre mydemoApp
    home_page.verifier_que_le_logo_est_visible()

    # selectionner un article
    home_page.add_backPack_orange_in_cart()
    productDetails_page.verifyRedirectionToProductDetails("Sauce Labs Backpack (orange)")

    # click on star_button
    productDetails_page.click_on_star_button()

    #verifer message in popin & continye button
    home_page.close_popin_review()
