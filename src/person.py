#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

"""Person class."""


class Person:

    __firstname = None
    __lastname = None
    __height = None
    __weight = None
    __age = None

    def get_firstname(self):
        """Get firstname."""
        return self.__firstname

    def get_lastname(self):
        """Get lastname."""
        return self.__lastname

    def get_height(self):
        """Get height."""
        return self.__height

    def get_weight(self):
        """Get weight."""
        return self.__weight

    def get_age(self):
        """Get age."""
        return self.__age

    def set_firstname(self, firstname=''):
        """Set firstname."""
        self.__firstname = firstname
        return self

    def set_lastname(self, lastname=''):
        """Set lastname."""
        self.__lastname = lastname
        return self

    def set_height(self, height=''):
        """Set height."""
        self.__height = height
        return self

    def set_weight(self, weight=''):
        """Set weight."""
        self.__weight = weight
        return self

    def set_age(self, age=''):
        """Set age."""
        self.__age = age
        return self

    def get_person(self):
        """Return person like dictionary."""
        person_dict = {
            'firstname': self.__firstname,
            'lastname': self.__lastname,
            'height': self.__height,
            'weight': self.__weight,
            'age': self.__age
        }
        return person_dict

    def get_person_like_json(self):
        """Return person like json string."""
        return json.dumps(self.get_person())
