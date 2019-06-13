
#!/usr/bin/python3
"""Test module for base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout
import io

class TestRectangle(unittest.TestCase):
    def test_rect_attr(self):
        """Method tests Rectangle private attributes"""
        Base._Base__nb_objects = 0
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.height, 2)
        r4 = Rectangle(1, 1, 0, 20)
        self.assertEqual(r4.y, 20)
        self.assertEqual(r4.x, 0)
        r4.x = 5
        self.assertEqual(r4.x, 5)

    def test_rect_height(self):
        """Method tests rectangles height attribute"""
        self.assertRaisesRegex(TypeError,
                                "height must be an integer",
                                Rectangle, 10, '2')
        self.assertRaisesRegex(ValueError,
                               "height must be > 0",
                               Rectangle, 10, -2)
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, [1, 2, 3])
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, 1.3)
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, False)
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, "hello")
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, {'1': 1, '2': 2})
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, float('inf'))
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, float('-inf'))
        self.assertRaisesRegex(TypeError,
                               "height must be an integer",
                               Rectangle, 10, float('NaN'))
    def test_rect_width(self):
        """Method tests rectangles width attribute"""
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, '2', 1)
        self.assertRaisesRegex(ValueError,
                               "width must be > 0",
                               Rectangle, -2, 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, [1, 2, 3], 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, 1.3, 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, False, 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, "hello", 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, {'1': 1, '2': 2}, 1)
        self.assertRaisesRegex(TypeError,
                                "width must be an integer",
                                Rectangle, float('inf'), 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, float('-inf'), 1)
        self.assertRaisesRegex(TypeError,
                               "width must be an integer",
                               Rectangle, float('NaN'), 1)

    def test_rect_x(self):
        """Method tests rectangles 'x' attribute"""
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, '2')
        self.assertRaisesRegex(ValueError,
                               "x must be >= 0",
                               Rectangle, 1, 1, -2)
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, [1, 2, 3])
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, 1.3)
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, False)
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, "hello")
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, {'1': 1, '2': 2})
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, float('inf'))
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, float('-inf'))
        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 1, 1, float('NaN'))

    def test_rect_y(self):
        """Method tests rectangles 'y' attribute"""
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, '2')
        self.assertRaisesRegex(ValueError,
                               "y must be >= 0",
                               Rectangle, 1, 1, 1, -2)
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, [1, 2, 3])
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, 1.3)
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, False)
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, "hello")
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, {'1': 1, '2': 2})
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, float('inf'))
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, float('-inf'))
        self.assertRaisesRegex(TypeError,
                               "y must be an integer",
                               Rectangle, 1, 1, 1, float('NaN'))

    def test_rect_area(self):
        """Method tests rectangle area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
        r4 = Rectangle(1, 1)
        self.assertEqual(r4.area(), 1)

    def test_rect_display(self):
        """Method tests the display method of the rectangle"""
        r1 = Rectangle(4, 6)
        self.assertRaises(TypeError, r1.area, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        self.assertEqual(s, "####\n####\n####\n####\n####\n####\n")
        r2 = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = f.getvalue()
        self.assertEqual(s, "##\n##\n")
        r2 = Rectangle(1, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = f.getvalue()
        self.assertEqual(s, "#\n#\n")
        r2 = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = f.getvalue()
        self.assertEqual(s, "#\n")
        r3 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r3.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n  ##\n")
        r3 = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with redirect_stdout(f):
            r3.display()
        s = f.getvalue()
        self.assertEqual(s, " ###\n ###\n")

    def test_rect_str(self):
        """Method tests rectangles __str__ method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_rect_update(self):
        """Method tests rectangles update method"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        r1.update(x=1, height=2, y=3, width=4)
        f = io.StringIO()
        with redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        self.assertEqual(s, "[Rectangle] (89) 1/3 - 4/2\n")

    def test_to_dictionary(self):
        """Method tests to_dictionary method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        dict_t = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, dict_t)
        self.assertEqual(type(r1_dict), dict)
if __name__ == '__main__':
    unittest.main()