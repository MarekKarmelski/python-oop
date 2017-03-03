#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.bmi import BMI
from src.cat_bmi import CatBMI
from src.dog_bmi import DogBMI

bmi = BMI(87, 1.96)
current_bmi = bmi.get_bmi()
print('Human BMI: %0.2f' % current_bmi)

cat_bmi = CatBMI(8, 0.34)
current_bmi = cat_bmi.get_bmi()
print('Cat BMI: %0.2f' % current_bmi)

dog_bmi = DogBMI(76, 0.65)
current_bmi = dog_bmi.get_bmi()
print('Dog BMI: %0.2f' % current_bmi)
