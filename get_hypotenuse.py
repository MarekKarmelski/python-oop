#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get hypotenuse program."""

from src.pitagoras import Pitagoras


class HypotenuseProgram:

    def run(self):
        data = self.get_data()
        hypotenuse = Pitagoras()
        hypotenuse.set_a(data['a'])
        hypotenuse.set_b(data['b'])
        current_hypotenuse = hypotenuse.get_hypotenuse()
        print('Hypotenuse: %0.2f' % current_hypotenuse)

    def get_data(self):
        """User data function."""
        data = {}
        a = self.is_number(input('Type length of a: '))
        while a is False:
            print('Length of a is not number.')
            a = self.is_number(input('Type length of a: '))
        data['a'] = a
        b = self.is_number(input('Type length of b: '))
        while b is False:
            print('Length of b is not number.')
            b = self.is_number(input('Type length of b: '))
        data['b'] = b
        return data

    def is_number(self, number):
        """Check if is number."""
        if isinstance(number, (float, int)):
            return number
        if not isinstance(number, str):
            return False
        number = number.replace(',', '.')
        try:
            return float(number)
        except ValueError:
            return False


hypotenuse_program = HypotenuseProgram()
hypotenuse_program.run()
