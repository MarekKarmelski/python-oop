#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.dog_bmi import DogBMI


class BmiProgram:

    def run(self):
        dog_data = self.get_data()
        bmi = DogBMI(dog_data['weight'], dog_data['height'])
        calculated_bmi = bmi.get_bmi()
        print('Dog BMI: %0.2f' % calculated_bmi)

    def get_data(self):
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
