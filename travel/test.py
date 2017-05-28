from travel.card import Card
from travel.journey import Journey

import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card(10)

    def test_amounts(self):
        self.assertEqual(self.card.funds, 10)
        self.assertFalse(self.card.can_pay(11))
        self.assertTrue(self.card.can_pay(10))

class JourneyTests(unittest.TestCase):
    def test_zones_travelled(self):
        self.assertEqual(Journey.calculate_num_zones('A', 'E'), 4)
        self.assertEqual(Journey.calculate_num_zones('C', 'A'), 2)
        self.assertRaises(KeyError, Journey.calculate_num_zones, 'E', 'F')
