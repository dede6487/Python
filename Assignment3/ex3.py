chars = {}
inp = input("Enter string: ")

inp = inp.lower()

for c in inp:
    if c not in chars:
        chars[c] = 1
    else:
        chars[c] += 1

print(chars)
