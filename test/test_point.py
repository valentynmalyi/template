from math import isclose

from point import LineSegment, Point
from vector import Vector


class TestLineSegment:
    def test_vector_property(self):
        assert LineSegment(Point(1, 1), Point(2, 1)).vector == Vector(1, 0)

    def test_square_length_property(self):
        assert LineSegment(Point(1, 1), Point(2, 2)).vector.square_length == 2

    def test_length_property(self):
        assert isclose(LineSegment(Point(2, 2), Point(1, 1)).vector.length, 2 ** 0.5)
