# Powerlifting

width = int(input("Enter width: "))
squat = float(input("Enter squat: "))
bench = float(input("Enter bench: "))
dead = float(input("Enter deadlift: "))

# assuming correct user input, the length of rows with contents
# larger than the input width were not cut down
# this effectively results in a minimum input width 22

print("#" * width)
print("# Powerlifting 2022W" + " " * max(0, (width - 21)) + "#")
print("#" * width)
print("Maximum Squat: " + f"{squat:>{max(0, width-15-2)}.1f}" + "kg")
print("Maximum Bench Press: " + f"{bench:>{max(0, width-21-2)}.1f}" + "kg")
print("Maximum Deadlift: " + f"{dead:>{max(0, width-18-2)}.1f}" + "kg")
print("-" * width)
print("Total: " + f"{(squat + bench + dead):>{max(0, width-7-2)}.1f}" + "kg")
