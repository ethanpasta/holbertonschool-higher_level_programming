#!/usr/bin/python3
"""Test module for base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Custom unittest class for base module"""

    def test_id(self):
        """Method tests base attribute with different values"""
        Base.__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base('a')
        self.assertEqual(b4.id, 'a')
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base(12)
        self.assertEqual(b6.id, 12)
        b7 = Base([1, 2, 3])
        self.assertEqual(b7.id, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
