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


class Calculation():

    def __init__(self, to_process):
        self.x = []
        self.y = []
        self.y_approx = []
        self.result_x = 0
        self.to_process = to_process
        print(self.to_process)

    def calculate(self):
        print(self.to_process)
        try:
            for index, value in enumerate(self.to_process):
                result_x = math.sqrt(value[2]) / math.sqrt(value[3])
                self.x.append(round(result_x, 2))
                angleRadiant = (float(value[1]) * math.pi) / 180
                result_y1 = (0.5 + math.cos(angleRadiant)) / 2
                result_y2 = (value[2] + value[3]) / math.sqrt(value[2])
                res_y = result_y1 * result_y2
                self.y.append(res_y)
        except Exception as exc:
            print(exc)
        else:
            self.x.sort()
            self.y.sort()
            y_2 = []
            correlation_matrix = np.corrcoef(x, y)
            correlation_xy = correlation_matrix[0, 1]
            r_squared_1 = correlation_xy ** 2
            r_squared_2 = correlation_xy / 2
            # print('Applying R square')
            for i in range(len(self.y)):
                self.y[i] *= r_squared_1
                y_2 = self.y[i] * r_squared_2
            if 0 in self.x:
                index = self.x.index(0)
                b = self.y[index]
            else:
                _ = min(self.x)
                index = self.x.index(_)
                b = self.y[index]

            opposite = max(y) - min(y)
            adjacent = max(x) - min(x)
            a = opposite / adjacent
            # print('Formula is next: {}*x+{}'.format(a, b))
            ## Finding result
            polarity_part = a ** 2
            dispersive_part = b ** 2
            total = dispersive_part + polarity_part
            # print('''Dispersive part = {}
            # Polarity part = {}
            # Total = {}'''.format(dispersive_part, polarity_part, total))

            # values for making ticks in x and y axis
            xnumbers = np.linspace(0, 7, 15)
            ynumbers = np.linspace(0, 20, 11)
            y_approx = []
            for i, _ in enumerate(x):
                result = a * _ + b
                y_approx.append(result)
            plt.plot(x, y, 'r', x, y_approx, 'g')  # r, g - red, green colour
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


def do_calculation(**kwargs):
    # global x, y, y_approx, y_start, y_2, a, b
    # x = []
    #
    # for key, value in CONSTANT_DICT.items():
    #     result_x = math.sqrt(value[1]) / math.sqrt(value[0])
    #     x.append(round(result_x, 2))
    # y = []
    # for key, value in CONSTANT_DICT.items():
    #     user_value = float(kwargs[key])
    #     angle_radian = user_value * PI / 180
    #     result_y_1 = 0.5 + math.cos(angle_radian) / 2
    #     result_y_2 = (value[0] + value[1]) / math.sqrt(value[0])
    #     result_y_final = result_y_1 * result_y_2
    #     y.append(result_y_final)
    # x.sort()
    # y.sort()
    print('x', x, '\n', 'y', y)
    y_2 = []
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0, 1]

    r_squared_1 = correlation_xy ** 2
    r_squared_2 = correlation_xy / 2
    # print('Applying R square')
    for i in range(len(y)):
        y[i] *= r_squared_1
        y_2 = y[i] * r_squared_2

    # print(x)
    # print(y)
    # print(y_start)

    if 0 in x:
        index = x.index(0)
        b = y[index]
    else:
        _ = min(x)
        index = x.index(_)
        b = y[index]
    ## Move to "a", we will look for "a" as tg from triangular
    opposite = max(y) - min(y)
    adjacent = max(x) - min(x)
    a = opposite / adjacent
    # print('Formula is next: {}*x+{}'.format(a, b))
    global polarity_part, dispersive_part, total
    ## Finding result
    polarity_part = a ** 2
    dispersive_part = b ** 2
    total = dispersive_part + polarity_part
    # print('''Dispersive part = {}
    # Polarity part = {}
    # Total = {}'''.format(dispersive_part, polarity_part, total))

    # values for making ticks in x and y axis
    xnumbers = np.linspace(0, 7, 15)
    ynumbers = np.linspace(0, 20, 11)
    y_approx = []
    for i, _ in enumerate(x):
        result = a * _ + b
        y_approx.append(result)
    plt.plot(x, y, 'r', x, y_approx, 'g')  # r, g - red, green colour
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of a surface free energy")
    plt.xticks(xnumbers)
    plt.yticks(ynumbers)
    plt.legend(['basic', 'approximate'])
    # plt.text(x=0.75, y=0.75, ')
    plt.text(0.75, 13, f'y={round(a, 2)}x+{round(b, 2)}', horizontalalignment='center', verticalalignment='center')
    plt.grid()
    plt.axis([-0.1, 2.0, 2.9, 20.1])  # [xstart, xend, ystart, yend]
    plt.show()
