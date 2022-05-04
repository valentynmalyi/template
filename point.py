from vector import Vector


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def create_vector(self):  # getting vector from segment
        return Vector(self.b.x - self.a.x, self.b.y - self.b.y)
