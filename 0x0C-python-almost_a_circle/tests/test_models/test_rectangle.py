#!/usr/bin/python3
"""
Contains tests for Rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
import io
from os import path, remove
from contextlib import redirect_stdout


class TestAttr(unittest.TestCase):
    """Tests to check the attributes of class"""

    def setUp(self):
        """Define in zero at the atributte"""
        Base._Base__nb_objects = 0

    def test_attribute_id(self):
        """Check the atributtes of Class and Id atributte object"""
        b1 = Rectangle(10, 2)
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b2 = Rectangle(2, 10)
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        b3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(b3.id, 12)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_attributes_object(self):
        """Check the atributtes of atributtes object"""
        b1 = Rectangle(10, 2)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

        b2 = Rectangle(2, 10, 10, 10)
        self.assertEqual(b2.width, 2)
        self.assertEqual(b2.height, 10)
        self.assertEqual(b2.x, 10)
        self.assertEqual(b2.y, 10)


class ValidateAttr(unittest.TestCase):
    """Validate the attributes of object class"""

    def setUp(self):
        """Define in zero at the atributte"""
        Base._Base__nb_objects = 0

    def test_validate_attr_obj(self):
        """validate the atributtes of object"""
        with self.assertRaises(TypeError):
            b1 = Rectangle(5, '5')

        with self.assertRaises(ValueError):
            b1 = Rectangle(5, 0)

        with self.assertRaises(ValueError):
            b1 = Rectangle(0, 6)

        with self.assertRaises(ValueError):
            b1 = Rectangle(5, -5)

        with self.assertRaises(ValueError):
            b1 = Rectangle(-5, 3)

        with self.assertRaises(ValueError):
            b1 = Rectangle(5, 55, -5, 6)

        with self.assertRaises(TypeError):
            b1 = Rectangle(5, 55, None, 6)

        with self.assertRaises(TypeError):
            b1 = Rectangle(5, 55, {'a': 5}, 6)

        with self.assertRaises(TypeError):
            b1 = Rectangle(5, (5, 6), None, 6)

        with self.assertRaises(TypeError):
            b1 = Rectangle(5, [5], 5, 6)

        with self.assertRaises(TypeError):
            b1 = Rectangle(5.6, 54, 5, 6)


class ValidateMethods(unittest.TestCase):
    """Validate the area method of object class"""

    def setUp(self):
        """Define in zero at the atributte"""
        Base._Base__nb_objects = 0

    def test_validate_area(self):
        """validate the area method of object"""

        b1 = Rectangle(2, 10, 10, 10)
        self.assertEqual(b1.area(), 20)

        b1 = Rectangle(20, 1)
        self.assertEqual(b1.area(), 20)

    def test_display_whxy(self):
        """Testing the display method"""
        with io.StringIO() as buffer, redirect_stdout(buffer):
            b2 = Rectangle(3, 3, 2, 3)
            b2.display()
            output = buffer.getvalue()
            print(output)
            self.assertEqual(output, "\n" * 3 + (" " * 2 + "#" * 3 + "\n") * 3)

    def test_display_wh(self):
        """Testing the display method"""
        with io.StringIO() as buffer, redirect_stdout(buffer):
            b2 = Rectangle(3, 3)
            b2.display()
            output = buffer.getvalue()
            print(output)
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_str_(self):
        """Testing the _str_ method"""
        b1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(b1), '[Rectangle] (12) 2/1 - 4/6')

        b2 = Rectangle(5, 5, 1)
        self.assertEqual(str(b2), '[Rectangle] (1) 1/0 - 5/5')

    def test_update(self):
        """Testing the update method, *args"""
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_to_dictionary(self):
        """Testing the to dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        my_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r1.to_dictionary(), my_dictionary)

    def test_create(self):
        """Testing the to create method"""

        my_dictionary = {'x': 1}
        r2 = Rectangle.create(**my_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 1/1')

        my_dictionary = {'x': 1, 'y': 9}
        r2 = Rectangle.create(**my_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (2) 1/9 - 1/1')

        my_dictionary = {'x': 1, 'y': 9, 'id': 1}
        r2 = Rectangle.create(**my_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/9 - 1/1')

        my_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2}
        r2 = Rectangle.create(**my_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/9 - 1/2')

        my_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r2 = Rectangle.create(**my_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/9 - 10/2')

    def test_save_to_file(self):
        """Testing the to create method"""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            contents = file.read()

        str_return = Base.from_json_string(contents)

        my_list = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}]
        self.assertEqual(str_return, my_list)

    def test_save_to_file(self):
        """Testing the to create method"""

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            contents = file.read()

        str_return = Base.from_json_string(contents)

        my_list = []
        self.assertEqual(str_return, my_list)
