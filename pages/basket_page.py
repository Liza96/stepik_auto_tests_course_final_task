from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def sould_be_empty_baskets_message(self):
        baskets_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        empty_message = "Your basket is empty."
        assert baskets_message.find(empty_message) != -1, "No empty message, but it should be"

    def sould_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS) == True,\
            "Items in basket are presented, but should not be"