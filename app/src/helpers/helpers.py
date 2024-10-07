# external imports
from math import cos, sin, radians
from typing import List
# internal imports
from ..actors.points.point import Point


@staticmethod
def rotate(p: tuple, angle: float) -> tuple:
    """Rotate a point around the origin by a given angle in degrees."""
    x, y = p
    angle = radians(angle)
    x_new = x * cos(angle) - y * sin(angle)
    y_new = x * sin(angle) + y * cos(angle)
    return x_new, y_new


@staticmethod
def rotate_figure(points: List[tuple], angle: float, center: tuple) -> List[tuple]:
    """Rotate a figure around a center point by a given angle in degrees."""
    return [translate(rotate(p, angle), center[0], center[1]) for p in translate_figure(points, (-center[0], -center[1]))]


@staticmethod
def translate_figure(points: List[tuple], center: tuple) -> List[tuple]:
    """Translate a figure by a given center point."""
    return [translate(p, center[0], center[1]) for p in points]


@staticmethod
def translate(p: tuple, dx: float, dy: float) -> tuple:
    """Translate a point by dx and dy."""
    return p[0] + dx, p[1] + dy
