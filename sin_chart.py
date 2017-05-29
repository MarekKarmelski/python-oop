#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SIN chart."""


import matplotlib.pyplot as plt
import numpy as np


class SinChart:

    def draw(self):
        x = np.arange(-100, 100)
        y = np.sin(x)
        plt.plot(x, y, c='red', label='sin(x)')
        plt.axvline(x=0, c='red')
        plt.xlim([-100, 100])
        plt.ylim([-10, 10])
        plt.title('SIN')
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.legend()
        plt.show()
        pass


sin_chart = SinChart()
sin_chart.draw()
