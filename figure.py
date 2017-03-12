#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Figure class."""

import math


class Figure:

    def __init__(self, *args):
        self.data = args
        for arg in args:
            if arg.isidentifier():
                setattr(self, arg, self.get_input(arg))

    def __str__(self):
        return ' '.join([
            '{}={}'.format(atr, getattr(self, atr))
            for atr in dir(self) if not atr.startswith((
                'get', 'set', '_', 'data', 'is'
            )) and atr.isidentifier()
        ])

    @staticmethod
    def get_input(data):
        # TODO: Handle excpetions
        return int(input('Podaj bok {} :'.format(data)))

    @classmethod
    def get_name(cls):
        return cls.__name__

    def get_field(self):
        raise NotImplemented

    def get_circuit(self):
        raise NotImplemented

    def is_closed_figure(self):
        raise NotImplemented


"""Figure class."""


class Polygon(Figure):

    def get_amount_of_sides(self):
        return len(self.data)

    def get_angles(self):
        return len(self.data)

    def get_circuit(self):
        circuit = 0
        for atr in dir(self):
            if not atr.startswith((
                    'get', 'set', '_', 'data', 'is'
            )) and atr.isidentifier():
                circuit += getattr(self, atr)
        return circuit

    def is_closed_figure(self):
        closed = True
        if len(self.data) > 2:
            for atr_name in self.data:
                sum = 0
                getattr(self, atr_name)
                for atr in dir(self):
                    if not atr.startswith((
                            'get', 'set', '_', 'data', 'is'
                    )) and atr.isidentifier() and atr is not atr_name:
                        sum += getattr(self, atr)
                if getattr(self, atr_name) >= sum:
                    closed = False
                    break
            return closed
        else:
            return closed

"""Figure class."""


class Quadrangle(Polygon):

    def is_quadrangle(self):
        if len(self.data) == 4:
            return True
        else:
            return False

"""Figure class."""


class Pentangle(Polygon):

    def get_field(self):
        sum = 0
        for atr in dir(self):
            if not atr.startswith((
                    'get', 'set', '_', 'data', 'is'
            )) and atr.isidentifier():
                sum += getattr(self, atr)
        if sum % 5 == 0:
            return (((sum / 5) ** 2) * (5 * (5 + (2 * (5 ** 0.5)))) ** 0.5) / 4
        else:
            raise Exception('Pentangle is not regular')

"""Figure class."""


class Circle(Figure):

    def get_field(self):
        return math.pi * (getattr(self, self.data[0])) ** 2

    def get_circuit(self):
        return 2 * math.pi * getattr(self, self.data[0])

    def is_closed_figure(self):
        return True

"""Figure class."""


class Square(Figure):

    def get_field(self):
        return (getattr(self, self.data[0])) ** 2

    def get_circuit(self):
        return (getattr(self, self.data[0])) * 4

    def is_closed_figure(self):
        return True
