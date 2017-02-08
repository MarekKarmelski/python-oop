#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BMI class."""


class Bmi:

    __weight = None
    __height = None

    def set_weight(self, person_weight):
        """Set width."""
        if isinstance(person_weight, (int, float)):
            self.__weight = person_weight
        else:
            print('Wrong weight.')

    def set_height(self, person_height):
        """Set height."""
        if isinstance(person_height, (int, float)):
            self.__height = person_height
        else:
            print('Wrong height.')

    def calculate(self):
        """Calculate bmi."""
        if self.__weight is None or self.__height is None:
            print('weight or height is incorrect.')
        else:
            return self.__weight / self.__height ** 2
