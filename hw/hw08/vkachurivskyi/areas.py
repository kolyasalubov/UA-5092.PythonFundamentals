from math import pi, pow

def rectangle_area(a, b):
    """Обчислює площу прямокутника"""
    return a * b

def triangle_area(h, a):
    """Обчислює площу трикутника"""
    return 0.5 * h * a

def circle_area(r):
    """Обчислює площу кола"""
    return pi * pow(r, 2)