##encode = utf8

import math
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

LIQUIDS = ['water',
           'ethylene_glycol',
           'formamide',
           'a_brom']  # a-brom is a-bromonaphtalene
SIGMA = [(18.7, 53.6),
         (29.3, 18.2),
         (39.4, 19.6),
         (44.4, 0)]  # first value in tuple is dispersive part and second is polar
CONSTANT_DICT = dict(zip(LIQUIDS, SIGMA))
PI = 3.141592653


class Calculation:

    def __init__(self, to_process, name):
        cur_dtime = datetime.now()
        self.current_date = str(cur_dtime.date())
        self.x = []
        self.y = []
        self.result = None
        self.to_process = to_process
        self.name = name

    def calculate(self):
        if self.name == 'Owens-Vens':
            self.method_owens_vens()
        else:
            raise NameError(f'such method {self.name} is not valid now')

    def method_owens_vens(self):
        for value in self.to_process:
            result_x = math.sqrt(value[3]) / math.sqrt(value[2])
            angle_radiant = (float(value[1]) * math.pi) / 180
            y1 = 0.5 + (math.cos(angle_radiant)) / 2
            y2 = (value[2] + value[3]) / math.sqrt(value[2])
            res_y = y1 * y2
            self.y.append(res_y)
            self.x.append(round(result_x, 2))
        self.x.sort()
        self.y.sort()
        x = np.array(self.x)
        y = np.array(self.y)
        a, b = np.polyfit(x, y, 1)

        # Finding result
        polarity_part = a ** 2
        dispersive_part = b ** 2
        total = dispersive_part + polarity_part
        self.result = (dispersive_part, polarity_part, total)

        # values for making ticks in x and y axis
        xnumbers = np.linspace(0, 7, 15)
        ynumbers = np.linspace(0, 20, 11)
        plt.plot(x, y, 'r', x, a * x + b, 'g')  # r, g - red, green colour
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Plot of a surface free energy")
        plt.xticks(xnumbers)
        plt.yticks(ynumbers)
        plt.legend(['basic', 'approximate'])
        plt.text(0.75, self.y[-1], f'y={round(a, 2)}x+{round(b, 2)}', horizontalalignment='center',
                 verticalalignment='center')
        plt.grid()
        plt.axis([0, 2.0, 2.9, self.y[-1] + 1])  # [xstart, xend, ystart, yend]
        self.save_fig()

    def save_fig(self):
        curent_index = 0
        while True:
            fname = f'result/{self.current_date}_{self.name}({curent_index}).png'
            if not os.path.exists(fname):
                plt.savefig(fname)
                break
            else:
                curent_index += 1
                continue


if __name__ == '__main__':
    calc = Calculation(name='Owens-Vens', to_process=[('Water', 54.25, 26.4, 46.4), ('Formamide', 24.0, 22.4, 34.6),
                                                      ('Ethylene Glycole', 31.5, 26.4, 21.3),
                                                      ('α-bromnaphtalene', 1.86, 44.4, 0)])
    calc.calculate()
