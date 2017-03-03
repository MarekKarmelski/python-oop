#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Element class."""


class Element:

    name = 'ELEMENT'
    traversed_by = []
    beats = []

    def __new__(cls):
        if cls.__name__ is 'Element':
            raise Exception("Unable to create an instance of abstract class Element")

    @classmethod
    def __str__(cls):
        return cls.__name__

    def __eq__(self, other):
        return self.name == other.name
