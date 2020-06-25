import unittest
from more_fun_with_collections import datetime_assignment


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(datetime_assignment.half_birthday(2020, 4, 20), True)


if __name__ == '__main__':
    unittest.main()
