import unittest
from src.pub import Pub

#


class TestPub(unittest.TestCase):

    # When creating setUp make sure the U is capitalized
    def setUp(self):
        self.pub = Pub("The Dancing Pony", 500.00)
        self.pub1 = Pub("Big Fat Lady", 999.00)

    # the def here has to start with test_
    def test_pub_has_name(self):
        self.assertEqual("The Dancing Pony", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(500.00, self.pub.cash)
