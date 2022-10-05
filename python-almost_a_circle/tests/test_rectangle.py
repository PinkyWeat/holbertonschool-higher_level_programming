#!/usr/bin/python3
"""Python Interpreter"""
import unittest
from models.rectangle import Rectangle

class TestRectangle1(unittest.TestCase):
    """this will test Rectangle's capacity"""

    def test_1(self):
        """init args(1, 2)"""
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)

    def test_1b(self):
        """init args(1, 2, 3)"""
        self.r = Rectangle(1, 2, 3)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)

    def test_1c(self):
        """init args(1, 2, 3, 4)"""
        self.r = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_1d(self):
        """init args("1", 2), etc"""
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_1e(self):
        """init args (1, 2, 3, 4, 5)"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)
        self.assertEqual(self.r.id, 5)

    def test_1f(self):
        """init args (-1, 2)"""
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

class TestRectangleArea(unittest.TestCase):
    """tests the area method"""
    def setUp(self):
        self.r = Rectangle(1, 2)

    def test_1(self):
        self.assertEqual(self.r.area(), 2)
