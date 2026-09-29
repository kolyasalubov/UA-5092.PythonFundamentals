from math import pi, pow


def rectangle_area(a: float, b: float) -> float:
    """Обчислює площу прямокутника за двома сторонами.
    Повертає площу як число з плаваючою крапкою.
    """
    return a * b


def triangle_area(h: float, a: float) -> float:
    """Обчислює площу трикутника за висотою та основою.
    Повертає площу як число з плаваючою крапкою.
    """
    return 0.5 * h * a


def circle_area(r: float) -> float:
    """Обчислює площу круга за його радіусом.
    Використовує функції pi та pow з вбудованого модуля math.
    """
    return pi * pow(r, 2)


