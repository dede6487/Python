import math


class Complex:

    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def print(self):
        if self.imaginary < 0:
            print(f"{self.real} - {abs(self.imaginary)}i")
        else:
            print(f"{self.real} + {self.imaginary}i")

    def abs(self) -> float:
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)

