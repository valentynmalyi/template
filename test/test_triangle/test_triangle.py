import pytest

from point import Point
from triangle.triangle import RightTriangle, Triangle


class TestRightTriangle:
    def test_init_triangle(self):
        assert isinstance(RightTriangle(Point(0, 0), Point(1, 0), Point(0, 2)), Triangle)
        with pytest.raises(Exception):
            RightTriangle(Point(3, 3), Point(1, 0), Point(0, 2))
