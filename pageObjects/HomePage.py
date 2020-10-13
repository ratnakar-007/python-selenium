from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input[placeholder='Password']")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    gender = (By.ID, "exampleFormControlSelect1")
    employment_status = (By.CSS_SELECTOR, "input[value='option2']")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    success_message_filed = (By.CLASS_NAME, "alert-success")

    def __init__(self, dr):
        self.dr = dr

    def click_shop_button(self):
        self.dr.find_element(*HomePage.shop).click()
        checkout_Page = CheckoutPage(self.dr)
        return checkout_Page

    def get_name_field(self):
        return self.dr.find_element(*HomePage.name)

    def get_password_field(self):
        return self.dr.find_element(*HomePage.password)

    def get_email_field(self):
        return self.dr.find_element(*HomePage.email)

    def get_checkbox_field(self):
        return self.dr.find_element(*HomePage.checkbox)

    def get_gender_field(self):
        return self.dr.find_element(*HomePage.gender)

    def get_employment_status_field(self):
        return self.dr.find_element(*HomePage.employment_status)

    def get_submit_field(self):
        return self.dr.find_element(*HomePage.submit)

    def get_success_message_field(self):
        return self.dr.find_element(*HomePage.success_message_filed)