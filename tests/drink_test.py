import unittest
from src.drink import Drink

#


class TestDrink(unittest.TestCase):

    # When creating setUp make sure the U is capitalized
    def setUp(self):
        self.drink = Drink("Red Bull", 1.5, 0)

    # the def here has to start with test_

    def test_drink_has_name(self):
        self.assertEqual("Red Bull", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(1.5, self.drink.price)
