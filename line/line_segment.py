from point import Point
from line import Vector


class LineSegment:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    @property
    def vector(self) -> Vector:
        return Vector(self.b.x - self.a.x, self.b.y - self.a.y)

    @property
    def square_length(self) -> int:
        return self.vector.square_length

    @property
    def length(self) -> float:
        return self.vector.length
