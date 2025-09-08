from math import *

x = 0.4 * 10 ** 4
y = -0.875
z = -0.475 * 10 ** (-3)
s = abs(cos(x) - cos(y)) ** (1 + 2 * sin(y) ** 2) * (1 + z + z ** 2 / 2 + z ** 3 / 3 + z ** 4 / 4)
print(s)
