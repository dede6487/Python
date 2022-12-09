from ex3 import Shape


class Rectangle(Shape):

    def __init__(self,  x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.width = width
        self. height = height

    def to_string(self) -> str:
        return super().to_string() + f", width={self.width}, height={self.height}"

    def area(self) -> float:
        return self.width * self.height
