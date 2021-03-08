##encode = utf8

import math
import numpy as np
import matplotlib.pyplot as plt

LIQUIDS = ['water',
           'ethylene_glycol',
           'formamide',
           'a_brom']  # a-brom is a-bromonaphtalene
SIGMA = [(18.7, 53.6),
         (29.3, 18.2),
         (39.4, 19.6),
         (44.4, 0)]  # first value in tuple is dispersive part and second is polar
CONSTANT_DICT = dict(zip(LIQUIDS, SIGMA))
polarity_part = None
dispersive_part = None
total = None
PI = 3.141592653
x = []
y = []
y_2 = []
y_approx = []
y_start = []
a = None
b = None


class Calculation:

    def __init__(self, to_process):
        self.x = []
        self.y = []
        self.y_approx = []
        self.result_x = 0
        self.to_process = to_process

    def calculate(self):
        print(self.to_process)
        try:
            for value in self.to_process:
                result_x = math.sqrt(value[3]) / math.sqrt(value[2])
                self.x.append(round(result_x, 2))
                angle_radiant = (float(value[1]) * math.pi) / 180
                result_y1 = 0.5 + (math.cos(angle_radiant)) / 2
                result_y2 = (value[2] + value[3]) / math.sqrt(value[2])
                res_y = result_y1 * result_y2
                self.y.append(res_y)
        except Exception as exc:
            print(exc)
        else:
            self.x.sort()
            self.y.sort()
            y_2 = []
            correlation_matrix = np.corrcoef(self.x, self.y)
            correlation_xy = correlation_matrix[0, 1]
            r_squared_1 = correlation_xy ** 2
            r_squared_2 = correlation_xy / 2
            # print('Applying R square')
            for i in range(len(self.y)):
                self.y[i] *= r_squared_1
                y_2 = self.y[i] * r_squared_2

            print(self.y)
            print(y_2)
            try:
                if 0 in self.x:
                    index = self.x.index(0)
                    b = self.y[index]
                else:
                    _ = min(self.x)
                    index = self.x.index(_)
                    b = self.y[index]

                opposite = max(self.y) - min(self.y)
                adjacent = max(self.x) - min(self.x)
                a = opposite / adjacent
                print('Formula is next: {}*x+{}'.format(a, b))
                ## Finding result
                polarity_part = a ** 2
                dispersive_part = b ** 2
                total = dispersive_part + polarity_part
                self.result = [dispersive_part, polarity_part, total]

                # values for making ticks in x and y axis
                xnumbers = np.linspace(0, 7, 15)
                ynumbers = np.linspace(0, 20, 11)
                y_approx = []
                for i, _ in enumerate(self.x):
                    result = a * _ + b
                    y_approx.append(result)
            except Exception as exception_2:
                print(exception_2)
            else:
                try:
                    plt.plot(self.x, self.y, 'r', self.x, y_approx, 'g')  # r, g - red, green colour
                    plt.xlabel("x")
                    plt.ylabel("y")
                    plt.title("Plot of a surface free energy")
                    plt.xticks(xnumbers)
                    plt.yticks(ynumbers)
                    plt.legend(['basic', 'approximate'])
                    # plt.text(x=0.75, y=0.75, ')
                    plt.text(0.75, 13, f'y={round(a, 2)}x+{round(b, 2)}', horizontalalignment='center',
                             verticalalignment='center')
                    plt.grid()
                    plt.axis([-0.1, 2.0, 2.9, 20.1])  # [xstart, xend, ystart, yend]
                    plt.show()
                except Exception as Exc:
                    print(Exc)
