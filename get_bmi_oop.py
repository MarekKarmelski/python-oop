#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.bmi import Bmi


bmi = Bmi()
bmi.set_weight(87)
bmi.set_height(1.96)

current_bmi = bmi.calculate()
print(current_bmi)
