from point import Point
from line import LineSegment, line_exceptions


class TriangleException(Exception):
    pass


class IsLine(TriangleException):
    def __init__(self, line: LineSegment):
        self.line = line
        pass

    def __str__(self) -> str:
        return f"This triangle is a line {self.line}"


class IsPoint(line_exceptions.EqualPoints, IsLine):
    def __str__(self) -> str:
        return f"This triangle equal to point: {self.point}"

