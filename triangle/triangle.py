from math import isclose

from point import Point
from line import LineSegment, exceptions as line_exception
# from triangle.exceptions import NoTriangle
from triangle import exceptions


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c
        self._validate_equal_points()

    def __repr__(self) -> str:
        return f"A{self.a}, B{self.b}, C{self.c}"

    def _validate_equal_points(self) -> None:
        try:
            [LineSegment(self.a, self.b), LineSegment(self.b, self.c), LineSegment(self.a, self.c)]
        except line_exception.EqualPoints:
            raise exceptions.NoTriangle


class RightTriangle(Triangle):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__(a, b, c)
        self._validate_is_right(a, b, c)

    def _validate_is_right(self, a: Point, b: Point, c: Point) -> None:
        side = sorted([LineSegment(a, b).length, LineSegment(b, c).length, LineSegment(a, c).length])
        if not isclose(side[2] ** 2, side[1] ** 2 + side[0] ** 2):
            raise Exception(f"triangle {self} isn't a right triangle")


