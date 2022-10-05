#!/usr/bin/python3
"""Python Interpreter"""
from contextlib import redirect_stdout
import io
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """this will test Square's capacity"""

    def test_1(self):
        """init args(1)"""
        self.s = Square(1)
        self.assertEqual(self.s.size, 1)

    def test_1b(self):
        """init args(1, 2)"""
        self.s = Square(1, 2)
        self.assertEqual(self.s.width, 1)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.x, 2)

    def test_1c(self):
        """init args("1", 2), etc"""
        self.assertRaises(TypeError, Square, "1", 2)
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")

    def test_1d(self):
        self.s = Square(1, 2, 3)
        self.assertEqual(self.s.width, 1)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 3)

    def test_1e(self):
        self.s = Square(1, 2, 3, 4)
        self.assertEqual(self.s.width, 1)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 3)
        self.assertEqual(self.s.id, 4)

    def test_1f(self):
        """init args (-1, 2)"""
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
