#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_norma(self):
        l = [5, 1, 2, 3]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_mixed(self):
        l = [4, 'a', 3]
        self.assertRaises(TypeError, max_integer, l)

    def test_none_arg(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_negative(self):
        l = [1, -2, 0, -3]
        result = max_integer(l)
        self.assertEqual(result, 1)

    def test_empty(self):
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_not_list(self):
        self.assertRaises(TypeError, max_integer, 9)

    def test_float(self):
        l = [1.2, 4.4, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        l = ["abc", "abcd", "zab"]
        result = max_integer(l)
        self.assertEqual(result, "zab")

    def test_one(self):
        l = [10]
        result = max_integer(l)
        self.assertEqual(result, 10)

    def test_unique(self):
        l = [5, 5, 5, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_middle(self):
        l = [1, 2, 10, 3, 1]
        result = max_integer(l)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
