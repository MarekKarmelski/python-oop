#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.bmi import BMI
from src.cat_bmi import CatBMI
from src.dog_bmi import DogBMI

bmi = BMI()
bmi.set_weight(87)
bmi.set_height(1.96)

current_bmi = bmi.calculate()
print('Human BMI: %0.2f' % current_bmi)

cat_bmi = CatBMI()
cat_bmi.set_weight(8)
cat_bmi.set_height(0.34)

current_bmi = cat_bmi.calculate()
print('Cat BMI: %0.2f' % current_bmi)

dog_bmi = DogBMI()
dog_bmi.set_weight(76)
dog_bmi.set_height(0.65)

current_bmi = dog_bmi.calculate()
print('Dog BMI: %0.2f' % current_bmi)
