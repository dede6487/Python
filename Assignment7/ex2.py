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

    def add(self, other: "Complex"):
        if not isinstance(other, Complex):
            print("Error: add can only add complex numbers")
            raise TypeError
        self.real += other.real
        self.imaginary += other.imaginary

    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
        if not isinstance(comp, Complex):
            print("Error: add_all can only add complex numbers")
            raise TypeError
        s = Complex(comp.real, comp.imaginary)
        for c in comps:
            if not isinstance(c, Complex):
                print("Error: add_all can only add complex numbers")
                raise TypeError
            s.real += c.real
            s.imaginary += c.imaginary
        return s


c1 = Complex(1.0, -2.0)
c1.print()
c2 = Complex(9.0, 100.0)
c1.add(c2)
c1.print()
c_sum = Complex.add_all(c1, c1, c2, Complex(33.75, -14.25))
c_sum.print()
c1.print()
will_fail = Complex.add_all(100)