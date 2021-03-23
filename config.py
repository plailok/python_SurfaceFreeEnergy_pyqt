THEORY = '''https://www.ossila.com/pages/a-guide-to-surface-energy#:~:text=One%20of%20the%20most%20basic, 
Zisman%20model%2C%20published%20in%201964.&text=This%20model%20assumes%20that%20the,
as%20the%20critical%20surface%20tension '''
LIQUIDS = ['Water', 'Formamide', 'Ethylene Glycole', '\u03B1-bromnaphtalene']
HORIZONTAL_HEADER_SETTING = ['Liquid', '\u03C3p [mN/m]', '\u03C3d [mN/m]']
HORIZONTAL_HEADER_RESULT = ['\u03B8d [mN/m]', '\u03C3p [mN/m]', '\u03C3total [mN/m]', 'Method']

TEMPERATURE = {'Water': {'21': ('w111', 111),
                         '22': ('w222', 222),
                         '23': ('w333', 333),
                         '24': ('w444', 444),
                         '25': (26.4, 46.4),
                         '26': ('w666', 666)},
               'Formamide': {'21': ('f111', 111),
                             '22': ('f222', 222),
                             '23': ('f333', 333),
                             '24': ('f444', 444),
                             '25': (22.4, 34.6),
                             '26': ('f666', 666)},
               'Ethylene Glycole': {'21': ('e111', 111),
                                    '22': ('e222', 222),
                                    '23': ('e333', 333),
                                    '24': ('e444', 444),
                                    '25': (26.4, 21.3),
                                    '26': ('e666', 666)},
               '\u03B1-bromnaphtalene': {'21': ('a111', 111),
                                         '22': ('a222', 222),
                                         '23': ('a333', 333),
                                         '24': ('a444', 444),
                                         '25': (44.4, 0),
                                         '26': ('a666', 666)}}
