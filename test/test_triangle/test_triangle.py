from itertools import permutations

import pytest

from point import Point
from triangle.triangle import exceptions, RightTriangle, Triangle


class TestTriangle:
    def test_validate_is_line(self):
        with pytest.raises(exceptions.IsLine):
            Triangle._validate_line_segment(Point(0, 0), Point(0, 0), Point(1, 0))

    def test_validate_is_point(self):
        Triangle(Point(1, 1), Point(0, 0), Point(1, 0))
        with pytest.raises(exceptions.IsPoint):
            Triangle(Point(0, 0), Point(0, 0), Point(0, 0))


class TestRightTriangle:
    def test_validate_is_right(self):
        assert isinstance(RightTriangle(Point(0, 0), Point(1, 0), Point(0, 2)), Triangle)
        with pytest.raises(exceptions.IsNotRight):
            RightTriangle(Point(3, 3), Point(1, 0), Point(0, 2))
