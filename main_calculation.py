##encode = utf8

import math
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime


class Calculation:

    def __init__(self, to_process, name, index):
        cur_dtime = datetime.now()
        self.current_date = str(cur_dtime.date())
        self.x = []
        self.y = []
        self.result = None
        self.index = index
        self.to_process = to_process
        self.name = name

    def calculate(self):
        if self.name == 'Owens-Wendt':
            self.method_owens_vens()
        elif self.name == 'Zisman':
            self.method_zeisman()
        elif self.name == 'van-Oss':
            self.method_van_oss()
        elif self.name == 'Fowkes':
            self.method_fowkes()
        else:
            raise NameError(f'such method {self.name} is not valid now')

    def method_zeisman(self):
        for value in self.to_process:
            surface_tension = value[2]
            self.x.append(surface_tension)
            angle_radiant = (float(value[1]) * math.pi) / 180
            cos_thetta = math.cos(angle_radiant)
            self.y.append(cos_thetta)
        self.x.sort()
        self.y.sort()
        x = np.array(self.x)
        y = np.array(self.y)
        a, b = np.polyfit(x, y, 1)
        y1 = np.ones(len(x))
        xnumbers = np.linspace(min(self.x), max(self.x), 10)
        ynumbers = np.linspace(min(self.y), max(self.y), 10)

        plt.plot(x, y, 'r', x, y1, 'g', x, a * x + b, 'b')
        plt.xlabel("Surface Tension")
        plt.ylabel(r"Cos$\beta$")
        plt.title("Plot of a surface free energy")
        plt.xticks(xnumbers)
        plt.yticks(ynumbers)
        plt.legend(['basic', 'cos = 1', 'approximate'])
        plt.text(0.5, self.y[-1], f'y={round(a, 2)}x+{round(b, 2)}', horizontalalignment='center',
                 verticalalignment='center')
        plt.grid()

        plt.axis([min(self.x) - 2, max(self.x) + 2, min(self.y), 1 + 0.05])
        result = (1 - b) / a
        self.result = ('Null', 'Null', result, self.name)
        self.save_fig()
        plt.show()
        plt.gcf().clear()

    def method_van_oss(self):
        print('Van-OSS')
        try:
            for value in self.to_process:
                print(value)
        except Exception as exc:
            print(exc)
            pass
        else:
            pass

    def method_fowkes(self):
        try:
            self.to_process = sorted(self.to_process, key=lambda x: x[-1])
            self.result = []
            result = []
            tension_dispersive = -1
            for value in self.to_process:
                angle_radiant = (value[1] * math.pi) / 180
                if value[3] == 0:
                    total = value[2]
                    right_part1 = (1 + math.cos(angle_radiant)) / 2
                    tension_dispersive = (math.pow(right_part1, 2) * total) / 2
                else:
                    total = value[2] + value[3]
                    right_part1 = (total * (1 + math.cos(angle_radiant))) / 2
                    right_part2 = math.sqrt(value[3] * tension_dispersive) if tension_dispersive != -1 else 0
                    right_part = right_part1 - right_part2
                    tension_polar = math.pow(right_part, 2) / value[3]
                    result.append(tension_polar)
            real_tension_polar = sum(result) / len(result)
            total_tension = real_tension_polar + tension_dispersive
            self.result = (tension_dispersive, real_tension_polar, total_tension, self.name)
        except Exception as exc:
            raise ValueError(exc)

    def method_owens_vens(self):
        try:
            for value in self.to_process:
                result_x = math.sqrt(value[3]) / math.sqrt(value[2])  # может быть ошибка! смотри сюда!
                angle_radiant = (float(value[1]) * math.pi) / 180
                y1 = 0.5 + (math.cos(angle_radiant)) / 2
                y2 = (value[2] + value[3]) / math.sqrt(value[2])
                res_y = y1 * y2
                self.y.append(round(res_y, 2))
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
            self.result = (dispersive_part, polarity_part, total, self.name)
        except Exception as exc:
            raise ValueError(exc)
        else:
            # values for making ticks in x and y axis
            xnumbers = np.linspace(0, 7, 15)
            ynumbers = np.linspace(0, 20, 11)
            plt.plot(x, y, 'r', x, a * x + b, 'b')  # r, g - red, green colour
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
            plt.gcf().clear()

    def save_fig(self):
        while True:
            fname = f'result/{self.current_date}_{self.name}({self.index}).png'
            if not os.path.exists(fname):
                plt.savefig(fname)
                break
            else:
                break


if __name__ == '__main__':
    calc = Calculation(name='Zisman',
                       to_process=[('Water', 46.77, 26.4, 46.4), ('Formamide', 23.5, 22.4, 34.6),
                                   ('Ethylene Glycole', 14, 26.4, 21.3),
                                   ('α-bromnaphtalene', 1, 44.4, 0)],
                       index=1)
    calc.calculate()
