class TriangleException(Exception):
    pass


class NoTriangle(TriangleException):
    # def __init__(self):
    #     self.point = point

    def __str__(self) -> str:
        return f"This triangle is a line"
