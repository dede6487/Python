def round_(number, ndigits: int = None):
    if ndigits is None:
        return int(number)
    else:
        number = float(number)
        intnumber = number * 10**(ndigits+1)
        roundn = intnumber % 10
        intnumber = intnumber - roundn

        if roundn < 5:
            roundn = 0
        else:
            roundn = 10

        number = (intnumber + roundn) * (10**(-(ndigits+1)))

        return number


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

