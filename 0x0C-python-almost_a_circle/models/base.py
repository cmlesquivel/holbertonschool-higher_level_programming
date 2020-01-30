#!/usr/bin/python3
"""Base module"""
import json
import csv


class Base():
    """Define Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Define constructor of object class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        data = []
        my_str = ''
        file_name = cls.__name__ + '.json'

        if list_objs is not None:

            for item in list_objs:
                data.append(item.to_dictionary())

        my_str = Base.to_json_string(data)

        with open(file_name, 'w') as file:
                file.write(my_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string  to object python """
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance starting from dictionary"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

        elif cls.__name__ == 'Square':
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        "returns a list of instances starting from file"

        file_name = cls.__name__ + '.json'

        my_instances = []

        try:
            with open(file_name, 'r') as file:
                contents = file.read()
        except:
            return my_instances

        my_list = cls.from_json_string(contents)

        for item in my_list:
            my_instances.append(cls.create(**item))
        return my_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a object into csv"""

        file_name = cls.__name__ + '.csv'
        my_dicc_obj = []
        my_json = ''

        for item in list_objs:
            my_dicc_obj.append((item.to_dictionary()))

        if file_name == 'Rectangle.csv':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif file_name == 'Square.csv':
            fieldnames = ['id', 'size', 'x', 'y']

        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for item in my_dicc_obj:
                writer.writerow(item)

    @classmethod
    def load_from_file_csv(cls):
        """return list of objects from csv file"""

        file_name = cls.__name__ + '.csv'
        my_list_obj = []

        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for key, value in row.items():
                    row[key] = int(value)

                my_list_obj.append(cls.create(**row))

        return my_list_obj
