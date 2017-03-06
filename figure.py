#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Figure class."""


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

    def get_field(self, function):
        raise NotImplemented

    def get_circuit(self):
        raise NotImplemented

    def is_closed_figure(self):
        raise NotImplemented


"""Figure class."""


class Polygon(Figure):
    def get_amount_of_sides(self):
        raise NotImplemented

    def get_angles(self):
        raise NotImplemented

"""Figure class."""


class Quadrangle(Polygon):
    def is_quadrangle(self):
        pass

"""Figure class."""


class Pentangle(Polygon):
    pass

"""Figure class."""


class Circle:
    pass

"""Figure class."""


class Square:
    pass