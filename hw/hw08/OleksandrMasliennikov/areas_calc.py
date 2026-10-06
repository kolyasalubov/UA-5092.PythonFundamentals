from math import pow, pi


def rectangle_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError('a and b must be positive')
    return a * b


def triangle_area(h, a):
    if h <= 0 or a <= 0:
        raise ValueError('h and a must be positive')
    return 0.5 * h * a


def circle_area(r):
    if r <= 0:
        raise ValueError('r must be positive')
    return pi * pow(r, 2)
