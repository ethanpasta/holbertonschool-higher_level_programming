#!/usr/bin/python3
"""Module for testing Square class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
from contextlib import redirect_stdout

class TestSquare(unittest.TestCase):
    """Custom unittest class for Square module"""

    def test_square_attr(self):
        """Method tests squares attributes"""
        Base._Base__nb_objects = 0
        self.assertRaises(TypeError, Square)
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_square_x(self):
        """Method tests squares 'x' attribute"""
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, '2')
        self.assertRaisesRegex(ValueError,
                               "x must be >= 0",
                               Square, 1, -2)
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, [1, 2, 3])
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, 1.3)
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, False)
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, "hello")
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, {'1': 1, '2': 2})
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, float('inf'))
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, float('-inf'))
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Square, 1, float('NaN'))

    def test_rect_y(self):
        """Method tests rectangles 'y' attribute"""
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, '2')
        self.assertRaisesRegex(ValueError,
                               "y must be >= 0",
                               Square, 1, 1, -2)
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, [1, 2, 3])
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, 1.3)
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, False)
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, "hello")
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, {'1': 1, '2': 2})
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, float('inf'))
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, float('-inf'))
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Square, 1, 1, float('NaN'))

    def test_square_size(self):
        """Method tests squares size attribute"""
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, '2')
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, 0)
        self.assertRaisesRegex(ValueError,
                               "width must be > 0",
                               Square, -2)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, [1, 2, 3])
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, 1.3)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, False)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, "hello")
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, {'1': 1, '2': 2}, 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, float('inf'))
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, float('-inf'))
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Square, float('NaN'))
    def test_square_area(self):
        """Method tests squares area"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s1.size = 10
        self.assertEqual(s1.area(), 100)

    def test_square_display(self):
        """Method tests squares string representation"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = f.getvalue()
        self.assertEqual(s, "#####\n#####\n#####\n#####\n#####\n")
        f = io.StringIO()
        with redirect_stdout(f):
            print(s1)
        s = f.getvalue()
        self.assertEqual(s, "[Square] (1) 0/0 - 5\n")
        s2 = Square(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = f.getvalue()
        self.assertEqual(s, "  ##\n  ##\n")
        f = io.StringIO()
        with redirect_stdout(f):
            print(s2)
        s = f.getvalue()
        self.assertEqual(s, "[Square] (2) 2/0 - 2\n")
        s3 = Square(3, 1, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        self.assertEqual(s,"\n\n\n ###\n ###\n ###\n")
        f = io.StringIO()
        with redirect_stdout(f):
            print(s3)
        s = f.getvalue()
        self.assertEqual(s, "[Square] (3) 1/3 - 3\n")

    def test_square_update(self):
        """Test square update method"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 5)
        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 2)
        s1.update(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 2)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.size, 2)
        s1.update(x=12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.size, 2)
        s1.update(size=7, y=1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.size, 7)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.size, 7)

    def test_to_dictionary(self):
        """Test method for to_dictionary"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        s1_dict_t = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dict, s1_dict_t)
        self.assertEqual(type(s1_dict), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertEqual(s1 == s2, False)

    def test_create(self):
        """Method tests rectangles create method"""
        r1 = Square(3, 5, 1)
        r1_dic = r1.to_dictionary()
        r2 = Square.create(**r1_dic)
        self.assertEqual(str(r1), str(r2))

    def test_save_to_file(self):
        """Method tests squares save_to_file method"""
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([r1, r2])
        with open('Square.json', 'r') as f:
            self.assertEqual(len(f.read()), len(str([r1.to_dictionary(), r2.to_dictionary()])))
        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file(None)
        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), "[]")
        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file(self):
        """Method tests load_from_file method"""
        r1 = Square(5)
        r2 = Square(7, 9, 1)
        list_input = [r1, r2]
        Square.save_to_file(list_input)
        list_output = Square.load_from_file()
        self.assertEqual(str(list_input[0].to_dictionary()), str(list_output[0].to_dictionary()))
