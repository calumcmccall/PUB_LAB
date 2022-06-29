import unittest
from src.pub import Pub
from src.drink import Drink

#


class TestPub(unittest.TestCase):

    # When creating setUp make sure the U is capitalized
    def setUp(self):
        self.pub = Pub("The Dancing Pony", 500.00)
        self.pub1 = Pub("Big Fat Lady", 999.00)
        self.tennents = Drink("Tennents", 1.5, 4.5)
        self.white_wine = Drink("Tennents", 2.5, 6)

        self.pub.stock = {
            self.tennents: 99,
            self.white_wine: 45
        }

    # the def here has to start with test_

    def test_pub_has_name(self):
        self.assertEqual("The Dancing Pony", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(500.00, self.pub.cash)

    def test_pub_has_stock(self):
        self.assertEqual(99, self.pub.stock[self.tennents])

    def test_stock(self):
        self.assertEqual(261.0, self.pub.check_stock_value())
