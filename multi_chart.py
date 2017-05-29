#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Multi chart."""

import matplotlib.pyplot as plt
import numpy as np


class MultiChart:

    def draw(self):
        x = np.arange(-5, 6)
        fig, axs = plt.subplots(nrows=2, ncols=2)
        m = 1
        for ax in axs.flatten():
            m += 1
            y = x ** m
            ax.plot(x, y, 'r')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('x ** ' + str(m))
        plt.tight_layout()
        plt.show()
        pass


multi_chart = MultiChart()
multi_chart.draw()
