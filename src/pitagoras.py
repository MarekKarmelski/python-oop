#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pitagoras class."""


class Pitagoras:

    __a = None
    __b = None

    def set_a(self, a):
        """Set a."""
        if isinstance(a, (int, float)):
            self.__a = a
        else:
            print('a: must be a number.')

    def set_b(self, b):
        """Set b."""
        if isinstance(b, (int, float)):
            self.__b = b
        else:
            print('b: must be a number.')

    def get_hypotenuse(self):
        """Calculate hypotenuse."""
        if self.__a is None or self.__b is None:
            print('a or b is incorrect.')
        else:
            return (self.__a ** 2 + self.__b ** 2) ** 1 / 2
