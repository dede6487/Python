import copy

actions = "\nAvailable actions: \na - Add lifter \nr - Remove lifter \nu - Update lifter\nv - View lifters \nx - Exit the program"

lifters = dict()

emptyEntry = {"squat": [], "bench": [], "dead": []}

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
        lifters.pop(name, print("Lifter '" + name + "' does not exist!"))
    elif inp == "u":
        name = input("Enter lifter name to update: ")
        if name in lifters.keys():
            update = input("Enter lift (one of 'squat', 'bench press', 'deadlift'): ")
            weight = input("Enter weight(s): ")

        else:
            print("Lifter '" + name + "' does not exist!")
    else:
        print("Invalid action '" + inp + "'. Try again!")
