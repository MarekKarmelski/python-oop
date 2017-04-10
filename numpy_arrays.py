#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Numpy."""

import numpy as np
from pprint import pprint


class NumpyOOP:

    def ex_one(self):
        """Task #1"""
        m = np.arange(1, 26).reshape(5, 5)
        pprint(m)

    def ex_two(self):
        """Task #2"""
        m = np.arange(1, 26).reshape(5, 5)
        m2 = m[2:, 1:]
        pprint(m2)

    def ex_three(self):
        """Task #3"""
        m = np.arange(1, 26).reshape(5, 5)
        m2 = m[3, 4]
        pprint(m2)

    def ex_four(self):
        """Task #4"""
        m = np.arange(1, 26).reshape(5, 5)
        m2 = m[:3, 1]
        pprint(m2)

    def ex_five(self):
        """Task #5"""
        m = np.arange(1, 26).reshape(5, 5)
        pprint(np.sum(m))

    def ex_six(self):
        """Task #6"""
        m = np.arange(1, 26).reshape(5, 5)
        pprint(np.sum(m, axis=0))

    def ex_seven(self):
        """Task #7"""
        m = np.arange(1, 26).reshape(5, 5)
        pprint(np.sum(m, axis=1))

numpy_oop = NumpyOOP()
numpy_oop.ex_one()
numpy_oop.ex_two()
numpy_oop.ex_three()
numpy_oop.ex_four()
numpy_oop.ex_five()
numpy_oop.ex_six()
numpy_oop.ex_seven()
