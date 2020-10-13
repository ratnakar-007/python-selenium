from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, dr):
        self.dr = dr

    checkout_product_name = (By.XPATH, "//div[@class='media']//h4")
    checkout_button = (By.CSS_SELECTOR, ".btn-success")
    location_field = (By.ID, "country")
    location_link_text = (By.LINK_TEXT, "India")
    agree_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CLASS_NAME, "btn-success")
    success_message_field = (By.CLASS_NAME, "alert")

    def get_checkout_product_name(self):
        return self.dr.find_element(*ConfirmPage.checkout_product_name)

    def get_checkout_button(self):
        return self.dr.find_element(*ConfirmPage.checkout_button)

    def get_location_field(self):
        return self.dr.find_element(*ConfirmPage.location_field)

    def get_location_link_text(self):
        return self.dr.find_element(*ConfirmPage.location_link_text)

    def get_agree_checkbox(self):
        return self.dr.find_element(*ConfirmPage.agree_checkbox)

    def get_purchase_button(self):
        return self.dr.find_element(*ConfirmPage.purchase_button)

    def get_success_messgae_field(self):
        return self.dr.find_element(*ConfirmPage.success_message_field)