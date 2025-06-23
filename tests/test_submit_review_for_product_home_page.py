import time

from pagesObjects.HomePage import HomePage


def test_submit_review_product_home_page(setup):
    home_page = HomePage(setup)

    # visualiser le titre mydemoApp
    home_page.verifier_que_le_logo_est_visible()

    #mettre une note
    home_page.click_on_star_review()

    #Continue after submit review
    home_page.close_popin_review()





