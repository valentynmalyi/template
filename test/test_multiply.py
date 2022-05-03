from multiply import multiply, Vector


def test_multiply():
    v1 = Vector(1, 1)
    v2 = Vector(1, 2)
    assert multiply(v1, v2) == 3


class TestVector:
    def test__add__(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        v3 = v1 + v2
        assert v3.x == 2
        assert v3.y == 3
