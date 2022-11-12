def round_(number, ndigits: int = None):
    if ndigits:
        return int(number)
    else:
        number = float(number)
        intnumber = int(number)
        decimal = float(number % (10**(-ndigits)))
        return float(intnumber + decimal)

print(round(777.777))
print(round_(777.777, 0))
print(round_(777.777, 1))
print(round_(777.777, 2))
print(round_(777.777, 3))
print(round_(777.777, 4))
print(round_(777.777, -1))
print(round_(777.777, -2))
print(round_(777.777, -3))
print(round_(777.777, -4))

