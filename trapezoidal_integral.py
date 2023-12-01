from math import sin, exp, pi, sqrt

def trapezoidal_integration(f, a=0, b=1, n=100):
    h = (b - a) / n
    result = 0

    for i in range(n):
        result += h / 2 * (f(a + i * h) + f(a + (i + 1) * h))

    return result

# 問い1
result1 = trapezoidal_integration(sin, 0, pi/2, 50)
print("問い1:", result1)

# 問い2
def func2(x):
    return 4 / (1 + x**2)

result2 = trapezoidal_integration(func2, 0, 1, 100)
print("問い2:", result2)

# 問い3
def func3(x):
    return sqrt(pi) * exp(-x**2)

result3 = trapezoidal_integration(func3, -100, 100, 1000)
print("問い3:", result3)
