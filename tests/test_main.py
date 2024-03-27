import unittest
from decimal import Decimal
from main import get_set_price
import os


class Test_get_set_price(unittest.TestCase):
    def test_return_value(self):
        cat_owl_decimal_price = Decimal('49.99')
        return_val = get_set_price('./HTML_Docs/cat_owl_html_source.html', from_online=False)
        self.assertEqual(cat_owl_decimal_price, return_val)


if __name__ == '__main__':
    print("Current Working Directory:", os.getcwd())
    unittest.main()
