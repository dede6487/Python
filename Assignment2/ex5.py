actions = "\nAvailable actions: \n a - Add numbers \n v - View statistics \n x - Exit the program \n"

print("Welcome to Data Statistics!")

count = 0
sum_ = 0
avg = 0
min_ = 0
max_ = 0

while True:
    print(actions)
    inp1 = input("Enter action: ")
    if inp1 == "a":
        while True:
            inp2 = input("Enter number or 'x' when you are done: ")
            if inp2 != "x":
                count += 1
                sum_ += int(inp2)
                avg = sum_ / count
                if int(inp2) < min_ or count == 1:
                    min_ = int(inp2)
                if int(inp2) > max_ or count == 1:
                    max_ = int(inp2)
            else:
                break
    elif inp1 == "v":
        if count == 0:
            print("No numbers have been added yet!")
        else:
            print("Count: " + str(count))
            print("Sum: " + str(sum_))
            print("Avg: " + str(avg))
            print("Min: " + str(min_))
            print("Max: " + str(max_))
    elif inp1 == "x":
        print("Bye!")
        break
    else:
        print("Invalid action '" + str(inp1) + "'. Try again!")
