import math
from ex3 import Shape


class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def to_string(self) -> str:
        return super().to_string() + f", radius={self.radius}"

    def area(self) -> float:
        return self.radius * self.radius * math.pi
