from pageObjects.HomePage import HomePage
from utilis.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        # Home page related code
        homePage = HomePage(self.dr)

        # Checkout page related code
        checkout_page = homePage.click_shop_button()
        product_names = checkout_page.get_product_name()
        i = -1
        for product_name in product_names:
            i = i+1
            product_name = product_name.text
            log.info(product_name)
            if product_name == "iphone X":
                checkout_page.get_add_to_card_button()[i].click()
                break

        # Confirm page related code
        confirm_page = checkout_page.click_on_checkout_button()
        product_checkout = confirm_page.get_checkout_product_name().text
        log.info("Checkout product :"+product_checkout)
        assert product_checkout == "iphone X"
        confirm_page.get_checkout_button().click()
        log.info("Entering location as Ind")
        confirm_page.get_location_field().send_keys("Ind")
        self.verify_link_text("India")
        confirm_page.get_location_link_text().click()
        confirm_page.get_agree_checkbox().click()
        confirm_page.get_purchase_button().click()
        success_message = confirm_page.get_success_messgae_field().text
        print(success_message)
        assert "Success" in success_message
