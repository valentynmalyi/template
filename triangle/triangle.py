from itertools import permutations
from math import isclose

from line import exceptions as line_exception, LineSegment
from point import Point

from . import exceptions


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c
        self._validate()

    def __repr__(self) -> str:
        return f"A{self.a}, B{self.b}, C{self.c}"

    def _validate(self) -> None:
        self._validate_is_point()
        self._validate_is_line()

    def _validate_is_line(self) -> None:
        for a, b, c in permutations([self.a, self.b, self.c], 3):
            self._validate_line_segment(a, b, c)

    @staticmethod
    def _validate_line_segment(a: Point, b: Point, c: Point) -> None:
        try:
            LineSegment(a, b)
        except line_exception.EqualPoints:
            raise exceptions.IsLine(LineSegment(a, c))

    def _validate_is_point(self) -> None:
        if self.a == self.b == self.c:
            raise exceptions.IsPoint(self.a)


class RightTriangle(Triangle):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__(a, b, c)
        self._validate_is_right(a, b, c)

    def _validate_is_right(self, a: Point, b: Point, c: Point) -> None:
        side = sorted([LineSegment(a, b).length, LineSegment(b, c).length, LineSegment(a, c).length])
        if not isclose(side[2] ** 2, side[1] ** 2 + side[0] ** 2):
            raise exceptions.IsNotRight(f'{self}')
