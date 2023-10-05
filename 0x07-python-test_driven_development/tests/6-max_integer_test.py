#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_integers(self):
        """Test valid integers."""
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)
        self.assertEqual(max_integer([50]), 50)
        self.assertEqual(max_integer([-5, -10, -15]), -5)
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-2, -6, -8, -4]), -2)

    def test_floats(self):
        """Test valid floats."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3]), -1.1)
        self.assertEqual(max_integer([0.5, -0.1, 0.0]), 0.5)

    def test_other_types(self):
        """Test other compatible data types."""
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([True, False, True]), True)


if __name__ == '__main__':
    unittest.main()
