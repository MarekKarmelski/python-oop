#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BMI Tests."""


import unittest
from src.bmi import BMI


class TestCatBMIMethods(unittest.TestCase):

    def test_bmi_no_height_no_weight(self):
        human_bmi = BMI()
        self.assertEqual(human_bmi.get_bmi(), False)

    def test_bmi_no_height(self):
        human_bmi = BMI(weight=86)
        self.assertEqual(human_bmi.get_bmi(), False)

    def test_bmi_no_weight(self):
        cat_bmi = BMI(height=1.85)
        self.assertEqual(cat_bmi.get_bmi(), False)

    def test_get_bmi(self):
        human_bmi = BMI(weight=86, height=1.85)
        self.assertEqual(human_bmi.get_bmi(), 25.127830533235937)

    def test_bmi_norm_underweight(self):
        human_bmi = BMI(weight=60, height=1.95)
        self.assertEqual(human_bmi.norm(), -1)

    def test_get_bmi_norm_ok(self):
        human_bmi = BMI(weight=84, height=1.85)
        self.assertEqual(human_bmi.norm(), 0)

    def test_get_bmi_overrweight(self):
        human_bmi = BMI(weight=86, height=1.55)
        self.assertEqual(human_bmi.norm(), 1)

if __name__ == '__main__':
    unittest.main()
