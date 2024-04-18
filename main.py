import requests
from decimal import Decimal
from bs4 import BeautifulSoup


class LegoPriceTracker:
    """
    A instance of this class keeps info regarding a specific Lego set's price.
    """

    __price = None

    def __init__(self, set_num):
        """
        :param set_num: Lego's ID number for the specific set
        """
        # TODO: what should be done if an invalid set number is given?
        self.set_num = set_num

    def get_price_lego_website(self):
        """
        Program that returns the price of the Lego set assign to the class instance

        :return: The current price of the set from Lego.com
        """

        url = f'https://www.lego.com/en-us/product/{self.set_num}'
        # using headers to speed up response time
        # https://stackoverflow.com/questions/62599036/python-requests-is-slow-and-takes-very-long-to-complete-http-or-https-request
        headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 ("
                                 "KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
        response = requests.get(url, headers=headers)
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')

        # find the price data, get the price by itself, then change the price into a decimal.
        prices = soup.find_all("meta", property='product:price:amount')
        price = prices[0].get(
            "content")  # set page should only have 1 price, but might need to make
        # edge cases for when a set's page has more than 1 price on it.
        self.__price = Decimal(price)

        return self.__price
