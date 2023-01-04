import math


class Complex:

    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        else:
            if self.real == other.real and self.imaginary == other.imaginary:
                return True
            else:
                return False

    def __repr__(self):
        return f"Complex(real={self.real}, imaginary={self.imaginary})"

    def __str__(self):
        return f"{self.real}" + " {sign} ".format(sign="+" if self.imaginary >= 0 else "-") + f"{abs(self.imaginary)}i"

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __add__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        else:
            return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __iadd__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        else:
            self.real += other.real
            self.imaginary += other.imaginary
            return self

    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
        real = 0
        imaginary = 0
        real += comp.real
        imaginary += comp.imaginary
        for c in comps:
            real += c.real
            imaginary += c.imaginary
        return Complex(real, imaginary)
