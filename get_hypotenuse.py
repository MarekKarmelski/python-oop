#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get bmi program."""

from src.pitagoras import Pitagoras


hypotenuse = Pitagoras()
hypotenuse.set_a(21)
hypotenuse.set_b(43)

current_hypotenuse = hypotenuse.get_hypotenuse()
print(current_hypotenuse)
