from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

h = (pi / 2 - 0) / 100
a = 0
b = pi / 2
result = 0

for i in range(100):
    result += h / 2 * (sin(a + i * h) + sin(a + (i + 1) * h))

print(result)
