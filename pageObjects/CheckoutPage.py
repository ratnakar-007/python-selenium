from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, dr):
        self.dr = dr

    product_name = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    add_to_cart_button = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkout_button = (By.CSS_SELECTOR, ".btn-primary")

    def get_product_name(self):
        return self.dr.find_elements(*CheckoutPage.product_name)

    def get_add_to_card_button(self):
        return self.dr.find_elements(*CheckoutPage.add_to_cart_button)

    def click_on_checkout_button(self):
        self.dr.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.dr)
        return confirm_page
