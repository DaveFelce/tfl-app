from transport.vehicle import Bus, Tube
import unittest

class Vehicles(unittest.TestCase):

    def test_bus(self):
        bus = Bus()
        self.assertEqual(bus.fare(), 3)

    def test_tube(self):
        tube = Tube()
        self.assertRaises(KeyError, tube.fare, 9)
        self.assertEqual(tube.fare(3), 6)
        self.assertEqual(tube.fare(4), 7)




