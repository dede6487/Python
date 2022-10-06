a = float(input("Edge length:"))

print("Surface: " + f"{a * a * (3 ** (1 / 2)): .4f}")
print("Volume: " + f"{a * a * a * (1 / 12) * (2 ** (1 / 2)): .4f}")
print("Height: " + f"{(a / 3) * (6 ** (1 / 2)): .4f}")
