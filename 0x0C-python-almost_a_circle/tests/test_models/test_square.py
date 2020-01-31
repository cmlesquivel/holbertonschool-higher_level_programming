#!/usr/bin/python3
"""
Contains tests for Rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import sys
import io
from os import path, remove
from contextlib import redirect_stdout


class TestAttr(unittest.TestCase):
    """Tests to check the attributes of Base class"""

    def setUp(self):
        """Define in zero at the atributte"""
        Base._Base__nb_objects = 0

    def test_attribute_id(self):
        """Check the atributtes of Class and Id"""
        b1 = Square(10)
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b2 = Square(2)
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        b3 = Square(10, 2, 0, 12)
        self.assertEqual(b3.id, 12)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_attributes_object(self):
        """Check the atributtes of atributtes object"""
        b1 = Square(10)
        self.assertEqual(b1.size, 10)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)
        self.assertEqual(b1.id, 1)

        b2 = Square(2, 1, 10, 5)
        self.assertEqual(b2.size, 2)
        self.assertEqual(b2.x, 1)
        self.assertEqual(b2.y, 10)
        self.assertEqual(b2.id, 5)


class ValidateAttr(unittest.TestCase):
    """Validate the attributes of object class"""

    def setUp(self):
        """Define in zero at the atributte"""
        Base._Base__nb_objects = 0

    def test_validate_attr_obj(self):
        """validate the atributtes of object"""
        with self.assertRaises(TypeError):
            b1 = Square('5')

        with self.assertRaises(ValueError):
            b1 = Square(0)

        with self.assertRaises(ValueError):
            b1 = Square(-5)

        with self.assertRaises(ValueError):
            b1 = Square(1, -5)

        with self.assertRaises(ValueError):
            b1 = Square(5, 55, -5, 6)

        with self.assertRaises(TypeError):
            b1 = Square(5, 55, None, 6)

        with self.assertRaises(TypeError):
            b1 = Square(5, 55, {'a': 5}, 6)

        with self.assertRaises(TypeError):
            b1 = Square(5, (5, 6), None, 6)

        with self.assertRaises(TypeError):
            b1 = Square(5, [5], 5, 6)

        with self.assertRaises(TypeError):
            b1 = Square(5.6, 54, 5, 6)


class ValidateArea(unittest.TestCase):
    """Validate the area method of object class"""

    def setUp(self):
        """Define in zero at the atributte"""
        Base._Base__nb_objects = 0

    def test_validate_area(self):
        """validate the area method of object"""

        b1 = Square(2, 10, 10, 10)
        self.assertEqual(b1.area(), 4)

        b1 = Square(20, 1)
        self.assertEqual(b1.area(), 400)

    def test_display_whxy(self):
        """Testing the display method"""
        with io.StringIO() as buffer, redirect_stdout(buffer):
            b2 = Square(3, 3, 2, 3)
            b2.display()
            output = buffer.getvalue()
            print(output)
            self.assertEqual(output, "\n" * 2 + (" " * 3 + "#" * 3 + "\n") * 3)

    def test_display_wh(self):
        """Testing the display method"""
        with io.StringIO() as buffer, redirect_stdout(buffer):
            b2 = Square(3, 0)
            b2.display()
            output = buffer.getvalue()
            print(output)
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_str_(self):
        """Testing the _str_ method"""
        b1 = Square(3, 1, 3)
        self.assertEqual(str(b1), '[Square] (1) 1/3 - 3')

        b2 = Square(5)
        self.assertEqual(str(b2), '[Square] (2) 0/0 - 5')

    def test_update(self):
        """Testing the update method, *args"""
        r1 = Square(5)

        r1.update(10)
        self.assertEqual(str(r1), '[Square] (10) 0/0 - 5')

        r1.update(1, 2, 3, 4)
        self.assertEqual(str(r1), '[Square] (1) 3/4 - 2')

    def test_to_dictionary(self):
        """Testing the to dictionary method"""
        r1 = Square(10, 2, 1)
        my_square = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertDictEqual(r1.to_dictionary(), my_square)

    def test_create(self):
        """Testing the to create method"""

        my_dictionary = {'x': 1}
        r2 = Square.create(**my_dictionary)
        self.assertEqual(str(r2), '[Square] (1) 1/0 - 1')

        my_dictionary = {'x': 1, 'y': 9}
        r2 = Square.create(**my_dictionary)
        self.assertEqual(str(r2), '[Square] (2) 1/9 - 1')

        my_dictionary = {'x': 1, 'y': 9, 'id': 1}
        r2 = Square.create(**my_dictionary)
        self.assertEqual(str(r2), '[Square] (1) 1/9 - 1')

        my_dictionary = {'x': 1, 'y': 9, 'id': 1, 'size': 2}
        r2 = Square.create(**my_dictionary)
        self.assertEqual(str(r2), '[Square] (1) 1/9 - 2')

    def test_save_to_file(self):
        """Testing the to save to file method"""
        r1 = Square(10, 7, 2, 8)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            contents = file.read()

        str_return = Base.from_json_string(contents)

        my_list = [{"y": 2, "x": 7, "id": 8, "size": 10}]
        self.assertEqual(str_return, my_list)

    def test_save_to_file_none(self):
        """Testing the to save to file method none"""

        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            contents = file.read()

        str_return = Base.from_json_string(contents)

        my_list = []
        self.assertEqual(str_return, my_list)

    def test_save_to_file_list(self):
        """Testing the to save to file method list"""

        Square.save_to_file([])

        with open("Square.json", "r") as file:
            contents = file.read()

        str_return = Base.from_json_string(contents)

        my_list = []
        self.assertEqual(str_return, my_list)

    def test_save_to_file_list_value(self):
        """Testing the to save to file method list value"""

        Square.save_to_file([Square(1, 2)])

        with open("Square.json", "r") as file:
            contents = file.read()

        str_return = Base.from_json_string(contents)

        my_list = [{"y": 0, "x": 2, "id": 1, "size": 1}]
        self.assertEqual(str_return, my_list)

    def test_save_to_file_empty(self):
        """Testing the to save to file method empty"""

        with self.assertRaises(TypeError):
            Square.save_to_file()
