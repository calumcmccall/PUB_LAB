import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

#


class TestCustomer(unittest.TestCase):

    # When creating setUp make sure the U is capitalized
    def setUp(self):
        self.customer = Customer("Callum", 100.00, 26)
        self.drink = Drink("Tennents", 1.5, 4.5)
        self.pub = Pub("The Prancing Pony", 500.00)

    # the def here has to start with test_

    def test_customer_has_name(self):
        self.assertEqual("Callum", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(26, self.customer.age)

    def test_customer_pays_for(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(98.50, self.customer.wallet)
        self.assertEqual(501.50, self.pub.cash)

    def test_customer_drunker(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(4.5, self.customer.drunkness)
