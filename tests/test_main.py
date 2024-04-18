import unittest
from decimal import Decimal
from main import LegoPriceTracker


class TestPriceLegoWebsite(unittest.TestCase):
    """
    Test get_set_price() with the live version of the Lego set's webpage
    """

    test_set = LegoPriceTracker('71476')
    return_val_online = test_set.get_price_lego_website()

    def test_return_value(self):
        cat_owl_decimal_price = Decimal('49.99')
        self.assertEqual(self.return_val_online, cat_owl_decimal_price)

    def test_return_type(self):
        self.assertIsInstance(self.return_val_online, Decimal)


if __name__ == '__main__':
    unittest.main()
