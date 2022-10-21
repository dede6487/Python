actions = "Available actions: \n a - Add numbers \n v - View statistics \n x - Exit the program \n"

print("Welcome to Data Statistics! \n \n" + actions)

numbers = []
count = 0
sum_ = 0
avg = 0
min_ = 0
max_ = 0


inp1 = None
while inp1 != "x":
    inp1 = input("Enter action: ")
    if inp1 == "a"
        inp2 = None
        while inp2 != "x":
            inp2 = input("Enter number or 'x' when you are done: ")
            numbers += [inp2]
            count += 1
            sum_ += inp2
            avg = sum_ / count
            for n in numbers:

    elif inp1 == "v":
        if count == 0:
            print("No numbers have been added yet!")
        else:
            print("Count: " + str(count))

    else:
        print("Invalid action '" + str(inp1) + "'. Try again!")
