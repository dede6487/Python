from ex4 import Rectangle


class Square(Rectangle):

    def __init__(self, x: int, y: int, length: int):
        super().__init__(x, y, length, length)

    # no need for new to_string, superclass handles that
    # no need for area, superclass handles that
