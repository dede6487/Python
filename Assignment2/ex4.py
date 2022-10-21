start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

r = range(start, stop, step)

odd_counter = 0
even_sum = 0

for c in r:
    if c % 2 == 0:  # even
        even_sum += c
    else:
        odd_counter += 1
    if c == r[1]:
        print("2nd value in range = " + str(c))
    if c == r[len(r)-1]:
        print("Last value in range = " + str(c))

print("odd_counter = " + str(odd_counter))
print("even_sum = " + str(even_sum))
