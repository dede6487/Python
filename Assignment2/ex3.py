num = input("Enter number to guess: ")

while True:
    guess = input("Enter number: ")
    if guess == num:
        break
    elif guess == "exit":
        print("You lost!")
        break
    elif guess < num:
        print("Your number is smaller")
    elif guess > num:
        print("Your number is bigger")