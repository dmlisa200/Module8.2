import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_A_value(self):
        self.assertEqual(assign_average.switch_average('A'), 'Ankeny')

    def test_B_value(self):
        self.assertEqual(assign_average.switch_average('B'), 'Ames')

    def test_C_value(self):
        self.assertEqual(assign_average.switch_average('C'), 'Waukee')

    def test_D_value(self):
        self.assertEqual(assign_average.switch_average('D'), 'Grimes')

    def test_E_value(self):
        self.assertEqual(assign_average.switch_average('E'), 'Des Moines')

    def test_other_value(self):
        self.assertEqual(assign_average.switch_average('F'), 'Invalid town name')

if __name__ == '__main__':
    unittest.main()
