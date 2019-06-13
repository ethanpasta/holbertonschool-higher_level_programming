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

    def test_to_json_string(self):
        """Method tests to_json_string method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dic = r1.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic_t = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dic_t = '[{"width": 10, "y": 8, "id": 1, "x": 2, "height": 7}]'
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(json_dic), str)

if __name__ == '__main__':
    unittest.main()
