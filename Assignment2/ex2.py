text = str(input("Enter text: "))
upper = 0

for char in text:
    if char.isupper():
        upper += 1

character_s = "character" if upper == 1 else "characters"  # Elvis operator

print("The text contains " + str(upper) + " uppercase " + character_s)
