from __future__ import annotations


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        a = self.x + other.x
        b = self.y + other.y
        return Vector(a, b)


def multiply(a: Vector, b: Vector) -> float:
    return a.x * b.x + a.y * b.y
