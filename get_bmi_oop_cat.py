#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.cat_bmi import CatBMI


class BmiProgram:

    def run(self):
        cat_data = self.get_cat_data()
        bmi = CatBMI(cat_data['weight'], cat_data['height'])
        calculated_bmi = bmi.get_bmi()
        print('Cat BMI: %0.2f' % calculated_bmi)

    def get_cat_data(self):
        """Data function."""
        data = {}
        weight = self.is_number(input('Type weight: '))
        while weight is False:
            print('Weight is not number.')
            weight = self.is_number(input('Type weight: '))
        data['weight'] = weight
        height = self.is_number(input('Type height: '))
        while height is False:
            print('Height is not number.')
            height = self.is_number(input('Type height: '))
        data['height'] = height
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


bmi_program = BmiProgram()
bmi_program.run()
