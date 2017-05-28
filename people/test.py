from people.user import User
import unittest

class TestUser(unittest.TestCase):
    def test_user(self):
        user = User('Mike')
        self.assertEqual(user.name, 'Mike')