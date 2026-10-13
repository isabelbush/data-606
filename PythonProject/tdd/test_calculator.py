from calculator import subtract

import unittest

class TestCalculator(unittest.TestCase):
    def test_subtract_equals_0(self):
        self.assertEqual(subtract(1, 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-1, -2), 1)

    def subtract(self):
        actual_result = subtract(10, 5)
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()