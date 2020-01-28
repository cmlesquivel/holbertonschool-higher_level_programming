#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
from models.base import Base


class TestAttr(unittest.TestCase):
    """Tests to check the attributes of Base class"""

    def setUp(self):
        """Define in zero at the atributte Base Class"""
        Base._Base__nb_objects = 0

    def test_attribute_id(self):
        """Check the atributtes of Class and Id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        b3 = Base(20)
        self.assertEqual(b3.id, 20)
        self.assertEqual(Base._Base__nb_objects, 2)
