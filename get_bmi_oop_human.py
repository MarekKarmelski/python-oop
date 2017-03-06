#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.bmi import BMI


class BmiProgram:

    LINE_LENGTH = 50
    KCAL = 6000

    sports = {
        'Squash': 748,
        'Football': 544,
        'Basketball': 476
    }

    food = {
        'Potatoes': 767,
        'Chocolate': 5456,
        'Bananas': 887
    }

    def run(self):
        data = self.__get_data()
        bmi = BMI(data['weight'], data['height'])
        calculated_bmi = bmi.get_bmi()
        self.__print_line()
        print('BMI: %0.2f' % calculated_bmi)
        self.__print_line()
        bmi_norm = bmi.norm()
        if bmi_norm == -1:
            print('You are underweight!')
            self.__print_line()
            correct_weight = bmi.get_correct_weight()
            if correct_weight is not False:
                print('Your correct weight should be: %0.0f' % correct_weight)
                self.__print_line()
                print('To increase the weight You need to eat[kg]:')
                self.__print_line()
                self.__to_increase_weight(correct_weight - data['weight'])
        elif bmi_norm == 0:
            print('You have a healthy weight!')
            self.__print_line()
        elif bmi_norm == 1:
            print('You are overweight!')
            self.__print_line()
            correct_weight = bmi.get_correct_weight()
            if correct_weight is not False:
                print('Your correct weight should be: %0.0f' % correct_weight)
                self.__print_line()
                print('To reduce the weight You need exercise[h]:')
                self.__print_line()
                self.__to_reduce_weight(data['weight'] - correct_weight)

    def __get_data(self):
        """User data function."""
        user_data = {}
        weight = self.__is_number(input('Type weight: '))
        while weight is False:
            print('Weight is not number.')
            weight = self.__is_number(input('Type weight: '))
        user_data['weight'] = weight
        height = self.__is_number(input('Type height: '))
        while height is False:
            print('Height is not number.')
            height = self.__is_number(input('Type height: '))
        user_data['height'] = height
        return user_data

    def __is_number(self, number):
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

    def __print_line(self):
        """Print line."""
        print('-' * self.LINE_LENGTH)

    def __to_increase_weight(self, weight):
        to_increase = weight * self.KCAL
        eat = {}
        for key, value in self.food.items():
            eat[key] = round(to_increase / value, 2)
        print(eat)

    def __to_reduce_weight(self, weight):
        to_reduce = weight * self.KCAL
        exercise = {}
        for key, value in self.sports.items():
            exercise[key] = round(to_reduce / value, 2)
        print(exercise)


bmi_program = BmiProgram()
bmi_program.run()
