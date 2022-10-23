lower = []
upper = []
rest = []
unique = set()

inp = input("Enter string: ")

for c in inp:
    unique.add(str(c))
    if c.isupper():
        upper += str(c)
    elif c.islower():
        lower += str(c)
    else:
        rest += str(c)

print(lower)
print(upper)
print(rest)
print(unique)

