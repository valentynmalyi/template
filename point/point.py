from math import isclose

from geometry import Figure

from .validations import PointValidation


class Point(Figure):
    validation_class = PointValidation

    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return isclose(self.x, other.x) and isclose(self.y, other.y)
