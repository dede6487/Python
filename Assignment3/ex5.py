import copy

actions = "\nAvailable actions: \na - Add lifter \nr - Remove lifter \nu - Update lifter\nv - View lifters \nx - Exit the program"

lifters = dict()

emptyEntry = {"squat": list(), "bench press": list(), "deadlift": list()}

print("Welcome to Powerlifting Data Collector!\n")

while True:
    print(actions)
    inp = input("Enter action: ")
    if inp == "a":
        name = input("Enter new lifter name: ")
        if name not in lifters.keys():
            lifters[name] = copy.deepcopy(emptyEntry)
        else:
            print("Lifter '" + name + "' already exists!")
    elif inp == "r":
        name = input("Enter lifter name to remove: ")
        x = lifters.pop(name, False)
        if not x:
            print("Lifter '" + name + "' does not exist!")
    elif inp == "u":
        name = input("Enter lifter name to update: ")
        if name in lifters.keys():
            update = input("Enter lift (one of 'squat', 'bench press', 'deadlift'): ")
            weight = input("Enter weight(s): ")
            lifters[name][update].extend(float(a) for a in weight.split())
        else:
            print("Lifter '" + name + "' does not exist!")
    elif inp == "v":
        for l in lifters:
            print("------------------------------")
            print("Name: " + l)
            print("squat: ", end="")
            print(lifters[l]["squat"])
            print("bench press: ", end="")
            print(lifters[l]["bench press"])
            print("deadlift: ", end="")
            print(lifters[l]["deadlift"])
    elif inp == "x":
        print("Bye!")
        break
    else:
        print("Invalid action '" + inp + "'. Try again!")
