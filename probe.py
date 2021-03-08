import math

radian = (46.77 * math.pi) / 180
print(radian)

y = 0.5 + (math.cos(radian) / 2)
y_1 = (0.5 + math.cos(radian)) / 2
# print(y == y_1)
y_norm = 0.5 + math.cos(radian) / 2

print(f'y = {y},'
      f'y1 = {y_1}'
      f'y_norm = {y_norm}')