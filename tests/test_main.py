import unittest
from decimal import Decimal
from main import get_set_price


class Test_get_set_price_local(unittest.TestCase):
    """
    Test get_set_price() with a download version of a Lego set's webpage
    """
    return_val_local = get_set_price('./HTML_Docs/cat_owl_html_source.html', from_online=False)

    def test_return_value(self):
        cat_owl_decimal_price = Decimal('49.99')
        self.assertEqual(self.return_val_local, cat_owl_decimal_price)

    def test_return_type(self):
        self.assertIsInstance(self.return_val_local, Decimal)


class Test_get_set_price_online(unittest.TestCase):
    """
    Test get_set_price() with the live version of the Lego set's webpage
    """
    return_val_online = get_set_price('https://www.lego.com/en-us/product/71476')

    def test_return_value(self):
        cat_owl_decimal_price = Decimal('49.99')
        self.assertEqual(self.return_val_online, cat_owl_decimal_price)

    def test_return_type(self):
        self.assertIsInstance(self.return_val_online, Decimal)


if __name__ == '__main__':
    unittest.main()
