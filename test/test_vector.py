from vector import Vector


class TestVector:
    def test__add__(self):
        # Now you can write test shorter
        assert Vector(1, 1) + Vector(1, 2) == Vector(2, 3)

    def test__mul__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        res = v1 * v2
        assert res == 3

    def test__eq__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 1)
        assert v1 == v2
