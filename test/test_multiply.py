from vector import Vector
from point import Point, LineSegment


class TestVector:
    def test__add__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        v3 = v1 + v2
        assert v3.x == 2
        assert v3.y == 3

    def test__mul__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        res = v1 * v2
        assert res == 3


class TestLineSegment:
    def test_create_vector(self):
        a = Point(1, 1)
        b = Point(2, 1)
        res = LineSegment(a, b).create_vector()
        assert res.x == 1, res.y == 0
